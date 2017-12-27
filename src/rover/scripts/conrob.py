#!/usr/bin/python

import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
import math
import numpy as np
#import time

ADC.setup()

#Code to drive the Dc motor using PWM for speed control
#Min PWM duty cycle = 80
#Anything below will stall motors
#Frequency set at 40kHz

#Right motor connections M1
#Speed control => P8_13
PWM.start("P8_13",0.0,40000)
#Direction control => 
GPIO.setup("P9_16",GPIO.OUT)
GPIO.setup("P9_14",GPIO.OUT)

#Left motor connections M2
#Speed control => P9_21
PWM.start("P9_22",0.0,40000)
#Direction control => 
GPIO.setup("P9_12",GPIO.OUT)
GPIO.setup("P9_18",GPIO.OUT)

#Encoder setup
#Left E1
GPIO.setup("P9_26",GPIO.IN)
#Right
GPIO.setup("P9_30", GPIO.IN)

global goal 
global fire 
global prev_heading_error 
global total_heading_error 
global dprogress
global prev_left_tick
global prev_right_tick
global left_tick
global right_tick
global flag_left
global flag_right
global X
global Y
global Theta
global flag_change
global flag_direction_l
global flag_direction_r

###################HARDWARE##############################################    
def count():
    #Function to count ticks

    global left_tick
    global right_tick
    global flag_left
    global flag_right
    global flag_direction_l
    global flag_direction_r

    if GPIO.input("P9_26"):
        flag_left = True
        
    if GPIO.input("P9_30"):
        flag_right = True
        
    if (not GPIO.input("P9_26")) and flag_left:
        flag_left = False    
        left_tick += flag_direction_l
        #print "counting left ticks", left_tick
    if (not GPIO.input("P9_30")) and flag_right:
        flag_right = False    
        right_tick +=flag_direction_r
        #print "counting right ticks", right_tick

    return

def localise():
    #Function that will return the current location of the robot
    #PS. THE ORIENTATION MUST BE RETURNED IN RADIANS        

    global prev_left_tick
    global prev_right_tick
    global left_tick
    global right_tick
    global X
    global Y
    global Theta
    global flag_direction_l
    global flag_direction_r
    
    R = 31.5 #in mm 
    L  = 137 #in mm 
    ticks_per_rev = 16
    m_per_tick = (2*np.pi*R)/ticks_per_rev  
            
    count()

    Dl = m_per_tick*(left_tick - prev_left_tick)
    Dr = m_per_tick*(right_tick - prev_right_tick)
        
    Dc = (Dr + Dl)/2.0
    
    X_dt = Dc*np.cos(Theta)
    Y_dt = Dc*np.sin(Theta)
    Theta_dt = (Dr - Dl)/L
        
    X += X_dt
    Y += Y_dt
    Theta += Theta_dt

    print "X :",X," Y :",Y," Theta :",((Theta*180)/math.pi)    
    prev_left_tick = left_tick
    prev_right_tick = right_tick

    loc = [X, Y, Theta]

    return loc    
    
def robot_setvel(V,W):
    #Function to set the linear and rotational velocity of robot           
    
    global flag_direction_l
    global flag_direction_r
    
    R = 31.5 #in mm 
    L  = 137 #in mm 

    # 1. Limit v,w from controller to +/- of their max
    w = max(min(W, 3.5), -3.5)
    v = max(min(V, 250), -250)
            
    # 2. Compute desired vel_r, vel_l needed to ensure w
    Vr = ((2.0*v) + (w*L))/(2*R)
    Vl = ((2.0*v) - (w*L))/(2*R)
                        
    # 3. Find the max and min vel_r/vel_l
    vel_rl_max = max(Vr, Vl)
    vel_rl_min = min(Vr, Vl)
            
    # 4. Shift vel_r and vel_l if they exceed max/min vel
    if (vel_rl_max > 20.0):
        vel_r = Vr - (vel_rl_max - 100.0)
        vel_l = Vl - (vel_rl_max - 100.0)
    elif (vel_rl_min < -20.0):
        vel_r = Vr - (vel_rl_min + 100.0)
        vel_l = Vl - (vel_rl_min + 100.0)
    else:
        vel_r = Vr
        vel_l = Vl            
    
    if (vel_r > 0):
        GPIO.output("P9_16",GPIO.HIGH) 
        GPIO.output("P9_14",GPIO.LOW)
        flag_direction_r = 1
    else:
        GPIO.output("P9_16",GPIO.LOW) 
        GPIO.output("P9_14",GPIO.HIGH)    
        vel_r *= -1.0
        flag_direction_r = -1

    vel_r += 80         
    PWM.set_duty_cycle("P8_13",vel_r)        
    
    if (vel_l > 0):
        GPIO.output("P9_12",GPIO.HIGH) 
        GPIO.output("P9_18",GPIO.LOW)
        flag_direction_l = 1
    else:
        GPIO.output("P9_12",GPIO.LOW) 
        GPIO.output("P9_18",GPIO.HIGH) 
        vel_l *= -1.0
        flag_direction_l = -1
    
        
    vel_l += 80              
    PWM.set_duty_cycle("P9_22",vel_l)
    
    return    

def stop():
    #Function to stop the robot
    
    #Right motor stop
    GPIO.output("P9_16",GPIO.HIGH) 
    GPIO.output("P9_14",GPIO.HIGH)
    PWM.stop("P8_13")
    
    #Left motor stop
    GPIO.output("P9_12",GPIO.HIGH) 
    GPIO.output("P9_18",GPIO.HIGH)
    PWM.stop("P9_22")
    
    PWM.cleanup()
    return
        
def robot_getsonarrange(num):
    #Function to return IR reading in mm    

    #The IR calibration data(See separate module written for the same)
    z = np.poly1d([-538.95227761, 2151.58255867, -3406.46234825, 2712.32486717, -1130.34287295, 223.22591169])

    value =  ADC.read("AIN6")*1.8
    reading = z(value)
    print "Dist. for sensor at AIN 6",reading
    
    return reading
    
#########################SUPPORT##############################################
def obstacle_reading():
    #Function to compute obstacle point from range sensors
    
    #get the current robot location
    _, _, thetaa = localise()
    
    #Get sonar readings
    pi = math.pi
    sonoffset = [-(pi/2.0), -(pi/4.0), 0.0, (pi/4.0), (pi/2.0)]
    sonweight = [4, 2, 5, 2, 4]
           
    readings = []
  
    for i in range(len(sonoffset)):
        r = robot_getsonarrange(i)
        r = r*sonweight[i]
        angl = thetaa - sonoffset[i]
        delx = r*math.cos(angl)
        dely = r*math.sin(angl)
        readings.append([(delx, dely)])
          
    return np.mean(readings, axis=0)
    
def fw_tanvec(side):
    #The follow vector calculator for Follow Wall behavior   
    
    #The follow wall threshold distance
    dfw = 600.0
    
    #get the current robot location
    _, _, thetaa = localise()
    
    pi = math.pi
    sonoffset = [-(pi/2.0), -(pi/4.0), 0.0, (pi/4.0), (pi/2.0)]
           
    readings = []
    
    if side == 'l':
        for i in [0, 1]:
            r = robot_getsonarrange(i)
            angl = thetaa - sonoffset[i]
            delx = r*math.cos(angl)
            dely = r*math.sin(angl)
            readings.append([(delx, dely)])
            
    else:            
        for i in [4, 3]:
            r = robot_getsonarrange(i)
            angl = thetaa - sonoffset[i]
            delx = r*math.cos(angl)
            dely = r*math.sin(angl)
            readings.append([(delx, dely)])
            
    Ufw_t = np.subtract(readings[1],readings[0])                  
    Upfw_t = Ufw_t/np.linalg.norm(Ufw_t)    
    temp = (np.dot(readings[0], Upfw_t))*Upfw_t    
    Ufw_p = readings[0] - temp
    Upfw_p = Ufw_p - (dfw*(Ufw_p/np.linalg.norm(Ufw_p)))
    Upfw_p = Upfw_p/(np.linalg.norm(Upfw_p))
    Ufw = (Upfw_p + (4.0*Upfw_t))/5.0
    
    return Ufw    
    
##########################EVENTS###############
def at_goal():
    #Event which checks if we have reached the goal(within threshold)     
    
    global goal
    
    #The threshold distance 
    distThresh = 150#mm
    
    xd = goal[0]
    yd = goal[1]
    
    #get the current robot location
    xa, ya,_ = localise()
    
    #check if we have reached goal point
    d = math.sqrt(pow((xd - xa),2) + pow((yd - ya),2))
    
    if d <= distThresh:
        print "Reached goal"
        return True
    else:
        return False
        
def at_obstacle():
    #Event which checks if we have detected any obstacle (within safe distance)
    
    #The safe distance
    d_safe = 1000
    
    for i in range(5):
        r = robot_getsonarrange(i)
        if r < d_safe:
            print "Obstacle detected"
            return True

    return False 
    
def unsafe():
    #Event which checks if we have detected any obstacle (within unsafe distance)
    
    #The unsafe distance
    d_unsafe = 500.0
    
    for i in range(5):
        r = robot_getsonarrange(i)
        if r < d_unsafe:
            print "Unsafe"
            return True
            
    return False

def obstacle_cleared():
    #Event which checks if we have cleared all obstacle (within safe distance)
    
    #The safe distance
    d_safe = 1000
    
    for i in range(5):
        r = robot_getsonarrange(i)
        if r < d_safe:            
            return False

    print "Obstacle cleared"            
    return True
    
def no_progress():
    #Event which checks progress
    #If made ==> sets it
    #If not ==>  checks it and raises flag
    
    global goal
    global dprogress
    
    xd = goal[0]
    yd = goal[1]
    
    #Epsilon slack
    E = 300.0        
    
    #get the current robot location
    xa, ya, _ = localise()
    
    #check if we have reached goal point
    d = math.sqrt(pow((xd - xa),2) + pow((yd - ya),2))
    
    #The first setting
    if dprogress < 0:
        dprogress = d
        return False
        
    if dprogress > d:
        #Progress made
        dprogress = d
        print "progress made"
        return False
    elif d > (dprogress + E):
        #progress not made        
        print "No progress"
        return True
    else:
        return False                                   

def chk_wall(side):
    #Event to check whether to continue following the given side
    
    global goal
    
    xd = goal[0]
    yd = goal[1]
    
    #get the current robot location
    xa, ya, _ = localise()    
    
    #The normalized gtg vector
    Ugtg = [((xd - xa),(yd - ya))]
    Ugtg = Ugtg/np.linalg.norm(Ugtg)
    
    #The normalized ao vector
    [[Uao]] = obstacle_reading()
    Uao = Uao/np.linalg.norm(Uao)        
    
    #The normalized follow wall vector
    Ufw = fw_tanvec(side)
    Ufw = Ufw/np.linalg.norm(Ufw) 
    
    a = np.array([[Ugtg[0], Uao[0]],[Ugtg[1], Uao[1]]])
    c = np.array([[Ufw[0]], [Ufw[1]]])
    
    Sigma = np.dot(np.linalg.pinv(a),c)
    
    if Sigma[0][0] > 0 and Sigma[1][0] > 0:
        return True
    else:        
        print "wall follow stopped"
        return False
                                                   
###########################GUARD################################################
def guard(num):
    #The Guard Function
    #1.sets fire to desired controller
    #2.resets the controller errors
    
    #Controller errors
    global prev_heading_error
    global total_heading_error
    global fire
    global flag_change
    
    prev_heading_error = 0.0
    total_heading_error = 0.0
    
    fire = num
    flag_change = True
    
    return    

##################CONTROLLERS###################################################
def gtg():
    #The Go to goal controller
    
    global goal
    global prev_heading_error
    global total_heading_error   
    global flag_change
    
    if flag_change:
        print "Go to goal controller engaged"
        flag_change = False
    
    #Controller parameters
    Kp = 0.2
    Kd = 0.0
    Ki = 0.0
    
    xd = goal[0]
    yd = goal[1]
    
    #get the current robot location
    xa, ya, thetaa = localise()
    
    #determine how far to rotate to face the goal point
    #PS. ALL ANGLES ARE IN RADIANS
    dt = (math.atan2((yd - ya), (xd -xa))) - thetaa
    #restrict angle to (-pi,pi)
    dt = ((dt + math.pi)%(2.0*math.pi)) - math.pi
    dt = ((dt*180.0)/math.pi)
        
    #control input for angular velocity
    W = (Kp*dt) + (Ki*total_heading_error) + (Kd*(dt - prev_heading_error))
    total_heading_error = total_heading_error + dt
    prev_heading_error = dt
  
    #find distance to goal
    d = math.sqrt(pow((xd - xa),2) + pow((yd - ya),2))
    
    #velocity parameters
    velMult = 100#mm/s
    distThresh =150#mm
    
    #control input for linear velocity
    V = ((math.atan((d - distThresh)/25)) - (math.atan(dt/10)))*velMult
    
    #print "V :", V, "W :", W
    #request robot to execute velocity
    robot_setvel(V,W)
    
    #Check events
    if at_goal():
        #call stop_robot()
        guard(5)
    elif at_obstacle():
        #call ao_gtg()
        guard(2)
    elif no_progress:
        if chk_wall('l'):
            #call fw('l')
            guard(41)
        else:
            #call fw('r')
            guard(42)
                                       
    return                     
    
def ao_gtg():
    #The Avoid obstacle and Go to goal controller
    
    global goal
    global prev_heading_error
    global total_heading_error 
    global flag_change
    
    if flag_change:
        print "Avoid obstacle and Go to goal controller engaged"
        flag_change = False
    
    #Controller parameters
    Kp = 0.2;
    Kd = 0.0;
    Ki = 0.0;
    
    xd = goal[0]
    yd = goal[1]
    
    #get the current robot location
    xa, ya, thetaa = localise()
    
    #determine how far to rotate to face the goal point
    #PS. ALL ANGLES ARE IN RADIANS
    dt = (math.atan2((yd - ya), (xd -xa))) - thetaa
    #restrict angle to (-pi,pi)
    dtgtg = ((dt + math.pi)%(2.0*math.pi)) - math.pi
    
    #Get obstacle point reading from sensors
    [[obs_x, obs_y]] = obstacle_reading()
    
    #Determine how far to rotate to avoid obstacle
    dt =  (math.atan2(obs_x,obs_y))- thetaa
    #restrict angle to (-pi,pi)
    dtao = ((dt + math.pi)%(2.0*math.pi)) - math.pi
 
    #Combining both in 1:3 ratio 
    dtnet = (dtgtg + (3.0*dtao))/4.0
    dtnet = ((dtnet*180.0)/math.pi)
    
    #control input for angular velocity
    W = (Kp*dtnet) + (Ki*total_heading_error) + (Kd*(dtnet - prev_heading_error))
    total_heading_error = total_heading_error + dtnet
    prev_heading_error = dtnet
    
    #velocity parameters
    velMult = 50#mm/s
    
    #set constant linear velocity
    V = velMult
    
    #request robot to execute velocity
    robot_setvel(V,W)
    
    #Check events
    if at_goal():
        #call stop_robot()
        guard(5)
    elif unsafe():
        #call ao()
        guard(3)
    elif no_progress:
        if chk_wall('l'):
            #call fw('l')
            guard(41)
        else:
            #call fw('r')
            guard(42)
    elif obstacle_cleared():
        #call gtg()
        guard(1)            
                                       
    return                
    
def ao():
    #The Avoid obstacle controller
    
    global prev_heading_error
    global total_heading_error 
    global flag_change
    
    if flag_change:
        print "Avoid obstacle controller engaged"
        flag_change = False
    
    #Controller parameters
    Kp = 0.2;
    Kd = 0.0;
    Ki = 0.0;

    #get the current robot location
    _, _, thetaa = localise()
    
    #Get obstacle point reading from sensors
    [[obs_x, obs_y]] = obstacle_reading()
    
    #Determine how far to rotate to avoid obstacle
    dt =  (math.atan2(obs_x,obs_y))- thetaa
    #restrict angle to (-pi,pi)
    dt = ((dt + math.pi)%(2.0*math.pi)) - math.pi
    dt = ((dt*180.0)/math.pi)
    
    #control input for angular velocity
    W = (Kp*dt) + (Ki*total_heading_error) + (Kd*(dt - prev_heading_error))
    total_heading_error = total_heading_error + dt
    prev_heading_error = dt
    
    #velocity parameters
    velMult = 20#mm/s
    
    #set constant linear velocity
    V = velMult
    
    #request robot to execute velocity
    robot_setvel(V,W)
    
    #Check events
    if at_goal():
        #call stop_robot()
        guard(5)
    elif obstacle_cleared():
        #call ao_gtg()
        guard(2)            
                                       
    return
        
def fw(side):
    #The Follow Wall Controller
    
    global prev_heading_error
    global total_heading_error 
    global flag_change
    
    if flag_change:
        print "Follow wall controller engaged on ", side
        flag_change = False
    
    
    #Controller parameters
    Kp = 0.2;
    Kd = 0.0;
    Ki = 0.0;        
    
    #get the current robot location
    _, _, thetaa = localise()
    
    #get the follow wall vector
    fw_x, fw_y = fw_tanvec(side)
    
    #Determine how far to rotate to follow wall
    dt =  (math.atan2(fw_x, fw_y))- thetaa
    #restrict angle to (-pi,pi)
    dt = ((dt + math.pi)%(2.0*math.pi)) - math.pi
 
    #control input for angular velocity
    W = (Kp*dt) + (Ki*total_heading_error) + (Kd*(dt - prev_heading_error))
    total_heading_error = total_heading_error + dt
    prev_heading_error = dt
    
    #velocity parameters
    velMult = 75#mm/s
    
    #set constant linear velocity
    V = velMult
    
    #request robot to execute velocity
    robot_setvel(V,W)
    
    #Check events
    if at_goal():
        #call stop_robot()
        guard(5)
    elif ((not no_progress()) and (not chk_wall(side))):
        #call ao_gtg()
        guard(2)            
                                       
    return
              
def stop_robot():
    #The controller to stop the robot
    
    global fire
    global flag_change
    
    if flag_change:
        print "Stop controller engaged"
        flag_change = False
    
    stop()
    fire = 0   
    
    print "System exit"
    return
                 
##################################MAIN######################################
def main():
    
    global goal
    global fire
    global dprogress
    global prev_left_tick
    global prev_right_tick
    global left_tick
    global right_tick
    global flag_left
    global flag_right
    global X
    global Y
    global Theta
    global flag_change
    
    #print "Enter the goal co:ordinates \nEnter Xi:"
    #Xi = input()
    Xi = 1000.0
    #print 'Enter Yi:'
    #Yi = input()
    Yi = 0.0
    goal = [Xi, Yi]
    
    #Initializing the localization variables
    prev_left_tick = 0
    prev_right_tick = 0
    left_tick = 0
    right_tick = 0
    flag_left = False
    flag_right = False
    X = 0.0
    Y = 0.0
    Theta = 0.0

    #The progress variable initialization
    dprogress = -1
    
    print "Auto Drive engaged:::\n"
    
    #It all begins with the Go to goal controller(Gtg)
    guard(1)
    flag_change = True
    
    #Begin the controller loop
    #Till there burns the fire
    while fire:
      
        if fire == 1:
            gtg()
            continue
        elif fire == 2:
            ao_gtg()
            continue         
        elif fire == 3:
            ao()    
            continue    
        elif fire == 41:
            fw('l') 
            continue               
        elif fire == 42:
            fw('r')
            continue
        else:
            stop_robot()
                                 
        return
    
main()                    
 
#Encoder given in through level converter 
#Enter all remaining controller parameters
#Fix velocities for avoid obstacle controller etc.
#!/usr/bin/env python

##Aim: The node to publish state(x,y -position and theta -orientation) of robot 
##Subcribes : None
##Publishes : R_pose
#---------------------------------------------
import numpy as np

import rospy
from geometry_msgs.msg import Twist

def reset_counter():
    #Function to reset the tick counters
    # and initialise all the variables
    
    global prev_left_tick
    global prev_right_tick
    global X
    global Y
    global Theta
    
    enc_lfile = open("/sys/devices/ocp.3/48302000.epwmss/48302180.eqep/position","w")
    enc_rfile = open("/sys/devices/ocp.3/48304000.epwmss/48304180.eqep/position","w")
    
    enc_lfile.write('0')
    enc_rfile.write('0')
    
    print "Quadrature encoders reset"  
    
    enc_lfile.close()
    enc_rfile.close()  
    
    prev_left_tick = 0
    prev_right_tick = 0
    X = 0.0
    Y = 0.0
    Theta = 0.0    
    return

def turn_off():
    #Function for safe shutdown 
    
    print "Localiser node turning off"
    return   

def count():
    #Function to get tick count from file 
	
    enc_lfile = open("/sys/devices/ocp.3/48302000.epwmss/48302180.eqep/position","r")    
    enc_rfile = open("/sys/devices/ocp.3/48304000.epwmss/48304180.eqep/position","r")
    
    left_tick = int(enc_lfile.read())
    right_tick = int(enc_rfile.read())
    ticks = [left_tick, right_tick]
     
    enc_lfile.close()
    enc_rfile.close()

    return ticks

def localise():
    #Function that will return the current location of the robot
    #PS. THE ORIENTATION MUST BE RETURNED IN RADIANS        

    global prev_left_tick
    global prev_right_tick
    global X
    global Y
    global Theta
    
    #Hardware details    
    R = 30.5 #in mm 
    L  = 183.0 #in mm 
    ticks_per_rev = 1000.0/3.0
    mm_per_tick = (2*np.pi*R)/ticks_per_rev  
            
    left_tick, right_tick  = count()

    Dl = mm_per_tick*(left_tick - prev_left_tick)
    Dr = mm_per_tick*(right_tick - prev_right_tick)
        
    Dc = (Dr + Dl)/2.0
    
    X_dt = Dc*np.cos(Theta)
    Y_dt = Dc*np.sin(Theta)
    Theta_dt = (Dl - Dr)/(2.0*L)
        
    X += X_dt
    Y += Y_dt
    Theta += Theta_dt

    print "X :",X," Y :",Y," Theta :",((Theta*180)/np.pi)        
    #print "l: ", left_tick, "r: ", right_tick
    prev_left_tick = left_tick
    prev_right_tick = right_tick

    return

def main():
    #The main function
    global X
    global Y
    global Theta
    
    #Reset the counters
    reset_counter()
    
    pub = rospy.Publisher('R_pose', Twist, queue_size = 10)
    msg = Twist()
    
    rospy.init_node('localiser')
    rospy.on_shutdown(turn_off)
    print('Localiser node running')
    
    r = rospy.Rate(10) #10Hz
    while not rospy.is_shutdown():
        localise()
        msg.linear.x = X
        msg.linear.y = Y
        msg.angular.z = Theta
        pub.publish(msg)
        r.sleep    

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
    

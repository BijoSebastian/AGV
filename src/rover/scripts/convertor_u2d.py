#!/usr/bin/env python

##Aim: Convert linear and angular velocity from unicycle model to 
##     left and right wheel velocities of differential drive. 
##Subcribes : velocity_command
##Publishes : left_wheel, right_wheel
#---------------------------------------------

import rospy
from sensor_msgs.msg import JointState
from geometry_msgs.msg import Twist

def pub_data(vel_l, vel_r):
    #Function to publish data
    
    p1 = rospy.Publisher('left_wheel', JointState, queue_size = 10)
    p2 = rospy.Publisher('right_wheel', JointState, queue_size = 10)
    
    #Message for Left wheel    
    msg1 = JointState()
    msg1.velocity = [vel_l]
    p1.publish(msg1)

    #Message for right wheel
    msg2 = JointState()
    msg2.velocity = [vel_r]
    p2.publish(msg2)
    
    #Keep logs of published data
    #rospy.loginfo('Left Motor velocity')
    #rospy.loginfo(msg1.velocity)
    #rospy.loginfo('Right Motor velocity')
    #rospy.loginfo(msg2.velocity)
    print 'vel_r: ',vel_r,'vel_l:',vel_l  
    return
    
def turn_off():
    #Function for safe shutdown 
    
    print('model convertor (U2D) node turning off')
    pub_data(0.0, 0.0)
    return

def convert(msg):
    #Fucntion that does the converting part
    
    V = msg.linear.x#(mm/s)
    W = msg.angular.z#(rad/s)
    
    #Most of the parameters in here needs to be reprogrammed.
    R = 30.0 #Radius of the wheel in mm 
    L  = 200.0 #distance between the two wheels in mm 
    vel_max = 8.33 #Rad/s --> maximum angular velocity attainable by the wheel

    # 1. Limit v,w from controller to +/- of their max
    w = max(min(W, 2.5), -2.5)
    v = max(min(V, 250), -250)
            
    # 2. Compute desired vel_r, vel_l in rad/s needed to ensure v,w
    Vr = ((2.0*v) + (w*L))/(2*R)
    Vl = ((2.0*v) - (w*L))/(2*R)
                        
    # 3. Find the max and min vel_r/vel_l
    vel_rl_max = max(Vr, Vl)
    vel_rl_min = min(Vr, Vl)
            
    # 4. Shift vel_r and vel_l if they exceed max/min angular velocity of wheels
    if (vel_rl_max > vel_max):
        vel_r = Vr - (vel_rl_max - vel_max)
        vel_l = Vl - (vel_rl_max - vel_max)
    elif (vel_rl_min < (-1 *vel_max)):
        vel_r = Vr - (vel_rl_min + vel_max)
        vel_l = Vl - (vel_rl_min + vel_max)
    else:
        vel_r = Vr
        vel_l = Vl 
    
    # 5. Rad/S to PWM mapping
    vel_r = (40*vel_r)/vel_max
    vel_l = (40*vel_l)/vel_max

    pub_data(vel_l, vel_r)
    return

def main():
    
    #Initialising             
    rospy.init_node('convertor_u2d')
    rospy.on_shutdown(turn_off)

    print('model convertor (U2D) node running')
    rospy.Subscriber("velocity_command", Twist, convert)
    rospy.spin()    

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
    

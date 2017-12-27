#!/usr/bin/env python

##Aim: The node to obtain range data from 5 IR sensors and publish.  
##Subcribes : None
##Publishes : Range
#---------------------------------------------
import numpy as np
import rospy
from sensor_msgs.msg import LaserScan

import Adafruit_BBIO.ADC as ADC
ADC.setup()

IR_Range = [0.0]*5

def turn_off():
    #Function for safe shutdown 
    
    print "Ranger node turning off"
    return   

def getsonarrange():
    #Function to return IR reading in mm    
    
    global IR_Range
    
    #The IR calibration data(See separate module written for the same)
    z = np.poly1d([-56752.50397336, 106943.71793566, -78566.34020543, 28444.79303048, -5258.33803966, 458.35422818])
    
    value =  ADC.read("AIN0")*1.8        
    IR_Range[0] = float(z(value))
    value =  ADC.read("AIN1")*1.8    
    IR_Range[1] = float(z(value))
    value =  ADC.read("AIN2")*1.8    
    IR_Range[2] = float(z(value))
    value =  ADC.read("AIN3")*1.8    
    IR_Range[3] = float(z(value))
    value =  ADC.read("AIN6")*1.8    
    IR_Range[4] = float(z(value))
    
    print "Range sensor reading",IR_Range[2]
    
    return 

def main():
    #The main function
    global IR_Range
    
    pub = rospy.Publisher('Range_data', LaserScan, queue_size = 5)
    msg = LaserScan()

    rospy.init_node('ranger')
    rospy.on_shutdown(turn_off)
    print('Ranger node running')
    
    r = rospy.Rate(0.005) #2Hz
    while not rospy.is_shutdown():
        getsonarrange()
        msg.ranges = IR_Range
	msg.header.stamp = rospy.get_rostime()
        pub.publish(msg)
        r.sleep    

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

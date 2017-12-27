#!/usr/bin/env python

##Aim: Publish the orientation dta as obtained from the IMU Fusion 
##Subcribes : None
##Publishes : R_yaw
#---------------------------------------------

import rospy
from geometry_msgs.msg import Twist

import sys, getopt

sys.path.append('.')
import RTIMU
import os.path
import time
import math

def turn_off():
    #Function for safe shutdown 
    
    print "IMU node turning off"
    return   


def main():
 
    SETTINGS_FILE = "RTIMULib"

    print("Using settings file " + SETTINGS_FILE + ".ini")
    if not os.path.exists(SETTINGS_FILE + ".ini"):
        print("Settings file does not exist, will be created")

    s = RTIMU.Settings(SETTINGS_FILE)
    imu = RTIMU.RTIMU(s)
    
    print("IMU Name: " + imu.IMUName())
    
    if (not imu.IMUInit()):
        print("IMU Init Failed")
        sys.exit(1)
    else:
        print("IMU Init Succeeded")

        # this is a good time to set any fusion parameters

        imu.setSlerpPower(0.02)
        imu.setGyroEnable(True)
        imu.setAccelEnable(True)
        imu.setCompassEnable(False)

        poll_interval = imu.IMUGetPollInterval()
        print("Recommended Poll Interval: %dmS\n" % poll_interval)
        
    pub = rospy.Publisher('R_yaw', Twist, queue_size = 10)
    msg = Twist()
    
    rospy.init_node('IMU_fusion')
    rospy.on_shutdown(turn_off)
    print('IMU node running')
    
    r = rospy.Rate(1000.0/poll_interval) #~250Hz
    while not rospy.is_shutdown():
        if imu.IMURead():
            #x, y, z = imu.getFusionData()
            #print("%f %f %f" % (x,y,z))
            data = imu.getIMUData()
            fusionPose = data["fusionPose"]
            print("r: %f p: %f y: %f" % (math.degrees(fusionPose[0]),math.degrees(fusionPose[1]), math.degrees(fusionPose[2])))
            msg.angular.z = fusionPose[2]
            pub.publish(msg)
            r.sleep  
        
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass        
        

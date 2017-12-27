#!/usr/bin/env python

##Aim: Drive the 2 motors at desired velocity
##Subcribes : left_wheel, right_wheel
##Publishes : None
#---------------------------------------------

import rospy
from sensor_msgs.msg import JointState

import Adafruit_BBIO.GPIO as GPIO

def motor_init():
    #Function to intialise the DC motor speed control using PWM
    #Frequency set at 40kHz

    #Right motor connections M1
    #Speed control => P9_21
    pwmfile = open("/sys/class/pwm/pwm1/period_ns","w")    
    pwmfile.write('2000000')
    pwmfile.close()
    pwmfile = open("/sys/class/pwm/pwm1/duty_ns","w")    
    pwmfile.write('0')
    pwmfile.close()
    pwmfile = open("/sys/class/pwm/pwm1/run","w")    
    pwmfile.write('1')
    pwmfile.close()
    
    #Direction control => 
    GPIO.setup("P9_12",GPIO.OUT)
    GPIO.setup("P9_14",GPIO.OUT)
    #Initialise low
    GPIO.output("P9_12",GPIO.LOW) 
    GPIO.output("P9_14",GPIO.LOW)

    #Left motor connections M2
    #Speed control => P9_22
    pwmfile = open("/sys/class/pwm/pwm0/period_ns","w")    
    pwmfile.write('2000000')
    pwmfile.close()
    pwmfile = open("/sys/class/pwm/pwm0/duty_ns","w")    
    pwmfile.write('0')
    pwmfile.close()
    pwmfile = open("/sys/class/pwm/pwm0/run","w")    
    pwmfile.write('1')
    pwmfile.close()
    
    #Direction control => 
    GPIO.setup("P9_16",GPIO.OUT)
    GPIO.setup("P9_18",GPIO.OUT)
    #Initialise low
    GPIO.output("P9_16",GPIO.LOW) 
    GPIO.output("P9_18",GPIO.LOW)
    return

def turn_off():
    #Function for safe shutdown 
    
    print('motor_driver node turning off')    
    
    #Right motor stop
    GPIO.output("P9_12",GPIO.LOW) 
    GPIO.output("P9_14",GPIO.LOW)
    pwmfile = open("/sys/class/pwm/pwm1/duty_ns","w")    
    pwmfile.write('0')
    pwmfile.close()
    pwmfile = open("/sys/class/pwm/pwm1/run","w")    
    pwmfile.write('0')
    pwmfile.close()
    
    #Left motor stop
    GPIO.output("P9_16",GPIO.LOW) 
    GPIO.output("P9_18",GPIO.LOW)
    pwmfile = open("/sys/class/pwm/pwm0/duty_ns","w")    
    pwmfile.write('0')
    pwmfile.close()
    pwmfile = open("/sys/class/pwm/pwm0/run","w")    
    pwmfile.write('0')
    pwmfile.close() 
     
    return   

def set_left(msg):
    #Callback function to set vel_l
    
    vel_l = msg.velocity[0]
     
    if(vel_l == 0):
        GPIO.output("P9_16",GPIO.LOW) 
        GPIO.output("P9_18",GPIO.LOW)
    else:
        if (vel_l > 0):
            GPIO.output("P9_16",GPIO.HIGH)
            GPIO.output("P9_18",GPIO.LOW)
        else:
            GPIO.output("P9_16",GPIO.LOW)
            GPIO.output("P9_18",GPIO.HIGH)
            vel_l *= -1.0
            
    pwmfile = open("/sys/class/pwm/pwm0/duty_ns","w")    
    vel_l = int(vel_l)
    pwmfile.write(str(vel_l*20000))
    pwmfile.close()   
     
    return
   
def set_right(msg):
    #Callback function to set vel_r
    
    vel_r = msg.velocity[0]
    
    if(vel_r == 0):
        GPIO.output("P9_12",GPIO.LOW) 
        GPIO.output("P9_14",GPIO.LOW)
    else:
        if (vel_r > 0):
            GPIO.output("P9_12",GPIO.HIGH)
            GPIO.output("P9_14",GPIO.LOW)
        else:
            GPIO.output("P9_12",GPIO.LOW)
            GPIO.output("P9_14",GPIO.HIGH)
            vel_r *= -1.0
    
    pwmfile = open("/sys/class/pwm/pwm1/duty_ns","w")    
    vel_r = int(vel_r)
    pwmfile.write(str(vel_r*20000))
    pwmfile.close()   
     
    return
    
def main():
    
    #Initialising the hardware
    motor_init()
            
    rospy.init_node('motor_driver')
    rospy.on_shutdown(turn_off)

    print('motor_driver node running')
    
    rospy.Subscriber("left_wheel", JointState, set_left)
    rospy.Subscriber("right_wheel", JointState, set_right)
  
    rospy.spin()    

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
    

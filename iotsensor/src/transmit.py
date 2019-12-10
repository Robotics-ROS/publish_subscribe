#!/usr/bin/env python2.7


import rospy
from iotsensor.msg import temp_humidity
import random

def transmitter(sensor):
    pub= rospy.Publisher('tempHumidityTransmit', temp_humidity, queue_size=10)
    rospy.init_node('iotsensor_topic', anonymous= True)
    rate= rospy.Rate(1)
    pub.publish(sensor)
    rate.sleep()

if __name__ == "__main__":
    i= 0
    while not rospy.is_shutdown():
        sensor= temp_humidity()
        sensor.id= 1
        sensor.name= 'Temperature and Humidity Sensor'
        sensor.temperature= 104.94 + (random.random()*2)
        sensor.humidity= 78.47 + (random.random()*2)
        i+=1    
        rospy.loginfo('transmitting {}'.format(i))
        transmitter(sensor)
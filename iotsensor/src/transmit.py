#!/usr/bin/env python2.7


import rospy
from iotsensor.msg import temp_humidity
from iotsensor.srv import math, mathRequest, mathResponse
import random

def sumcallback(req):
    print('Returning [{} + {} = {}]'.format(req.a, req.b, (req.a + req.b)))
    return mathResponse(req.a + req.b)


def transmitter(sensor):
    pub= rospy.Publisher('tempHumidityTransmit', temp_humidity, queue_size=10)
    rate= rospy.Rate(1)
    pub.publish(sensor)
    rate.sleep()

if __name__ == "__main__":
    i= 0
    rospy.init_node('iotsensor_topic', anonymous= True)
    s= rospy.Service('mathSum', math, sumcallback)
    print(s.resolved_name)
    while not rospy.is_shutdown():
        sensor= temp_humidity()
        sensor.id= 1
        sensor.name= 'Temperature and Humidity Sensor'
        sensor.temperature= 104.94 + (random.random()*2)
        sensor.humidity= 78.47 + (random.random()*2)
        i+=1    
        rospy.loginfo('transmitting {}'.format(i))
        transmitter(sensor)

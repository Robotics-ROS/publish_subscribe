#!/usr/bin/env python2.7

import rospy
from iotsensor.msg import temp_humidity
from iotsensor.srv import math
import time

def servicetest(x, y):
    rospy.wait_for_service('mathSum')
    try:
        print('found service')
        add= rospy.ServiceProxy('mathSum', math)
        resp= add(x, y)
        print 'got response', resp
        return resp.sum
        
    except:
        print('service call failed')
        pass


def callbacklistener(data):
    # rospy.loginfo(rospy.get_caller_id() + "Heard\n" + data)
    print('data= ', data.name)
    pass


if __name__ == "__main__":
    rospy.init_node('iotsensor_listener', anonymous= True)
    rospy.Subscriber('tempHumidityTransmit', temp_humidity, callbacklistener)
    while True:
        servicetest(1, 5)
        time.sleep(1)

    # rospy.Service
    # print('Subscribed')
    rospy.spin()

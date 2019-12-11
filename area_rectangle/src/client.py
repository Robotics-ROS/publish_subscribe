#!/usr/bin/python

import rospy
import time
import random
from area_rectangle.srv import area, areaRequest, areaResponse

def request(x, y):
    rospy.wait_for_service('areaCal')
    try:
        ar= rospy.ServiceProxy('areaCal', area)
        print('area= {}'.format(ar(x, y).result))
        pass
    except:
        pass

if __name__ == "__main__":
    rospy.init_node('client_node', anonymous= True)
    while True:
        x = ((100 + random.random()) / 13.0) 
        y = ((2 + random.random()) / 13.0) 
        request(x, y)
        time.sleep(1)

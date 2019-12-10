#!/usr/bin/env python2.7

import rospy
from iotsensor.msg import temp_humidity

def callbacklistener(data):
    # rospy.loginfo(rospy.get_caller_id() + "Heard\n" + data)
    print('data= ', data.name)
    pass


if __name__ == "__main__":
    rospy.init_node('iotsensor_listener', anonymous= True)
    rospy.Subscriber('tempHumidityTransmit', temp_humidity, callbacklistener)
    print('Subscribed')
    rospy.spin()

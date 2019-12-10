#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def mover():
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size= 10)
    rospy.init_node('mover', anonymous= True)
    rate= rospy.Rate(10)

    while not rospy.is_shutdown():
        msg= Twist()
        msg.linear.x, msg.linear.y, msg.linear.z = 1.0, 1.0, 0.0 
        msg.angular.x, msg.angular.y, msg.angular.z = 0.0, 0.0, 1.0 
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()



if __name__ == '__main__':
    try:
        mover()
    except rospy.ROSInterruptException:
        pass
    
#!/usr/bin/env python2.7

import rospy
from turtlesim.msg import Pose

def posecallback(data):
    rospy.loginfo(data)

def main():
    try:
        rospy.init_node('turtlesim_pose_display', anonymous=True)
        print 'initialized'
        rospy.Subscriber("/turtle1/pose", Pose, posecallback)
        print 'subscribed'
        rospy.spin()
    except rospy.ROSInterruptException:
        pass


if __name__ == "__main__":
    main()

# class Turtle():
#     def __init__(self):
#         self.pose= Pose()
#         pass

#     def getPose(self):
#         return self.pose.position.x
        

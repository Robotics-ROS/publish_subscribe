#!/usr/bin/env python2.7


import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time
from std_srvs.srv import Empty








def rotate(xGoal, yGoal, velocity_message):
    while True:
        # object to twisting instructions
        # calculate distance and direction
        
        distance_to_goal= math.sqrt((xCurrent - xGoal)**2 + (yCurrent - yGoal)**2)
        angle_to_goal= math.atan2((yGoal - yCurrent) , (xGoal - xCurrent))

        linear_speed= (distance_to_goal * 0.1)
        
        angular_speed= (angle_to_goal - R.theta) * 4.0
        
        velocity_message.linear.x= 0
        velocity_message.angular.z= angular_speed
            
        velocity_publisher.publish(velocity_message)
        if(abs(angle_to_goal - R.theta) <= 0.0001):
            break
        # time.sleep(.1)  


def roll(xGoal, yGoal, velocity_message):
    while True:
        # object to twisting instructions
        # calculate distance and direction
        
        distance_to_goal= math.sqrt((xCurrent - xGoal)**2 + (yCurrent - yGoal)**2)
        angle_to_goal= math.atan2((yGoal - yCurrent) , (xGoal - xCurrent))

        linear_speed= 4.0#(distance_to_goal * 0.1)
        angular_speed= (R.theta- angle_to_goal) * 0.1
        print yGoal - yCurrent, xGoal - xCurrent, angle_to_goal
        # print(angular_speed, R.theta)
        velocity_message.linear.x= linear_speed
        velocity_message.angular.z= 0#angular_speed
            
        velocity_publisher.publish(velocity_message)
        
        if(abs(distance_to_goal) <= 0.1):
            break  


def gotoGoal(xGoal, yGoal):
    global x, y, yaw
    velocity_message = Twist()


    print 'Aquiring target...'
    rotate(xGoal, yGoal, velocity_message)
    print 'Target aquired...'
    print 'Ready to launch...'
    roll(xGoal, yGoal, velocity_message)
    print 'Reached Target...'





def getPoseCallback(req):
    global xCurrent, yCurrent, R
    xCurrent, yCurrent, R= req.x, req.y, req

def main():
    global command_vel_topic, position_topic, velocity_publisher, pose_subscriber
    command_vel_topic = 'turtle1/cmd_vel'
    position_topic = 'turtle1/pose'
    velocity_publisher= rospy.Publisher(command_vel_topic, Twist, queue_size= 10)
    pose_subscriber = rospy.Subscriber(position_topic, Pose, getPoseCallback)

    rospy.init_node('cleaning_turtle', anonymous= True)
    extent= 10
    i= 0;
    while True:
        gotoGoal(1+i, 1 + i)
        gotoGoal(1+i, extent-i)
        gotoGoal(extent-i, extent-i)
        gotoGoal(extent-i, 1+i)
        gotoGoal(1+i+1, 1+i)
        # gotoGoal(extent-i, 1+i)
        i= i+1

        if(i >= 10):
            break
    gotoGoal(1, 1)
    


    rospy.spin()

if __name__ == "__main__":
    main()



#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan 
from geometry_msgs.msg import Point, Twist

def callback(msg):

	
	threshold = 0.70 # Threshold of Laser scanner range
	
	
	if msg.ranges[0]<threshold or msg.ranges[10]<threshold or msg.ranges[350]<threshold:

		# Checks if there are any laser scanner measurements in its direction of motion, +10 and -10 degrees.
		# Linear velocity is 0, Angular velocity is 0.3 which means it rotates counter clock wise.

		go.linear.x = 0.0
		go.angular.z = 0.3

		if msg.ranges[0]>threshold and msg.ranges[10]>threshold and msg.ranges[350]>threshold:

			# Angular velocity is 0, Linear velocity is 0.5 which means it moves forward.

			go.linear.x = 0.5
			go.angular.z = 0.0

	elif msg.ranges[0]>threshold and msg.ranges[10]>threshold and msg.ranges[350]>threshold:

		go.linear.x = 0.5
		go.angular.z = 0.0

	pub.publish(go) # Publish messages to move.
	



rospy.init_node('obstacle_avoid_node') # Node Initialization

pub = rospy.Publisher("/cmd_vel", Twist, queue_size = 10) # Publisher object to publish Twist type messages. Velocity commands are given to the vehicle.

sub = rospy.Subscriber("/scan", LaserScan, callback) # Subscriber object to read laser scanner measurements from the robot.


go = Twist()

rospy.spin() # Program executes continuously till it is stopped manually.



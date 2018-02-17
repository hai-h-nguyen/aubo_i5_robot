#The ROS Node Publisher template

#!usr/bin/env python

#remove or add the library/libraries for ROS
import rospy, time, math, random

#remove or add the message type
from std_msgs.msg import Int32, Float32, String, Float64, Float64MultiArray, MultiArrayDimension
from time import sleep

#you can define functions to provide the required functionality
def makeMultiArray(gripper_left, gripper_right):
	arrayList = []
	arrayList.append(gripper_left)
	arrayList.append(gripper_right)
        
	dim = MultiArrayDimension()
	dim.size = 2
	dim.label = ''
	dim.stride = 1
 
	tempArray = Float64MultiArray()
	tempArray.data = arrayList
	tempArray.layout.dim.append(dim)
	tempArray.layout.data_offset = 0
	return tempArray

if __name__=='__main__':
    #add here the node name. In ROS, nodes are unique named.
    rospy.init_node('ref_publisher')

    #publish messages to a topic using rospy.Publisher class
    shoulder_pub = rospy.Publisher('/shoulder_joint_controller/command', Float64, queue_size=10)
    foreArm_pub = rospy.Publisher('/foreArm_joint_controller/command', Float64, queue_size=10)
    upperArm_pub = rospy.Publisher('/upperArm_joint_controller/command', Float64, queue_size=10)
    wrist1_pub = rospy.Publisher('/wrist1_joint_controller/command', Float64, queue_size=10)
    wrist2_pub = rospy.Publisher('/wrist2_joint_controller/command', Float64, queue_size=10)
    wrist3_pub = rospy.Publisher('/wrist3_joint_controller/command', Float64, queue_size=10)
    
    gripper_pub = rospy.Publisher('/gripper_controller/command', Float64MultiArray, queue_size=10)
    data = 0.0
    
    #set a publishing rate. Below is a publishing rate of 10 times/second
    rate=rospy.Rate(20)

    while not rospy.is_shutdown():
		shoulder_pub.publish(0.0)
		foreArm_pub.publish(data)
		upperArm_pub.publish(data)
		wrist1_pub.publish(data)
		wrist2_pub.publish(data)
		wrist3_pub.publish(1.0)
		
		gripper_pub.publish(makeMultiArray(0.5, 0.5))
		
		rate.sleep()
		



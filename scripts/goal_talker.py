#!/usr/bin/env python
import rospy
import geometry_msgs.msg

rospy.init_node("fake_goal")
pub = rospy.Publisher("/move_base_simple/goal", geometry_msgs.msg.PoseStamped, queue_size=10)
msg = geometry_msgs.msg.PoseStamped()
msg.header.frame_id = "/map"
msg.pose.position.x = 2
msg.pose.position.y = 2
msg.pose.orientation.w = 1
while not rospy.is_shutdown():
	msg.header.stamp = rospy.Time.now()
	pub.publish(msg)
#!/usr/bin/env python
import rospy
import geometry_msgs.msg
import tf

rospy.init_node("fake_goal")
pub = rospy.Publisher("/move_base_simple/goal", geometry_msgs.msg.PoseStamped, queue_size=10)
msg = geometry_msgs.msg.PoseStamped()
msg.header.frame_id = "/map"
msg.pose.position.x = 0.5
msg.pose.position.y = 0
ori = tf.transformations.quaternion_from_euler(0,0,2)
msg.pose.orientation.x = ori[0]
msg.pose.orientation.y = ori[1]
msg.pose.orientation.z = ori[2]
msg.pose.orientation.w = ori[3]
while not rospy.is_shutdown():
	msg.header.stamp = rospy.Time.now()
	pub.publish(msg)
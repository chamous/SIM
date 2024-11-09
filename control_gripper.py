#! /usr/bin/env python


import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_execute_trajectory', anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
gripper_group = moveit_commander.MoveGroupCommander("gripper")
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=1)

gripper_group_variable_values = gripper_group.get_current_joint_values()

##### OPEN ######
print "Opening Gripper..."
gripper_group_variable_values[0] = 00.010
gripper_group.set_joint_value_target(gripper_group_variable_values)
plan2 = gripper_group.go()
gripper_group.stop()
gripper_group.clear_pose_targets()

rospy.sleep(3)

##### CLOSE ######
print "Closing Gripper..."
gripper_group_variable_values[0] = -00.010
gripper_group.set_joint_value_target(gripper_group_variable_values)
plan2 = gripper_group.go()
gripper_group.stop()
gripper_group.clear_pose_targets()

rospy.sleep(1)

moveit_commander.roscpp_shutdown()

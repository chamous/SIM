#! /usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_get_data', anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group_arm = moveit_commander.MoveGroupCommander("arm")
group_gripper = moveit_commander.MoveGroupCommander("gripper")
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=1)

########### ROBOT INFO ##############

#Get a RobotState message describing the current state of the robot
print "Robot State: %s" %robot.get_current_state()

#Get the names of the groups defined for the robot
print "Robot Groups: %s" %robot.get_group_names()

########### ARM INFO #############

#Get the name of the frame where all planning is performed
print "Reference frame: %s" % group_arm.get_planning_frame()

#Get the name of the link that is considered to be an end-effector. Return an empty string if there is no end-effector.
print "End Effectors: %s" %group_arm.get_end_effector_link()

#Get the current configuration of the group as a list (these are values published on /joint_states) 
print "Current Joint Values: %s" %group_arm.get_current_joint_values()

#Get the current pose of the end-effector of the group. Throws an exception if there is not end-effector. 
print "Current Pose: %s" %group_arm.get_current_pose()

#Specify the amount of time to be used for motion planning. 
print "Planning time: %s" %group_arm.get_planning_time()

#Get the active joints of this group 
print "Active Joints: %s" %group_arm.get_active_joints()

#Get a list of all the names of joint configurations.
print "Named Groups: %s" %group_arm.get_named_targets()
#Get a dictionary of joint values of a named target
print "%s" %group_arm.get_named_target_values('home')

########### GRIPPER INFO #############
print "Named Groups: %s" %group_gripper.get_named_targets()
print "%s" %group_gripper.get_named_target_values('open')
print "%s" %group_gripper.get_named_target_values('close')

moveit_commander.roscpp_shutdown()

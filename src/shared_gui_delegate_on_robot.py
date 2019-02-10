"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Hongyu Liu, Xinlai Chen, Zichen Tan.
  Winter term, 2018-2019.
"""


class DelegateThatReceives(object):
    def __init__(self, robot):
        """ :type robot: rosebot.Robot"""
        self.robot = robot

    def forward(self, left_wheel_speed, right_wheel_speed):
        self.robot.drive_system.go(int(left_wheel_speed), int(right_wheel_speed))

    def stop(self):
        self.robot.drive_system.stop()

    def backward(self,left_wheel_speed, right_wheel_speed):
        self.robot.drive_system.go(-int(left_wheel_speed), -int(right_wheel_speed))

    def calibrate_arm(self):
        self.robot.arm_and_claw.calibrate_arm()

    def raise_arm(self):
        self.robot.arm_and_claw.raise_arm()

    def lower_arm(self):
        self.robot.arm_and_claw.lower_arm()

    def move_arm_to_position(self, position):
        self.robot.arm_and_claw.move_arm_to_position(int(position))

    def left(self, left_wheel_speed, right_wheel_speed):
        self.robot.drive_system.left(int(left_wheel_speed),int(right_wheel_speed))

    def right(self, left_wheel_speed, right_wheel_speed):
        self.robot.drive_system.right(int(left_wheel_speed),int(right_wheel_speed))

    def go_straight_for_seconds(self, seconds, speed):
        self.robot.drive_system.go_straight_for_seconds(int(seconds), int(speed))
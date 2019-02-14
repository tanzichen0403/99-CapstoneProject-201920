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
        self.is_time_to_stop = False

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

    def go_straight_for_inches_using_time(self, inches, speed):
        self.robot.drive_system.go_straight_for_inches_using_time(int(inches), int(speed))

    def go_straight_for_inches_using_encoder(self, inches, speed):
        self.robot.drive_system.go_straight_for_inches_using_encoder(int(inches), int(speed))

    def quit(self):
        print('got quit')
        self.is_time_to_stop = True

    def beep(self, n):
        self.robot.sound_system.beep_for_n_time(int(n))

    def play_a_tone_for_a_givien_frenquency(self, freq, dur):
        self.robot.sound_system.play_a_tone_for_a_givien_frenquency(int(freq),int(dur))

    def speaker(self, x):
        self.robot.sound_system.say_a_phrase(str(x))

    def beep_and_run(self, init,rate, speed):
        ""
        self.robot.m1_beep_while_apporach(init,rate,speed)

    def trace_item(self, forward_speed,spin_speed):
        ""
        self.robot.m1_carmra(self,forward_speed,spin_speed)
    def line_followingd(self,speed):
        self.robot.m1_Bang_bang_control(speed)
        ""

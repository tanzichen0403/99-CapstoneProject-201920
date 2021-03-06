"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Hongyu Liu.
  Winter term, 2018-2019.
"""

import rosebot
import mqtt_remote_method_calls as com
import time
import shared_gui_delegate_on_robot

def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """
    # run_test_arm()
    # run_test_calibrate_arm()
    real_thing()
    # run_test_camera(50,30)
    # run_test_led(2,50)
    # run_test_led2()


def run_test_arm():
    robot = rosebot.RoseBot()
    robot.arm_and_claw.raise_arm()

def run_test_calibrate_arm():
    robot = rosebot.RoseBot()
    robot.arm_and_claw.calibrate_arm()

def real_thing():
    robot = rosebot.RoseBot()
    delegate_that_receives = shared_gui_delegate_on_robot.DelegateThatReceives(robot)
    mqtt_receiver = com.MqttClient(delegate_that_receives)
    mqtt_receiver.connect_to_pc()

    while True:
        time.sleep(0.01)
        if delegate_that_receives.is_time_to_stop:
            break

def run_test_camera(speed1, speed2):
    robot = rosebot.RoseBot()
    a = speed1
    b = speed2
    robot.m1_carmra(a,b)

def run_test_led(initial, rate_of_increase):
    robot = rosebot.RoseBot()
    robot.m3_led(initial,rate_of_increase)

def run_test_led2():
    robot = rosebot.RoseBot()
    robot.led_system.right_led.turn_on()
    robot.led_system.left_led.turn_on()
# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
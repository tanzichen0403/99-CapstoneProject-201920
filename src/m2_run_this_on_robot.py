"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Xinlai Chen.
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
    run_test_arm()
    real_thing()

def run_test_arm():
    robot=rosebot.RoseBot()
    robot.arm_and_claw.lower_arm()

def real_thing():
    robot=rosebot.RoseBot()
    delegate_that_receives=shared_gui_delegate_on_robot.DegelateThatReceives(robot)
    mqtt_receiver=com.MqttClient(delegate_that_receives)
    mqtt_receiver.connect_to_pc()
    while True:
        time.sleep(0.01)
        if delegate.is_time_to_stop:
            break
# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
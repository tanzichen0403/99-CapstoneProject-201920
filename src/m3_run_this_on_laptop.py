"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Hongyu Liu.
  Winter term, 2018-2019.
"""

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import shared_gui


def main():
    """
    This code, which must run on a LAPTOP:
      1. Constructs a GUI for my part of the Capstone Project.
      2. Communicates via MQTT with the code that runs on the EV3 robot.
    """
    # -------------------------------------------------------------------------
    # Construct and connect the MQTT Client:
    # -------------------------------------------------------------------------
    mqtt_sender = com.MqttClient()  #If put things in () it will be a receiver.
    mqtt_sender.connect_to_ev3()


    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------
    root = tkinter.Tk()
    root.title('CSSE120 Capstone Project, Winter 2018-2019')


    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main_frame = ttk.Frame(root, padding = 10, borderwidth=5, relief='groove')
    main_frame.grid()



    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    teleop_frame, arm_frame, control_arm, drive_system_frame, sound_system_frame, m3_personal_frame, m3_camera_frame, m3_led_frame, m3_do_math_frame = get_shared_frames(main_frame, mqtt_sender)

    # exit button:


    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # done: Implement and call get_my_frames(...)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(teleop_frame, arm_frame, control_arm, drive_system_frame, sound_system_frame, m3_personal_frame, m3_camera_frame, m3_led_frame, m3_do_math_frame)

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()


def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame = shared_gui.get_teleoperation_frame(main_frame, mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(main_frame, mqtt_sender)
    control_arm = shared_gui.get_control_frame(main_frame, mqtt_sender)
    drive_system_frame = shared_gui.get_drivesystem_frame(main_frame, mqtt_sender)
    sound_system_frame = shared_gui.get_soundsystem_frame(main_frame, mqtt_sender)
    m3_personal_frame=shared_gui.m3_personal_frame(main_frame,mqtt_sender)
    m3_camera_frame=shared_gui.m3_carmer_frame(main_frame, mqtt_sender)
    m3_led_frame = shared_gui.get_m3_led_frame(main_frame, mqtt_sender)
    m3_do_math_frame = shared_gui.get_m3_do_math_frame(main_frame, mqtt_sender)

    return teleop_frame, arm_frame, control_arm, drive_system_frame, sound_system_frame, m3_personal_frame, m3_camera_frame, m3_led_frame, m3_do_math_frame


def grid_frames(teleop_frame, arm_frame, control_frame, drive_system_frame, sound_system_frame, m3_personal_frame,m3_camera_frame, m3_led_frame, m3_do_math_frame):
    teleop_frame.grid(row=0, column=0)
    arm_frame.grid(row=1,column=0)
    control_frame.grid(row=2, column=0)
    drive_system_frame.grid(row=3,column=0)
    sound_system_frame.grid(row=0,column=1)
    m3_personal_frame.grid(row=1,column=1)
    m3_camera_frame.grid(row=2,column=1)
    m3_led_frame.grid(row=3, column=1)
    m3_do_math_frame.grid(row=0, column=2)

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
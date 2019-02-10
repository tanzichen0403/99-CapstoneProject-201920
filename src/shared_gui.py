"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Constructs and returns Frame objects for the basics:
  -- teleoperation
  -- arm movement
  -- stopping the robot program

  This code is SHARED by all team members.  It contains both:
    -- High-level, general-purpose methods for a Snatch3r EV3 robot.
    -- Lower-level code to interact with the EV3 robot library.

  Author:  Your professors (for the framework and lower-level code)
    and Hongyu Liu, Xinlai Chen, Zichen Tan.
  Winter term, 2018-2019.
"""

import tkinter
from tkinter import ttk
import time


def get_teleoperation_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's motion
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Teleoperation")
    left_speed_label = ttk.Label(frame, text="Left wheel speed (0 to 100)")
    right_speed_label = ttk.Label(frame, text="Right wheel speed (0 to 100)")

    left_speed_entry = ttk.Entry(frame, width=8)
    left_speed_entry.insert(0, "100")
    right_speed_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "100")

    forward_button = ttk.Button(frame, text="Forward")
    backward_button = ttk.Button(frame, text="Backward")
    left_button = ttk.Button(frame, text="Left")
    right_button = ttk.Button(frame, text="Right")
    stop_button = ttk.Button(frame, text="Stop")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    left_speed_label.grid(row=1, column=0)
    right_speed_label.grid(row=1, column=2)
    left_speed_entry.grid(row=2, column=0)
    right_speed_entry.grid(row=2, column=2)

    forward_button.grid(row=3, column=1)
    left_button.grid(row=4, column=0)
    stop_button.grid(row=4, column=1)
    right_button.grid(row=4, column=2)
    backward_button.grid(row=5, column=1)

    # Set the button callbacks:
    forward_button["command"] = lambda: handle_forward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    backward_button["command"] = lambda: handle_backward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    left_button["command"] = lambda: handle_left(
        left_speed_entry, right_speed_entry, mqtt_sender)
    right_button["command"] = lambda: handle_right(
        left_speed_entry, right_speed_entry, mqtt_sender)
    stop_button["command"] = lambda: handle_stop(mqtt_sender)

    return frame


def get_arm_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's Arm
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Arm and Claw")
    position_label = ttk.Label(frame, text="Desired arm position:")
    position_entry = ttk.Entry(frame, width=8)

    raise_arm_button = ttk.Button(frame, text="Raise arm")
    lower_arm_button = ttk.Button(frame, text="Lower arm")
    calibrate_arm_button = ttk.Button(frame, text="Calibrate arm")
    move_arm_button = ttk.Button(frame,
                                 text="Move arm to position (0 to 5112)")
    blank_label = ttk.Label(frame, text="")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    position_label.grid(row=1, column=0)
    position_entry.grid(row=1, column=1)
    move_arm_button.grid(row=1, column=2)

    blank_label.grid(row=2, column=1)
    raise_arm_button.grid(row=3, column=0)
    lower_arm_button.grid(row=3, column=1)
    calibrate_arm_button.grid(row=3, column=2)

    # Set the Button callbacks:
    raise_arm_button["command"] = lambda: handle_raise_arm(mqtt_sender)
    lower_arm_button["command"] = lambda: handle_lower_arm(mqtt_sender)
    calibrate_arm_button["command"] = lambda: handle_calibrate_arm(mqtt_sender)
    move_arm_button["command"] = lambda: handle_move_arm_to_position(
        position_entry, mqtt_sender)

    return frame


def get_control_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame has
    Button objects to exit this program and/or the robot's program (via MQTT).
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Control")
    quit_robot_button = ttk.Button(frame, text="Stop the robot's program")
    exit_button = ttk.Button(frame, text="Stop this and the robot's program")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    quit_robot_button.grid(row=1, column=0)
    exit_button.grid(row=1, column=2)

    # Set the Button callbacks:
    quit_robot_button["command"] = lambda: handle_quit(mqtt_sender)
    exit_button["command"] = lambda: handle_exit(mqtt_sender)

    return frame


def get_drivesystem_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's motion
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")


    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="DriveSystem")

    speed_label = ttk.Label(frame, text="Enter the speed",anchor=tkinter.W,justify=tkinter.LEFT)
    speed_entry = ttk.Entry(frame, width=8,justify=tkinter.LEFT)
    speed_entry.insert(0, "100")

    second_label = ttk.Label(frame, text="How many seconds do you want to go",anchor=tkinter.W,justify=tkinter.LEFT)
    second_entry = ttk.Entry(frame, width=8,justify=tkinter.LEFT)
    second_entry.insert(0, "10")

    inches_label = ttk.Label(frame, text="How many inches do you want to go",anchor=tkinter.W,justify=tkinter.LEFT)
    inches_entry = ttk.Entry(frame, width=8,justify=tkinter.LEFT)
    inches_entry.insert(0, "10")

    encoder_label = ttk.Label(frame, text="How many inches do you want to go(by using encoder)",anchor=tkinter.W,justify=tkinter.LEFT)
    encoder_entry = ttk.Entry(frame, width=8, justify=tkinter.LEFT)
    encoder_entry.insert(0, "10")

    second_button = ttk.Button(frame, text="Go for seconds")
    inches_button = ttk.Button(frame, text="Go for inches")
    encoder_button = ttk.Button(frame, text='Go for inchers(encoder)')

    # Grid the widgets:
    frame_label.grid(row=0, column=1)

    speed_label.grid(row=1, column=0)
    speed_entry.grid(row=2, column=0)

    second_label.grid(row=3, column=0)
    second_entry.grid(row=4, column=0)
    second_button.grid(row=4, column=2)

    inches_label.grid(row=5, column=0)
    inches_entry.grid(row=6, column=0)
    inches_button.grid(row=6, column=2)

    encoder_label.grid(row=7, column=0)
    encoder_entry.grid(row=8, column=0)
    encoder_button.grid(row=8, column=2)

    # Set the button callbacks:
    second_button["command"] = lambda: handle_go_straight_for_seconds(second_entry, speed_entry, mqtt_sender)
    inches_button["command"] = lambda: handle_go_straight_for_inches_using_time(inches_entry, speed_entry,mqtt_sender)
    encoder_button["command"] = lambda: handle_go_straight_for_inches_using_encoder(encoder_button, speed_entry,
                                                                                    mqtt_sender)

    return frame

def get_soundsystem_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's motion
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")


    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Soundsystem")

    beeper_label = ttk.Label(frame, text="How many times you want to beep")
    beeper_entry = ttk.Entry(frame, width=8)
    beeper_entry.insert(0, "10")

    fren_label = ttk.Label(frame, text="Which frequency do you want to play?")
    fren_entry = ttk.Entry(frame, width=8)
    fren_entry.insert(0, "1000")

    Dur_label = ttk.Label(frame, text="How long do you want to play")
    Dur_entry = ttk.Entry(frame, width=8)
    Dur_entry.insert(0, "10")

    Phrase_label = ttk.Label(frame, text="What do you want to say?")
    Phrase_entry = ttk.Entry(frame, width=20, justify=tkinter.LEFT)
    Phrase_entry.insert(0, "Hey Jarvis")

    beeper_button = ttk.Button(frame, text="Beep!")
    Tone_button = ttk.Button(frame, text="Make A Tone!")
    Phrase_button = ttk.Button(frame, text='Say it!')


    #
    frame_label.grid(row=0, column=1)

    beeper_label.grid(row=1, column=0)
    beeper_entry.grid(row=2, column=0)
    beeper_button.grid(row=2,column=2)

    fren_label.grid(row=4, column=0)
    fren_entry.grid(row=5, column=0)
    Dur_label.grid(row=6, column=0)
    Dur_entry.grid(row=7, column=0)
    Tone_button.grid(row=7, column=2)

    Phrase_label.grid(row=9, column=0)
    Phrase_entry.grid(row=10, column=0)
    Phrase_button.grid(row=10, column=2)



    # Set the button callbacks:
    beeper_button["command"] = lambda: handle_beep(beeper_entry,mqtt_sender)
    Tone_button["command"] = lambda: handle_tone(fren_entry,Dur_entry,mqtt_sender)
    Phrase_button["command"] = lambda: say_a_pharse(Phrase_entry)

    return frame
###############################################################################
###############################################################################
# The following specifies, for each Button,
# what should happen when the Button is pressed.
###############################################################################
###############################################################################

###############################################################################
# Handlers for Buttons in the Teleoperation frame.
###############################################################################
def handle_forward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    with the speeds used as given.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print('forward',left_entry_box.get(),right_entry_box.get())
    mqtt_sender.send_message('forward',[left_entry_box.get(),right_entry_box.get()])

def handle_backward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negatives of the speeds in the entry boxes.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print('backward',left_entry_box.get(),right_entry_box.get())
    mqtt_sender.send_message('backward',[left_entry_box.get(),right_entry_box.get()])

def handle_left(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the left entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print('left', left_entry_box.get(),right_entry_box.get())
    mqtt_sender.send_message('left', [left_entry_box.get(),right_entry_box.get()])

def handle_right(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the right entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print('right', left_entry_box.get(),right_entry_box.get())
    mqtt_sender.send_message('right', [left_entry_box.get(),right_entry_box.get()])


def handle_stop(mqtt_sender):
    """
    Tells the robot to stop.
      :type  mqtt_sender:  com.MqttClient
    """
    print('stop')
    mqtt_sender.send_message('stop')

###############################################################################
# Handlers for Buttons in the ArmAndClaw frame.
###############################################################################
def handle_raise_arm(mqtt_sender):
    """
    Tells the robot to raise its Arm until its touch sensor is pressed.
      :type  mqtt_sender:  com.MqttClient
    """
    print('raise arm')
    mqtt_sender.send_message('raise_arm')


def handle_lower_arm(mqtt_sender):
    """
    Tells the robot to lower its Arm until it is all the way down.
      :type  mqtt_sender:  com.MqttClient
    """
    print('lower arm')
    mqtt_sender.send_message('lower_arm')


def handle_calibrate_arm(mqtt_sender):
    """
    Tells the robot to calibrate its Arm, that is, first to raise its Arm
    until its touch sensor is pressed, then to lower its Arm until it is
    all the way down, and then to mark taht position as position 0.
      :type  mqtt_sender:  com.MqttClient
    """
    print('calibrate arm')
    mqtt_sender.send_message('calibrate_arm')

def handle_move_arm_to_position(arm_position_entry, mqtt_sender):
    """
    Tells the robot to move its Arm to the position in the given Entry box.
    The robot must have previously calibrated its Arm.
      :type  arm_position_entry  ttk.Entry
      :type  mqtt_sender:        com.MqttClient
    """
    print('move arm to position')
    mqtt_sender.send_message('move_arm_to_position',[arm_position_entry.get()])

def handle_go_straight_for_seconds(seconds,speed, mqtt_sender):
    ""
    print('go straight for seconds')
    mqtt_sender.send_message('go_straight_for_seconds', [seconds.get(), speed.get()])

def handle_go_straight_for_inches_using_time(inches,speed, mqtt_sender):
    ""

def handle_go_straight_for_inches_using_encoder(inches,speed, mqtt_sender):
    ""
def handle_beep(n,mqtt_sender):
    ""
def handle_tone(fren,Dur,mqtt_sender):
    ""
def say_a_pharse(x):
    ""
###############################################################################
# Handlers for Buttons in the Control frame.
###############################################################################
def handle_quit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
      :type  mqtt_sender:  com.MqttClient
    """


def handle_exit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
    Then exit this program.
      :type mqtt_sender: com.MqttClient
    """

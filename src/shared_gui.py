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
    frame_label.grid(row=0, column=1,sticky='w')

    speed_label.grid(row=1, column=0,sticky='w')
    speed_entry.grid(row=2, column=0,sticky='w')

    second_label.grid(row=3, column=0,sticky='w')
    second_entry.grid(row=4, column=0,sticky='w')
    second_button.grid(row=4, column=2)

    inches_label.grid(row=5, column=0,sticky='w')
    inches_entry.grid(row=6, column=0,sticky='w')
    inches_button.grid(row=6, column=2)

    encoder_label.grid(row=7, column=0,sticky='w')
    encoder_entry.grid(row=8, column=0,sticky='w')
    encoder_button.grid(row=8, column=2)

    # Set the button callbacks:
    second_button["command"] = lambda: handle_go_straight_for_seconds(second_entry, speed_entry, mqtt_sender)
    inches_button["command"] = lambda: handle_go_straight_for_inches_using_time(inches_entry, speed_entry,mqtt_sender)
    encoder_button["command"] = lambda: handle_go_straight_for_inches_using_encoder(encoder_entry, speed_entry,
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

    beeper_label = ttk.Label(frame, text="How many times you want to beep?")
    beeper_entry = ttk.Entry(frame, width=8)
    beeper_entry.insert(0, "10")

    fren_label = ttk.Label(frame, text="Which frequency do you want to play?")
    fren_entry = ttk.Entry(frame, width=8)
    fren_entry.insert(0, "1000")

    Dur_label = ttk.Label(frame, text="How long do you want to play?")
    Dur_entry = ttk.Entry(frame, width=8)
    Dur_entry.insert(0, "10")

    Phrase_label = ttk.Label(frame, text="What do you want to say?")
    Phrase_entry = ttk.Entry(frame, width=40, justify=tkinter.LEFT)
    Phrase_entry.insert(0, "Welcome home sir, I am Jarvis")

    beeper_button = ttk.Button(frame, text="Beep!")
    Tone_button = ttk.Button(frame, text="Make A Tone!")
    Phrase_button = ttk.Button(frame, text='Say it!')


    #
    frame_label.grid(row=0, column=1)

    beeper_label.grid(row=1, column=0,sticky='w')
    beeper_entry.grid(row=2, column=0,sticky='w')
    beeper_button.grid(row=2,column=2)

    fren_label.grid(row=4, column=0,sticky='w')
    fren_entry.grid(row=5, column=0,sticky='w')
    Dur_label.grid(row=6, column=0,sticky='w')
    Dur_entry.grid(row=7, column=0,sticky='w')
    Tone_button.grid(row=7, column=2)

    Phrase_label.grid(row=9, column=0,sticky='w')
    Phrase_entry.grid(row=10, column=0,sticky='w')
    Phrase_button.grid(row=10, column=2)



    # Set the button callbacks:
    beeper_button["command"] = lambda: handle_beep(beeper_entry,mqtt_sender)
    Tone_button["command"] = lambda: handle_tone(fren_entry,Dur_entry,mqtt_sender)
    Phrase_button["command"] = lambda: say_a_pharse(Phrase_entry, mqtt_sender)

    return frame

def m1_personal_frame(window, mqtt_sender):
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
    frame_label = ttk.Label(frame, text="m1_JARVIS")

    speed_label = ttk.Label(frame, text="Enter the speed",anchor=tkinter.W,justify=tkinter.LEFT)
    speed_entry = ttk.Entry(frame, width=8,justify=tkinter.LEFT)
    speed_entry.insert(0, "100")

    init_fren_label = ttk.Label(frame, text="Enter your initial beep pace",anchor=tkinter.W,justify=tkinter.LEFT)
    init_fren_entry = ttk.Entry(frame, width=8,justify=tkinter.LEFT)
    init_fren_entry.insert(0, "3")

    rate_label = ttk.Label(frame, text="Enter the rate of increase of the frequencies",anchor=tkinter.W,justify=tkinter.LEFT)
    rate_entry = ttk.Entry(frame, width=8,justify=tkinter.LEFT)
    rate_entry.insert(0, "1")

    trace_color_label = ttk.Label(frame, text="Which color you want this robot to trace?",anchor=tkinter.W,justify=tkinter.LEFT)
    trace_color_entry = ttk.Entry(frame, width=8, justify=tkinter.LEFT)
    trace_color_entry.insert(0, "Blue")

    beep_while_run_button = ttk.Button(frame, text="beep_while_run")
    trace_button = ttk.Button(frame, text="Find the color")
    line_follow_button = ttk.Button(frame, text='Follow the line')

    # Grid the widgets:
    frame_label.grid(row=0, column=2,sticky='w')

    speed_label.grid(row=1, column=0,sticky='w')
    speed_entry.grid(row=1, column=4,sticky='w')

    init_fren_label.grid(row=2, column=0,sticky='w')
    init_fren_entry.grid(row=2, column=4,sticky='w')

    rate_label.grid(row=3, column=0,sticky='w')
    rate_entry.grid(row=3, column=4,sticky='w')
    beep_while_run_button.grid(row=4, column=4)

    trace_color_label.grid(row=5, column=0,sticky='w')
    trace_color_entry.grid(row=5, column=4,sticky='w')
    trace_button.grid(row=6, column=4)

    line_follow_button.grid(row=7,column=4)
    # Set the button callbacks:
    beep_while_run_button["command"] = lambda: beep_and_run(init_fren_entry,rate_entry, speed_entry, mqtt_sender)
    trace_button["command"] = lambda: trace_color(trace_color_entry, speed_entry,mqtt_sender)
    line_follow_button["command"] = lambda: line_following(speed_entry,mqtt_sender)

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
    print('go straight for inches using time')
    mqtt_sender.send_message('go_straight_for_inches_using_time', [inches.get(),speed.get()])

def handle_go_straight_for_inches_using_encoder(inches,speed, mqtt_sender):
    ""
    print('go_straight_for_inches_using_encoder')
    mqtt_sender.send_message('go_straight_for_inches_using_encoder', [inches.get(), speed.get()])

def handle_beep(n,mqtt_sender):
    ""
    print('beep',n.get())
    mqtt_sender.send_message('beep', [n.get()])

def handle_tone(fren,dur, mqtt_sender):
    ""
    print('play_a_tone_for_a_givien_frenquency')
    mqtt_sender.send_message('play_a_tone_for_a_givien_frenquency', [fren.get(),dur.get()])

def say_a_pharse(x, mqtt_sender):
    ""
    print('say_a_phrase')
    mqtt_sender.send_message('speaker', [x.get()])

###############################################################################
# Handlers for Buttons in the Control frame.
###############################################################################
def handle_quit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
      :type  mqtt_sender:  com.MqttClient
    """
    print('quit')
    mqtt_sender.send_message('quit')

def handle_exit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
    Then exit this program.
      :type mqtt_sender: com.MqttClient
    """
    print('exit')
    handle_quit(mqtt_sender)
    exit()
def beep_and_run(init_fren,rate,speed,mqtt):
    ""
    print('beep and run')
    mqtt.send_message('beep_and_run',[int(init_fren.get()),int(rate.get()),int(speed.get())])
def trace_color(color,speed,mqtt):
    ""

def line_following(speed,mqtt):
    ""
    mqtt.send_message('line_followingd',[int(speed.get())])
import tkinter
from tkinter import ttk
import time


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

    speed_label = ttk.Label(frame, text="Enter the speed", anchor=tkinter.W, justify=tkinter.LEFT)
    speed_entry = ttk.Entry(frame, width=8, justify=tkinter.LEFT)
    speed_entry.insert(0, "100")

    init_fren_label = ttk.Label(frame, text="Enter your initial beep pace", anchor=tkinter.W, justify=tkinter.LEFT)
    init_fren_entry = ttk.Entry(frame, width=8, justify=tkinter.LEFT)
    init_fren_entry.insert(0, "3")

    rate_label = ttk.Label(frame, text="Enter the rate of increase of the frequencies", anchor=tkinter.W,
                           justify=tkinter.LEFT)
    rate_entry = ttk.Entry(frame, width=8, justify=tkinter.LEFT)
    rate_entry.insert(0, "1")

    trace_color_label = ttk.Label(frame, text="Which color you want this robot to trace?", anchor=tkinter.W,
                                  justify=tkinter.LEFT)

    line_following_label = ttk.Label(frame, text="Begin your line following?", anchor=tkinter.W, justify=tkinter.LEFT)
    beep_while_run_button = ttk.Button(frame, text="beep_while_run")
    trace_button = ttk.Button(frame, text="Find the color")
    line_follow_button = ttk.Button(frame, text='Follow the line')

    # Grid the widgets:
    frame_label.grid(row=0, column=2, sticky='w')

    speed_label.grid(row=1, column=0, sticky='w')
    speed_entry.grid(row=1, column=4, sticky='w')

    init_fren_label.grid(row=2, column=0, sticky='w')
    init_fren_entry.grid(row=2, column=4, sticky='w')

    rate_label.grid(row=3, column=0, sticky='w')
    rate_entry.grid(row=3, column=4, sticky='w')
    beep_while_run_button.grid(row=4, column=4)

    trace_color_label.grid(row=6, column=0)
    trace_button.grid(row=6, column=4)

    line_follow_button.grid(row=7, column=4)
    line_following_label.grid(row=7, column=0)
    # Set the button callbacks:
    beep_while_run_button["command"] = lambda: beep_and_run(init_fren_entry, rate_entry, speed_entry, mqtt_sender)
    trace_button["command"] = lambda: trace_color(speed_entry, mqtt_sender)
    line_follow_button["command"] = lambda: line_following(speed_entry, mqtt_sender)

    return frame


def beep_and_run(init_fren, rate, speed, mqtt):
    ""
    print('beep and run')
    mqtt.send_message('beep_and_run', [int(init_fren.get()), int(rate.get()), int(speed.get())])


def trace_color(speed, mqtt):
    ""


def line_following(speed, mqtt):
    ""
    mqtt.send_message('line_followingd', [int(speed.get())])



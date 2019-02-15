"""Hongyu LIU
    Making frames
"""
import shared_gui
import tkinter
from tkinter import ttk

def led_frame(frame, frame_label):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's motion
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """

    initial_label = ttk.Label(frame, text="enter an initial:")
    rate_of_change_label = ttk.Label(frame, text="enter a rate of change(0 to 100):")

    initial_entry = ttk.Entry(frame, width=8)
    initial_entry.insert(0, "2")
    rate_of_change_entry = ttk.Entry(frame, width=8)
    rate_of_change_entry.insert(0, "50")

    run_led_button = ttk.Button(frame, text="Run LED!")

    # Trace color:
    speed_label = ttk.Label(frame, text="enter a speed to trace color:")
    direction_speed_label = ttk.Label(frame, text="enter a direction speed(negative:spin counterclockwise;"
                                            "positive:spin clockwise)")

    speed_entry = ttk.Entry(frame, width=8)
    speed_entry.insert(0,'50')

    direction_speed_entry = ttk.Entry(frame, width=8)
    direction_speed_entry.insert(0, '30')

    trace_button = ttk.Button(frame, text="trace color")

    speed_label.grid(row=3, column=0)
    direction_speed_label.grid(row=4, column=0)
    speed_entry.grid(row=3, column=1)
    direction_speed_entry.grid(row=4, column=1)
    trace_button.grid(row=4, column=2)


    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    initial_label.grid(row=1, column=0)
    initial_entry.grid(row=1, column=1)
    rate_of_change_label.grid(row=2, column=0)
    rate_of_change_entry.grid(row=2, column=1)
    run_led_button.grid(row=2, column=2)

    #button:
    run_led_button['command'] = lambda: shared_gui.handle_run_led(initial_entry,rate_of_change_entry,mqtt_sender)
    trace_button['command'] = lambda: shared_gui.handle_trace(speed_entry,direction_speed_entry, rate_of_change_entry, mqtt_sender)

    return frame
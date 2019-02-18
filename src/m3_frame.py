"""Hongyu LIU
    Making frames
"""
import shared_gui
import tkinter
from tkinter import ttk

def led_frame(frame, frame_label, mqtt_sender):
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
    run_led_button['command'] = lambda: shared_gui.handle_run_led(initial_entry,rate_of_change_entry, mqtt_sender)
    trace_button['command'] = lambda: shared_gui.handle_trace(speed_entry,direction_speed_entry, rate_of_change_entry, mqtt_sender)

    return frame

def get_m3_do_math_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()
    frame_label = ttk.Label(frame, text='Do some math here')
    m3_do_math_frame = m3_frame.math_frame(frame, frame_label, mqtt_sender)

def math_frame(frame, frame_label, mqtt_sender):

    first_label = ttk.Label(frame, text="first number:")
    second_label = ttk.Label(frame, text="+,-,*,/:")
    third_label = ttk.Label(frame, text="second number:")
    forth_label = ttk.Label(frame, text="+,-,*,/:")
    fifth_label = ttk.Label(frame, text="third number:")
    sixth_label = ttk.Label(frame, text="+,-,*,/:")
    seventh_label = ttk.Label(frame, text="forth number:")
    equal_label = ttk.Label(frame, text="=")

    first_entry = ttk.Entry(frame, width=8)
    first_entry.insert(0, "0")
    second_entry = ttk.Entry(frame, width=8)
    second_entry.insert(0, "+")
    third_entry = ttk.Entry(frame, width=8)
    third_entry.insert(0, "0")
    forth_entry = ttk.Entry(frame, width=8)
    forth_entry.insert(0, "+")
    fifth_entry = ttk.Entry(frame, width=8)
    fifth_entry.insert(0, "0")
    sixth_entry = ttk.Entry(frame, width=8)
    sixth_entry.insert(0, "+")
    seventh_entry = ttk.Entry(frame, width=8)
    seventh_entry.insert(0, "0")

    calculate_button = ttk.Button(frame, text="calculate")

# Grid labels
    frame_label.grid(row=0, column=3)
    first_label.grid(row=1, column=0)
    second_label.grid(row=1, column=1)
    third_label.grid(row=1, column=2)
    forth_label.grid(row=1, column=3)
    fifth_label.grid(row=1, column=4)
    sixth_label.grid(row=1, column=5)
    seventh_label.grid(row=1, column=6)

# Grid entrys
    first_entry.grid(row=2, column=0)
    second_entry.grid(row=2, column=1)
    third_entry.grid(row=2, column=2)
    forth_entry.grid(row=2, column=3)
    fifth_entry.grid(row=2, column=4)
    sixth_entry.grid(row=2, column=5)
    seventh_entry.grid(row=2, column=6)
    equal_label.grid(row=2, column=7)

    calculate_button.grid(row=1, column=7)

    #button:
    calculate_button['command'] = lambda: simple_calculate(first_entry,second_entry,third_entry,forth_entry,fifth_entry,sixth_entry,seventh_entry, mqtt_sender)

    return frame

def simple_calculate(first_entry,second_entry,third_entry,forth_entry,fifth_entry,sixth_entry,seventh_entry):
    a = first_entry.get()
    b = second_entry.get()
    c = third_entry.get()
    d = forth_entry.get()
    e = fifth_entry.get()
    f = sixth_entry.get()
    g = seventh_entry.get()

    answer = int(a) + int(c) + int(e) + int(g)
    if b == '-':
        pass


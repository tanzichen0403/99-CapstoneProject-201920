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

    line_follow_button.grid(row=7, column=4)
    line_following_label.grid(row=7, column=0, sticky='w')
    # Set the button callbacks:
    beep_while_run_button["command"] = lambda: beep_and_run(init_fren_entry, rate_entry, speed_entry, mqtt_sender)
    line_follow_button["command"] = lambda: line_following(speed_entry, mqtt_sender)

    return frame


def m1_feature_10(window, mqtt_sender):
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Trace a Object")

    forward_speed_label = ttk.Label(frame, text='set the forward speed', anchor=tkinter.W, justify=tkinter.LEFT)
    forward_speed_entry = ttk.Entry(frame, width=8, justify=tkinter.LEFT)
    forward_speed_entry.insert(0, '50')

    spin_speed_label1 = ttk.Label(frame, text="set the direction and speed of the spin", anchor=tkinter.W,
                                  justify=tkinter.LEFT)
    spin_speed_label2 = ttk.Label(frame, text='Postive-Clockwise; Negative-Counter-clockwise', anchor=tkinter.W)
    spin_speed_entry = ttk.Entry(frame, width=8, justify=tkinter.LEFT)
    spin_speed_entry.insert(0, "50")

    Trace_button = ttk.Button(frame, text='Begin Trace that shit')

    # Grid the widgets:
    frame_label.grid(row=0, column=3, )
    forward_speed_label.grid(row=1, column=0, sticky='w')
    forward_speed_entry.grid(row=1, column=4)
    spin_speed_label1.grid(row=2, column=0, sticky='w')
    spin_speed_label2.grid(row=3, column=0, sticky='w')
    spin_speed_entry.grid(row=3, column=4)
    Trace_button.grid(row=4, column=4)

    Trace_button['command'] = lambda: begin_trace_the_item(forward_speed_entry, spin_speed_entry, mqtt_sender)
    return frame


def key_board_control_frame():
    # Make root, frame and 3 buttons with callbacks.
    root = tkinter.Tk()

    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid()

    left_button = ttk.Button(main_frame, text='Close this window')
    left_button.grid()

    left_button['command'] = lambda: key_close_window(root)

    # root.bind_all('<KeyPress>', lambda event: pressed_a_key(event))
    # root.bind_all('<KeyRelease>', lambda event: released_a_key(event))

    root.bind_all('<Key-W>', lambda event: key_go_forward(event))
    root.bind_all('<Key-S>', lambda event: key_backward(event))
    root.bind_all('<Key-A>', lambda event: key_turn_left(event))
    root.bind_all('<Key-D>', lambda event: key_turn_right(event))
    root.bind_all('<Key-w>', lambda event: key_go_forward(event))
    root.bind_all('<Key-s>', lambda event: key_backward(event))
    root.bind_all('<Key-a>', lambda event: key_turn_left(event))
    root.bind_all('<Key-d>', lambda event: key_turn_right(event))

    root.mainloop()


def beep_and_run(init_fren, rate, speed, mqtt):
    ""
    print('beep and run')
    mqtt.send_message('beep_and_run', [int(init_fren.get()), int(rate.get()), int(speed.get())])


def line_following(speed, mqtt):
    ""
    mqtt.send_message('line_followingd', [int(speed.get())])


def begin_trace_the_item(forward_speed_entry, spin_speed_entry, mqtt):
    print('begin_trace_the_item')
    mqtt.send_message('trace_item', [int(forward_speed_entry.get()), int(spin_speed_entry.get())])

def key_go_forward(event=None):
    # Fancier version that allows EITHER key OR button presses.
    # The former provides the event, the latter does not.
    # It is UN-likely that you will want this fancier version.
    # Instead, use the SIMPLER version per   go_left.
    if event is None:
        print('Button press: ', end='')
    else:
        print('You pressed the ' + event.keysym + ' key: ', end='')
    print('Go forward')

def key_backward(event=None):
    # Fancier version that allows EITHER key OR button presses.
    # The former provides the event, the latter does not.
    # It is UN-likely that you will want this fancier version.
    # Instead, use the SIMPLER version per   go_left.
    if event is None:
        print('Button press: ', end='')
    else:
        print('You pressed the ' + event.keysym + ' key: ', end='')
    print('Backward')

def key_turn_left(event=None):
    # Fancier version that allows EITHER key OR button presses.
    # The former provides the event, the latter does not.
    # It is UN-likely that you will want this fancier version.
    # Instead, use the SIMPLER version per   go_left.
    if event is None:
        print('Button press: ', end='')
    else:
        print('You pressed the ' + event.keysym + ' key: ', end='')
    print('turn left')
def key_turn_right(event=None):
    # Fancier version that allows EITHER key OR button presses.
    # The former provides the event, the latter does not.
    # It is UN-likely that you will want this fancier version.
    # Instead, use the SIMPLER version per   go_left.
    if event is None:
        print('Button press: ', end='')
    else:
        print('You pressed the ' + event.keysym + ' key: ', end='')
    print('Turn right')

def key_close_window(root):
    root.destroy()
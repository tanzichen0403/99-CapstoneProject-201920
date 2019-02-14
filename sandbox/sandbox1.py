# Put whatever you want in this module and do whatever you want with it.
# It exists here as a place where you can "try out" things without harm.
# Zichen Tan
import tkinter
from tkinter import ttk
import time
#
# def get_drivesystem_frame(window, mqtt_sender):
#     """
#     Constructs and returns a frame on the given window, where the frame
#     has Entry and Button objects that control the EV3 robot's motion
#     by passing messages using the given MQTT Sender.
#       :type  window:       ttk.Frame | ttk.Toplevel
#       :type  mqtt_sender:  com.MqttClient
#     """
#     # Construct the frame to return:
#     frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
#     frame.grid()
#
#     # Construct the widgets on the frame:
#     frame_label = ttk.Label(frame, text="DriveSystem")
#
#     speed_label = ttk.Label(frame, text="Enter the speed")
#     speed_entry = ttk.Entry(frame, width=8)
#     speed_entry.insert(0, "100")
#
#     second_label = ttk.Label(frame, text="How many seconds do you want to go")
#     second_entry = ttk.Entry(frame, width=8)
#     second_entry.insert(0, "10")
#
#     inches_label = ttk.Label(frame, text="How many inches do you want to go")
#     inches_entry = ttk.Entry(frame, width=8)
#     inches_entry.insert(0, "10")
#
#     encoder_label = ttk.Label(frame, text="How many inches do you want to go(by using encoder)")
#     encoder_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
#     encoder_entry.insert(0, "10")
#
#     second_button = ttk.Button(frame, text="Go for seconds")
#     inches_button = ttk.Button(frame, text="Go for inches")
#     encoder_button = ttk.Button(frame, text='Go for inchers(encoder)')
#
#
#     # Grid the widgets:
#     frame_label.grid(row=0, column=1)
#
#     speed_label.grid(row=1, column=0)
#     speed_entry.grid(row=2, column=0)
#
#     second_label.grid(row=3, column=0)
#     second_entry.grid(row=4, column=0)
#     second_button.grid(row=4, column=2)
#
#     inches_label.grid(row=5, column=0)
#     inches_entry.grid(row=6, column=0)
#     inches_button.grid(row=6, column=2)
#
#     encoder_label.grid(row=7, column=0)
#     encoder_entry.grid(row=8, column=0)
#     encoder_button.grid(row=8, column=2)
#
#
#
#
#     # Set the button callbacks:
#     second_button["command"] = lambda: handle_go_straight_for_seconds(second_entry,speed_entry,mqtt_sender)
#     inches_button["command"] = lambda: handle_go_straight_for_inches_using_time(inches_entry,speed_entry)
#     encoder_button["command"] = lambda:handle_go_straight_for_inches_using_encoder(encoder_button,speed_entry,mqtt_sender)
#
#     return frame
#
# def get_soundsystem_frame(window, mqtt_sender):
#     """
#     Constructs and returns a frame on the given window, where the frame
#     has Entry and Button objects that control the EV3 robot's motion
#     by passing messages using the given MQTT Sender.
#       :type  window:       ttk.Frame | ttk.Toplevel
#       :type  mqtt_sender:  com.MqttClient
#     """
#     # Construct the frame to return:
#     frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
#     frame.grid()
#
#     # Construct the widgets on the frame:
#     frame_label = ttk.Label(frame, text="Soundsystem")
#
#     beeper_label = ttk.Label(frame, text="How many times you want to beep")
#     beeper_entry = ttk.Entry(frame, width=8)
#     beeper_entry.insert(0, "10")
#
#     fren_label = ttk.Label(frame, text="Which frequency do you want to play?")
#     fren_entry = ttk.Entry(frame, width=8)
#     fren_entry.insert(0, "1000")
#
#     Dur_label = ttk.Label(frame, text="How long do you want to play")
#     Dur_entry = ttk.Entry(frame, width=8)
#     Dur_entry.insert(0, "10")
#
#     Phrase_label = ttk.Label(frame, text="What do you want to say?")
#     Phrase_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
#     Phrase_entry.insert(0, "Hey Jarvis")
#
#     beeper_button = ttk.Button(frame, text="Go for seconds")
#     Tone_button = ttk.Button(frame, text="Go for inches")
#     Phrase_button = ttk.Button(frame, text='Go for inchers(encoder)')
#
#
#     #
#     frame_label.grid(row=0, column=1)
#
#     beeper_label.grid(row=1, column=0)
#     beeper_entry.grid(row=2, column=0)
#     beeper_button.grid(row=2,column=0)
#
#     fren_label.grid(row=3, column=0)
#     fren_entry.grid(row=4, column=0)
#     Dur_label.grid(row=5, column=0)
#     Dur_entry.grid(row=6, column=0)
#     Tone_button.grid(row=7, column=0)
#
#     Phrase_label.grid(row=8, column=0)
#     Phrase_entry.grid(row=9, column=0)
#     Phrase_button.grid(row=9, column=2)
#
#
#
#     # Set the button callbacks:
#     beeper_button["command"] = lambda: handle_beep(beeper_entry,mqtt_sender)
#     Tone_button["command"] = lambda: handle_tone(fren_entry,Dur_entry,mqtt_sender)
#     Phrase_button["command"] = lambda: say_a_pharse(Phrase_entry)
#
#     return frame
#
# def get_soundsystem_frame(window, mqtt_sender):
#     """
#     Constructs and returns a frame on the given window, where the frame
#     has Entry and Button objects that control the EV3 robot's motion
#     by passing messages using the given MQTT Sender.
#       :type  window:       ttk.Frame | ttk.Toplevel
#       :type  mqtt_sender:  com.MqttClient
#     """
#     # Construct the frame to return:
#     frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
#     frame.grid()
#
#     # Construct the widgets on the frame:
#     frame_label = ttk.Label(frame, text="personal control pannel for m1")
#
#     beeper_label = ttk.Label(frame, text="How many times you want to beep")
#     beeper_entry = ttk.Entry(frame, width=8)
#     beeper_entry.insert(0, "10")
#
#     fren_label = ttk.Label(frame, text="Which frequency do you want to play?")
#     fren_entry = ttk.Entry(frame, width=8)
#     fren_entry.insert(0, "1000")
#
#     Dur_label = ttk.Label(frame, text="How long do you want to play")
#     Dur_entry = ttk.Entry(frame, width=8)
#     Dur_entry.insert(0, "10")
#
#     Phrase_label = ttk.Label(frame, text="What do you want to say?")
#     Phrase_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
#     Phrase_entry.insert(0, "Hey Jarvis")
#
#     beeper_button = ttk.Button(frame, text="Go for seconds")
#     Tone_button = ttk.Button(frame, text="Go for inches")
#     Phrase_button = ttk.Button(frame, text='Go for inchers(encoder)')
#
#
#     #
#     frame_label.grid(row=0, column=1)
#
#     beeper_label.grid(row=1, column=0)
#     beeper_entry.grid(row=2, column=0)
#     beeper_button.grid(row=2,column=0)
#
#     fren_label.grid(row=3, column=0)
#     fren_entry.grid(row=4, column=0)
#     Dur_label.grid(row=5, column=0)
#     Dur_entry.grid(row=6, column=0)
#     Tone_button.grid(row=7, column=0)
#
#     Phrase_label.grid(row=8, column=0)
#     Phrase_entry.grid(row=9, column=0)
#     Phrase_button.grid(row=9, column=2)
#
#
#
#     # Set the button callbacks:
#     beeper_button["command"] = lambda: handle_beep(beeper_entry,mqtt_sender)
#     Tone_button["command"] = lambda: handle_tone(fren_entry,Dur_entry,mqtt_sender)
#     Phrase_button["command"] = lambda: say_a_pharse(Phrase_entry)
#
#     return frame
"""
Example showing for tkinter and ttk how to:
  -- 1. BIND callback functions (event-handlers) to KEYBOARD EVENTs.
  -- 2. RESPOND to KEYBOARD events.

There is LOTS more you can do with Events beyond what is shown here.
See the next module for more, and for all (or at least most) of the
details, see Section 30 of:
  tkinterReference-NewMexicoTech.pdf

in the Graphics section of the Resources web page for this course.
That document is also available in html form at:
  http://infohost.nmt.edu/tcc/help/pubs/tkinter/events.html

Authors: David Mutchler and his colleagues
         at Rose-Hulman Institute of Technology.
"""

import tkinter
from tkinter import ttk


def key_board_control_frame():
    # Make root, frame and 3 buttons with callbacks.
    root = tkinter.Tk()

    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid()
    label1=ttk.Label(main_frame,text='In this part')
    label2 = ttk.Label(main_frame, text='You can use your key board to control the robot')
    label3=ttk.Label(main_frame,text='W-Forward')
    label4 = ttk.Label(main_frame, text='S-Backward')
    label5 = ttk.Label(main_frame, text='A-Turn Left')
    label6 = ttk.Label(main_frame, text='D-Turn Right')
    label1.grid(row=0,column=2,sticky='n')
    label2.grid(row=1,column=2,sticky='n')
    label3.grid(row=2,column=2,sticky='n')
    label5.grid(row=3,column=0,sticky='w')
    
    label6.grid(row=3,column=4,sticky='e')
    label4.grid(row=4,column=2,sticky='n')


    close_window_button = ttk.Button(main_frame, text='Close this window')
    close_window_button.grid(column=2)

    close_window_button['command'] = lambda: key_close_window(root)

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

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
key_board_control_frame()
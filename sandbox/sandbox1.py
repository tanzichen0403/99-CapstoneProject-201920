# Put whatever you want in this module and do whatever you want with it.
# It exists here as a place where you can "try out" things without harm.
# Zichen Tan
import tkinter
from tkinter import ttk
import time

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
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="DriveSystem")

    speed_label = ttk.Label(frame, text="Enter the speed")
    speed_entry = ttk.Entry(frame, width=8)
    speed_entry.insert(0, "100")

    second_label = ttk.Label(frame, text="How many seconds do you want to go")
    second_entry = ttk.Entry(frame, width=8)
    second_entry.insert(0, "10")

    inches_label = ttk.Label(frame, text="How many inches do you want to go")
    inches_entry = ttk.Entry(frame, width=8)
    inches_entry.insert(0, "10")

    encoder_label = ttk.Label(frame, text="How many inches do you want to go(by using encoder)")
    encoder_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
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
    second_button["command"] = lambda: handle_go_straight_for_seconds(second_entry,speed_entry,mqtt_sender)
    inches_button["command"] = lambda: handle_go_straight_for_inches_using_time(inches_entry,speed_entry)
    encoder_button["command"] = lambda:handle_go_straight_for_inches_using_encoder(encoder_button,speed_entry,mqtt_sender)

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
    frame.grid()

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
    Phrase_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    Phrase_entry.insert(0, "Hey Jarvis")

    beeper_button = ttk.Button(frame, text="Go for seconds")
    Tone_button = ttk.Button(frame, text="Go for inches")
    Phrase_button = ttk.Button(frame, text='Go for inchers(encoder)')


    #
    frame_label.grid(row=0, column=1)

    beeper_label.grid(row=1, column=0)
    beeper_entry.grid(row=2, column=0)
    beeper_button.grid(row=2,column=0)

    fren_label.grid(row=3, column=0)
    fren_entry.grid(row=4, column=0)
    Dur_label.grid(row=5, column=0)
    Dur_entry.grid(row=6, column=0)
    Tone_button.grid(row=7, column=0)

    Phrase_label.grid(row=8, column=0)
    Phrase_entry.grid(row=9, column=0)
    Phrase_button.grid(row=9, column=2)



    # Set the button callbacks:
    beeper_button["command"] = lambda: handle_beep(beeper_entry,mqtt_sender)
    Tone_button["command"] = lambda: handle_tone(fren_entry,Dur_entry,mqtt_sender)
    Phrase_button["command"] = lambda: say_a_pharse(Phrase_entry)

    return frame
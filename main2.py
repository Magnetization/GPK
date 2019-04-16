import keyboard
import os
import threading
import time
from adjacent import is_adjacent, adjacent_rate
from tkinter import *
from queue import Queue
global keyboard_stream
'''
[keyname, event, time]
'''
keyboard_stream = []
keyboard_record = []
keyboard_pressed = []
previous_space_time = 0
started = False
start_time = 0
def convert_to_ms(time):
    return int(time*1000) % 100000

def do_press(event):
    # init press, start recording
    #global started
    global started
    global start_time
    if not started:
        keyboard_stream.append([event.name, 'press',event.time])
        keyboard_pressed.append(event.name)
        if event.name in ['space','backspace','enter']:
            keyboard_stream.clear()
            keyboard_pressed.clear()
        # for the judgement, add the time evaluation (only care about the press event)
        if len(keyboard_pressed) >= 4 and adjacent_rate(keyboard_pressed) > 2/3:
            print("alert!",keyboard_pressed[-1],keyboard_pressed[-2])
            started = True
            start_time = time.time() # mark the start time

            stop_recording = threading.Timer(2.0, stop_and_process)
            stop_recording.start()
    elif started:
        keyboard_record.append([event.name, 'press',event.time])
        keyboard_pressed.append(event.name)

    #print(event.name, event.scan_code, event.time,"press")

def do_release(event):
    if not started:
        keyboard_stream.append([event.name, 'release', event.time])
    elif started:
        keyboard_record.append([event.name, 'press',event.time])
    #print(event.name, event.scan_code, event.time,"release")
    #keyboard.write("α")


def listen_keyboard():
    #keyboard.add_hotkey('ctrl+q', quit)
    #global_timer = time.time()  # set initial timer
    keyboard.on_press(do_press)
    keyboard.on_release(do_release)

    keyboard.wait('esc')
    print(keyboard_stream)
    print()
    print(keyboard_pressed)
    print()
    print(keyboard_record)
    #print(raw)

def stop_and_process():
    print("stop")
    GUI = threading.Thread(target=start_GUI)
    GUI.start() 


def start_GUI():
    window = Tk()
    # 进入消息循环
    window.title('gpk')   #窗口标题
    window.geometry('400x50')  #窗口尺寸
    
    results = "1. 2. 3. 4. 5."
    options = Label(window, text = results, width = 30, height = 2,anchor=NW,font=("Arial",30))
    options.pack()
    window.mainloop()

if __name__ == '__main__':
    # listen = threading.Thread(target=listen_keyboard)
   
    # listen.start()
    stop_recording = threading.Thread(target=stop_and_process)
    stop_recording.start()

    
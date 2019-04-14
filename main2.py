import keyboard
import os
import threading
import time
from adjacent import is_adjacent, adjacent_rate
import tkinter as tk
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
        if event.name == 'space' or event.name == 'backspace':
            keyboard_stream.clear()
            keyboard_pressed.clear()

        if len(keyboard_pressed) >= 4 and adjacent_rate(keyboard_pressed) > 2/3:
            print("alert!",keyboard_pressed[-1],keyboard_pressed[-2])
            started = True
            start_time = time.time() # mark the start time

            stop_recording = threading.Timer(2.5, stop_and_process)
            stop_recording.start()
    elif started:
        keyboard_record.append([event.name, 'press',event.time])

    #print(event.name, event.scan_code, event.time,"press")

def do_release(event):
    if not started:
        keyboard_stream.append([event.name, 'release', event.time])
    elif started:
        keyboard_record.append([event.name, 'press',event.time])
    #print(event.name, event.scan_code, event.time,"release")
    #keyboard.write("α")

def stop_and_process():
    print("stop")

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

def start_GUI():
    window = tk.Tk()
    # 进入消息循环
    window.title('gpk')   #窗口标题
    window.geometry('200x100')  #窗口尺寸

    window.mainloop()

if __name__ == '__main__':
    listen = threading.Thread(target=listen_keyboard)
    #GUI = threading.Thread(target=start_GUI)
    listen.start()
    #GUI.start() 
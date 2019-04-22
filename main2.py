# -*- coding: utf-8 -*- 
import keyboard
import os
import threading
import time
from adjacent import is_adjacent, adjacent_rate
from tkinter import *
from queue import Queue
from predict import predict
from functools import partial
import numpy as np
global keyboard_stream
'''
[keyname, event, time]
'''
keyboard_stream = []
keyboard_record = []
keyboard_pressed = []
previous_space_time = 0
started = False  # mark that a gesture is on
processed = False  # mark it's in the process step
finished = False
previous_time = 0
def convert_to_ms(time):
    return int(time*1000) % 100000

def do_press(event):
    # init press, start recording
    #global started
    global started
    global previous_time
    global finished
    if not started:
        # record anyway
        keyboard_stream.append([event.name, 'press',event.time])
        keyboard_pressed.append(event.name)
        if event.name in ['space','backspace','enter']:
            keyboard_stream.clear()
            keyboard_pressed.clear()
        else:
            if previous_time == 0:
                # mark the initial of the program
                # then an key press event happen, store it in previous_time
                previous_time = event.time
            elif previous_time  != 0 :
                # mark that a previous key has been pressed 
                if event.time - previous_time  > 0.2:
                    # print("previous",previous_time)
                    # print("now", event.time)
                    keyboard_stream.clear()
                    keyboard_pressed.clear()
                    keyboard_stream.append([event.name, 'press',event.time])
                    keyboard_pressed.append(event.name)
                    previous_time  = event.time
                else:
                    previous_time  = event.time
            
            # for the judgement, add the time evaluation (only care about the press event)
        if len(keyboard_pressed) >= 4 and adjacent_rate(keyboard_pressed) > 2/3:
            #print("alert!",keyboard_pressed[-1],keyboard_pressed[-2])
            print("alert!", keyboard_pressed)
            started = True
            

            stop_recording = threading.Timer(1.5, stop_and_process)
            stop_recording.start()
        
    else:
        if not processed:
            keyboard_record.append([event.name, 'press',event.time])
            keyboard_pressed.append(event.name)
        else:
            if event.name in ['1','2','3','4','5','`'] and len(results) != 0:
                if event.name == '`':
                    #pass
                    for i in range(len(keyboard_pressed)):
                        keyboard.press('backspace')
                    keyboard.press('backspace')
                    finished = True
                    time.sleep(0.2)
                    reset()
                else:
                    for i in range(len(keyboard_pressed)):
                        keyboard.press('backspace')
                    keyboard.press('backspace')
                    keyboard.write(results[int(event.name) - 1])
                    finished = True
                    time.sleep(0.2)
                    reset()
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

def reset():
    
    keyboard_stream.clear()
    keyboard_pressed.clear()
    keyboard_record.clear()
    global started
    global processed
    global finished
    started = False    
    processed = False
    finished = False
    
   

def start_GUI():
    # entering the processing phrase
  
    
    window = Tk()
    # 进入消息循环
    global results
    window.title('gpk')   #窗口标题
    window.geometry('450x60')  #窗口尺寸
    
    print("showing window")
    #results = ["α","β","Ω","π","μ"]
    results = predict(keyboard_pressed)
    options = "1." + results[0] + " 2." + results[1] + " 3." + results[2] + " 4." + results[3] + " 5." + results[4]
    options = Label(window, text = options, width = 30, height = 2,anchor=NW,font=("Consolas",30))
    options.pack()
    raise_window_up(window)
    global processed
    processed = True 


    close_thread = threading.Thread(target=partial(detect_and_close,window))
    close_thread.start()
    window.mainloop()


def raise_window_up(window):
    window.attributes('-topmost', 1)
def raise_window_down(window):
    window.attributes('-topmost', 0)

def detect_and_close(window):
    while(1):
        if finished:
            window.destroy()

if __name__ == '__main__':


    listen = threading.Thread(target=listen_keyboard)

    listen.start()
    # stop_recording = threading.Thread(target=stop_and_process)
    # stop_recording.start()

    
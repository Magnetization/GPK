import keyboard
import os
import threading
from adjacent import is_adjacent, adjacent_rate
import tkinter as tk
from queue import Queue
global keyboard_stream
'''
[keyname, event, time]
'''
keyboard_stream = [[]]
keyboard_pressed = []
previous_space_time = 0
global started
started = False
def convert_to_ms(time):
    return int(time*1000) % 100000

def do_press(event):
    # init press, start recording
    keyboard_stream.append([event.name, 'press',convert_to_ms(event.time)])
    keyboard_pressed.append(event.name)

    #if len(keyboard_pressed) == 2 and is_adjacent(keyboard_pressed[0],keyboard_pressed[1]):
    #if len(keyboard_pressed) >= 2 and is_adjacent(keyboard_pressed[-1],keyboard_pressed[-2]):
    if event.name == 'space':
        keyboard_pressed.clear()
        # if not started:
        #     keyboard_pressed.clear()
        # if started:
        #     keyboard.stop_recording
    if len(keyboard_pressed) >= 3 and adjacent_rate(keyboard_pressed) > 2/3:
        print("alert!",keyboard_pressed[-1][0],keyboard_pressed[-2][0])
        #keyboard.press('backspace')
        # global raw
        # raw = Queue()
        # keyboard.start_recording(recorded_events_queue=raw)
        keyboard_pressed.clear()
    #print(event.name, event.scan_code, event.time,"press")

def do_release(event):
    keyboard_stream.append([event.name, 'release', convert_to_ms(event.time)])
    #print(event.name, event.scan_code, event.time,"release")
    #keyboard.write("α")

def listen_keyboard():
    #keyboard.add_hotkey('ctrl+q', quit) 
    keyboard.on_press(do_press)
    keyboard.on_release(do_release)

    keyboard.wait('esc')
    #print(keyboard_stream)
    print(keyboard_pressed)
    print(raw)

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
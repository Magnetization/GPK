import keyboard
import os
import threading
from adjacent import is_adjacent
import tkinter as tk
global keyboard_stream
'''
[keyname, event, time]
'''
keyboard_stream = [[]]

keyboard_pressed = []

def convert_to_ms(time):
    return int(time*1000) % 100000

def press_show(event):
    keyboard_stream.append([event.name, 'press',convert_to_ms(event.time)])
    keyboard_pressed.append(event.name)
    #if len(keyboard_pressed) == 2 and is_adjacent(keyboard_pressed[0],keyboard_pressed[1]):
    if len(keyboard_pressed) >= 2 and is_adjacent(keyboard_pressed[-1],keyboard_pressed[-2]):
        print("alert!")
        keyboard_pressed.clear()
    #print(event.name, event.scan_code, event.time,"press")

def release_show(event):
    keyboard_stream.append([event.name, 'release', convert_to_ms(event.time)])
    #print(event.name, event.scan_code, event.time,"release")
    #keyboard.write("α")

def listen_keyboard():
    #keyboard.add_hotkey('ctrl+q', quit) 
    keyboard.on_press(press_show)
    keyboard.on_release(release_show)

    keyboard.wait('esc')
    print(keyboard_stream)
    print(keyboard_pressed)

def start_GUI():
    window = tk.Tk()
    # 进入消息循环
    window.title('gpk')   #窗口标题
    window.geometry('200x100')  #窗口尺寸

    window.mainloop()

if __name__ == '__main__':
    listen = threading.Thread(target=listen_keyboard)
    GUI = threading.Thread(target=start_GUI)
    listen.start()
    GUI.start() 
	
# -*- coding: utf-8 -*-
import pythoncom
import pyHook
import time
import os
import tkinter as tk
import time
import threading
# def onKeyboardEvent(event):
#   "处理键盘事件"
#   if str(event.Key) == 'K':
#         os._exit(0)
#   print('-' * 20 + 'Keyboard Begin' + '-' * 20 + '\n')
#   print("Current Time:%s\n" % time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()))
#   print("MessageName:%s\n" % str(event.MessageName))
#   print("Message:%d\n" % event.Message)
#   print("Time:%d\n" % event.Time)
#   print("Window:%s\n" % str(event.Window))
#   print("WindowName:%s\n" % str(event.WindowName))
#   print("Ascii_code: %d\n" % event.Ascii)
#   print("Ascii_char:%s\n" % chr(event.Ascii))
#   print("Key:%s\n" % str(event.Key))
#   print('-' * 20 + 'Keyboard End' + '-' * 20 + '\n')
#   return True
global interval
interbal = 220
global raw_key_time
raw_key_time=[[]]

class KeyBoardManager():
    keyIsPressed = False
    def onKeyDown(self,event):
        if self.keyIsPressed:
            return True
        print(str(event.Key) + ' is pressed' + " Time:%d\n" % event.Time)
        #print("Time:%d\n" % event.Time)
        if str(event.Key) == "Escape":
            print("Exit the program")
            print(raw_key_time)
            os._exit(0)
        else:
            raw_key_time.append([str(event.Key), str(event.Time), 1])
            # 1 stands for press down
        self.keyIsPressed = True
        return True

    def onKeyUp(self,event):
        self.keyIsPressed = False
        print(str(event.Key) + ' is released' + " Time:%d\n" % event.Time)
        raw_key_time.append([str(event.Key), str(event.Time), 0])
        # 0 stands for release up
        return True

def listen_keyboard():
    mykbmanager = KeyBoardManager()
    hookmanager = pyHook.HookManager()
    hookmanager.KeyDown = mykbmanager.onKeyDown
    hookmanager.KeyUp = mykbmanager.onKeyUp
    hookmanager.HookKeyboard()
    pythoncom.PumpMessages()

def calculate_adjacent_rate():
    adjacent = 1
    for i in range(1, len(raw_key_time)):
        current_key = raw_key_time[i][0]
        next_key = raw_key_time[i+1][0]
        if is_adjacent(current_key, next_key):
            adjacent += 1
    return adjacent/(len(raw_key_time) - 1)

# def is_adjacent(key1, key2):


# def first_monitor_key():
#     is_first_time = True
#     init_length = 0
    
#     while(1):
#         if len(raw_key_time - 1) > init_length:
#             if is_first_time:
#                 # first time, need to monitor it all the time
#                 adjacent_rate = calculate_adjacent_rate()
#                 if adjacent_rate > 
#                 is_first_time = False
#             else :
#                 if int(raw_key_time[-1][1]) - int(raw_key_time[-2][1]) > interval :
#                     # show that there is a pause, indicate a stop, and the next input is gliding input
#                     # clear the current raw key
#                     raw_key_time = [[]]
#                     # process and make a prediction
#                     process_gliding()
#                 else :
#                     # still in normal typing mode
#                     # do nothing
#                     # pass
        


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
    #first_monitor = threading.Thread(target=first_monitor_key)
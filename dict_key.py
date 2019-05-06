# -*- coding: utf-8 -*- 
import matplotlib.pyplot as plt
import numpy as np
import random

np.seterr(divide='ignore',invalid='ignore')
global clustered_centroids
clustered_centroids = np.array([[-77.8,25],[-42.64516129,25.32258065],[-12.53125,25.34375],[ 17.53333333,25.36666667],[ 50.05,25.55],[-29.67741935,0],[29.7,0],[-49.77777778,-25.66666667],
    [-19.96428571,-25.64285714],[11.97368421,-25.47368421],[42.13888889,-25.44444444],[77.81818182,-25]])
def decode(str):
    '''
    This function is to transform the key pressed into the 
    corresponding key number  
    '''
    return {
       "0" : 48,
       "1" : 49,
       "2" : 50,
       "3" : 51,
       "4" : 52,
       "5" : 53,
       "6" : 54,
       "7" : 55,
       "8" : 56,
       "9" : 57,
       "a" : 65,
       "b" : 66,
       "c" : 67,
       "d" : 68,
       "e" : 69,
       "f" : 70,
       "g" : 71,
       "h" : 72,
       "i" : 73,
       "j" : 74,
       "k" : 75,
       "l" : 76,
       "m" : 77,
       "n" : 78,
       "o" : 79,
       "p" : 80,
       "q" : 81,
       "r" : 82,
       "s" : 83,
       "t" : 84,
       "u" : 85,
       "v" : 86,
       "w" : 87,
       "x" : 88,
       "y" : 89,
       "z" : 90,
       "-" : 189,
       "=" : 187,
       "`" : 192,
       "[" : 219,
       "]" : 221,
       "|" : 220,
       ";" : 186,
       "\'" : 222,
       "<"  : 188,
       "." : 190,
       "/" : 191,
       "undefined" : 32
    }.get(str,0)    #'error'为默认返回值，可自设置


def decode_keys(num):
    ''' decode the keys back into numbers'''
    return {
        # first row
       0 : "`",
       1 : "1",
       2 : "2",
       3 : "3",
       4 : "4",
       5 : "5",
       6 : "6",
       7 : "7",
       8 : "8",
       9 : "9",
       10 : "0",
       11 : "-",
       12 : "=",
       # second row
       13 : "q",
       14 : "w",
       15 : "e",
       16 : "r",
       17 : "t",
       18 : "y",
       19 : "u",
       20 : "i",
       21 : "o",
       22 : "p",
       23 : "[",
       24 : "]",
       25 : "\\",
       # third row
       26 : "a",
       27 : "s",
       28 : "d",
       29 : "f",
       30 : "g",
       31 : "h",
       32 : "j",
       33 : "k",
       34 : "l",
       35 : ";",
       36 : "'",
        # forth row
       39 : "z",
       40 : "x",
       41 : "c",
       42 : "v",
       43 : "b",
       44 : "n",
       45 : "m",
       46 : ",",
       47 : ".",
       48 : "/",
       # space
       53 : "undefined",
       54 : "undefined1",
       55 : "undefined2",
       56 : "undefined3",
       57 : "undefined4",
       58 : "undefined5",
       59 : "undefined6",
       60 : "undefined_",
       #"undefined7" : 60,
    }.get(num,"null")    #默认返回值，可自设置
def encode_keys(str):
    ''' encode the keys into numbers'''
    return {
        # first row
       "Oem_3" : 0, # `
       "1" : 1,
       "2" : 2,
       "3" : 3,
       "4" : 4,
       "5" : 5,
       "6" : 6,
       "7" : 7,
       "8" : 8,
       "9" : 9,
       "0" : 10,
       "Oem_Minus" : 11,   # -
       "Oem_Plus" : 12,
       # second row
       "Q" : 13,
       "W" : 14,
       "E" : 15,
       "R" : 16,
       "T" : 17,
       "Y" : 18,
       "U" : 19,
       "I" : 20,
       "O" : 21,
       "P" : 22,
       "Oem_4" : 23,  # [
       "Oem_6" : 24,  # ]
       "Oem_5" : 25,  # \
       # third row
       "A" : 26,
       "S" : 27,
       "D" : 28,
       "F" : 29,
       "G" : 30,
       "H" : 31,
       "J" : 32,
       "K" : 33,
       "L" : 34,
       "Oem_1" : 35, # ;
       "Oem_7" : 36,   # '
        # forth row
       "Z" : 39,
       "X" : 40,
       "C" : 41,
       "V" : 42,
       "B" : 43,
       "N" : 44,
       "M" : 45,
       "Oem_Comma" : 46, # ,
       "Oem_Period" : 47, # .
       "Oem_2" : 48, # /
       # space
    #    "undefined" :53,
    #    "undefined1":54,
    #    "undefined2":55,
    #    "undefined3":56,
    #    "undefined4":57,
    #    "undefined5":58,
    #    "undefined6":59,
    #    "undefined_" : 60,
       "Space"  :53,
       "Space1" :54,
       "Space2" :55,
       "Space3" :56,
       "Space4" :57,
       "Space5" :58,
       "Space6" :59,
       "Space_" :60,
    }.get(str,"-1")    #默认返回值，可自设置


def get_vectors():
    vector_list = [[]]
    for i in range(0,11):
        #vector_list.append([i])
        if i != 0:
            vector_list.append(get_vector(i,i+12))
        vector_list.append(get_vector(i,i+13))
        vector_list.append(get_vector(i,i+14))
    for i in range(13,26):
        if i == 13:
            #vector_list.append([i])
            vector_list.append(get_vector(i,i-13))
            vector_list.append(get_vector(i,i-12))
            vector_list.append(get_vector(i,i+1))
            vector_list.append(get_vector(i,i+13))
            vector_list.append(get_vector(i,i+14))
        elif i == 14:
            #vector_list.append([i])
            vector_list.append(get_vector(i,i-13))
            vector_list.append(get_vector(i,i-12))
            vector_list.append(get_vector(i,i-11))
            vector_list.append(get_vector(i,i-1))
            vector_list.append(get_vector(i,i+1))
            vector_list.append(get_vector(i,i+12))
            vector_list.append(get_vector(i,i+13))
        elif i == 23:
            #vector_list.append([i])
            vector_list.append(get_vector(i,i-14))
            vector_list.append(get_vector(i,i-13))
            vector_list.append(get_vector(i,i-12))
            vector_list.append(get_vector(i,i-1))
            vector_list.append(get_vector(i,i+1))
            vector_list.append(get_vector(i,i+11))
            vector_list.append(get_vector(i,i+12))
            vector_list.append(get_vector(i,i+13))
        elif i == 24:
            #vector_list.append([i])
            vector_list.append(get_vector(i,i-13))
            vector_list.append(get_vector(i,i-1))
            vector_list.append(get_vector(i,i+11))
            vector_list.append(get_vector(i,i+12))
        elif i == 25:
            #vector_list.append([i])
            vector_list.append(get_vector(i,i-14))
            vector_list.append(get_vector(i,i-1))
            vector_list.append(get_vector(i,i+11))
        else :
            #vector_list.append([i])
            vector_list.append(get_vector(i,i-14))
            vector_list.append(get_vector(i,i-13))
            vector_list.append(get_vector(i,i-12))
            vector_list.append(get_vector(i,i-11))
            vector_list.append(get_vector(i,i-1))
            vector_list.append(get_vector(i,i+1))
            vector_list.append(get_vector(i,i+11))
            vector_list.append(get_vector(i,i+12))
            vector_list.append(get_vector(i,i+13))
            vector_list.append(get_vector(i,i+14))
    for i in range(26,37):
        if i == 26:
            #vector_list.append([i])
            vector_list.append(get_vector(i,i-13))
            vector_list.append(get_vector(i,i-12))
            vector_list.append(get_vector(i,i-11))
            vector_list.append(get_vector(i,i+1))
            vector_list.append(get_vector(i,i+13))
            vector_list.append(get_vector(i,i+14))
        elif i == 27:
            #vector_list.append([i])
            vector_list.append(get_vector(i,i-14))
            vector_list.append(get_vector(i,i-13))
            vector_list.append(get_vector(i,i-12))
            vector_list.append(get_vector(i,i-11))
            vector_list.append(get_vector(i,i-1))
            vector_list.append(get_vector(i,i+1))
            vector_list.append(get_vector(i,i+12))
            vector_list.append(get_vector(i,i+13))
            vector_list.append(get_vector(i,i+14))
        elif i == 35:
            #vector_list.append([i])
            vector_list.append(get_vector(i,i-14))
            vector_list.append(get_vector(i,i-13))
            vector_list.append(get_vector(i,i-12))
            vector_list.append(get_vector(i,i-11))
            vector_list.append(get_vector(i,i-1))
            vector_list.append(get_vector(i,i+1))
            vector_list.append(get_vector(i,i+11))
            vector_list.append(get_vector(i,i+12))
            vector_list.append(get_vector(i,i+13))
        elif i == 36: 
            #vector_list.append([i])
            vector_list.append(get_vector(i,i-14))
            vector_list.append(get_vector(i,i-13))
            vector_list.append(get_vector(i,i-12))
            vector_list.append(get_vector(i,i-11))
            vector_list.append(get_vector(i,i-1))
            vector_list.append(get_vector(i,i+11))
            vector_list.append(get_vector(i,i+12))
        else : 
            #vector_list.append([i])
            vector_list.append(get_vector(i,i-14))
            vector_list.append(get_vector(i,i-13))
            vector_list.append(get_vector(i,i-12))
            vector_list.append(get_vector(i,i-11))
            vector_list.append(get_vector(i,i-1))
            vector_list.append(get_vector(i,i+1))
            vector_list.append(get_vector(i,i+11))
            vector_list.append(get_vector(i,i+12))
            vector_list.append(get_vector(i,i+13))
            vector_list.append(get_vector(i,i+14))
    for i in range(39,49):
        if i == 39:
            #vector_list.append([i])
            vector_list.append(get_vector(i,i-13))
            vector_list.append(get_vector(i,i-12))
            vector_list.append(get_vector(i,i-11))
            vector_list.append(get_vector(i,i+1))
            vector_list.append(get_vector(i,i+14))
        elif i == 40:
            #vector_list.append([i])
            vector_list.append(get_vector(i,i-14))
            vector_list.append(get_vector(i,i-13))
            vector_list.append(get_vector(i,i-12))
            vector_list.append(get_vector(i,i-11))
            vector_list.append(get_vector(i,i-1))
            vector_list.append(get_vector(i,i+1))
            vector_list.append(get_vector(i,i+13))
            vector_list.append(get_vector(i,i+14))
        elif i == 41:
            #vector_list.append([i])
            vector_list.append(get_vector(i,i-14))
            vector_list.append(get_vector(i,i-13))
            vector_list.append(get_vector(i,i-12))
            vector_list.append(get_vector(i,i-11))
            vector_list.append(get_vector(i,i-1))
            vector_list.append(get_vector(i,i+1))
            vector_list.append(get_vector(i,i+12))
            vector_list.append(get_vector(i,i+13))
            vector_list.append(get_vector(i,i+14))
        elif i == 46:
            #vector_list.append([i])
            vector_list.append(get_vector(i,i-14))
            vector_list.append(get_vector(i,i-13))
            vector_list.append(get_vector(i,i-12))
            vector_list.append(get_vector(i,i-11))
            vector_list.append(get_vector(i,i-1))
            vector_list.append(get_vector(i,i+1))
            vector_list.append(get_vector(i,i+11))
            vector_list.append(get_vector(i,i+12))
            vector_list.append(get_vector(i,i+13))
        elif i == 47:
            #vector_list.append([i])
            vector_list.append(get_vector(i,i-14))
            vector_list.append(get_vector(i,i-13))
            vector_list.append(get_vector(i,i-12))
            vector_list.append(get_vector(i,i-11))
            vector_list.append(get_vector(i,i-1))
            vector_list.append(get_vector(i,i+1))
            vector_list.append(get_vector(i,i+11))
            vector_list.append(get_vector(i,i+12))
        elif i == 48:
            #vector_list.append([i])
            vector_list.append(get_vector(i,i-14))
            vector_list.append(get_vector(i,i-13))
            vector_list.append(get_vector(i,i-12))
            vector_list.append(get_vector(i,i-1))
            vector_list.append(get_vector(i,i+11))
        else:
            #vector_list.append([i])
            vector_list.append(get_vector(i,i-14))
            vector_list.append(get_vector(i,i-13))
            vector_list.append(get_vector(i,i-12))
            vector_list.append(get_vector(i,i-11))
            vector_list.append(get_vector(i,i-1))
            vector_list.append(get_vector(i,i+1))
            vector_list.append(get_vector(i,i+11))
            vector_list.append(get_vector(i,i+12))
            vector_list.append(get_vector(i,i+13))
            vector_list.append(get_vector(i,i+14))
    result = vector_list[1:]
    x = [x_[0] for x_ in result]
    y = [y_[1] for y_ in result]
    return x, y, result
# -*- coding: utf-8 -*- 
import numpy as np
from fastdtw import dtw
import math
symbols_tobe_matched = ["α", "β", "Ω" , "π","μ" ,  "λ",  "ζ" ,"θ", "γ", "η" ,"σ" ,"∑", "∫"  , "Δ" , "φ" , "⊂", "⊃", "∪", "∩", "∞", "÷", "×", "√", "ε", "£","€"]
possibilities_matrix = np.array([
                [0.0514970543204, 0.118296791817, 0.053461512011, 0.239954400959, 0.0405724524138, 0.0, 0.0440787238636, 0.242448317949, ],
                [0.0125337417797, 0.0, 0.309958589696, 0.0, 0.291257231568, 0.0445888744037, 0.0108504632186, 0.0, ],
                [0.0216737825802, 0.0, 0.0198613682478, 0.0, 0.316436169202, 0.292015738666, 0.0358184090329, 0.0, ],
                [0.151666069885, 0.0, 0.0762198351096, 0.0384996596938, 0.0528262620265, 0.379589170536, 0.0087566170866, 0.0, ],
                [0.301724268429, 0.0, 0.0, 0.197858430743, 0.0, 0.0411905100081, 0.126728357767, 0.0927827374223, ],
                [2.87679176675e-15, 0.000271057502813, 0.123495302339, 5.85714910073e-16, 0.0736068612132, 0.000187949911929, 0.424476964768, 0.0, ],
                [0.0, 0.0, 2.31366404238e-21, 0.443881248537, 0.0303075488991, 0.0389074442303, 0.0022074483267, 0.053058042421, ],
                [0.0, 0.0845477530985, 0.137842465623, 0.0, 0.000158628605283, 0.0, 0.398813895267, 0.0, ],
                [1.94778200708e-07, 0.166670868666, 0.0131986599278, 1.19672836971e-35, 0.0, 0.0069408745074, 0.405584730978, 1.50480884768e-10, ],
                [9.33473975468e-12, 0.132061302892, 1.00643505272e-05, 0.020081459278, 0.0, 0.0, 0.172123168578, 0.359484895062, ],
                [0.0, 0.169683280892, 0.027333056963, 0.026261887559, 0.0, 0.00925995172123, 0.126814523724, 0.357931278937, ],
                [0.0, 0.119499001708, 0.0937800037818, 0.319820552786, 0.0, 0.0712093216275, 0.0978846711553, 0.0515555780695, ]
            ])
'''
below are the original vectors, without normalization
clustered_centroids = np.array([
            [-77.8, 25],                 #0
            [-42.64516129, 25.32258065], #1
            [-12.53125, 25.34375],       #2
            [17.53333333, 25.36666667],  #3
            [50.05, 25.55],              #4
            [-29.67741935, 0],           #5
            [29.7, 0],                   #6
            [-49.77777778, -25.66666667],#7
            [-19.96428571, -25.64285714],#8
            [11.97368421, -25.47368421], #9
            [42.13888889, -25.44444444], #10
            [77.81818182, -25]           #11
        ])
'''
clustered_centroids = np.array([
            [-0.9520540226789245, 0.3059299558736904],
            [-0.8598368981931307, 0.5105688087864514],
            [-0.44323004728450727, 0.8964079011165471],
            [0.5685915015131715, 0.8226200243168149],
            [0.8906589323925126, 0.45467204241016385],
            [-1.0, 0.0],
            [1.0, 0.0],
            [-0.8888031673925841, -0.45828913322585996],
            [-0.614320952843256, -0.7890562507817513],
            [0.42539177031743186, -0.9050093047843217],
            [0.8560456003452277, -0.5169003096628776],
            [0.9520748400258878, -0.30586516472079656]
    ])
def dictionary(symbol):
    '''
    number from 0-7 stands for 8 main directions,
    0: up ↑
    1: down ↓
    2: left ←
    3: right →
    4: left-up ↖
    5: right-up ↗
    6: left-down ↙
    7: right-down ↘
    '''
    return{
            "α": [list("624537")],
            "β": [list("537623762")],
            "Ω": [list("3453763")],
            "π": [list("32657")],
            "μ": [list("6567567")],
            "λ": [list("657"),list("607")],
            "ζ": [list("36363")],
            "θ": [list("5376423")],
            "γ": [list("765")],
            "η": [list("1031")],
            "€": [list("26734363")],
            "σ": [list("762453")],
            "∑": [list("32763"),list("2763")],
            "∫": [list("262")],
            "Δ": [list("634"),list("725")],
            "φ": [list("5376426")],
            "⊂": [list("2673")],
            "⊃": [list("3762")],
            "∪": [list("17350")],
            "∩": [list("05371")],
            "∞": [list("4675764")],
            "÷": [list("636")],
            "×": [list("617")],
            "√": [list("75")],
            "ε": [list("213213")],
            "£": [list("26343")],
            #"Ⅰ": [list("1")],
            #"Ⅱ": [list("151")],
            #ⅢⅣⅤⅥⅦⅧⅨⅩⅪⅫ"
        }.get(symbol,"")

'''
    This function reflects the position of every key
    data  retrived from a svg file
'''
def position(character):
    return{
        "0": [341, -96],
        "1": [74, -96],
        "2": [104, -96],
        "3": [133, -96],
        "4": [163, -96],
        "5": [193, -96],
        "6": [222, -96],
        "7": [252, -96],
        "8": [282, -96],
        "9": [311, -96],
        "a": [100, -147],
        "b": [230, -172],
        "c": [171, -172],
        "d": [159, -147],
        "e": [151, -121],
        "f": [189, -147],
        "g": [218, -147],
        "h": [248, -147],
        "i": [300, -121],
        "j": [278, -147],
        "k": [307, -147],
        "l": [337, -147],
        "m": [290, -172],
        "n": [260, -172],
        "o": [330, -121],
        "p": [360, -121],
        "q": [92, -121],
        "r": [181, -121],
        "s": [129, -147],
        "t": [211, -121],
        "u": [271, -121],
        "v": [201, -172],
        "w": [121, -121],
        "x": [141, -172],
        "y": [241, -121],
        "z": [111, -172],
        "-": [371, -96],
        "=": [401, -96],
        "`": [44, -96],
        "[": [390, -121],
        "]": [419, -121],
        "|": [431, -96],
        ";": [367, -147],
        "\'": [396, -147],
        "<": [319, -172],
        ",": [319, -172],
        ".": [349, -172],
        "/": [379, -172],
        "\\": [448, -121],
        "space":[240.7, -198]
            #"undefined_": [240.7, -198] # mean of undefined - undefined6
            #split the space in to 7 buttons, which they have the x location of e r t y u i o
            # "undefined": [151, -198], // e
            # "undefined1": [181, -198], // r
            # "undefined2": [211, -198], // t
            # "undefined3": [241, -198], // y
            # "undefined4": [271, -198], // u
            # "undefined5": [300, -198], // i
            # "undefined6": [330, -198], //o
                #    "undefined7" : [,-198],
    }.get(character,[0,0])

'''
@prag: ['key1', 'key2', ...]
@return: a five-element list containing top 5 results
this function is to give the top 5 prediction results
'''
def predict(input_seq, number = 5):
    length = len(symbols_tobe_matched)
    losses = np.zeros([1,length])
    vectors = divide_single_vector(remove_duplicate( input_seq ))
    for i in range(length):
        min_loss_for_one_symbol = float("inf")
        for j in range(len(dictionary(symbols_tobe_matched[i]))):

            loss, _ = dtw(vectors, dictionary(symbols_tobe_matched[i])[j], dist = get_possibility)
            if loss <= min_loss_for_one_symbol:
                min_loss_for_one_symbol = loss
        #losses[i], _ = dtw(vectors, dictionary(symbols_tobe_matched[i]), dist=get_possibility)
        losses[0][i] = min_loss_for_one_symbol

    _sorted = np.argsort(losses)
    top_number_result=[]
    for i in range(number):
        top_number_result.append(symbols_tobe_matched[_sorted[0][i]])

    return top_number_result

'''
This function is to remove duplicate keys in the inpue sequence
like  'a' 'b' 'c' 'c' 'd' will be shortened into 'a' 'b' 'c' 'd' 
'''
def remove_duplicate(input_seq):
    duplicate_removed = []
    for i in range(len(input_seq)):
        if i == 0:
            duplicate_removed.append(input_seq[i])
        else:
            if input_seq[i] != input_seq[i-1]:
                duplicate_removed.append(input_seq[i])
    return duplicate_removed

def get_possibility(first, second):
    temp = possibilities_matrix[int(first)][int(second)]
    if temp == 0:
        #return float("inf")
        return 999999
    else:
        return -math.log(temp)

def get_vector(one, two):
    x = position(two)[0] - position(one)[0]
    y = position(two)[1] - position(one)[1]
    return [x, y]





'''
@prag: ['key1', 'key2', ...]
@return: ['1','2',...]
pass in an input list, which contains all the keys pressed during the gliding
parse it into a list of integers and every integer stands for a vector among the 12 vectors
'''
def divide_single_vector(input_seq):
    parsed_vectors = []
    for index in range(len(input_seq) -1):
        normalize_vector = normalize(get_vector(input_seq[index], input_seq[index+1]))
        parsed_vectors.append(map_to_centroids(normalize_vector))
    return parsed_vectors



''' 
@prag: [x,y]
@return: vector i 
pass in a list with two characters
return the closest vector to represent the input 
if the input contains space,
the space should map to the exact location among the 7 space keys
'''
def map_to_centroids(list):

    distances = euclidean_distance(np.array(list), clustered_centroids)
    closest_i = np.argmin(distances)
    return closest_i

def euclidean_distance(one_sample, X):
    one_sample = one_sample.reshape(1, -1)
    X = X.reshape(X.shape[0], -1)
    distances = np.power(np.tile(one_sample, (X.shape[0], 1)) - X, 2).sum(axis=1)
    return distances

'''
@prag: [x,y]
@return: normalized [_x, _y]
pass in a list, which contains two elements,
return the normalized list
'''
def normalize(list):
    x = list[0]
    y = list[1]
    _sum = (x*x + y*y) ** 0.5
    _x = x / _sum
    _y = y / _sum
    return [_x, _y]

if __name__ =="__main__":
    test = list("8ujjjjjm")
    

    print(remove_duplicate(test))
    #print(divide_single_vector(test))
    #print(predict(list("8uhbvfrtyjm")))
    #a ,b = dtw([8, 8, 8, 5, 2, 2, 6, 6, 10, 9],['4', '6', '7', '5', '7', '6', '4'], dist = get_possibility)
    #a ,b = dtw([8, 8, 8, 5, 2, 2, 6, 6, 10, 9],['4', '6', '7', '5', '7', '6', '4'], dist = get_possibility)
    #print(a,b)
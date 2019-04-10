
global MATCHES
MATCHES = [
 ['q', '`', '1', '2' ,'w', 'a', 's', 'tab', 'caps'],
 ['w', '2', '3', 'q', 'e', 'a', 's', 'd'],
 ['e', '2', '3', '4', 'w', 'r', 's', 'd', 'f'],
 ['r', '3', '4', '5', 'e', 't', 'd', 'f', 'g'],
 ['t', '4', '5', '6', 'r', 'y', 'f', 'g', 'h'],
 ['y', '5', '6', '7', 't', 'u', 'g', 'h', 'j'],
 ['u', '6', '7', '8','9', 'y', 'i', 'g', 'h', 'j', 'k'],
 ['i', '6', '7', '8', '9', 'u', 'o', 'h', 'j', 'k', 'l'],
 ['o', '8','9', '0', 'i', 'p', 'k', 'l', ';'],
 ['p', '9', '0', '-', 'o', '[', 'l', ';', "'"],
 ['[', '0', '-','+', 'p', ']', 'l', ';', ''', '\\' ],
 [']', '-','+', '[', ';', ''', '\\'],
 ['a', 'tab', 'q', 'w', 'caps','s', 'z', 'x', 'left shift'],
 ['s', 'q', 'w', 'e', 'a', 'd', 'z', 'x', 'c'],
 ['d', 'w', 'e', 'r', 's', 'f', 'x', 'c', 'v'],
 ['f', 'e', 'r', 't', 'd', 'g', 'c', 'v', 'b'],
 ['g', 'r', 't', 'y', 'f', 'h', 'v', 'b', 'n'],
 ['h', 't', 'y', 'u', 'g', 'j', 'b', 'n', 'm'],
 ['j', 'y', 'u', 'i', 'h', 'k', 'b', 'n', 'm'],
 ['k', 'u', 'i', 'o', 'j', 'l', 'm', ',', '.'],
 ['l', 'i', 'o', 'p', 'k', ';', 'm', ',', '.', '/'],
 [';', 'o', 'p', '[', 'l', "'", '.', '/'],
 ["'", 'p', '[',']', ';', '.', '/'],
 ['z', 'a', 's', 'x'],
 ['x', 'a', 's', 'd', 'f', 'z', 'c', 'space'],
 ['c', 's', 'd', 'f', 'g', 'x', 'v', 'space'],
 ['v', 'd', 'f', 'g', 'h', 'c', 'b', 'space'],
 ['b', 'f', 'g', 'h', 'j', 'v', 'n', 'space'],
 ['n', 'g', 'h', 'j', 'k', 'b', 'm', 'space'],
 ['m', 'h', 'j', 'k', 'l', 'n', ',', 'space'],
 [',', 'j', 'k', 'l', ';', 'm', '.', 'space'],
 ['.', 'k', 'l', ';', "'", ',', '/', 'space'],
 ['/', 'l', ';', "'", '.', 'space']
 ]

def is_adjacent(key1, key2):
    keyName_1 = key1[0]
    keyName_2 = key2[0]
    for i in range(len(MATCHES)):
        if keyName_1 in MATCHES[i] and keyName_2 in MATCHES[i]:
            return True
    return False

def adjacent_rate(keystring):
    adjacent_num = 0
    for i in range(len(keystring)-1):
        if is_adjacent(keystring[i], keystring[i+1]):
            adjacent_num += 1
    return adjacent_num/len(keystring)
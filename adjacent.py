
global MATCHES
MATCHES = [
 ['Q', 'Oem_3', '1', '2' ,'W', 'A', 'S', 'Tab', 'Capital'],
 ['W', '2', '3', 'Q', 'E', 'A', 'S', 'D'],
 ['E', '2', '3', '4', 'W', 'R', 'S', 'D', 'F'],
 ['R', '3', '4', '5', 'E', 'T', 'D', 'F', 'G'],
 ['T', '4', '5', '6', 'R', 'Y', 'F', 'G', 'H'],
 ['Y', '5', '6', '7', 'T', 'U', 'G', 'H', 'J'],
 ['U', '6', '7', '8','9', 'Y', 'I', 'G', 'H', 'J', 'K'],
 ['I', '6', '7', '8', '9', 'U', 'O', 'H', 'J', 'K', 'L'],
 ['O', '8','9', '0', 'I', 'P', 'K', 'L', 'Oem_1'],
 ['P', '9', '0', 'Oem_Minus', 'O', 'Oem_4', 'L', 'Oem_1', "Oem_7"],
 ['Oem_4', '0', 'Oem_Minus','Oem_Plus', 'P', 'Oem_6', 'L', 'Oem_1', 'Oem_7', 'Oem_5' ],
 ['Oem_6', 'Oem_Minus','Oem_Plus', 'Oem_4', 'Oem_1', 'Oem_7', 'Oem_5'],
 ['A', 'Tab', 'Q', 'W', 'Capital','S', 'Z', 'X', 'Lshift'],
 ['S', 'Q', 'W', 'E', 'A', 'D', 'Z', 'X', 'C'],
 ['D', 'W', 'E', 'R', 'S', 'F', 'X', 'C', 'V'],
 ['F', 'E', 'R', 'T', 'D', 'G', 'C', 'V', 'B'],
 ['G', 'R', 'T', 'Y', 'F', 'H', 'V', 'B', 'N'],
 ['H', 'T', 'Y', 'U', 'G', 'J', 'B', 'N', 'M'],
 ['J', 'Y', 'U', 'I', 'H', 'K', 'B', 'N', 'M'],
 ['K', 'U', 'I', 'O', 'J', 'L', 'M', 'Oem_Comma', 'Oem_Period'],
 ['L', 'I', 'O', 'P', 'K', 'Oem_1', 'M', 'Oem_Comma', 'Oem_Period', 'Oem_2'],
 ['Oem_1', 'O', 'P', 'Oem_4', 'L', "Oem_7", 'Oem_Period', 'Oem_2'],
 ["Oem_7", 'P', 'Oem4','Oem_6', 'Oem_1', 'Oem_Period', 'Oem_2'],
 ['Z', 'A', 'S', 'X'],
 ['X', 'A', 'S', 'D', 'F', 'Z', 'C', 'Space'],
 ['C', 'S', 'D', 'F', 'G', 'X', 'V', 'Space'],
 ['V', 'D', 'F', 'G', 'H', 'C', 'B', 'Space'],
 ['B', 'F', 'G', 'H', 'J', 'V', 'N', 'Space'],
 ['N', 'G', 'H', 'J', 'K', 'B', 'M', 'Space'],
 ['M', 'H', 'J', 'K', 'L', 'N', ',', 'Space'],
 ['Oem_Comma', 'J', 'K', 'L', 'Oem_1', 'M', 'Oem_Period', 'Space'],
 ['Oem_Period', 'K', 'L', 'Oem_1', "Oem_7", 'Oem_Comma', 'Oem_2', 'Space'],
 ['Oem_2', 'L', 'Oem_1', "Oem_7", 'Oem_Period', 'Space']
 ]

def is_adjacent(key1, key2):
    keyName_1 = key1[0]
    keyName_2 = key2[0]
    for i in range(len(MATCHES)):
        if keyName_1 in MATCHES[i] and keyName_2 in MATCHES[i]:
            return True
    return False


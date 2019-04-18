from __future__ import absolute_import, division
import numbers
import numpy as np
import math
from collections import defaultdict
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

def get_possibility(first, second):
    temp = possibilities_matrix[int(first)][int(second)]
    if temp == 0:
        return float("inf")
    else:
        return -math.log(temp)
def __difference(a, b):
    return abs(a - b)
def __prep_inputs(x, y, dist):
    x = np.asanyarray(x, dtype='float')
    y = np.asanyarray(y, dtype='float')

    if x.ndim == y.ndim > 1 and x.shape[1] != y.shape[1]:
        raise ValueError('second dimension of x and y must be the same')
    if isinstance(dist, numbers.Number) and dist <= 0:
        raise ValueError('dist cannot be a negative integer')

    if dist is None:
        if x.ndim == 1:
            dist = __difference
        else: 
            dist = __norm(p=1)
    elif isinstance(dist, numbers.Number):
        dist = __norm(p=dist)
    
    print(x,y)
    return x, y, dist

def __norm(p):
    return lambda a, b: np.linalg.norm(np.atleast_1d(a) - np.atleast_1d(b), p)


def dtw(x, y, dist=None):
    ''' return the distance between 2 time series without approximation
        Parameters
        ----------
        x : array_like
            input array 1
        y : array_like
            input array 2
        dist : function or int
            The method for calculating the distance between x[i] and y[j]. If
            dist is an int of value p > 0, then the p-norm will be used. If
            dist is a function then dist(x[i], y[j]) will be used. If dist is
            None then abs(x[i] - y[j]) will be used.
        Returns
        -------
        distance : float
            the approximate distance between the 2 time series
        path : list
            list of indexes for the inputs x and y
        Examples
        --------
        >>> import numpy as np
        >>> import fastdtw
        >>> x = np.array([1, 2, 3, 4, 5], dtype='float')
        >>> y = np.array([2, 3, 4], dtype='float')
        >>> fastdtw.dtw(x, y)
        (2.0, [(0, 0), (1, 0), (2, 1), (3, 2), (4, 2)])
    '''
    x, y, dist = __prep_inputs(x, y, dist)
    return __dtw(x, y, None, dist)


def __dtw(x, y, window, dist):
    len_x, len_y = len(x), len(y)
    if window is None:
        window = [(i, j) for i in range(len_x) for j in range(len_y)]
    window = ((i + 1, j + 1) for i, j in window)
    print("window",window)
    D = defaultdict(lambda: (float('inf'),))
    D[0, 0] = (0, 0, 0)
    for i, j in window:
        dt = dist(x[i-1], y[j-1])
        D[i, j] = min((D[i-1, j][0]+dt, i-1, j), (D[i, j-1][0]+dt, i, j-1),
                      (D[i-1, j-1][0]+dt, i-1, j-1), key=lambda a: a[0])
    path = []
    i, j = len_x, len_y
    print("D",D)
    while not (i == j == 0):
        path.append((i-1, j-1))
        i, j = D[i, j][1], D[i, j][2]
    path.reverse()
    return (D[len_x, len_y][0], path)

sample1 = [8, 8, 8, 5, 2, 2, 6, 6, 10, 9]
sample2 = ['4', '6', '7', '5', '7', '6', '4']
a ,b = dtw(sample1,sample2, dist = get_possibility)
print(a,b)
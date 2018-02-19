#! python3
import numpy as np
from itertools import combinations


def get_new_range(n):
    new_n = n**2 - (n-1)**2
    range_o_n = list(itertools.takewhile(lambda x: x**2 <= new_n, range(n)))
    last_value = n-1
    range_o_n.append(last_value)
    return range_o_n


def decompose_exp4(n):
    lst_o_lists = []
    for r in range(2,6):
        if r <= 4 or n == 44:
            array = np.array(list(filter(lambda x: n-1 in x, combinations(get_new_range(n),r))))
        elif r > 4:
            array = np.array(list(filter(lambda x: n-1 in x and 1 in x, combinations(get_new_range(n),r))))
        b = array**2
        c = np.sum(b,axis=1)
        idx = np.where(c ==n**2)
        new_list = [list(x) for x in list(array[idx])]
        for x in new_list:
            lst_o_lists.append(x)
    lst = [x for x in lst_o_lists if x[0] != 0 and x[-1] == n-1]
    lengths = [len(x) for x in lst]
    lst2 = list(zip(lengths, lst))
    dct = dict(lst2)
    if len(dct.keys()) == 1:
        sums = [sum(x[-2:]) for x in lst]
        lst3 = list(zip(sums,lst))
        dct2 = dict(lst3)
        answer = dct2[max(dct2.keys())]
    elif len(lst) == 0:
        answer = []
    else:
        answer = dct[max(dct.keys())]
    return answer

decompose_exp4(11)

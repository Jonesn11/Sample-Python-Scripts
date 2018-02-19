#non hacky way
import numpy as np
from itertools import combinations,takewhile

def decompose(n):
    new_n = n**2 - (n-1)**2
    range_o_n = list(takewhile(lambda x: x**2 <= new_n, range(n)))
    last_value = n-1
    range_o_n.append(last_value)
    lst_o_lists = []
    for r in range(2,6):
        array = np.array(list(filter(lambda x: n-1 in x, combinations(range_o_n,r))))
        b = array**2
        c = np.sum(b,axis=1)
        idx = np.where(c ==n**2)
        new_list = [list(x) for x in list(array[idx])]
        for x in new_list:
            lst_o_lists.append(x)
    lst = [x for x in lst_o_lists if x[0] != 0 and x[-1] == n-1]
    if len(lst) == 0:
        answer = []
        return answer
    lengths = [len(x) for x in lst]
    lst2 = list(zip(lengths, lst))
    dct = dict(lst2)
    sums = [sum(x[-2:]) for x in lst]
    lst3 = list(zip(sums,lst))
    dct2 = dict(lst3)
    answer = dct2[max(dct2.keys())]
    return answer

print(decompose(11))

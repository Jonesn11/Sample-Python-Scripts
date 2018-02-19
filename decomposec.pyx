import cython

cpdef decompose_exp(double n) except *:
    cdef double n
	cdef int r
    lst_o_lists = []
    for r in range(2,6):
        lst_o_tup1 = []
        lst_o_tup1 += list(filter(lambda z: n-1 in z, itertools.combinations([x for x in range(n+1)],r)))
        array = np.array(lst_o_tup1)
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
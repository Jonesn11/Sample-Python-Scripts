# coding: utf-8
# %load emotion_regulation_app.py


def list_to_dict(x):
    x = dict(list(enumerate(x)))
    return x


def newkeys(d, d1):
    d2 = {d1[key]: value for key, value in d.items()}
    return d2


def additems(lst_o_lst):  # calculates the sum of lists and returns a list
    tot = [sum(x) for x in zip(*lst_o_lst)]
    tot = list(map(lambda x: round(x / 9, 2), tot))
    tot = tot[:-1]
    return tot


def interpret(lst_o_lst):
    list_sums = additems(lst_o_lst)
    names = ['Situation Selection', 'Situation Modification',
             'Attention Deployment', 'Cognitive Reappraisal', 'Response Supression']
    d = list_to_dict(list_sums)
    d1 = list_to_dict(names)
    d3 = newkeys(d, d1)
    return d3


def listsupd(lst_o_lst):
    my_lst1 = []
    for x in lst_o_lst:
        my_lst2 = []
        my_lst2 = [i * x[-1] for i in x]
        my_lst1.append(my_lst2)
    return my_lst1
dadsystem = [[1, 1, -1, 0, 0, 1],
             [1, 1, -1, 0, 0, 2],
             [0, 0, -1, 0, -1, 3],
             [0, 0, -1, 0, -1, 2],
             [0, 0, 0, 1, 0, 1],
             [1, 0, 1, 1, -1, 2],
             [0, 0, -1, 0, -1, 2],
             [1, 0, 1, 0, 0, 1],
             [1, 1, 1, 0, 1, 1],
             [1, 1, 1, 0, 0, 2],
             [-1, 1, 0, 0, -1, 3],
             [1, -1, -1, -1, 0, 2],
             [-1, 1, 1, 1, -1, 3],
             [0, -1, 0, 0, 0, 2]]


def removehyp(lst):
    my_lst = []
    lst_c = []
    for x in lst:
        lst_c.append(x)
        if x in [lst[0], lst[5], lst[8], lst[11], lst[12]]:
            my_lst.append(x)
    for x in my_lst:
        lst_c.remove(x)
    y = lst_c
    return y
mysystem = [[1, 1, -1, 0, 0, 3],
            [1, 1, -1, 0, 0, 1.5],
            [0, 0, -1, 0, -1, 2.25],
            [0, 0, -1, 0, -1, 1.875],
            [0, 0, 0, 1, 0, 1.5],
            [1, 0, 1, 1, -1, 1.125],
            [0, 0, -1, 0, -1, 2],
            [1, 0, 1, 0, 0, .75],
            [1, 1, 1, 0, 1, 2],
            [1, 1, 1, 0, 0, 2],
            [-1, 1, 0, 0, -1, 1],
            [1, -1, -1, -1, 0, 2],
            [-1, 1, 1, 1, -1, 3],
            [0, -1, 0, 0, 0, 2]]
momsystem = [[1, 1, -1, 0, 0, 3],
             [1, 1, -1, 0, 0, 2],
             [0, 0, -1, 0, -1, 2],
             [0, 0, -1, 0, -1, 1],
             [0, 0, 0, 1, 0, 2],
             [1, 0, 1, 1, -1, 2],
             [0, 0, -1, 0, -1, 2],
             [1, 0, 1, 0, 0, 1],
             [1, 1, 1, 0, 1, 3],
             [1, 1, 1, 0, 0, 3],
             [-1, 1, 0, 0, -1, 2],
             [1, -1, -1, -1, 0, 1],
             [-1, 1, 1, 1, -1, 3],
             [0, -1, 0, 0, 0, 2]]


def ereg(system):
    new_list = removehyp(system)
    new_list = listsupd(new_list)
    return interpret(new_list)

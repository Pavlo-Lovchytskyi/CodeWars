#https://www.codewars.com/kata/57a6633153ba33189e000074/train/python
inp = ("abracadabra")
def ordered_count(inp):
    l = []
    for i in inp:
        if i not in l:
            l.append(i)
    return [(i, inp.count(i)) for i in l]
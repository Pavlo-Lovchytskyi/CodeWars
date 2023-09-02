from collections import Counter

def find_it(seq: list) -> int:
    for elem, count in Counter(seq).items():
        if count % 2 != 0:
            return elem
    

print(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]))
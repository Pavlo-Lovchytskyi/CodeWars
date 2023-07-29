a = [1,2,2,3,3,3,4,3,3,3,2,2,1]

list_a = []
for i in a:
    if a.index(i) % 2 != 0:
        list_a.append(i)

print(list_a)
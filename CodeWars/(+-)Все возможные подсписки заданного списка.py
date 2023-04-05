def all_sub_lists(data):
    spisok = sorted(data)
    new_list = [[]]

    for len_substr in range(len(spisok)):
        for i in range(len(spisok) - len_substr):
            new_list.append(spisok[i:i+len_substr+1])
            print(new_list)

    return new_list


all_sub_lists([4, 6, 1, 3])
# [[], [1], [2], [3], [1, 2], [2, 3], [1, 2, 3]]

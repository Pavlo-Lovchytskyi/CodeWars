class List:

    def remove_(self, integer_list: list, values_list: list) -> list:
        return [item for item in integer_list if item not in values_list]


a = List()
print(a.remove_([1, 1, 2, 3, 1, 2, 3, 4, 4, 3, 5, 6, 7, 2, 8], [1, 3, 4, 2]))
# [5, 6 ,7 ,8]

#    list_a = []

#    for item in integer_list:
#         if item not in values_list:
#             list_a.append(item)
#     return list_a

def capitals(word: str) -> list:
    return [index for index, elem in enumerate(word) if elem.isupper()]


print(capitals("rpdFpgRMbUaIYNczUODTZEVy"))
# [3, 6, 7, 9, 11, 12, 13, 16, 17, 18, 19, 20, 21, 22]

# [3, 6, 7, 9, 11, 12, 13, 16, 17, 18, 19, 20, 21, 22]

#    list_index = []

#    for index, elem in enumerate(word):

#         if elem.isupper():
#             list_index.append(index)

#     return list_index

#https://www.codewars.com/kata/56582133c932d8239900002e/train/python
#input array: [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]
#ouptut: 5
collection = [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]
def most_frequent_item_count(collection):
    if collection:
        return max([collection.count(item) for item in collection])
    return 0
print(most_frequent_item_count(collection))
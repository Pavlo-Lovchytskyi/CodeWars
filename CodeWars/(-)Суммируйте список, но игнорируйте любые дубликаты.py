# https://www.codewars.com/kata/5993fb6c4f5d9f770c0000f2/train/python
# Пожалуйста, напишите функцию, которая суммирует список, но игнорирует любые повторяющиеся
# элементы в списке.
# Например, для списка [3, 4, 3, 6] функция должна вернуть 10.
# test.assert_equals(sum_no_duplicates([1, 1, 2, 3]), 5)
# test.assert_equals(sum_no_duplicates([1, 1, 2, 2, 3]), 3)

def sum_no_duplicates(l):
    return sum(n for n in set(l) if l.count(n) == 1)



assert (sum_no_duplicates([1, 1, 2, 3]), 5)

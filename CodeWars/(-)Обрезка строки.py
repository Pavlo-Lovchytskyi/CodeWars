# https://www.codewars.com/kata/563fb342f47611dae800003c/train/python
#Возвращает функцию, которая обрезает строку (первый заданный аргумент),
# если она длиннее максимальной длины строки (второй заданный аргумент).
# Результат также должен заканчиваться на "..."
# Эти точки в конце также увеличивают длину строки.
# Итак, в приведенном выше примере trim("Creating kata is fun", 14)должно вернуться"Creating ka..."
# Если строка меньше или равна 3 символам, то длина точек не добавляется к длине строки.
# например trim("He", 1), должен вернуться"H..."
# Если строка меньше или равна максимальной длине строки, просто верните строку без обрезки или точек.
# например trim("Code Wars is pretty rad", 50), должен вернуться"Code Wars is pretty rad"
# test.assert_equals(trim("Creating kata is fun", 14),"Creating ka...")
#         test.assert_equals(trim("He", 1),"H...")
#         test.assert_equals(trim("Hey", 2),"He...")
#         test.assert_equals(trim("Hey", 3),"Hey")
#         test.assert_equals(trim("Coding rocks", 12),"Coding rocks")
#         test.assert_equals(trim("Code Wars is pretty rad", 50), "Code Wars is pretty rad")
#         test.assert_equals(trim("London is freezing",18),"London is freezing")



def trim(phrase, size):
    if len(phrase) <= size:
        return phrase
    elif size <= 3:
        return phrase[:size] + '...'
    else:
        return phrase[:size - 3] + '...'




assert(trim("Creating kata is fun", 14),"Creating ka...")
assert(trim("He", 1),"H...")
assert(trim("Hey", 2),"He...")
assert(trim("Hey", 3),"Hey")
assert(trim("Coding rocks", 12),"Coding rocks")
assert(trim("Code Wars is pretty rad", 50), "Code Wars is pretty rad")
assert(trim("London is freezing",18),"London is freezing")
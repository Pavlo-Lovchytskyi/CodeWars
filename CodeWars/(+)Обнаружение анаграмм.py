#https://www.codewars.com/kata/529eef7a9194e0cbc1000255/train/python
#Анаграмма — это результат перестановки букв
#слова для получения нового слова (см. Википедию ).
#Примечание: анаграммы нечувствительны к регистру .
#Завершите возвращаемую функцию, trueесли
#два заданных аргумента являются анаграммами друг
#друга; вернуть falseиначе.
#"foefet"является анаграммой"toffee"
#"Buckethead"является анаграммой"DeathCubeK"
test = "Buckethead"
original = "DeathCubeK"
def is_anagram(test, original):
    return True if sorted(test.lower()) == sorted(original.lower()) else False

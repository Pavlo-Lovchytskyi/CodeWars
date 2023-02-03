#https://www.codewars.com/kata/54ba84be607a92aa900000f1
#Изограмма — это слово, в котором нет повторяющихся букв,
# последовательных или непоследовательных. Реализуйте функцию, определяющую,
# является ли строка, содержащая только буквы, изограммой.
# Предположим, что пустая строка является изограммой. Игнорировать регистр букв.
#"Дерматоглифика" --> истина "аба" --> ложь "moOse" --> ложь (игнорировать регистр букв)
#isIsogram "Dermatoglyphics" = true
#isIsogram "moose" = false
#isIsogram "aba" = false
string = "aba"
def is_isogram(string):
    return True if len(set(string.lower())) == len(string.lower()) else False






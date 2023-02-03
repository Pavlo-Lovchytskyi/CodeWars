# Напишите функцию, которая принимает строку и выводит строки
# из 1 и 0, где гласные становятся 1, а не гласные — 0.
#https://www.codewars.com/kata/580751a40b5a777a200000a1/train/python
# Должны быть включены все негласные, включая небуквенные
# символы (пробелы, запятые и т. д.).
# vowelOne "abceios" -- "1001110"
# vowelOne "aeiou, abc" -- "1111100100"
def vowel_one(s):
    return "".join("1" if c in "aeiou" else "0" for c in s.lower())




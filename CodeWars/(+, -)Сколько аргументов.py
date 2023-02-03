#https://www.codewars.com/kata/5c44b0b200ce187106452139/train/python
#Создайте функцию args_count, которая возвращает
#количество переданных аргументов
#args_count(1, 2, 3) -> 3
#args_count(1, 2, 3, 10) -> 4
def args_count(*args, **kwargs):
    return len(args)+len(kwargs)

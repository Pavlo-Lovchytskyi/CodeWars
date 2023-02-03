#https://www.codewars.com/kata/54c27a33fb7da0db0100040e/train/python
def is_square(n):
    if n == 0:
        return True
    else:
        for i in range(n + 1):
            i2 = i * i # квадрат очередного числа
            if i2 == n:
                return True
            elif i2 > n: # если квадрат больше n, то нет смысла проверять дальше
                break
    return False
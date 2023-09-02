# https: // www.codewars.com/kata/541c8630095125aba6000c00/train/python

def digital_root(n):
    digits = [int(num) for num in str(n)]

    for char in digits:
        print(digital_root(n + 1))



print(digital_root(942))

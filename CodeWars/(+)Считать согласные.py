# https://www.codewars.com/kata/564e7fc20f0b53eb02000106/train/python
# Завершите функцию, которая принимает строку текста на английском языке и
# возвращает количество согласных в строке.
# Согласные – это все буквы, используемые для написания английского языка,
# за исключением гласных a, e, i, o, u.
# def sample_tests():
#     test.assert_equals(consonant_count(''), 0, 'Test string is empty string');
#     test.assert_equals(consonant_count('aaaaa'), 0, 'Test string: "aaaaa"');
#     test.assert_equals(consonant_count('XaeiouX'), 2, 'Test string: "XaeiouX"');
#     test.assert_equals(consonant_count('Bbbbb'), 5, 'Test string: "Bbbbb"');
#     test.assert_equals(consonant_count('helLo world'), 7, 'Test string: "helLo world"');
#     test.assert_equals(consonant_count('h^$&^#$&^elLo world'), 7, 'Test string: "h^$&^#$&^elLo world"');
#     test.assert_equals(consonant_count('0123456789'), 0, 'Test string: "0123456789"')
#     test.assert_equals(consonant_count('012345_Cb'), 2, 'Test string: "012345_Cb"')


def consonant_count(s):
    count = 0
    for i in s.lower():
        if i in 'bcdfghjklmnpqrstvwxyz':
            count += 1
    return count



assert (consonant_count('XaeiouX'), 2, 'Test string: "XaeiouX"')
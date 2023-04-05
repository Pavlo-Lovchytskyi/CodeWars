dict_numbers = {'1': [',', '.', '?', '!', ':'],
                '2': ['a', 'b', 'c'],
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z'],
                '0': [' ']
                }


def sequence_buttons(string):
    string_number = ''

    for single_character in string:
        str_ing = single_character

        for k, v in dict_numbers.items():
            if str_ing.lower() in v:
                indx = v.index(str_ing.lower())
                string_number += k+k*indx
    print(string_number)
    return string_number


print(sequence_buttons('Hi there!'))
# 'Hi there!' => "44444084433777331111"

def accum(string: str) -> str:
    assert_str = ''
    len_str = len(string)

    for index, elem in enumerate(string):
        indx_1 = index + 1

        if indx_1 != len_str:
            test_str = elem * indx_1 + '-'
            assert_str += test_str.capitalize()
            test_str = ''
        else:
            test_str = elem * indx_1
            assert_str += test_str.capitalize()
            test_str = ''

    return assert_str


result = accum("ZpglnRxqenU")
expected_result = "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu"
assert result == expected_result, f"Ожидаемый результат: {expected_result}, Полученный результат: {result}"

result_1 = accum("NyffsGeyylB")
expected_result_1 = "N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb"
assert result_1 == expected_result_1, f"Ожидаемый результат: {expected_result_1}, Полученный результат: {result_1}"



'''
def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))'''

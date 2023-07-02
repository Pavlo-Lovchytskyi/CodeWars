def sum_digits(number: int) -> int:
    return sum(int(d) for d in str(abs(number)))


print(sum_digits(-32))


''' test.assert_equals(sum_digits(10), 1)
    test.assert_equals(sum_digits(99), 18)
    test.assert_equals(sum_digits(-32), 5)'''

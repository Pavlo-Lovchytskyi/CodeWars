def printer_error(string: str) -> str:
    good_str = 0
    not_good_str = 0

    for elem in string:
        if ord(elem) >= 97 and ord(elem) <= 109:
            good_str += 1

        else:
            not_good_str += 1
    normal_str = str(not_good_str) + '/' + str(len(string))
    return normal_str


print(printer_error("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"))


# 97 - 122 this is to z

# 97 - 109 this is to m

'''     s="aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
        test.assert_equals(printer_error(s), "3/56")
        s = "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
        test.assert_equals(printer_error(s), "6/60")
        s = "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu"
        test.assert_equals(printer_error(s) , "11/65")'''

import string


def is_valid_password(password):

    upper_case = any(
        [1 if i in string.ascii_uppercase else 0 for i in password])
    lower_case = any(
        [1 if i in string.ascii_lowercase else 0 for i in password])
    digits = any([1 if i in string.digits else 0 for i in password])
    lenght = len(password)

    if lenght == 8:
        lenght = True
    elif lenght < 8 or lenght > 8:
        lenght = False

    score = 0
    charat = [upper_case, lower_case, digits, lenght]
    for i in range(len(charat)):
        if charat[i]:
            score += 1
    if score == 4:
        return True
    else:
        return False


print(is_valid_password('AAAa9'))


# NmlDl1V0
# z,qrE*IE

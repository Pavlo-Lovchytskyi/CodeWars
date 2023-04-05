def encode(data):

    if len(data) == 0:
        return []

    else:
        char = data[0]
        count = 1
        i = 1

        while i < len(data) and data[i] == char:
            count += 1
            i += 1

        if count >= 1:
            return [char, count] + encode(data[count:])

        else:
            return [char] + encode(data[1:])


print(encode(["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"]))

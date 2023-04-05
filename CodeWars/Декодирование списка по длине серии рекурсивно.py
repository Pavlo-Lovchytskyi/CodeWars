def decode(data):

    if len(data) == 0:
        return []

    else:
        char = data[0]
        count = 1

        if len(data) > 1:
            count = int(data[1])
            return [char] * count + decode(data[2:])

        else:
            return [char] + decode(data[1:])


print(decode(["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]))

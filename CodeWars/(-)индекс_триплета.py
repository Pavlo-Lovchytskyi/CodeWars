def gimme(input_array: list):
    return input_array.index(sorted(input_array)[1])



print(gimme([5, 10, 14]))  # 1

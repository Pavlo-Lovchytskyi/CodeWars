def small_enough(array: list, limit: int)-> bool:
    return True if sorted(array)[-1] <= limit else False


print(small_enough([101, 45, 75, 105, 99, 107], 107))  # True

def open_or_senior(data: list) -> list:
    return ['Senior' if age > 54 and handicap > 7 and handicap < 27 else 'Open' for (age, handicap) in data]


print(open_or_senior([(74, 10), (55, 6), (12, -2), (68, 7)]))

def calculate_years(principal: int, interest: float, tax: float, desired: int):
    year = 0

    while principal < desired:
        principal += (interest * principal) * (1- tax)
        year += 1

    return year


print(calculate_years(1000, 0.05, 0.18, 1100)) # 3






# sum = 1000
# p = 1000 + 1000 * 0.05  # 1050
# p_1 = p - sum  # 50
# a = p_1 * 0.18
# print(p - a)

'''
principal = Начальна сумма вкладу
interest = процент виручки вкладу
tax = процент налогів з виручки
desired = желаєма сумма'''

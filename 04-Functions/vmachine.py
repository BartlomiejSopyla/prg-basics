def f(amount_to_pay):
    coins5 = amount_to_pay // 5
    rest5 = amount_to_pay % 5
    coins2 = rest5 // 2
    rest2 = rest5 % 2
    total = coins5 + coins2 + rest2
    return total
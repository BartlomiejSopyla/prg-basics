def f(x, y):
    count = 0
    for digit in range(x, y):
        if digit < 0 and digit % 2 == 0:
            count += 1
    return count
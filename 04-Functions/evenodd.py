def f(number, even):
    sum_digits = 0

    for i in str(number):
        i = int(i)
        if even and i %2 == 0:
            sum_digits += i
        elif not even and i %2 != 0:
            sum_digits += i
    return sum_digits


            
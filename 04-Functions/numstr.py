def f(n):
    countdown = 1
    result = ''
    while countdown <= n:
        result += str(countdown)
        countdown += 1
    return result
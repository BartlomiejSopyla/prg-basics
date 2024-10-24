def f(n):
    result = ''
    while n > 0:
        if n != 1:
            result += '*/'
        else:
            result += '*'
        n -= 1
    return result
        

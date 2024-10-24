def f(number1, number2, operator):
    result = 0
    if operator == '+':
        result = number1 + number2
    elif operator == '-':
        result = number1 - number2
    elif operator == '*':
        result = number1 * number2
    elif operator == '%':
        result = number1 % number2
    elif operator == '**':
        result = number1 ** number2
    else:
        print('Invalid operator')
    return result
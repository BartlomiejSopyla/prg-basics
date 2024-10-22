###
# Functions to read any data type from the keyboard
#
def input_string(message):
    text = input(message)
    return str(text)

def input_integer(message):
    number = input(message)
    return int(number)

def input_real(message):
    real = input(message)
    return float(real)

def input_boolean(message):
    boolean = input(message)
    return bool(boolean)


<<<<<<< HEAD
=======
# Define a function that calculates and returns the sum of the digits in a number. Then write a program that reads a number from the keyboard and prints the sum of its digits.

# Steps of the algorithm to sum digits in a number:

# Take an integer input from the user. The number can be positive, negative, or zero.
# Handle Negative Numbers: Convert the number to its absolute value using the abs() function. 
# This step ensures the algorithm correctly processes negative numbers by ignoring the negative sign.
# Convert to String: Convert the number to a string using str(). This allows iteration over each digit in the number.
# Iterate Over Digits:
# Loop through each character (digit) in the string representation of the number.
# Convert each character back to an integer.
# Sum Digits: Add each integer value to a running total.
# Output the Result: Return the sum of the digits
>>>>>>> db686eb2e29e12eb2ec9c2bd57476948c6abc43d
###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
<<<<<<< HEAD
    number = abs(number)
    digits = str(number)
    total_sum = 0
    for digit in digits:
        total_sum += int(digit)
    return total_sum

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')
=======
    integer = input('Enter a number: ')
    if integer<0:
        integer = abs(integer)
    integer = str(integer)
    return ...

any_number = int(input('Enter integer number: '))
result = sum_digits(...)
print('The sum of the digits in the number ... is ...')
>>>>>>> db686eb2e29e12eb2ec9c2bd57476948c6abc43d

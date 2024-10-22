# Using built-in Python functions, write a program that calculates and prints:

# the largest number: 7,5,6,3,8,2
# the smallest number: 4,7,2,3,9,8
# length of the phrase: "computer science"
# letter read from the keyboard
# number representing the string "20303"
# binary string representing decimal number 304
# hexadecimal string representing decimal number 304
# integer representing the Unicode code of the € sign
# absolute value of -17

###
# Program for testing built-in functions
#
max_number = max(7,5,6,3,8,2)
print('Max number of 7,5,6,3,8,2 is', max_number)

min_number = min(4,7,2,3,9,8)
print('Min number of 4,7,2,3,9,8 is', min_number)

str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)


letter = input('Enter letter: ')
if letter.isalpha():
    print(f'Letter from keyboard: {letter}')
else:
    print('Not a letter')

string1 = '20303'
print(f"Number representing the string '20303': {int(string1)}")

num = 304
print(f'Binary string representing decimal number 304: {bin(num)[2:]}')
print(f'Hexadecimal string representing decimal number 304: {hex(num)[2:]}')
print(f"Integer representing the Unicode code of the € sign: {ord('€')}")
print(f'Absolute value of -17, {abs(-17)}')
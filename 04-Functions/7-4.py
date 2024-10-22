import range

number = int(input('Enter the number: '))
x = 2
y = 15

if range.rangee(number, x, y):
    print(f'Number {number} in the range <{x}, {y}>: yes')
else:
    print(f'Number {number} in the range <{x}, {y}>: no')



# Most female names in Polish end with the letter "a". 
# Write a program that prints the name entered from the keyboard, provided it is a female name. Sample result:

# Enter name: Anna
# Anna -- Polish female name

name = input('Podaj imie: ')
if name.endswith('a'):
    print(f'{name} -- Polish female name')
else:
    print(f'{name} -- Not polish female name')
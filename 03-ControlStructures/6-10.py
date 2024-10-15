# Write a program that calculates a dog's age in dog's years. For the first two years, a dog's life is equal to 10.5 human years. 
# After that, each dog year is equal to 4 human years. Sample result:

# Enter the dog's age in human years: 15
# The dog's age in dog's years is 73 years.

age = float(input('Enter your dog age: '))

if age <=2:
    dog_age = 10.5 * age
    print(f'The dog s age in dog s years is {dog_age} years.')
else:
    dog_age= 10.5 * 2 + (4 * (age - 2))
    print(f'The dog s age in dog s years is {dog_age} years.')
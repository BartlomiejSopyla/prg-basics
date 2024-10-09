###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

#determine temperature in Celsius
#calculate temperature in Kelvin
#calculate temperature in Fahrenheit
#display results

celc = float(input('Determine temperature in Celsius: '))
kel = celc + 273.15
fah = (celc*9/5) + 32
print(f'Temperature in Celsius: {celc}')
print(f'Temperature in Kelvin: {kel}')
print(f'Temperature in Fahrenheit: {fah}')
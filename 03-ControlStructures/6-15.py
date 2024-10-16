# EAN-13 (European Article Number) is a barcode for marking goods. 
# The first 3 digits (590) usually indicate goods manufactured in Poland. 
# Write a program that checks whether the EAN-13 number entered from the keyboard consists of exactly 13 characters (digits). 
# Print a message if the number is correct. Additionally, only when the article number is correct, 
# print a message when the product was manufactured in Poland. Sample result:

# Enter EAN-13 article number: 5901230094938
# Article number is correct
# Article manufactured in Poland

ean = input('Enter EAN-13 article number: ')
lenght = len(ean)

if lenght == 13 and ean.isdigit():
    country = ean[:3]
    if country == '590':
        print('Article number is correct')
        print('Article manufactured in Poland')
    else:
        print('Article not manufactured in Poland')
else:
    print('Incorrect article number')
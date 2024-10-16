# In one of the online stores, a 25% discount is charged for each product purchased over two. 
# Write a program that calculates the amount to be paid. 
# Read the number of purchased products and the product price from the keyboard. 
# Sample result:

# Number of products purchased: 5
# Product price: 40
# Amount to pay: 170.00

how_many = int(input('Number of products purchased: '))
product_price = float(input('Product price: '))

if how_many > 2:
    regular_price = 2*product_price
    discounted_price = (how_many - 2)*product_price*0.75
    final_price = regular_price + discounted_price
    print(f'Amount to pay: {final_price}')
else:
    final_price = how_many*product_price
    print(f'Amount to pay: {final_price}')
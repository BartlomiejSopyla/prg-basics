# A computer program analyses the price of a product in an online store. 
# If the product price decreases by at least 10%, the program prints a purchase recommendation:

# Buy the product!!
# Product price reduced by 17%

# Create such program. The current and previous price of the product are included in variables. Sample result:

# Current product price: 140.00
# Previous product price: 200.00
# Buy the product!!
# Product price reduced by 30%

p_price = float(200)
c_price = float(140)

if c_price < p_price*0.9:
    discount = ((p_price - c_price)/p_price)*100
    print(f'Current product price: {c_price}')
    print(f'Previous product price: {p_price}')
    print('Buy this product!!')
    print(f'Product price reduced by {discount}%')
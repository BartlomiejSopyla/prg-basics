price = float(input("Enter price: "))
discount = float(input("Enter discount %: "))
discountp= (discount/100)*price
final_price= price-discountp
reduction = price-final_price
print("Discount price: ", final_price)
print("Reduction: ", reduction)

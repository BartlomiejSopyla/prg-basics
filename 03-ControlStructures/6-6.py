# The parking meter calculates the parking fee based on the number of hours the car was parked according to the following rules:

# 1-2 hours: 5 PLN
# 3-6 hours: 15 PLN
# Over 6 hours: 20 PLN

hours = int(input('Number of hours the car was parked: '))

if 1<=hours<=2:
    charge = 5
    print(f'Charge: {charge}PLN')
elif 3<=hours<=6:
    charge = 15
    print(f'Charge: {charge}PLN')
else:
    charge = 20
    print(f'Charge: {charge}PLN')
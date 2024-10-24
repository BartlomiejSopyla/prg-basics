import vmachine

value1 = 23
value2 = 8
value3 = 2
value4 = 0

result1 = vmachine.f(value1)
result2 = vmachine.f(value2)
result3 = vmachine.f(value3)
result4 = vmachine.f(value4)

print(f'Minimum amount of coins that needs to be used in order to pay {value1}: {result1}')
print(f'Minimum amount of coins that needs to be used in order to pay {value2}: {result2}')
print(f'Minimum amount of coins that needs to be used in order to pay {value3}: {result3}')
print(f'Minimum amount of coins that needs to be used in order to pay {value4}: {result4}')
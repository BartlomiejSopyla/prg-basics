import evenodd

value1 = 3124
value2 = 20576
value3 = 13115

boolt = True
boolf = False

result1 = evenodd.f(value1, boolt)
result2 = evenodd.f(value1, boolf)
result3 = evenodd.f(value2, boolf)
result4 = evenodd.f(value2, boolt)
result5 = evenodd.f(value3, boolt)

print(f'Even numbers: {boolt}, the sum in {value1} is: {result1}')
print(f'Even numbers: {boolf}, the sum in {value1} is: {result2}')
print(f'Even numbers: {boolt}, the sum in {value2} is: {result3}')
print(f'Even numbers: {boolf}, the sum in {value2} is: {result4}')
print(f'Even numbers: {boolt}, the sum in {value3} is: {result5}')
import math
# ###
# # Calculates the area of a triangle based on the lengths
# # of the triangle's sides
# #3, 4, 5 (result is 6)
# 5, 12, 13 (result is 30)
# 7, 24, 25 (result is 84)
def triangle_area(a,b,c):
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area

pole1 = triangle_area(3,4,5)
pole2 = triangle_area(5,12,13)
pole3 = triangle_area(7,24,25)
print(f'The area of ​​a triangle with sides 3,4,5 is {pole1}')
print(f'The area of ​​a triangle with sides 5,12,13 is {pole2}')
print(f'The area of ​​a triangle with sides 7,24,25 is {pole3}')
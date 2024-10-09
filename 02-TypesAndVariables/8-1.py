###
# Calculation of circle area and circumference 
#

# determine radius and PI values
# calculate area 
# calculate circumference 
# display results

import math

radius = int(input('Enter radius: '))
pi = math.pi
area = pi*(radius**2)
circumference = 2*pi*radius

print(f'Circle area: {round(area, 2)}')
print(f'Circle circumference: {round(circumference, 2)}')
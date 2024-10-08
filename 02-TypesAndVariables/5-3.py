###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = int(input('Podaj krawędź a: \n'))
b = int(input('Podaj krawędź b: \n'))
c = int(input('Podaj krawędź b: \n'))
volume = a*b*c
cuboid_surface_area = 2*(a*b)+2*(b*c)+2*(a*c)
print(f'The volume of a cuboid is: {volume}')
print(f'The surface area of a cuboid is: {cuboid_surface_area}')
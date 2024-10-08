import math
#Tree 1: 160 Tree 2: 90 Tree 3: 230 Tree 4: 120
circumference = float(input('Enter tree circumference in cm: '))
diameter = circumference/math.pi
cut_down = diameter>=50

print('Tree can be cut down: ', cut_down)
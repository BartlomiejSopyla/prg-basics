# Write a program that creates the following pattern. Sample result:

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

star = '*'

for i in range(1,6):
    print(star*i)

for i in range(4,0,-1):
    print(star*i)
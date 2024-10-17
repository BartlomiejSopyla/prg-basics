# Write a program that allows you to convert time in 24-hour format to 12-hour format. 
# The time in 24-hour format (hh:mm) is read from the keyboard. Sample result:

# Enter time (24-hour format): 16:32
# Time in 12-hour format: 4:32pm

time24 = input('Enter time (24-hour format): ')
hours = int(time24[:2])
minutes = int(time24[3:5])

if hours <= 12:
    print(f'Time in 12-hour format: {time24}am')
elif hours > 12:
    hours -= 12
    print(f'Time in 12-hour format: {hours}:{minutes}pm')
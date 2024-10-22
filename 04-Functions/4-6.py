###
<<<<<<< HEAD
=======
# Define a function that returns the full name of a day of the week based on its number.
>>>>>>> db686eb2e29e12eb2ec9c2bd57476948c6abc43d
# Function that returns the full name of a day of the week
# based on its number
#
def day_name(day_number):
    result = ''
    if day_number == 1:
        result = 'Monday'
    elif day_number == 2:
        result = 'Tuseday'
    elif day_number == 3:
<<<<<<< HEAD
        result = 'Wednesday'
    elif day_number == 4:
        result = 'Thursday'
    elif day_number == 5:
        result = "Friday"
=======
        result = 'Wenseday'
    elif day_number == 4:
        result = 'Thursday'
    elif day_number == 5:
        result = 'Friday'
>>>>>>> db686eb2e29e12eb2ec9c2bd57476948c6abc43d
    elif day_number == 6:
        result = 'Saturday'
    elif day_number == 7:
        result = 'Sunday'
<<<<<<< HEAD
=======
    else:
        print('Wrong day number')
>>>>>>> db686eb2e29e12eb2ec9c2bd57476948c6abc43d
    return result

# Function usage
print('The name of day 5 in the week is', day_name(5))
print('The name of day 3 in the week is', day_name(3))
print('The name of day 7 in the week is', day_name(7))
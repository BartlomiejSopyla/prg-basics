<<<<<<< HEAD
def time_string(hours, minutes, time_format):
    if time_format == '24':
        return f"{hours:02}:{minutes:02}"
    elif time_format == '12':
        suffix = 'am' if hours < 12 else 'pm'
        if hours == 0 and minutes == 0:
             return f"{hours:02}:{minutes:02} Midnight"
        elif hours <= 12:
            return f"{hours:02}:{minutes:02}{suffix}"
        else:
            formated_time = hours - 12
            return f"{formated_time:02}:{minutes}{suffix}"
    else:
        print("Invalid time format, please enter '12' or '24'")

result = time_string(13, 46, '24')
print(result)
=======
# Define a function time_string(hours, minutes, time_format) that, given the number of hours (0..23) and the number of minutes (0..59), 
# returns a string specifying the time in the given format ('24' for 24-hour time and '12' for 12-hour time).

# Then write a program that tests whether the function works correctly.

# time_string(15, 38, '24') returns '15:38'
# time_string(8, 3, '24') returns '08:03'
# time_string(0, 5 '24') returns '00:05'
# time_string(11, 15, '12') returns '11:15am'
# time_string(0, 7, '12') returns '12:07am'
# time_string(7, 30, '12') returns '7:30am'
# time_string(12, 46, '12') returns '12:46pm'
# time_string(13, 10, '12') returns '1:10pm'
# time_string(19, 02, '12') returns '7:02pm'
# Hint: Use f-strings formatting. Search the Internet for 'Format numbers using f-strings'.

def time_string(hours, minutes, time_format):
    if time_format == '24':
        hours = str(hours)
        minutes = str(minutes)
        time = hours + ':' + minutes
    elif time_format == '12':
        if hours<=12:
            if hours<10:
                hours = str(hours)
                minutes = str(minutes)
                time = '0' + hours + ':' + minutes + 'am'
            else:
                hours = str(hours)
                minutes = str(minutes)
                time = hours + ':' + minutes + 'am'
        else:
            hours -= 12
            hours = str(hours)
            minutes = str(minutes)
            time = hours + ':' + minutes + 'pm'
    return time

time2 = time_string(11, 15, '12')
print(time2)
>>>>>>> db686eb2e29e12eb2ec9c2bd57476948c6abc43d

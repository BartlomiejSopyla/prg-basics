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


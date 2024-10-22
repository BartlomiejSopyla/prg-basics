def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100

<<<<<<< HEAD
def cm_to_in(n):
    return round(n*0.39, 2)

def feet_and_inches_to_cm(feet, inch):
    feet_cm = feet * 30.48
    inch_cm = inch * 2.54
    total = feet_cm + inch_cm
    return total
=======
def cm_to_inch(n):
    return n*0.39

def feet_and_inch_to_cm(f,i):
    f = f * 30.48
    i = i * 2.54
    total = f+i
    return total

>>>>>>> db686eb2e29e12eb2ec9c2bd57476948c6abc43d
if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
<<<<<<< HEAD
    print(f'30cm = {cm_to_in(30)}inches')
    print(f'5ft 7 = {feet_and_inches_to_cm(5,7)}cm')
=======
    print(f'30cm = {cm_to_inch(30)}')
    print(f'5f10 = {feet_and_inch_to_cm(5,10)}')
>>>>>>> db686eb2e29e12eb2ec9c2bd57476948c6abc43d


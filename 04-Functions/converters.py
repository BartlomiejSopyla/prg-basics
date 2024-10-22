def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100

def cm_to_inch(n):
    return n*0.39

def feet_and_inch_to_cm(f,i):
    f = f * 30.48
    i = i * 2.54
    total = f+i
    return total

if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f'30cm = {cm_to_inch(30)}')
    print(f'5f10 = {feet_and_inch_to_cm(5,10)}')


def f(detector):
    people_in_room = 0
    max_people = 0
    for i in detector:
        if i == '+':
            people_in_room +=1
        elif i == '-':
            people_in_room -=1
        
        if people_in_room > max_people:
            max_people = people_in_room
        
    return max_people >= 3
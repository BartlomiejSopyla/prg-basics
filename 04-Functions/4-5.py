<<<<<<< HEAD
###
# Calculates the final grade for a test based
# on the number of points obtained
#
=======
# ###
# # Calculates the final grade for a test based
# # on the number of points obtained
# #Less than 10 points, final grade: Fail
# At least 10 points, final grade: Satisfactory
# At least 14 points, final grade: Good
# At least 18 points, final grade: Excellent
>>>>>>> db686eb2e29e12eb2ec9c2bd57476948c6abc43d
def pts_to_grade(points):
    grade = ''
    if points >= 18:
        grade = 'Excellent'
<<<<<<< HEAD
    elif points < 18 and points >= 14:
        grade = 'Good'
    elif points > 14 and points <= 10:
=======
    elif points <18 and points >= 14:
        grade = 'Good'
    elif points <14 and points >= 10:
>>>>>>> db686eb2e29e12eb2ec9c2bd57476948c6abc43d
        grade = 'Satisfactory'
    else:
        grade = 'Fail'
    return grade

test_result = 18
final_grade = pts_to_grade(test_result)
print(f'You scored {test_result} points on the test. Your final grade is {final_grade}')
# Yes-no question are often used in surveys to gauge people's attitudes with regard to specific ideas or beliefs. 
# Write a program that prints a survey consisting of three questions. 
# Save the answers to logical type variables. Then view the survey result. 
# Sample result:

# SURVEY Are you interested in computer science? (y/n): y
# Do you like playing computer games? (y/n): n
# Do you have an Instagram account? (y/n): y

# SURVEY RESULTS Interested in computer science: Yes
# Playing computer games: No
# Has an Instagram account: Yes

question1 = input('Are you interested in computer science? (y/n): ').lower()
anwser1 = True if question1 == 'y' else False

question2 = input('Do you like playing computer games? (y/n): ').lower()
anwser2 = True if question2 == 'y' else False

question3 = input('Do you have an Instagram account? (y/n): ').lower()
anwser3 = True if question3 == 'y' else False

print('SURVEY RESULTS: ')
print(f'Interested in computer science: {'Yes' if anwser1 == True else 'No'}')
print(f'Playing computer games: {'Yes' if anwser2 == True else 'No'}')
print(f'Interested in computer science: {'Yes' if anwser3 == True else 'No'}')
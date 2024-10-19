# The payment card is secured with a four-digit PIN code (0805). 
# Write a program that checks if the PIN code entered in the payment terminal is correct. 
# The user has up to three possibilities for entering a PIN code. 
# In case of three unsuccessful attempts, the card is blocked. Sample result:

# Enter the PIN code: 2398
# Incorrect...
# Enter the PIN code: 0912
# Incorrect...
# Enter the PIN code: 7860
# Incorrect...
# Sorry, your payment card has been blocked.

code = '0805'
attempts = 3

while attempts > 0:
    enter = input('Enter the PIN code: ')
    if enter != code:
        attempts -=1
        if attempts>0:
             print('Incorrect...')
        else:
            print('Sorry, your payment card has been blocked.')
    else:
        print('Correct PIN')
        break
###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    char = ord(plain_text)
    char = char+1
    # add one to the character's code
    plain_text=char
    # replace new character code with its
    # corresponding character (use chr())
    ...
    # add encrypted character to encrypted text
    ...

print(plain_text...)
print(encrypted_text...)
def letters(text, letter):
    count = 0
    for i in text:
        text = text.lower()
        if i == letter:
            count += 1
    return count

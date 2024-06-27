input_string = input()

letters = input_string[1:-1].replace(" ", "").split(',')

unique_letters = set()

for letter in letters:
    if letter.isalpha():  
        unique_letters.add(letter)

print(len(unique_letters))

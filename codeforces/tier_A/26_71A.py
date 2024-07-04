
n = int(input())

for _ in range(n):
    word = input()
    if len(word) > 10:
        abbreviated_word = f"{word[0]}{len(word) - 2}{word[-1]}"
        print(abbreviated_word)
    else:
        print(word)

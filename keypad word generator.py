
keys = {
    '2': 'abc', '3': 'def', '4': 'ghi',
    '5': 'jkl', '6': 'mno', '7': 'pqrs',
    '8': 'tuv', '9': 'wxyz'
}

def count_combos(word):
    if len(word) == 0:
        return 1

    for digit in keys:
        if word[0] in keys[digit]:
            return len(keys[digit]) * count_combos(word[1:])

    return 0


input("Letters per digit - Press Enter")

print("count_combos('cat') =", count_combos('cat'))
print("count_combos('rabbit') =", count_combos('rabbit'))

d = input("Enter a word (try tree or ball ):  ")
guess = input("Guess the number of combinations: ")

input("Press Enter to see the answer.")

print("Word:", d)
print("Correct answer:", count_combos(d))
print("Your guess:", guess)



def ways(n):
    if n <= 1:
        return 1
    return ways(n-1) + ways(n-2)


def count_paren(n):
    if n == 0:
        return 1

    return count_paren(n-1) + count_paren(n-2)

n=int(input("Enter the number of pairs of parentheses: "))
guess=input("Enter your guess for the number of arrangements: ")
input(f"Number of arrangements for {n} pairs of parentheses is: {count_paren(n)}")
print(f"Your guess was: {guess}")
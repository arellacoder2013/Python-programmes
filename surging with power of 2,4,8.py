# ================================
# POWER OF TWO SCANNER
# ================================

# PART 1 — The n & (n-1) Trick

n = 16

print("PART 1: n & (n-1) Trick")
print(n, "->", bin(n))
print(n & (n - 1), "->", bin(n & (n - 1)))

# PART 2 — Power of 2 Check

def is_power_of_2(num):
    return num > 0 and (num & (num - 1)) == 0
numbers = [1, 2, 4, 6, 8, 12, 16, 18, 32]

print("\nPART 2: Power of 2")

for num in numbers:
    print(num, "->", is_power_of_2(num))


# PART 3 — Power of 4 Check

def is_power_of_4(num):
    if not is_power_of_2(num):
        return False
    position = 0
    while num > 1:
        num = num >> 1
        position += 1
    return position % 2 == 0

print("\nPART 3: Power of 4")

for num in numbers:
    print(num, "->", is_power_of_4(num))

# PART 4 — Power of 8 Check

def is_power_of_8(num):
    if not is_power_of_2(num):
        return False

    position = 0

    while num > 1:
        num = num >> 1
        position += 1

    return position % 3 == 0


print("\nPART 4: Power of 8")

for num in numbers:
    print(num, "->", is_power_of_8(num))


# PART 5 — Binary Exponentiation

def binary_power(base, exponent):
    answer = 1

    while exponent > 0:
        if exponent & 1:
            answer *= base

        base *= base
        exponent >>= 1

    return answer


print("\nPART 5: Binary Exponentiation")
print("2^5 =", binary_power(2, 5))
print("3^4 =", binary_power(3, 4))
print("5^3 =", binary_power(5, 3))


# SUMMARY

print("\nPower of 2: one bit is set.")
print("Power of 4: position is even.")
print("Power of 8: position is divisible by 3.")
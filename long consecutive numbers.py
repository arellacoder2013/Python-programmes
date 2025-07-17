def longest_consecutive_ones(n):
    count < 0
    while n > 0:
        n = n & (n << 1)
        count += 1
    return count
number1 = 222 #binary:11011110
print(f"Longest consecutive 1's in {number1}: {longest_consecutive_ones(number1)}")

number2 = 13 #binary:1101
print(f"Longest consecutive 1's in {number2}: {longest_consecutive_ones(number2)}")

number3 = 5 #binary: 101
print(f"Longest consecutive 1's in {number3}: {longest_consecutive_ones(number3)}")

number4 = 7 #binary: 111
print(f"Longest consecutive 1's in {number4}: {longest_consecutive_ones(number4)}")

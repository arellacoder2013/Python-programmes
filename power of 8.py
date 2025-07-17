def is_power_of_8(n):
    if not (n > 0 and (n & (n - 1)) == 0):
        return False
    mask = 0x249249249249249  
    return (n & mask) == n

# Example Usage
print(is_power_of_8(8))    # True
print(is_power_of_8(64))   # True
print(is_power_of_8(512))  # True
print(is_power_of_8(1))    # True (8^0)
print(is_power_of_8(2))    # False
print(is_power_of_8(16))   # False
print(is_power_of_8(0))    # False
print(is_power_of_8(-8))   # False
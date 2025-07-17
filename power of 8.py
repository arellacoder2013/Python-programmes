def is_power_of_8(n):
    if not (n > 0 and (n & (n - 1)) == 0):
        return False
    # Check if the single set bit is at a position that is a multiple of 3
    # This mask checks for bits at positions 0, 3, 6, 9, ...
    # Any power of 8 will have its single set bit at one of these positions.
    # The mask ensures that if the number has a single set bit,
    # it must align with one of these "power of 8" positions.
    # Note: This mask is for 64-bit integers.
    # For smaller integers, a shorter mask can be used, e.g., 0xB6DB6DB6 for 32-bit.
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
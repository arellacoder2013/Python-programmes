
switch_value = 45 #binary:101101

def show_bits(number):
    return bin(number)[2:]

print(" SMART SWITCH MONITOR")
print("Value:", switch_value)
print("Binary:", show_bits(switch_value))

binary_value = show_bits(switch_value)

set_bits = binary_value.count("1")
zero_bits = binary_value.count("0")

print("💡 ON switches:", set_bits)
print("⭕ OFF switches:", zero_bits)

count = 0
temp = switch_value

while temp > 0:
    if temp & 1:
        count += 1
    temp = temp >> 1

print("🔢 Total ON:", count)

position = 0
temp = switch_value

while temp > 0:
    if temp & 1:
        break
    position += 1
    temp = temp >> 1

print("👉 First ON position:", position)

for i in range(6):
    mask = 1 << i
    print("🎯 Bit", i, "Mask:", mask, "Binary:", show_bits(mask))

switch_names = [
    "Bedroom Light 💡",
    "TV 📺",
    "Air Conditioner ❄️",
    "Garage Door 🚪",
    "Kitchen Light 💡",
    "Alarm 🚨"
]

for i in range(6):
    mask = 1 << i

    if switch_value & mask:
        print("✅", switch_names[i], "ON")
    else:
        print("❌", switch_names[i], "OFF")



print("SMART SWITCH SUMMARY")
print("================================")
print("Switch Value:", switch_value)
print("Binary Form:", show_bits(switch_value))
print("Total ON Switches:", count)
print("First ON Switch Position:", position)
print("================================")



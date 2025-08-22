binary_str = '1011'
decimal = 0

for digit in binary_str:
    decimal = decimal * 2 + int(digit)

print("decimal number is",decimal)  # Output: 11




decimal_num = 697
binary_str = bin(decimal_num)
print("binary number is ",binary_str)


def binary_to_hex(binary_str1):
    decimal1 = int(binary_str1, 2)
    return hex(decimal1)

print(binary_to_hex('1010111001'))
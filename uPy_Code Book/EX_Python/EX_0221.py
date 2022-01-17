"""
EX_0221 (Python Bitwise operators)
Basic Python programming by appsofttech.com
"""
# Bitwise operators: &, |, ^, ~, <<, >>

a = 11  # 0b01011
b = 21  # 0b10101
c = 1
d = 0
e = 0xA

print(bin(a))
print(bin(b))
print(bin(a&b))     # 0b00001
print(bin(a|b))     # 0b11111
print(bin(a^b))     # 0b11110
print(bin(~c))      # -0b10
print(bin(~d))      # -0b1
print(bin(b<<1))    # 0b101010
print(bin(b>>1))    # 0b1010
print(e)

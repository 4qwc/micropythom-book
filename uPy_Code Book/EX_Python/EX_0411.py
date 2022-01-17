"""
EX_0411 (Python String format())
Basic Python programming by appsofttech.com
"""
# String format() with index

a = 10
b = 20
c = 30

num = "a: {} b: {} c: {:.2f}"
print(num.format(a, b, c))
print("...................")
num = "a: {1} b: {0} c: {2:.2f}"
print(num.format(a, b, c))

print('...')

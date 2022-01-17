"""
EX_0308 (Python continue)
Basic Python programming by appsofttech.com
"""
# continue

a = 0

while a < 10:
    a += 1
    if a >= 5 and a <= 8:
        continue
    print(a)

print('...')

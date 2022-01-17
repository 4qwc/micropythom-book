"""
EX_0210 (Python Dictionary)
Basic Python programming by appsofttech.com
"""
# Access & Change Items in Dic

a = {1: 2020, 'a': 2021, 'b': 2022, 2: 2023}
b = {1: 2021, 2: 2020, 3: 2022, 4: 2023}

print('Dic a:', a)
print('Dic b:', b)

print(a[1])
a[1] = 2025
print(a[1])
x = b.get(1)
print(x)

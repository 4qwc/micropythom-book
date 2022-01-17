"""
EX_0211 (Python Dictionary)
Basic Python programming by appsofttech.com
"""
# Adding & Removing Items to Dic

a = {1: 2020, 'a': 2021, 'b': 2022, 2: 2023}
b = {1: 2021, 2: 2020, 3: 2022, 4: 2023}

print('Dic a:', a)
a['c'] = 2024
print('Dic a:', a)
a.pop(1)
print('Dic a:', a)
del a[2]
print('Dic a:', a)

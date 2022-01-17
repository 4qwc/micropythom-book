"""
EX_0403 (Python functions)
Basic Python programming by appsofttech.com
"""
# keyword global

a = 10

def increment_one():
    global a
    print("function increment_one")
    a = a + 1
    print(a)

increment_one()
print('...')

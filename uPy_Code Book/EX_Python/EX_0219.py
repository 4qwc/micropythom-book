"""
EX_0219 (Python Identity operators)
Basic Python programming by appsofttech.com
"""
# Identity operators: is, is not

a = ["Programming", "Python"]
b = a
c = ["Programming", "Python"]
d = "ProgrammingPython"
e = "ProgrammingPython"
f = "Programming"

print(a is b)
print(b is a)
print(c is a)
print(d is e)
print(d is not e)
print(f is e)
print(f is not e)

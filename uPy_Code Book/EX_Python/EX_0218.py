"""
EX_0218 (Python Logical operators)
Basic Python programming by appsofttech.com
"""
# Logical operators: and, or, not

a = 10
b = 21
c = 20

"""
---------------------------------------
and operator|or operator|not operator
------------|---------- |------------
T and T: T  |T or T: T  |not F: T
T and F: F  |T or F: T  |not T: F
F and T: F  |F or T: T  |
F and F: F  |F or F: R  |
"""

print((a>b) and (a<c))
print((a>b) or (a<c))
print(not(a>b))
print(not(a<b))

"""
EX_0222 (Python Collections (Arrays))
Basic Python programming by appsofttech.com
"""
# Collections (Arrays)

myList = ["AppSoftTech", "MicroPython", "ESP32"]

print(type(myList))
print(myList)
print(len(myList))

print(myList[0])
print(myList[0:3])
print(myList[0:2])
print(myList[0:])
print(myList[1:])

for ml in myList:
    print(ml)

myList[0] = "AST"  # valid.....
print(myList)

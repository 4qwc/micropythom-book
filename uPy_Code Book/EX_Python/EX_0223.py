"""
EX_0223 (Python Collections (Arrays))
Basic Python programming by appsofttech.com
"""
# Collections (Arrays)

myTuple = ("AppSoftTech", "MicroPython", "ESP32")

print(type(myTuple))
print(len(myTuple))

print(myTuple)
print(myTuple[0])
print(myTuple[2])
print(myTuple[0:2])

for mt in myTuple:
    print(mt)

# myTuple[0] = "AST"  # error.....

myTuple = ("AST", "MicroPython", "ESP32")
print(myTuple)



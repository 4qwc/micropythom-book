"""
EX_0225 (Python Collections (Arrays))
Basic Python programming by appsofttech.com
"""
# Collections (Arrays)

myDict = {"Company": "AppSoftTech", "Language":"MicroPython", "ESP":32}

print(type(myDict))
print(len(myDict))
print(myDict)

print(myDict["Company"])

for idx in myDict:
    print(idx, end=": ")
    print(myDict[idx])





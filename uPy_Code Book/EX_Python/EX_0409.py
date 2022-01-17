"""
EX_0409 (Python input())
Basic Python programming by appsofttech.com
"""
# input()

n = input("Input Number for Loop:")

if (int(n) > 0):
    for i in range(1, int(n)+1):
        print(i)

print('...')

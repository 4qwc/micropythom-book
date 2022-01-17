"""
EX_0213 (Python Variables)
Basic Python programming by appsofttech.com
"""
# Local Variables

a = "a is global"

def my_func():
    a = "a is local"
    print("a (in my_func) :", a)

my_func()
print("a (main) :", a)

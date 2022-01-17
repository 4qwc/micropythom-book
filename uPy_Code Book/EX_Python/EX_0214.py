"""
EX_0214 (Python Variables)
Basic Python programming by appsofttech.com
"""
# Local Variables

a = "a is global"

def my_func_a():
    a = "a is local"
    def my_func_b():
        nonlocal a
        a = "a is nonlocal"
        print("a (my_func_b) :", a)

    my_func_b()
    print("a (my_func_a) :", a)

my_func_a()
print("a (main) :", a)

def function_sum():
    a = 100
    b = 100
    c = a+b

    print(c)

def function_1(a, b):
    # a = 100
    # b = 100
    c = a+b

    print(c)

def function_2(a, b, c, d=0, e=10):
    print(a, b, c, d, e)


def function_3(*args, **kwargs):
    print(args)
    print(kwargs)

# function_sum()
# function_1(10, 30)
# function_2(1, 2, 3, 40, 50)
# function_3(10, 20, 50, 60, 30, 80, 100, name="hasan", age=20, dept="CSE")

"""
this is a multiline comment

this is a multiline comment
"""
def function_4(num):
    return num

# number = function_4(100)
print(function_4(100)+100)

# sum_num = function_1(10, 20)+1000
# print(sum_num)
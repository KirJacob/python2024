import Les0MyHelper


def function1():
    print("do something, proper indention for function body")


def function2x(x):
    return 2 * x


def sum_of_two_num(x, y):
    return x + y


def bmi_calculator(name, weight, height):
    bmi = weight / (height ** 2)
    bool_bmi = bmi < 25
    print("your body index is: " + str(bmi))
    if bool_bmi:
        print(name + " doesnt have obesity")
    else:
        print(name + " has obesity")
    return bmi


Les0MyHelper.separator("function example")
a = function2x(4)
print(function2x(3))
print(a)
print(sum_of_two_num(1, 2))

name1 = "Tom"
height1 = 1.90
weight1 = 80
bmi_calculator(name1, weight1, height1)

name2 = "Katy"
height2 = 1.70
weight2 = 60
bmi_calculator(name2, weight2, height2)

name3 = "Bob"
height3 = 2
weight3 = 150
bmi_calculator(name3, weight3, height3)


# convert miles to kilometers
def convert(miles):
    return miles * 1.60934


# calculate are of rectangle
def area_rec(x, y):
    return x * y


# is even
def is_even(x):
    return x % 2 == 0


Les0MyHelper.separator("Functions lesson -- exercises")
print((convert(2)))
print(area_rec(2, 3))
print(is_even(3))
print(is_even(4))

import Les0MyHelper


def say_hello(name):
    return "hello " + name + " from python3"


print("Hi from PyScriptOne")
print(say_hello("Kirill"))

# Data Types in Python
intSample = 10
floatSample = 2.5
strSample = "Kirill"
listSample = [5, 2, "Hey"]
dictSample = {"Ukraine": "Kyiv", "Belarus": "Minsk"}
tupSample = ("Kyiv", "Center", 3.0, 2021)
setSample = {"a", 3, "b", "b"}
boolSample = False

print(listSample[0], listSample[1])
print(dictSample["Ukraine"])
print(setSample)
# setSample ?

# if else, elif
if intSample > 10:
    print("greater than 10")
    print("inside if")
elif intSample == 10:
    print("equal to 10")
elif intSample < 0:
    print("less than zero")
else:
    print("less than 10")
    print("inside else")

print("out of if block")

print("Kyiv" in ("Paris", "Berlin", "Kyiv"))

Les0MyHelper.separator("square equation sample")
Les0MyHelper.separator("words")
a = 1
b = -40
c = 1
print("determinant calculation")
d = b * b - 4 * a * c
if d > 0:
    print("d greateer than zero, two solutions")
    if (d > 10):
        print("d is greater than 10, additional if")
elif d == 0:
    print("d equal to zero, one solution")
else:
    print("no solutions, or no real solutions")

# this is comment which is started from #
print("----------body index calculation----------")
name = "Tom"
height = 1.85
weight = 112
bmi = weight / (height ** 2)
boolBmi = bmi < 25
print("your body index is: " + str(bmi))
if boolBmi:
    print(name + " doesnt have obesity")
else:
    print(name + " has obesity")

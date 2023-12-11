import Les0MyHelper


a = ["Hey", "Hello", "Goodbye"]

print(a[0])
print(a[1])
print(a[2])

# for each syntax
for element in a:
    print(element)

b = [20, 30, 50, 60]
for number in b:
    print(number)


def list_sum(list_elem):
    total_sum = 0  # - accumulator variable
    for num in list_elem:
        total_sum = total_sum + num
    return total_sum


print(list_sum(b))
list(range(1, 5))  # generate range from 1 to 5
print(list_sum(list(range(1, 5))))

total_sum2 = 0
for i in range(1, 4):
    print(i)
    total_sum2 += i
print(total_sum2)

Les0MyHelper.separator("show numbers from 1 to 100 divisible to 3")
print(list(range(1, 100)))
total_sum3 = 0
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        total_sum3 += i
        print(i)
print("total_sum3=" + str(total_sum3))


#  my_function(n, k)
#  n > 20 => 0
#  n <=20 => 1..to n, all even numbers pow to k and sum, return sum

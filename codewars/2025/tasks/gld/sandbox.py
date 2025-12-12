def even_numbers():
    num = 0
    while True:
        yield num
        num += 2


# Использование генератора
# evens = even_numbers()
# for _ in range(5):
#     print(next(evens), end=" ")


evens = even_numbers()
for element in range(10):
    input_param = input("eneter smth=")
    print(f"input_param={input_param} generator={next(evens)}")
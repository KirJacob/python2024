# callable variable
def hello():
    print("Hello!")


hello()


def user_age_in_seconds():
    user_age = int(input("Enter your age: "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    return age_seconds


print(user_age_in_seconds())

# dont reuse existing names
# def print():
#     print("helo wold") - it called itself

friends = ["Kirill", "Tolik"]
# shadow variable from outer scope


def add_friends():
    friend_name = input("Enter your name:")
    f = friends + [friend_name]
    return f


f = add_friends()
print(f)

# using functions before they get defined is not possible


def add_friend():
    friends.append("Rolf")


add_friend()
print(friends)




users = [
    (0, "Job", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "longp4assword"),
    (3, "username", "1234")
]

# example of a dictionary comprehension is below
username_mapping = {user[1]: user for user in users}
print(username_mapping)

lst01 = [1, 2, 3, 4]
recall_comprehension = [num for num in lst01]

username_input = input("Enter your username: ")
username_password = input("Enter your password: ")

# it doesnt matter where to save first variable
_, username, password = username_mapping[username_input]

if username_password == password:
    print("Your details are correct!")
else:
    print("Your details are incorrect!")

# processing
if username_mapping[username_input][2] == username_password:
    print("Login is succesful")
else:
    print("Login or password is wrong")

# add more cases, try again, 3 attempts not existing user, wrong password

username_password = input("Try again?: ")
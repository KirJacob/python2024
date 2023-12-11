movies_watched = {"The Matrix", "Green Book", "Her"}
user_movie = input("Enter something you have watched recently?:")
print(user_movie in movies_watched)

if user_movie in movies_watched:
    print(f"i've watched {user_movie} too!")
else:
    print("i haven't watched that yet")

number = 7
user_input = "y"

while user_input != "n":
    user_input = input("Would you like to play? (y/n)").lower()
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif abs(number - user_number in (1, -1)):  # another option abs(number-user_number) == 1
        print("You were off by one.")
    else:
        print("Sorry its wrong!")

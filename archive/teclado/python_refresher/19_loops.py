friends = ["Rolf", "Jen", "Bob", "Anne"]

print("---------------------------")
for friend in friends:
    print(f"{friend} is my friend")

print("---------------------------")
for num in range(4):
    print(f"{friends[num]} is my friend")


grades = [35, 67,98, 100, 100]
total = sum(grades)
amount = len(grades)
print(total/amount)
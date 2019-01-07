name = input("Enter your name!")

while len(name)<=0:
    print("Name is blank! Please enter your name!")
    name = input("Enter your name!")

print(name[: : 2])

for i in range(0, len(name), 2):
    print(name[i], end="")
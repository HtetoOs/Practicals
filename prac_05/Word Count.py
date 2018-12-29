txt = input(">>>")
print("Text:", txt)

while txt != "":
    count = txt.count(input("Please enter the character to count:"))
    print(count)
print("Input cannot be blank")
txt = input(">>>")


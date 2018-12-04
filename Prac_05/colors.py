COLORS = ["AB is AliceBlue", "AW is AntiqueWhite", "AW1 is AntiqueWhite1", "AQ1 is aquamarine", "AZ1 is azurel1"]
CLR_CODES = {"AB": "#f0f8ff", "AW": "#faebd7", "AW1": "#ffefdb", "AQ1": "#7fffd4", "AZ1": "#f0ffff"}
CLR_NAMES = {"AB": "AliceBlue", "AW": "AntiqueWhite", "AW1": "AntiqueWhite1", "AQ1": "aquamarine", "AZ1": "azurel1"}
print()
for i in range(len(COLORS)):
    print(COLORS[i])
print()

CODE = input("Enter a short name to get the code:").upper()
while CODE != "":
    if CODE in CLR_CODES:
        print("Code for", CLR_NAMES[CODE], "is", "<",CLR_CODES[CODE],">")
    else:
        print("Invalid CODE!")
    CODE = input("Enter a short name to get the code:").upper()

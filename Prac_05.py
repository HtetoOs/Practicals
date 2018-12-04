"""

CP1404/CP5632 Practical

State names in a dictionary

File needs reformatting

"""



# TODO: Reformat this file so the dictionary code follows PEP 8 convention
STATES = ["QLD is Queenland", "NSW is New South Wales", "NT is Northern Territory", "WA is Western Australia", "ACT is Australian Capital Territory", "VIC is Victoria", "TAS is Tasmania"]
STATE_NAMES = {"QLD": "Queensland", "qld": "Queensland", "NSW": "New South Wales", "nsw": "New South Wales", "NT" :"Northern Territory", "nt": "Northern Territory", "WA" : "Western Australia", "wa" : "Western Australia", "ACT":"Australian Capital Territory", "act":"Australian Capital Territory", "VIC":"Victoria", "vic":"Victoria", "TAS":"Tasmania", "tas":"Tasmania"}

for i in range(len(STATES)):
    print(STATES[i],)
print("\n")


state = input("Enter short state: ")

while state != "":

    if state in STATE_NAMES:

        print(state, "is", STATE_NAMES[state])

    else:

        print("Invalid short state")

    state = input("Enter short state: ")
import random
picks = int(input("How many quick picks?>>>"))
for i in range(picks):
    pick1 = random.randint(1, 10) + random.randint(1,7)
    pick2 = pick1 + random.randint(1, 7)
    pick3 = pick2 + random.randint(1, 7)
    pick4 = pick3 + random.randint(1, 7)
    pick5 = pick4 + random.randint(1, 7)
    print("{:3}{:3}{:3}{:3}{:3}".format(pick1,pick2,pick3,pick4,pick5))

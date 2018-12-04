import random

MAX_INCREASE = 0.1
MAX_DECREASE = 0.05
MIN_PRICE = 0.1
MAX_PRICE = 100
INITIAL_PRICE = 1
OUTPUT_FILE = "Results.txt"

out_file = open(OUTPUT_FILE, 'w')

price = INITIAL_PRICE
print("Original Value: ${:,.2f}".format(price))
i = 0

while price >= MIN_PRICE and price <= MAX_PRICE:
    price_charge = 0
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)

    else:
        price_change = random.uniform(-MAX_DECREASE, 0)
    price *= (1 + price_change)
    i += 1
    print("On day {} price is: ${:,.2f}".format(i, price), file = out_file)

out_file.close()

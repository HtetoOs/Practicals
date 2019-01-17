n = int(input("Please input how many rows the pyramid will have."))
n1 = 0

for i in range(n):
    n1 = n + n1
    n -= 1

print(n1)

n = int(input("Please input how many rows the pyramid will have.(recursion)"))

def rec_pyramid(n):
    """Calculate blocks needed for a given number of rows of a 2D pyramid."""
    # base case: we need zero blocks for zero (or fewer!) rows
    if n <= 0:
        return 0
    # recursive case: each row contains the number of blocks as its row number
    # ... plus the rest of it
    return n + rec_pyramid(n - 1)

print(rec_pyramid(n))

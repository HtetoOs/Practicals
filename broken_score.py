def main():
    score = float(input("Enter score: "))
    print(decideScore(score))

def decideScore(score):
    if score < 50 and score > 0:
        return("Bad")
    elif score >= 50 and score < 90:
        return("Passable")
    elif score >= 90 and score < 100:
        return("Excellent")
    else:
        return("Please enter a score between 0 and 100.")

main()
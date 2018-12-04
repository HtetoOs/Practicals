def main():
        numIncomes=[]
        numMonths = int(input("How many months? >>>"))

        for months in range(1, numMonths+1):
                       incomes = float(input("Enter income for month " + str(months) + ":"))
                       numIncomes.append(incomes)


        print("\nIncome Report\n--------------")
        total = 0
        for months in range(1, numMonths+1):
                incomes = numIncomes[months-1]
                total += incomes
                print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(months, incomes, total))
main()
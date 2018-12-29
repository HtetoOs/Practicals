from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    limo = Car(100,"My Limo")
    limo.add_fuel(20)
    limo.drive(115)
    print(limo.odometer)
    print(limo)



main()
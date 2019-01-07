from Prac_08.taxi import Taxi

class SilverServiceTaxi(Taxi):
    flagfall = 4.5

    def __init__(self, name, fuel,fanciness):
        super().__init__(name,fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km
        self.price_per_km *= fanciness
        self.current_fare_distance = 0

    def get_fare(self):
        """Return the price for the taxi trip."""
        return self.price_per_km * self.current_fare_distance + self.flagfall

    def drive(self, distance):
        distance_driven = super().drive(distance)
        return distance_driven

    def __str__(self):
        return "Silver Service Taxi details {} plus flagfall of {}".format(super().__str__(),self.flagfall)
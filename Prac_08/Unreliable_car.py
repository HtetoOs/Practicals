from Prac_06.car import Car

class UnreliableCar(Car):

    def __init__(self,name,fuel,reliability):
        super().__init__(name,fuel)
        self.reliability = reliability
        self.current_fare_distance = 0

    def __str__(self):
        return "{}, {} is the reliability that this car will run.".format(super().__str__(),self.fuel,self.reliability)

    def drive(self,distance):
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven
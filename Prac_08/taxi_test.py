from Prac_08.taxi import Taxi

NewTaxi = Taxi("Prius1", 100)
NewTaxi.drive(20)
print(NewTaxi)
print(NewTaxi.get_fare())
NewTaxi.start_fare()
NewTaxi.drive(40)
print(NewTaxi)
print(NewTaxi.get_fare())

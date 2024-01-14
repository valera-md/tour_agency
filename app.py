from tourist import Tourist
from date_time import Period
from tour import TourBuilder
from money import Money

tour = TourBuilder("Italy","The best parst of Italy",[Tourist("John Doe", 21), Tourist("Jane Doe", 30), Tourist("Jenny", 6)],Period("01.01.2021","02.01.2021")).withEnsurance().withGuide().build()
print(f'Destination: "{tour.destination}"')
print(f'Tour name: "{tour.name}"')
for tourist in tour.tourists:
    print(tourist)
print(f"Period: {tour.period}")
print(f"Total price: {Money(tour.cost, tour.currency)}")

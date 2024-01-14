from money import Money

_destinations = ({ "name": "Greece", "price": Money(100,"EUR")},{ "name": "France", "price": Money(120,"EUR")}, { "name": "Italy", "price": Money(200,"EUR")}, { "name": "USA", "price": Money(300,"USD")})
class _Tour:
    def __init__(self,destination,name,tourists,period):
        self.destination = destination
        self.name = name
        self.tourists = tourists
        self.period = period  
        self.cost, self.currency = self.calculateCost()
    def calculateCost(self):
        for destination_tour in _destinations:
            if destination_tour["name"] == self.destination:
                ticket_cost = destination_tour["price"].amount
                break
        tour_price = 0
        for tourist in self.tourists:
            if tourist.age <= 6:
                tour_price += ticket_cost * 0.5
            elif 7 <= tourist.age <= 15:
                tour_price += ticket_cost * 0.75
            else:
                tour_price += ticket_cost
        return (tour_price, destination_tour["price"].currency)

class TourBuilder:
    def __init__(self,destination,name,tourists,period):
        self._tour = _Tour(destination,name,tourists,period)
    def withEnsurance(self):
        ensurance = True
        self._tour.cost += self._tour.cost * 0.05
        return self
  #def withEnsurance(self):
  #  ???
  #  return self 
    def withGuide(self):
        guided = True
        self._tour.cost += 100
        return self        
    def build(self):
        return self._tour

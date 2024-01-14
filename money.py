class Money:
    _currencies = ("MDL","USD","EUR","RUB","RON")
    def __init__(self,amount,currency):
        try:
            if amount < 0:
                raise ValueError
            else:
                self.amount = amount
        except ValueError:
            print('the amount cannot be negative')
            exit()
        try:
            if currency not in self._currencies:
                raise TypeError
            else:
                self.currency = currency
        except TypeError:
            print('wrong currency')
            exit()
    
    def  __str__(self):
        return f'"{self.amount:.2f}{self.currency}"' # e.g. "100.00MDL"

#m = Money(100.00, "MDL")
#print(m)
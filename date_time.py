class Period:
    def __init__(self,start,end):
        try:
            if start > end:
                raise ValueError
            else:
                self.start = start
                self.end = end
        except ValueError:
            print('start date must be less then end date')
            exit()
    def  __str__(self):
        return f'"[{self.start} .. {self.end}]"' # e.g. "[01.01.2021 .. 02.01.2021]"

#p = Period("01.01.2021","02.01.2021")
#print(p)

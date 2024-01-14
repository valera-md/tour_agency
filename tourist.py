class Tourist:
    def __init__(self,name,age):
        try:
            if len(name) < 3:
                raise ValueError
            else:
                self.name = name
        except ValueError:
            print('the name must be at least 3 characters long')
            exit()
        try:
            if age < 1:
                raise ValueError
            else:
                self.age = age
        except ValueError:
            print('the age must not be less than 1 year')
            exit()      
    def  __str__(self):
        return f'"{self.name} ({self.age} years)"' # e.g. "John Doe (31 years)"

#t = Tourist("John Doe", 31)
#print(t)
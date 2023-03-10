class Abhi:
    name='Abhinav'
    age=18
    year=2016
    no_object=0

    #Constructor
    def __init__(self,age):
        self.age=age
        print(age)
        Abhi.no_object+=1
    def bike(self,bike):
        print(self.name+' has '+bike+' bike')

a=Abhi(12)
a.bike('bullet')
a1=Abhi(21)
print(a.no_object)
print(a.age)
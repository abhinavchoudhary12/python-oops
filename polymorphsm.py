x=2
y=4
a=x+y
print(a)
print(x-y)
print(x*y)

print("#######in background  #######")
#in background when we use add operator python call special methods
print(x.__add__(y))
print(x.__sub__(y))
print(x.__mul__(y))



#operator overloading
#addition of two instance using special methods

class Cart:
    item=[]
    def __init__(self,item):
        self.item=item
    def __add__(self, other):
        return Cart(self.item + other.item)
    #toString
    def __str__(self):
        return ("Cart({})".format(self.item))


cart1=Cart(['apple','orange','dragon-fruit'])
cart2=Cart(['caoli-flower'])
print(cart1+cart2)
maincart=cart1+cart2
print(maincart.item)

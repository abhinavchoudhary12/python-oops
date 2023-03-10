class Cart:
    item=[]
    def __init__(self,item):
        self.item+=item

    def __str__(self):
        return '{}'.format(self.item)


    def __repr__(self):
        return 'Cart({})'.format(self.item)

c=Cart(["roman","greak","myanmar"])

print(c.__str__())
print(c.__repr__())
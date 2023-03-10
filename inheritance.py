class Animal:
    legs=4
    face="danger"
    def show(self):
        print("in parent class")
        print(str(self.legs)+'  '+self.face)
class frog(Animal):
    #overridding
    def show(self):
        print("in child class")
        print(self.legs)
        print(self.face)
f=Animal()
f.show()

f1=frog()
f1.show()
class Test:

    #private variable
    def __init__(self):

       self._a=12
       #name mangling
       self.__b=21
    #private methods

    def __abhi(self):
        print("i am private method")
t=Test()
print(dir(t))

#accesing private method using class name
t._Test__abhi()

#getter setter


class Test1:
    def __init__(self):
        #private variable
        self.__e=12

    def setVal(self,value):
        self.__e=value

    def getVal(self):
        return self.__e


t1=Test1()

print("getting value from getter "+str(t1.getVal()))

t1.setVal(14)

print(t1.getVal())
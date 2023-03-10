class Library:
    books=["frozen","danis richi"]


    def __init__(self,id,book):
        print("constructor")
        self.id=id
        self.book=book

    def transatction(self):
        return ("book issued is {} to {}".format(self.book,self.id))


    @classmethod
    def const(cls,a,b):
        print("alternative constructor")
        print(a)
        print(b)
   #always have a cls(it is the class name) as the first argument
    @classmethod
    def add_book(cls,other):
        cls.books+=other
        return cls.books


    #no need to have self or cls as parameters
    @staticmethod
    def librarian(name):
        return ("librarian name is {}".format(name))

Library.const(12,21)

ab=Library(1234,"frozen")
print(ab.transatction())

Library.add_book(["navate"])

print(ab.books)

print(Library.librarian("tripathi"))



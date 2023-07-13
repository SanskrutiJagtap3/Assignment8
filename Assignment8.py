class A:
    def __init__(self, e, f, g):
        self.__e = e
        self._f = f
        self.g = g
    
    def display(self):
        print("Inside Class A Block...")
        print("e:", self.__e)
        print("f:", self._f)
        print("g:", self.g)

class B(A):
    def display(self):
        try:
            print("Inside Class B Block...")
            print("e:", self.__e)  # Raises exception when accessing private member
        except AttributeError:
            print("Private variable 'a' cannot be accessed...")
        print("f:", self._f)
        print("g:", self.g)

#Object created and used for calling respective functions
e=A(10, 20, 40)
e.display()

f=B(80, 90, 70)
f.display()
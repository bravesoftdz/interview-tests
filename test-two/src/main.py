class A:
    def __init__(self):
        self.X = "Class A atribute X"     
        print("Class 'A' created")   

    @property
    def X(self):
        return self.__X

    @X.setter
    def X(self, valor):
        self.__X = valor

class B(A):
    def __init__(self):
        super().__init__()
        self.Y = 'Class B atribute Y extend class A' 
        print("Class 'B' created")                     

    @property
    def Y(self):
        return self.__Y      

    @Y.setter
    def Y(self, valor):
        self.__Y = valor


class C(A):
    def __init__(self):
        super().__init__()  
        self.Z = 'Class C atribute Z extend class A'
        print("Class 'C' created")   
        
    @property
    def Z(self):
        return self.__Z

    @Z.setter
    def Z(self, valor):
        self.__Z = valor

class D(B, C):
    pass
   

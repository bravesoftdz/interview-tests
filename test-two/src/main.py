class A:    
    __X = "Class A atribute X"    

    def __init__(self):
        print("Class 'A' created")


    @property
    def X(self):
        return self.__X

    @X.setter
    def X(self, valor):
        self.__X = valor

class B(A):
            
    __Y = 'Class B atribute Y extend class A' 
    
    def __init__(self):
        super().__init__()
        print("Class 'B' created")

    @property
    def Y(self):
        return self.__Y      

    @Y.setter
    def Y(self, valor):
        self.__Y = valor

class C(A):
        
    __Z = 'Class C atribute Z extend class A'

    def __init__(self):
        super().__init__()
        print("Class 'C' created")
           
    @property
    def Z(self):        
        return self.__Z

    @Z.setter
    def Z(self, valor):
        self.__Z = valor

class D(C, B):

    def __init__(self):
        super().__init__()
        print("Class 'D' created")
    


   

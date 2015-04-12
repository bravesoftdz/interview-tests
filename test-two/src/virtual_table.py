class A:    

    X = "I am in Class A"

    def __init__(self, children):
        print("Class 'A' created by %s" % children)

class B(A):            

    X = "I am in Class B"
   
    def __init__(self, children):
        super().__init__("B")
        print("Class 'B' created by %s" % children)

class C(A):
        
    X = "I am in Class C"

    def __init__(self, children):
        super().__init__("C")
        print("Class 'C' created by %s" % children)
           

class D(B, C):
    def __init__(self):
        super().__init__("D")
        print("Class 'D' created")


print("-" * 30)

d = D()

print("-" * 30)

print(d.X)

# Comentado o atributo "X" na classe "C" é possível comprovar que ele está na classe "A"
# print(d.__class__.__bases__[1].X)

print("-" * 30)
#A classe "D" usa a mesma instancia da classe "A"
# Classe B
print("Classe B")
print("  Adress B class:", hex(id(d.__class__.__bases__[0])))
print("  Adress A class in B class:", hex(id(d.__class__.__bases__[0].__bases__.__class__)))
print("  Name B base class:", d.__class__.__bases__[0].__bases__[0].__name__)

# Classe C
print("Classe C")
print("  Adress C class:", hex(id(d.__class__.__bases__[1])))
print("  Adress A class in C class:", hex(id(d.__class__.__bases__[1].__bases__.__class__)))
print("  Name C base class:", d.__class__.__bases__[1].__bases__[0].__name__)



   

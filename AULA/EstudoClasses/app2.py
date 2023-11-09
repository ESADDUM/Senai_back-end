class a:
    def __init__(self,_a1,_a2=0):
       self.a1 = _a1
       self.a2 = _a2
    
    def retornar_A(self):
        return self.a1+self.a2
class b:
    def __init__(self) -> None:
        self.b1=0
        self.b2=0
    def DefinirB(self,Valos_b1,Valor_b2):
        self.b1 =Valor_b1
        self.b2 =Valor_b2

class a(b):
    def __init__(self,_a1:int=0,_a2:int=0) -> None:
        super().__init__()
        self.a1 = _a1
        self.a2 = _a2
    

    def retornar_A(self) -> int:
        if(isinstance ((self.a1+self.a2),int)):
            return self.a1+self.a2

#Objeto A
Objeto_a = a(3,5)
Soma_manual = Objeto_a.a1+Objeto_a.a2
Soma_A = Objeto_a.retornar_A()
print("O valor resultante foi:")
print(Soma_A)

#Objeto B
Objeto_b =b()
Objeto_b.DefinirB(2,4)



class Madeira:
    def __init__(self,TipoMadeira) -> None:
        self.Madeira = TipoMadeira

class caixa(Madeira):
    def __init__(self, nome:str, TipoMadeira) -> None:
        super().__init__(TipoMadeira)
        self.nome_da_caixa = nome
    def TipoCaixa(self):
        return self.nome_da_caixa+" "+self.Madeira
    
CaixaMadeira = caixa("Caixa basica", "Carvalho")
CaixaMadeira_Artesanato = caixa("Mini caixa", "MDF")
lista_caixas = [CaixaMadeira,CaixaMadeira_Artesanato]

comando =""
while(comando!="0"):
    Caixa = input("Qual o nome da sua caixa? ")
    Tipo = input("Qual o tipo da madeira? ")
    CaixaMadeira = caixa(Caixa,Tipo)
    lista_caixas.append(CaixaMadeira)
    comando = input("Deseja continuar? ")

for i in lista_caixas:
    print(i.TipoCaixa())
   


#Classes:
# Uma classe em Python é uma estrutura que define um conjunto de atributos e métodos que representam um objeto.
# O sistema conta com quatro classes: Mercado, Bebidas, Enlatados e Ensacados.
# As classes Bebidas, Enlatados e Ensacados herdam as características da classe Mercado usando super().__init__(). 
# Desta forma as subclasses têm acesso aos atributos e métodos da classe mãe e podem adicionar ou modificar esses atributos e métodos conforme necessário.

class Mercado:
    def __init__(self, NomeProduto, TipoProduto, SetorNome, Validade, Peso, UnMedida):
        self.NomeProduto = NomeProduto
        self.TipoProduto = TipoProduto
        self.SetorNome = SetorNome
        self.Validade = Validade
        self.Peso = Peso
        self.UnMedida = UnMedida

# Cada classe tem seus próprios atributos. 
# A classe Bebidas tem o atributo adicional TipoBebida. 
# A classe Enlatados tem o atributo Refrigerado
# A classe Ensacados tem os atributos TipoDoEnsacado e Refrigerado.

class Bebidas(Mercado):
    def __init__(self, NomeProduto, TipoProduto, SetorNome, Validade, Peso, UnMedida, TipoBebida):
        super().__init__(NomeProduto, TipoProduto, SetorNome, Validade, Peso, UnMedida)
        self.TipoBebida = TipoBebida

class Enlatados(Mercado):
    def __init__(self, NomeProduto, TipoProduto, SetorNome, Validade, Peso, UnMedida, Refrigerado):
        super().__init__(NomeProduto, TipoProduto, SetorNome, Validade, Peso, UnMedida)
        self.Refrigerado = Refrigerado

class Ensacados(Mercado):
    def __init__(self, NomeProduto, TipoProduto, SetorNome, Validade, Peso, UnMedida, TipoDoEnsacado):
        super().__init__(NomeProduto, TipoProduto, SetorNome, Validade, Peso, UnMedida)
        self.TipoDoEnsacado = TipoDoEnsacado

# Criando objetos ou instancias
# Instâncias são objetos criados a partir de uma classe. 
# Exemplo: produto1, produto2 e produto3 são instâncias das classes Bebidas, Enlatados e Ensacados.

produto1 = Bebidas("Coca-Cola", "Refrigerante", "Bebidas", "30/09/2023", 2.0, "litros", "Refrigerante")
produto2 = Enlatados("Atum em Lata", "Enlatado", "Enlatados", "15/12/2024", 0.3, "kg", "NãoRefrigerado")
produto3 = Ensacados("Arroz", "Ensacado", "Ensacados", "31/12/2023", 5.0, "kg", "Tipo A")
produto4 = Bebidas("Vodka", "Cerveja","Bebidas", "15/12/2024", 0.6, "litros", "Alcoólica")
produto5 = Bebidas("leite Integral", "leite","Bebidas", "20/11/2023", 1.0, "litros", "Não Alcoólica")

# Colocando os objetos em uma lista
lista_de_produtos = [produto1, produto2, produto3, produto4, produto5]

# Imprimindo todos os tipos de produtos usando um loop "for"
for produto in lista_de_produtos:
    print(f"Nome: {produto.NomeProduto}, Tipo: {produto.TipoProduto} Setor: {produto.SetorNome} Validade: {produto.Validade}")


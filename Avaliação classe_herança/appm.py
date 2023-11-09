class Mercado:
    def __init__(self, setornome, local, produtos, corredor):
        self.setornome = setornome
        self.local = local
        self.produtos = produtos
        self.corredor = corredor

    def exibir_informacoes(self):
        print(f"Setor: {self.setornome}")
        print(f"Localização: {self.local}")
        print(f"Produtos: {self.produtos}")
        print(f"Corredor: {self.corredor}")


class SetorPadaria(Mercado):
    def __init__(self, local, produtos, corredor):
        super().__init__("Padaria", local, produtos, corredor)


class SetorLacticinios(Mercado):
    def __init__(self, local, produtos, corredor):
        super().__init__("Lacticinios", local, produtos, corredor)


class SetorVestuario(Mercado):
    def __init__(self, local, produtos, corredor):
        super().__init__("Vestuário", local, produtos, corredor)


# Exemplo de uso:
setor_alimentos = SetorAlimentos("Corredor 1", ["Frutas", "Vegetais"], "A1")
setor_eletronicos = SetorEletronicos("Corredor 2", ["Smartphones", "Laptops"], "B2")
setor_vestuario = SetorVestuario("Corredor 3", ["Roupas", "Calçados"], "C3")

setor_alimentos.exibir_informacoes()
setor_eletronicos.exibir_informacoes()
setor_vestuario.exibir_informacoes()

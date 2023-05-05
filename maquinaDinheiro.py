class MaquinaDinheiro:
    VALOR_MOEDAS = {
        "25": 0.25,
        "10": 0.10,
        "5": 0.05,
        "1": 0.01
    }

    def __init__(self):
        self.lucro = 0
        self.dinheiroRecebido = 0

    def relatorio(self):
        print(f"Dinheiro: R${self.lucro}")

    def processaMoedas(self):
        print("Insira as moedas.")
        for moeda in self.VALOR_MOEDAS:
            self.dinheiroRecebido += int(input(f"Quantas moedas de {moeda} centavos? ")) * self.VALOR_MOEDAS[moeda]
        return self.dinheiroRecebido

    def realizaPagamento(self, custo):
        self.processaMoedas()
        if self.dinheiroRecebido >= custo:
            troco = round(self.dinheiroRecebido - custo, 2)
            if troco > 0:
                print(f"Aqui está o seu troco de R${troco}.")
            self.lucro += custo
            self.dinheiroRecebido = 0
            return True
        else:
            print("Desculpe, o dinheiro não é suficiente. Valor reembolsado.")
            self.dinheiroRecebido = 0
            return False

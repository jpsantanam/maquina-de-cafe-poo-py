class ItemCardapio:
    def __init__(self, nome, agua, leite, cafe, custo):
        self.nome = nome
        self.custo = custo
        self.ingredientes = {
            "agua": agua,
            "leite": leite,
            "cafe": cafe
        }


class Cardapio:
    def __init__(self):
        self.menu = [
            ItemCardapio(nome="latte", agua=200, leite=150, cafe=24, custo=2.5),
            ItemCardapio(nome="expresso", agua=50, leite=0, cafe=18, custo=1.5),
            ItemCardapio(nome="cappuccino", agua=250, leite=50, cafe=24, custo=3),
        ]

    def getItens(self):
        options = ""
        for item in self.menu:
            options += f"{item.nome}/"
        return options[:-1]

    def encontraBebida(self, pedido):
        for item in self.menu:
            if item.nome == pedido:
                return item
        print("Desculpe, o item não está disponível.")

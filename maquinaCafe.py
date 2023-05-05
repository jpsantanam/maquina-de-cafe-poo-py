class MaquinaCafe:
    def __init__(self):
        self.recursos = {
            "agua": 300,
            "leite": 200,
            "cafe": 100,
        }

    def relatorio(self):
        print(f"Água: {self.recursos['agua']}ml")
        print(f"Leite: {self.recursos['leite']}ml")
        print(f"Café: {self.recursos['cafe']}g")

    def recursoSuficiente(self, bebida):
        consegueFazer = True
        for item in bebida.ingredientes:
            if bebida.ingredientes[item] > self.recursos[item]:
                print(f"Desculpe, não há {item} suficiente.")
                consegueFazer = False
        return consegueFazer

    def fazCafe(self, pedido):
        for item in pedido.ingredientes:
            self.recursos[item] -= pedido.ingredientes[item]
        print(f"Aqui está o seu {pedido.nome} ☕. Aproveite!")

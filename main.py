from cardapio import Cardapio
from maquinaCafe import MaquinaCafe
from maquinaDinheiro import MaquinaDinheiro

cardapio = Cardapio()
maquinaDinheiro = MaquinaDinheiro()
maquinaCafe = MaquinaCafe()
cardapioLista = cardapio.getItens().split("/")


def main():
    escolhaUsuario = input(f"Você deseja um {cardapioLista[0]}, um {cardapioLista[1]} ou um {cardapioLista[2]}? ")

    if escolhaUsuario != "off":
        if escolhaUsuario == "relatorio":
            maquinaCafe.relatorio()
            maquinaDinheiro.relatorio()
        elif escolhaUsuario in cardapio.getItens().split("/"):
            pedido = cardapio.encontraBebida(escolhaUsuario)
            if maquinaCafe.recursoSuficiente(pedido) and maquinaDinheiro.realizaPagamento(pedido.custo):
                maquinaCafe.fazCafe(pedido)
        else:
            print("Você digitou uma opção inválida!")
        main()


if __name__ == "__main__":
    main()

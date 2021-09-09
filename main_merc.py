from mercado_ligado import MercadoLigado, Celula

class Mercado:
    def __init__(self, nome, marca, quantidade):
        self.nome = nome
        self.marca = marca
        self.quantidade = quantidade

    def __repr__(self):
        return ('Produto {:13} ------- Marca > {:^13}    |     Qtd {}'.format(self.nome, self.marca, self.quantidade))

def main():
    m1 = Mercado('Leite em Pó', 'Ninho', 530)
    m2 = Mercado('Achocolatado', 'Toddy', 120)
    m3 = Mercado('Açúcar', 'União', 630)
    m4 = Mercado('Detergente', 'Ypê', 450)
    m5 = Mercado('Sabonete', 'Dove', 200)
    m6 = Mercado('Arroz', 'Tio João', 431)
    m7 = Mercado('Feijão', 'Camil', 567)
    m8 = Mercado('Farofa', 'Yoki', 890)
    m9 = Mercado('Granola', 'Mãe Terra', 563)
    m10= Mercado('Café', '3 Corações', 423)

    lista = MercadoLigado()
    lista.inserir_no_inicio(m1)
    lista.inserir_no_inicio(m2)
    lista.inserir(2, m3)
    lista.inserir(0, m4)
    lista.inserir(1, m5)
    lista.inserir_no_inicio(m10)
    lista.inserir(3, m6)
    lista.inserir(0, m9)
    lista.inserir(4, m8)
    lista.inserir(6, m7)

    print(lista.quantidade)
    lista.imprimir()
    removido = lista.remover_do_inicio()
    print("\nRemovido: {}".format(removido))
    print("")

    print(lista.quantidade)
    lista.imprimir()
    removido = lista.remover(2)
    print("\nRemovido: {}".format(removido))
    print("")
    print(lista.quantidade)
    lista.imprimir()

    print(lista.quantidade)
    lista.imprimir()
    removido = lista.remover(2)
    print("\nRemovido: {}".format(removido))
    print("")
    print(lista.quantidade)
    lista.imprimir()

    print(lista.quantidade)
    lista.imprimir()
    removido = lista.remover(0)
    print("\nRemovido: {}".format(removido))
    print("")
    print(lista.quantidade)
    lista.imprimir()
main()
class Mercado:
    def __init__(self, nome, marca, quantidade):
        self.nome = nome
        self.marca = marca
        self.quantidade = quantidade

    def lista(self):
        print('Produto {} --- Marca -> {} --- Quantidade {}'.format(self.nome, self.marca, self.quantidade))

    @staticmethod
    def somar_produtos(args):
        return sum(args)
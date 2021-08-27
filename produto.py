class Produto:
    def __init__(self, codigo, descricao, preco):
        self.codigo = codigo
        self.descricao = descricao
        self.preco = preco

    def lista(self):
        print('{} --- {} --- R$ {}'.format(self.codigo, self.descricao, self.preco))

    @staticmethod
    def somar_produtos(args):
        return sum(args)
class Filme:
    def __init__(self, nome, duracao, ano):
        self.nome = nome
        self.duracao = duracao
        self.ano = ano

    def lista(self):
        print('Consta em nossa base de dados o filme {} com duração de {}min do ano {}.'.format(self.nome, self.duracao, self.ano))

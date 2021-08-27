class Serie:
    def __init__(self, nome, ano, temporadas, nota):
        self.nome = nome
        self.ano = ano
        self.temporadas = temporadas
        self.nota = nota

    def lista(self):
        print('Consta em nossa base de dados a série {} com {} temporada(s) de {} com nota {}'.format(self.nome, self.temporadas, self.ano, self.nota))
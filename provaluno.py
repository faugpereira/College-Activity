class Aluno:
    def __init__(self, nome, ra, nota1, nota2):
        self.nome = nome
        self.ra = ra
        self.nota1 = nota1
        self.nota2 = nota2

    def media(self):
        return(self.nota1+self.nota2)/2

    def lista(self):
        print('\nNOME: {:10}    RA: {:12}    \nnota 1 = {}  \nnota 2 = {}  \nmédia = {}'.format(self.nome, self.ra, self.nota1, self.nota2, self.media()))
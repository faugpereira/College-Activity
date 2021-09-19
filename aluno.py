class Aluno:
    def __init__(self, nome, curso, p1, p2):
        self.nome = nome
        self.curso = curso
        self.p1 = p1
        self.p2 = p2

    def media(self):
        return(self.p1+self.p2)/2

    def lista(self):
        print('{} do curso {} tem nota P1 = {} e P2 = {} cuja média é {}'.format(self.nome, self.curso, self.p1, self.p2, self.media()))
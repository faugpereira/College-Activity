class Funcionario:
    def __init__(self, codigo, nome, salario):
        self.codigo = codigo
        self.nome = nome
        self.salario = salario

    def lista(self):
        print('{} -> {} recebe R$ {}'.format(self.codigo, self.nome, self.salario))
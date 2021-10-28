from fila_banco import Fila

class Banco:

    def __init__(self, senha, horario, tipo_atendimento):
        self.senha = senha
        self.horario = horario
        self.tipo_atendimento = tipo_atendimento

    def __repr__(self):
        return self.senha


def main():
    atendimento = Fila()

    senha1 = Banco('1', '10h24', 'Atendimento Pessoal - Física')
    senha2 = Banco('2', '10h24', 'Caixa')
    senha3 = Banco('3', '10h25', 'Investimentos')
    senha4 = Banco('4', '10h27', 'Captação')

    print('\nRetirada senha {}'.format(senha1))
    atendimento.entrar(senha1)

    print('\nRetirada senha {}'.format(senha2))
    atendimento.entrar(senha2)

    print('\nRetirada senha {}'.format(senha3))
    atendimento.entrar(senha3)

    print('\nRetirada senha {}'.format(senha4))
    atendimento.entrar(senha4)

    senha = atendimento.sair()
    print('\nAtendendo senha: {} . '.format(senha),end='')
    print('Sem senhas para atender? {}'.format(atendimento.vazia))

    senha = atendimento.sair()
    print('Atendendo senha: {} . '.format(senha),end='')
    print('Sem senhas para atender? {}'.format(atendimento.vazia))

    senha = atendimento.sair()
    print('Atendendo senha: {} . '.format(senha),end='')
    print('Sem senhas para atender? {}'.format(atendimento.vazia))

    senha = atendimento.sair()
    print('Atendendo senha: {} . '.format(senha), end='')
    print('Sem senhas para atender? {}'.format(atendimento.vazia))

main()
from pilha_tarefa import Pilha

class Tarefa:

    def __init__(self, codigo, nome, descricao, prazo):
        self.codigo = codigo
        self.nome = nome
        self.descricao = descricao
        self.prazo = prazo

    def __repr__(self):
        return self.codigo

def main():
    tarefas = Pilha()
    tarefa1 = Tarefa('1', 'Exercício', 'Despertar o corpo com aquela atividade física matinal saudável', '1h30m' )
    tarefa2 = Tarefa('2', 'Café', 'Iniciar o dia com um belo café da manhã para fortalecer o corpo', '30m')
    tarefa3 = Tarefa('3', 'Estudar', 'Ler, assistir (vídeo-aulas) ou fazer atividades pendentes de fixação para retomar e entender o conteúdo estudado no dia anterior', '40m')
    tarefa4 = Tarefa('4', 'Pausas', 'Pequenas pausas intercaladas para espairecer e fazer com que os estudos sejam ainda mais produtivos', '25m')
    tarefa5 = Tarefa('5', 'Almoço', 'Preparar alimentos para consumir durante as refeições mais longas', '2h40m')
    tarefa6 = Tarefa('6', 'Ler notícias', 'Se inteirar do que tem ocorrido na atualidade através das notícias do dia', '1h40m')
    tarefa7 = Tarefa('7', 'Lazer', 'Momento dedicado aos games, séries, animes, mangás ou atividades não físicas de lazer', '2h')

    tarefas.empilhar(tarefa1)
    tarefas.empilhar(tarefa2)
    tarefas.empilhar(tarefa3)
    tarefas.empilhar(tarefa4)
    tarefas.empilhar(tarefa5)
    tarefas.empilhar(tarefa6)
    tarefas.empilhar(tarefa7)

    sucesso = tarefas.desempilhar()
    print('\nVocê está indo bem, continue assim! Eliminada a tarefa:')
    print(sucesso)

    sucesso = tarefas.desempilhar()
    print('\nVocê está indo bem, continue assim! Eliminada a tarefa:')
    print(sucesso)

    sucesso = tarefas.desempilhar()
    print('\nVocê está indo bem, continue assim! Eliminada a tarefa:')
    print(sucesso)

    sucesso = tarefas.desempilhar()
    print('\nVocê está indo bem, continue assim! Eliminada a tarefa:')
    print(sucesso)

    sucesso = tarefas.desempilhar()
    print('\nVocê está indo bem, continue assim! Eliminada a tarefa:')
    print(sucesso)

    sucesso = tarefas.desempilhar()
    print('\nVocê está indo bem, continue assim! Eliminada a tarefa:')
    print(sucesso)

    sucesso = tarefas.desempilhar()
    print('\nPARABÉNS!\nVocê não tem mais tarefas a serem realizadas no dia. Eliminada a tarefa:')
    print(sucesso)

main()
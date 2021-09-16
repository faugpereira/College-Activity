from provcontatos import ContatoLigado, Celula

class Contato:
    def __init__(self, nome, numero, descricao, endereco):
        self.nome = nome
        self.numero = numero
        self.descricao = descricao
        self.endereco = endereco

    def __repr__(self):
        return ('Nome: {:^13} \ntel: {:^14}\nDescrição: {:^15}\nEndereço: {:^20}'.format(self.nome, self.numero, self.descricao, self.endereco))

def main():
    c1 = Contato('Camila Leite', 11998537405, 'Amiga de infância','Rua Calil, 560, Sacramento - LA')
    c2 = Contato('Ramon Oliveira', 189867490574, 'Conheci na Terra do Nunca', 'Avenida Peter Pan, s/n, Never Land - NL')
    c3 = Contato('Santi Arrúcar', 219503957483, 'Parceiro de Viagens', 'Cantinho Livre, 630, Paraíso - PO')
    c4 = Contato('Caique Latrone', 349475638564,'Produtor de Sonhos', 'Núvem Central, 450, Céu - UU')
    c5 = Contato('Sabrina Vonete', 841274757355, 'Cantora de New Age', 'Estação Musical, 200, Nota Fa - DO')
    c6 = Contato('Adailton Porroz', 475917359678,'Cientista de Dados', 'Cyber Robo, 431, Cyborgue - TU')
    c7 = Contato('Fernando Kijão', 784657857585,'Corretor de Imóveis', 'Sol Nascente, 567, Ilha Sul - QA')
    c8 = Contato('Farvoreto Eitfa', 62356328475, 'Advogado', 'Sem endereço')
    c9 = Contato('Graviola França', 123124245656,'Caminhos da Mãe Terra', 'Perfeito Amor, 563')
    c10= Contato('Safo', 124195893257,'Filósofa', 'Platão Vivo, 423')

    lista = ContatoLigado()
    lista.inserir_no_inicio(c1)
    lista.inserir_no_inicio(c2)
    lista.inserir(2, c3)
    lista.inserir(0, c4)
    lista.inserir(1, c5)
    lista.inserir_no_inicio(c10)
    lista.inserir(3, c6)
    lista.inserir(0, c9)
    lista.inserir(4, c8)
    lista.inserir(6, c7)

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
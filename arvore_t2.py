from arvore_lista_duplamente_ligada_t2 import ListaDuplamenteLigada

class ListaDeNodos(ListaDuplamenteLigada):

    def __init__(self):
        super().__init__()

    def imprimir(self, nivel):
        atual = self.inicio
        for i in range(0, self.quantidade):
            atual.conteudo.imprimir(nivel)
            atual = atual.proximo

    def localizar_nodo(self, conteudo):
        atual = self.inicio
        for i in range(0, self.quantidade):
            encontrado = atual.conteudo.localizar_nodo(conteudo)
            if encontrado:
                return encontrado
            atual = atual.proximo

    def posicao(self, conteudo):
        atual = self.inicio
        for i in range(0, self.quantidade):
            if atual.conteudo.conteudo == conteudo:
                return i
            atual = atual.proximo

    def buscar(self, conteudo):
        encontrados = []
        atual = self.inicio
        proximo = None
        for i in range(0, self.quantidade):
            if conteudo == atual.conteudo.conteudo:
                return atual.conteudo.pai
            if atual is not None and atual.conteudo.filhos:
                while atual is not None and atual.conteudo.filhos:
                    encontrado = atual.conteudo.filhos.buscar(conteudo)
                    if encontrado:
                        encontrados.append(encontrado)
                    atual = atual.proximo
                return encontrados

class Nodo:

    def __init__(self, conteudo):
        self.conteudo = conteudo
        self.pai = None
        self.filhos = None

    def __repr__(self):
        return self.conteudo

    def imprimir(self, nivel=0):
        print("{}- {}".format("    "*nivel, self.conteudo))
        if self.filhos:
            self.filhos.imprimir(nivel+1)

    def inserir_filho(self, filho):
        if self.filhos is None:
            self.filhos = ListaDeNodos()
        nodo = Nodo(filho)
        nodo.pai = self
        self.filhos.inserir_no_fim(nodo)

    def localizar_nodo(self, conteudo):
        if conteudo == self.conteudo:
            return self
        if self.filhos:
            return self.filhos.localizar_nodo(conteudo)

    def remover(self):
        if self.pai:
            posicao = self.pai.filhos.posicao(self.conteudo)
            return self.pai.filhos.remover(posicao)
        return self

class Arvore:

    def __init__(self, conteudo):
        self.raiz = Nodo(conteudo)

    def imprimir(self):
        self.raiz.imprimir()

    def localizar_nodo(self, conteudo):
        return self.raiz.localizar_nodo(conteudo)

    def inserir_nodo(self, pai, filho):
        nodo_pai = self.localizar_nodo(pai)
        if nodo_pai:
            nodo_pai.inserir_filho(filho)

    def remover_nodo(self, conteudo):
        encontrado = self.raiz.localizar_nodo(conteudo)
        if encontrado:
            if encontrado is self.raiz:
                self.raiz = None
            else:
                encontrado.remover()
        return encontrado

    def buscar(self, conteudo):
        atual = self.raiz
        retorno = []
        if atual.filhos:
            retorno = atual.filhos.buscar(conteudo)
            if retorno:
                return retorno
            else:
                return "Nenhum aluno encontrado"

    """
    def encontrar_nodo(self, conteudo):
        while persona =! self.conteudo:
            if conteudo == self.conteudo:
                return self
            if self.filhos:
                return self.filhos.localizar_nodo(conteudo)
    
    def localizar_nodo(self, conteudo):
        if conteudo == self.conteudo:
            return self
        if self.filhos:
            return self.filhos.localizar_nodo(conteudo)
    
    while atual < nivel:
        nivel+1:
        for conteudo in nivel:
            if class.teacher = teacher
                print("O professor ministra as aulas: ") 
            else:
                print("Não encontradas aulas ministradas por esse professor ")
    
    def printTreeIndented(self, nivel=0):
        print("{}- {}".format("    "*nivel, self.conteudo))
        if self.raiz == None: return
            printTreeIndented(self.pai, nivel+1)
            print("{}- {}".format("    "*nivel, self.conteudo))
            self.printTreeIndented(self.raiz, nivel+1)
    
    def localizar_nodo(self, conteudo):
        if conteudo == self.conteudo:
            return self
        if self.filhos:
            return self.filhos.localizar_nodo(conteudo)
    
    while nivel <= raiz >= 4:
        nivel+1:
        for conteudo in nivel:
            if class.teacher = teacher
                print("O professor ministra as aulas: ") 
            else:
                print("Não encontradas aulas ministradas por esse professor ")
     
    for conteudo in nivel:
        if class.aluno = aluno
            print("O aluni está matriculado nas disciplinas: ") 
        else:
            print("Não encontradas as disciplinas em que este aluno está matriculado") 
    
    for class in school:
        if class.teacher = teacher
            return //  imprima aqui o professor exemplo - print("The teacher is %s") 
        else:
            // coloca aqui o script caso não tenha localizado nada exemplo - print("Not fou
    
            
    def printTreeInorder(tree) :
        if tree == None : return
        printTreeInorder(tree.left)
        print (tree.cargo, end="")
        printTreeInorder(tree.right)
                        
    """

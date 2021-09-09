from livros_ligados import LivroLigado, Celula

class Livro:
    def __init__(self, titulo, autor, genero):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero

    def __repr__(self):
        return 'Título: {:25} | Autor(a):   {:^66}   |  Classificação {}'.format(self.titulo, self.autor, self.genero)

def main():
    l1 = Livro('O Pequeno Príncipe', 'Antoine de Saint-Exupéry', 'Literatura Infantil')
    l2 = Livro('A Descoberta das Bruxas', 'Deborah Harkness', 'Romance')
    l3 = Livro('Dragões do Éter', 'Raphael Draccon', 'Fantasia')
    l4 = Livro('O Clã dos Magos', 'Trudi Canavan', 'Fantasia')
    l5 = Livro('Crônicas do Mundo Emerso', 'Licia Troisi', 'Fantasia')
    l6 = Livro('O Terceiro Travesseiro', 'Nelson Luiz de Carvalho', 'LGBTQIA+')
    l7 = Livro('Devassos no Paraíso', 'João Silvério Trevisan', 'LGBTQIA+')
    l8 = Livro('Diferentes, NÃO Desiguais', 'Beatriz Accioly Lins, Bernardo Fonseca Machado e Michele Escoura', 'LGBTQIA+')
    l9 = Livro('Guerra e Paz', 'Liev Tolstói', 'Literatura')

    lista = LivroLigado()
    lista.inserir_no_inicio(l1)
    lista.inserir_no_inicio(l2)
    lista.inserir(2, l3)
    lista.inserir(0, l4)
    lista.inserir(1, l5)
    lista.inserir(3, l9)
    lista.inserir_no_inicio(l7)
    lista.inserir(0, l8)
    lista.inserir(5, l6)

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
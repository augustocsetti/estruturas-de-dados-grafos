'''
    Tarefa sobre Grafos
    Augusto
    Murilo
'''


class Graph():  # classe para o grafo e seus métodos

    # método que cria um novo nodo
    # recebe por parâmetro o valor do nodo(sua chave/identicação)
    def new(self, value):
        self.node = Node(value)

    # método para inserir um novo nodo a um grafo já existente
    # recebe sua identificação e a quais nodos se liga (seus vértices)
    def push(self, value, vertex):
        pass

    def pop(self):
        pass

    def insert(self):
        pass

    def remove(self):
        pass

    def view(self):
        pass

    def identify(self):
        pass

    def grade(self):
        pass


class Node():  # classe para cada nodo

    def __init__(self, value):
        self.value = value
        self.next = False


def readFile():  # função para receber entrada - sugestão: mover para main
    with open('entrada.txt') as arquivo:
        linhas = [linha.rstrip() for linha in arquivo]  # remove tudo a direita - \n

    return linhas


def main():

    entrada = readFile()
    print(f'Entrada = {entrada}')

    g = []
    g.append(Graph())

    print(g)


main()

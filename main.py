'''
    Tarefa sobre Grafos
    Augusto
    Murilo
'''


class Graph():  # classe para o grafo e seus métodos

    def __init__(self, nodes='', edges='', directed=False):
        self.nodes = nodes
        self.edges = edges
        self.directed = directed

    # método para inserir um novo nodo a um grafo já existente
    def push(self, node):
        self.nodes.append(node)

    # método que remove um nodo
    def pop(self, node):
        self.aux = []
        self.index = -1

        # procura o índice no nodo a ser excluído
        for i in range(len(self.nodes)):
            if node == self.nodes[i]:
                self.index = i
                break

        if self.index >= 0:
            # não confundir com o método pop implementado - abaixo é o de listas
            self.nodes.pop(self.index)

            # procura por arestas que contenham o nodo excluído
            for i in range(len(self.edges)):
                if node in ''.join(self.edges[i]):
                    self.aux.append(''.join(self.edges[i]))

            # chama o método para remover arestas
            for i in range(len(self.aux)):
                self.remove(self.aux[i])

    # método para inserir arestras entre dois nodos já existentes
    def insert(self, edge):
        self.edges.append([edge[0], edge[1]])

    # método para remover arestas
    def remove(self, edge):
        # esta variável guarda as arestas que não serão excluídas
        # ela foi criada para evitar problemas de índice
        # eles ocorriam quanto o pop era usado no meio do loop
        self.temp = []

        for i in range(len(self.edges)):
            if [edge[0], edge[1]] != self.edges[i]:
                self.temp.append(self.edges[i])

        self.edges = self.temp

    # mostra lista com os nodos e suas arestas
    def view(self):
        for i in range(len(self.nodes)):
            print(f'{self.nodes[i]}: ', end='')
            for j in range(len(self.edges)):
                if self.nodes[i] in self.edges[j]:
                    print(f'{self.edges[j]} ', end='')
            print()

    def identify(self):
        pass

    # mostra o grau do nodo
    def grade(self, node):
        self.count = 0

        for edge in self.edges:
            if str(node) in list(edge):
                self.count += 1

        print(f'Grau do nodo {node} = {self.count}')

    # mostra a matriz de adjacência do grafo
    def adjacencyMatrix(self):
        # mostra os nodos na horizontal - primeira linha
        print('  ', end='')
        for i in range(len(self.nodes)):
            print(f'{self.nodes[i]} ', end='')

        print()

        # procura pelas nodos que possuem arestas entre si
        for i in range(len(self.nodes)):
            print(f'{self.nodes[i]} ', end='')

            for j in range(len(self.nodes)):
                # a comparação abaixo é feita com 'or' para garantir que
                #  tanto (1, 5) quanto (5, 1) sejam registradas corretamente (não direcionado)
                if [self.nodes[i], self.nodes[j]] in self.edges or [self.nodes[j], self.nodes[i]] in self.edges:
                    print('1 ', end='')
                else:
                    print('0 ', end='')
            print()


# função para receber entrada
def readFile():
    with open('entrada.txt') as file:
        lines = [line.rstrip() for line in file]

    return lines

# menu do programa
def menu():
    print('===============Opções===============')
    print('1 - Mostrar lista de adjacências')
    print('2 - Mostrar matriz de adjacências')
    print('3 - Inserir um nodo')
    print('4 - Remover um nodo')
    print('5 - Inserir uma aresta')
    print('6 - Remover uma aresta')
    print('7 - Criar um novo grafo')
    print('====================================')
    option = input('Opção: ')


def main():

    # lê os dados do arquivo de entrada
    data = readFile()

    # cria uma lista com os nodos a partir da primeira linha lida do arquivo de entrada
    nodes = []
    for char in data[0]:
        nodes.append(char)

    # as linhas seguintes são as arestas
    edges = []
    for linha in data[1:]:
        edges.append([linha[0], linha[1]])

    # cria o objeto passando como parâmetro os nodos e arestas
    grafos = []
    grafos.append(Graph(nodes, edges))

    # testes
    grafos[0].view()
    for node in nodes:
        grafos[0].grade(node)
    # grafos[0].adjacencyMatrix()
    grafos[0].push('6')
    grafos[0].adjacencyMatrix()
    grafos[0].insert('62')
    grafos[0].insert('66')
    # grafos[0].view()
    # grafos[0].adjacencyMatrix()
    grafos[0].pop('2')
    grafos[0].view()
    # grafos[0].adjacencyMatrix()
    # grafos[0].pop('1')
    # grafos[0].view()
    grafos[0].adjacencyMatrix()
    grafos[0].remove('15')
    grafos[0].view()
    print('------')
    grafos.append(Graph('', '', True))
    grafos[1].view()
    grafos[1].adjacencyMatrix()
    print(grafos[1].directed)
    menu()


main()

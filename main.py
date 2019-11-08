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
        print('\nOperação bem sucedida.\n')

    # método que remove um nodo
    # começa verificando se existem nodos no grafo
    # caso sim, verifica se o nodo informado pertence ou não ao grafo
    def pop(self, node):
        if len(self.nodes) == 0:
            print('\nERRO! Não existem nodos a excluir.\n')
        elif node not in self.nodes:
            print('\nERRO! O nodo informado não existe.\n')
        else:
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

            print('\nOperação bem sucedida.\n')

    # método para inserir arestras entre dois nodos já existentes
    # começa verificando se existem nodos no grafo
    # a seguir verifica se o tamanho da entrada é igual a 2
    # depois checa se a ligação é feita entre nodos que existem
    # e finaliza verificando se é uma aresta nova ou se já existia
    def insert(self, edge):
        if len(self.nodes) == 0:
            print('\nERRO! Não existem nodos neste grafo.\n')
        elif len(edge) != 2:
            print('\nERRO! Favor informar dois dígitos.\n')
        elif edge[0] not in self.nodes or edge[1] not in self.nodes:
            print('\nERRO! Um dos nodos não existe.\n')
        elif [edge[0], edge[1]] in self.edges:
            print('\nERRO! Aresta já existe.\n')
        else:
            self.edges.append([edge[0], edge[1]])
            print('\nOperação bem sucedida.\n')


    # método para remover arestas
    # verifica se existem arestas no grafo
    # logo após verifica se a aresta informada existe no grafo
    def remove(self, edge):
        if len(self.edges) == 0:
            print('\nERRO! Não existem arestas a ser exluídas.\n')
        elif [edge[0], edge[1]] not in self.edges:
            print('\nERRO! A aresta informada não existe.\n')
        else:
            self.edges.remove([edge[0], edge[1]])
            print('\nOperação bem sucedida.\n')

    # mostra lista com os nodos e suas arestas
    def view(self):
        for i in range(len(self.nodes)):
            print(f'{self.nodes[i]}: ', end='')

            for j in range(len(self.edges)):
                # grafo direcionado: verificamos o primeiro elemento da aresta
                # ex.: nodo '1', aresta '12' => somente o '1' de um '12' é levado em conta
                if self.directed:
                    if self.nodes[i] == self.edges[j][0]:
                        print(f'{self.edges[j]} ', end='')

                # grafo não direcionado: o importante é evitar que arestas 'iguais' se repitam
                # ex.: ['4', '5'] é igual a ['5', '4'] neste tipo de grafo
                # para isso foi utilizada a função reverse() do tipo list
                else:
                    # necessário utilizr .copy() porque o python faz a atribuição por referência
                    # isto modificava o elemento original, algo indesejável
                    self.temp = self.edges[j].copy()
                    self.temp.reverse()
                    if self.nodes[i] in self.edges[j] and self.temp not in self.edges[:j]:
                        print(f'{self.edges[j]} ', end='')
            print()

    def identify(self):
        pass

    # mostra o grau do nodo
    def grade(self, node):
        if node not in self.nodes:
            print('\nERRO! O nodo não existe.\n')
        else:
            self.entry = 0
            self.exit = 0

            for edge in self.edges:
                if self.directed:
                    if node == edge[0]:
                        self.exit += 1
                    if node == edge[1]:
                        self.entry += 1
                else:
                    if node in edge:
                        self.entry += 1
                        self.exit += 1

            print(f'\nGrau de entrada do nodo {node}: {self.entry}')
            print(f'Grau de saída do nodo {node}: {self.exit}\n')

    # mostra a matriz de adjacência do grafo
    def adjacencyMatrix(self):
        # mostra os nodos na horizontal - primeira linha
        print('  ', end='')
        for i in range(len(self.nodes)):
            print(f'{self.nodes[i]} ', end='')

        print()

        # procura pelos nodos que possuem arestas entre si
        for i in range(len(self.nodes)):
            print(f'{self.nodes[i]} ', end='')

            for j in range(len(self.nodes)):
                if self.directed:
                    if [self.nodes[i], self.nodes[j]] in self.edges:
                        print('1 ', end='')
                    else:
                        print('0 ', end='')
                # a comparação abaixo é feita com 'or' para garantir que
                #  tanto (1, 5) quanto (5, 1) sejam registradas corretamente (não direcionado)
                else:
                    if [self.nodes[i], self.nodes[j]] in self.edges or [self.nodes[j], self.nodes[i]] in self.edges:
                        print('1 ', end='')
                    else:
                        print('0 ', end='')
            print()

    # método para mudar a definição do grafo
    # não-orientado -> orientado e orientado -> não-orientado
    # NOME do método pode ser melhorado
    def direction(self):
        self.directed = not self.directed
        print('\nOperação bem sucedida.\n')

# função para receber entrada do arquivo
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
    print('7 - Informar o grau de um nodo')
    print('8 - Não-orientado -> orientado (e vice-versa)')
    print('0 = Encerra o programa')
    print('====================================')
    option = input('Opção: ')

    return option


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
    g = Graph(nodes, edges)

    # testes
    op = -1

    while op != 0:
        try:
            op = int(menu())
        except ValueError:
            print('\nFavor informar um valor válido.\n')
        if op == 1:
            g.view()
        elif op == 2:
            g.adjacencyMatrix()
        elif op == 3:
            g.push(input('Informe o novo nodo: '))
        elif op == 4:
            g.pop(input('Informe o nodo a ser excluído: '))
        elif op == 5:
            g.insert(input('Informe a aresta a ser incluída: '))
        elif op == 6:
            g.remove(input('Informe a aresta a ser excluída: '))
        elif op == 7:
            g.grade(input('Informe o nodo: '))
        elif op == 8:
            g.direction()
        elif op < 0 or op > 8:
            print('\nERRO! Favor informar um valor entre 0 e 7.\n')


main()
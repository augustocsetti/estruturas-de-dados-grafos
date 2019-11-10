'''
    Tarefa sobre Grafos
    Augusto
    Murilo
'''

# bibliotecas utilizdas para redirecionar o output (print) do método grade
import io
from contextlib import redirect_stdout

class Graph():  # classe para o grafo e seus métodos

    def __init__(self, nodes='', edges=''):

        self.nodes = []
        # percorre os nodos e encontra os que ele tem conexão (já direcionado)
        for node in nodes:
            edgeReal = []
            for edge in edges:
                if edge[0] == node:
                    edgeReal.append(edge[1])
            self.nodes.append(Node(node, edgeReal))

    # método para inserir um novo nodo a um grafo já existente
    def push(self, node):
        if node not in self.nodes:            
            self.nodes.append(node)
            print('\nOperação bem sucedida.\n')
        else:
            print('\nERRO! Este nodo já existe.\n')

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
            print(f'{self.nodes[i].node}: ', end='')
            if self.nodes[i].edges:
                for j in range(len(self.nodes[i].edges)):
                    print(f'--> {self.nodes[i].edges[j]}', end='  ')
            
            print()


    # este método identifica as fontes e sumidouros de um grafo
    # nodos fonte são aqueles nos quais não temos arestas de entrada
    # já os nodos sumidouros são aqueles em que não existe aresta de saída
    # utilizamos o método grade da classe para identificar estes nodos
    # eles são então armazenados em duas listas diferentes
    def identify(self):
        self.source = []
        self.sink = []

        # como a função grade tem um output desnessário neste caso
        # redirecionamos para uma variável, neste caso 'f'
        f = io.StringIO()
        with redirect_stdout(f):

            for node in self.nodes:
                self.grade(node)

                if self.entry == 0:
                    self.source.append(node)
                if self.exit == 0:
                    self.sink.append(node)

        print()

        if len(self.source) == 0:
            print('Não existem nodos fonte no grafo.')
        else:
            print('Nodo(s) fonte: ', end='')
            for i in range(len(self.source)):
                print(f'{self.source[i]} ', end='')
            print()            

        if len(self.sink) == 0:
            print('Não existem nodos sumidouro no grafo.')
        else:
            print('Nodo(s) sumidouro: ', end='')
            for i in range(len(self.sink)):
                print(f'{self.sink[i]} ', end='')
            print()
        
        print()


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
        print('     ', end='')
        for i in range(len(self.nodes)):
            print(f'{self.nodes[i].node}  ', end='')            

        print('\n')

        # procura pelos nodos que possuem arestas entre si
        for i in range(len(self.nodes)):
            # mostra os nodos na vertical - primeira coluna
            print(f'{self.nodes[i].node}    ', end='')

            for j in range(len(self.nodes)):
                if self.nodes[j].node in self.nodes[i].edges:
                    print('1  ', end='')
                else:
                    print('0  ', end='')

            print()
        print()

    # método para mudar a definição do grafo
    # não-orientado -> orientado e orientado -> não-orientado
    # NOME do método pode ser melhorado
    def direction(self):
        self.directed = not self.directed
        print('\nOperação bem sucedida.\n')


class Node():  # classe para os nodos e suas características
    def __init__(self, node='', edges=''):
        self.node = node
        self.edges = edges


# função para receber entrada do arquivo
def readFile():
    with open('entrada.txt') as file:
        lines = [line.rstrip() for line in file]
    for i in range(len(lines)):
        lines[i] = lines[i].split(" ")
    file.close()

    return lines[0], lines

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
    print('8 - Informar fontes e sumidouros do grafo')
    print('9 - Não-orientado -> orientado (e vice-versa)')
    print('0 = Encerra o programa')
    print('====================================')
    option = input('Opção: ')

    return option


def main():

    # lê os dados do arquivo de entrada e cria uma lista com
    # os nodos na posição 0 e as arestas nas posições seguintes
    nodes, data = readFile()


    # as linhas seguintes são as arestas
    edges = []
    for linha in data[1:]:
        edges.append([linha[0], linha[1]])


    # cria o objeto passando como parâmetro os nodos e arestas
    g = Graph(nodes, edges)
    g.view()
    g.adjacencyMatrix()#teste
'''

    # testes
    op = -1

    while op != 0:
        try:
            op = int(menu())

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
                g.identify()
            elif op == 9:
                g.direction()
            elif op < 0 or op > 9:
                print('\nERRO! Favor informar um valor entre 0 e 7.\n')

        except ValueError:
            print('\nFavor informar um valor válido.\n')
        

'''
main()
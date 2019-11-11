'''
    Tarefa sobre Grafos
    Augusto Cardoso Setti - Matrícula 119994
    Murilo Vitória da Silva - Matrícula 124816

QUESTÕES

- Acertar buscas com edgesD edgesND
- Criar classes específicas para buscas? Graph está ficando muito grande.
- Melhorar mostra informações com busca por profundidade e largura

- Aconteceu um erro quando estava testando várias maneiras de busca por largura
uma erro de char~int com uma lista. Testar!

FALTA
- Implementar um grafo usando a representação de matriz de adjacência.
- Implmentar os algoritmos Prim e Kruskal
'''

# bibliotecas utilizdas para redirecionar o output (print) do método grade
import sys, os

# definição de estados para busca em profundidade
WHITE = 0
GRAY = 1
BLACK = 2


class Node():  # classe para os nodos e suas características

    def __init__(self, label='', edgesD='', edgesND=''):
        self.label = label # valor do nodo
        self.edgesD = edgesD # arestas direcionadas
        self.edgesND = edgesND # arestas não direcionadas
        self.gradeIn = 0 # grau de entrada
        self.gradeOut = 0 # grau de saída

        # infos para funções de busca
        self.set = False # usado para marcar nodo em buscas
        self.father = None # marcação do nodo pai na busca por profundidade
        self.time = [] # tempo de abertura e fechamento na busca por profundidade


class Graph():  # classe para o grafo e seus métodos

    def __init__(self, nodes='', edges=''):

        self.nodes = []
        # percorre os nodos e encontra os que ele tem conexão
        for node in nodes:
            tempD = []
            tempND = []
            for edge in edges:
                # descreve relação para direcionado ou não direcionado
                if edge[0] == node:
                    tempD.append(edge[1])
                    tempND.append(edge[1])
                if edge[1] == node:
                    tempND.append(edge[0])
            # cria nodo e adiciona a lista de nodos
            self.nodes.append(Node(node, tempD, tempND))

        self.directed = True

    # método para inserir um novo nodo a um grafo já existente
    def push(self, label):
        for i in range(len(self.nodes)):
            if label == self.nodes[i].label:
                print('\nERRO! Este nodo já existe.\n')
                return

        self.nodes.append(Node(label, [], []))
       
        print('\nOperação bem sucedida.\n')

    # remove um nodo.
    def pop(self, label):
        # variável para armazenar posição do nodo a ser deletado
        indexLabel = -1
        # chama o método para remover arestas ligadas ao nodo (se houver)
        for i in range(len(self.nodes)):
            if self.nodes[i].label != str(label):
                j = 0
                while j < (len(self.nodes[i].edgesD)):
                    if self.nodes[i].edgesD[j] == label:
                        # exclui aresta
                        self.remove(self.nodes[i].label+" "+self.nodes[i].edgesD[j])
                        # condição para saída da repetição
                        j = len(self.nodes[i].edgesD)
                    j += 1
            # índice no nodo a ser excluído
            else:
                indexLabel = i

        # exclui nodo
        if indexLabel != -1:
            self.nodes.pop(indexLabel)
            print('\nOperação bem sucedida.\n')
        else:
            print('\nERRO! Nodo não existe no grafo.\n')

    # método para inserir arestras entre dois nodos já existentes
    def insert(self, edge):  
        # verifica se existem nodos no grafo
        if len(self.nodes) == 0:
            print('\nERRO! Não existem nodos neste grafo.\n')
            return

        edge = edge.split(" ")

        # procura pelos índices dos nodos
        self.exitNodeIndex = self.index(edge[0])
        self.entryNodeIndex = self.index(edge[1])
        
        # se um deles não existir mostra mensagem de erro
        if self.entryNodeIndex == -1 or self.exitNodeIndex == -1:
            print('\nERRO! Um dos nodos não existe.\n')
            return

        # veririca se a aresta já existe e, caso não exista, adicioná-las ao nodo

        if edge[1] not in self.nodes[self.exitNodeIndex].edgesD:
                self.nodes[self.exitNodeIndex].edgesD.append(edge[1])
                self.nodes[self.exitNodeIndex].edgesND.append(edge[1])
                self.nodes[self.entryNodeIndex].edgesND.append(edge[0])
                print('\nOperação bem sucedida.\n')
        else:
            print('\nERRO! Esta aresta já existe.\n')

    # remove arestas
    def remove(self, edge):
        # verifica se o nodo não está vazio
        if len(self.nodes) == 0:
            print('\nERRO! Não existem nodos no grafo.\n')
            return
            
        # trata entrada
        edge = edge.split(" ")
        label, edge = edge[0], edge[1]
        self.index = -1        

        # percorre os nodos
        for i in range(len(self.nodes)):

            # percorre nodos e busca índice duplicado (para não direcionado)
            for j in range(len(self.nodes)):
                if self.nodes[j].label == edge:
                    self.index = j
                    break

            # remove nodo duplicado para grafo não direcionado
            if self.index != -1:
                print()
                self.nodes[self.index].edgesND.remove(label)   
            
            # busca label em nodos
            if self.nodes[i].label == label:
                try:
                    self.nodes[i].edgesD.remove(edge)
                    self.nodes[i].edgesND.remove(edge)
                except:
                    print('\nERRO! Aresta não exite.\n')
                return
        # se o nodo não for encontrado
        print('\nERRO! Nodo não existe.\n')
        
    # mostra lista com os nodos e suas arestas
    def view(self):
        for i in range(len(self.nodes)):
            print(f'{self.nodes[i].label}: ', end='')

            if self.directed:
                if self.nodes[i].edgesD:
                    for j in range(len(self.nodes[i].edgesD)):
                        print(
                            f'--> {self.nodes[i].edgesD[j]}', end='  ')
            else:
                if self.nodes[i].edgesND:
                    for j in range(len(self.nodes[i].edgesND)):
                        print(
                            f'--> {self.nodes[i].edgesND[j]}', end='  ')
            print()
        print()

    # identifica as fontes e sumidouros do grafo
    def identify(self):
        self.source = [] # nodos fonte não têm arestas de entrada
        self.sink = [] # nodos sumidouros não têm aresta de saída

        # como a função grade tem um output desnessário usa-se
        # as funções sys para bloquear e liberar a saída
        sys.stdout = open(os.devnull, 'w')

        for i in range(len(self.nodes)):
            # chamamos o método grade para identificar os graus do nodo
            self.grade(self.nodes[i].label)
            # checa-se condição de fonte e sumidouro
            if self.nodes[i].gradeIn == 0:
                self.source.append(self.nodes[i].label)
            if self.nodes[i].gradeOut == 0:
                self.sink.append(self.nodes[i].label)

        sys.stdout = sys.__stdout__

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
    def grade(self, label):        
        self.indexTemp = self.index(label)

        # caso o índide seja -1 é porque o nodo informado não está na lista - volta para main()

        if self.indexTemp == None:
            print('\nERRO! O nodo não existe.\n')
            return
        else:
            # o grau de saída é o tamanho da varíavel que controla as arestas do nodo
            if self.directed:
                self.exit = len(self.nodes[self.indexTemp].edgesD)
                self.entry = 0
                
                # para o grau de entrada é necessário percorrer todos os nodos
                # veriicando a ocorrência do nodo informado nas arestas dos outros nodos
                for i in range(len(self.nodes)):
                    if label in self.nodes[i].edgesD:
                        self.entry += 1            
                
                # salvando informação de grau na classe nodo
                self.nodes[self.indexTemp].gradeIn = self.entry
                self.nodes[self.indexTemp].gradeOut = self.exit
            else:
                self.exit = len(self.nodes[self.indexTemp].edgesND)
                self.entry = len(self.nodes[self.indexTemp].edgesND)

            print(f'\nGrau de entrada do nodo {label}: {self.entry}')
            print(f'Grau de saída do nodo {label}: {self.exit}\n')

    # mostra a matriz de adjacência do grafo
    def adjacencyMatrix(self):
        # mostra os nodos na horizontal - primeira linha
        print('     ', end='')
        for i in range(len(self.nodes)):
            print(f'{self.nodes[i].label}  ', end='')            

        print('\n')

        # procura pelos nodos que possuem arestas entre si
        for i in range(len(self.nodes)):
            # mostra os nodos na vertical - primeira coluna
            print(f'{(self.nodes[i].label)}    ', end='')
            for j in range(len(self.nodes)):
                if self.directed:
                    if self.nodes[j].label in self.nodes[i].edgesD:
                        print('1  ', end='')
                    else:
                        print('0  ', end='')
                else:
                    if self.nodes[j].label in self.nodes[i].edgesND:
                        print('1  ', end='')
                    else:
                        print('0  ', end='')
                        
            print()
        print()


    # método para mudar a definição do grafo 
    def guidance(self):        
        self.directed = not self.directed
        print('\nOperação bem sucedida.\n')

    #ATENÇÃO! CASO COM ERRO
    # algoritmo de busca em largura BFS
    def breadthSearch(self, s):
        # 's' é o label do nodo inicial
        # bibliografia https://www.youtube.com/watch?v=cUlDbC0KrQo

        # inicializa set de todos elementos
        for elem in self.nodes:
            elem.set = False
        
        line = []

        # índice de s
        indexS = self.index(s)
        # marca nodo
        self.nodes[indexS].set = True
        # add a fila
        line.append(indexS)

        # percorre todos os valores que possuem conexão com ramo de 's'
        while(len(line) != 0):
            # define primeiro valor da fila para analisar arestas
            u = line[0]

            line.pop(0)
            #processa(u) faz alguma coisa com o nodo percorrido

            # percorre arestas do nodo u e checa se já foram setadas
            # se não seta e adiciona a fila
            for i in range (len(self.nodes[u].edgesD)):
                indexTemp = self.index(self.nodes[u].edgesD[i])
                if self.nodes[indexTemp].set == False:
                    self.nodes[indexTemp].set = True
                    line.append(indexTemp)

    # algoritmo de busca em largura DFS-1
    def depthSearch(self):
        # bibliografia https://www.youtube.com/watch?v=0B6VfRbppkE

        # inicializa set de todos elementos
        for elem in self.nodes:
            elem.set = WHITE
        
        # tempo de abertura e fechamento
        self.time = 0
        # percorre todos os nodos
        for i in range(len(self.nodes)):
            if self.nodes[i].set == WHITE:
                self.depthSearchVisit(i)

    # algoritmo de busca em largura DFS-2
    def depthSearchVisit(self, u):
        # marca primeira passagem sobre o nodo (cinza)
        self.nodes[u].set = GRAY

        # incrementa e adiciona tempo de entrada do nodo
        self.time += 1
        self.nodes[u].time.append(self.time)

        # busca nodos vizinhos
        for i in range(len(self.nodes[u].edgesD)):
            indexTemp = self.index(self.nodes[u].edgesD[i])
            # se não tiver sido 'aberto' (nodo branco) acessa e chama recursão
            if self.nodes[indexTemp].set == WHITE:
                # define pai do nodo encontrado
                self.nodes[indexTemp].father = self.nodes[u].label
                self.depthSearchVisit(indexTemp)

        # fecha nodo (seta cor preto) e adiciona tempo de saída
        self.nodes[u].set = BLACK
        self.time += 1
        self.nodes[u].time.append(self.time)

    #ATENÇÃO! MELHORAR
    # printa informações de cada nodo pós busca por profundidade
    def infosDepthSearch(self):
        for elem in self.nodes:
            print('label ',elem.label)
            print('pai ',elem.father)
            print('tempo ',elem.time)
            print('cor', elem.set)
            print()

    # retorna índice (da lista self.grafos) de algum nodo
    def index(self, label):
        for i in range(len(self.nodes)):
            if self.nodes[i].label == str(label):
                return i

    # retorna índice (da lista self.grafos) de algum nodo
    def index(self, label):
        for i in range(len(self.nodes)):
            if self.nodes[i].label == str(label):
                return i

              
def readFile(): # função para receber entrada do arquivo
    with open('entrada.txt') as file:
        lines = [line.rstrip() for line in file]
    for i in range(len(lines)):
        lines[i] = lines[i].split(" ")
    file.close()

    return lines[0], lines


def menu(): # menu do programa
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
    print('10 - Breadth First Search')
    print('11 - Depth First Search')
    print('0 = Encerra o programa')
    print('====================================')
    option = input('Opção: ')

    return option

#==============================================================================================================#

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

    
    # loop principal
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
                g.insert(input('Informe a aresta a ser incluída ([nodo1] [nodo2]): '))
            elif op == 6:
                g.remove(input('Informe a aresta a ser excluída ([nodo1] [nodo2]): '))
                print()
            elif op == 7:
                g.grade(input('Informe o nodo: '))
            elif op == 8:
                g.identify()
            elif op == 9:
                g.guidance()
            elif op == 10:
                g.breadthSearch(input('Informe o nodo para iniciar a busca: '))
            elif op == 11:
                g.depthSearch()
                g.infosDepthSearch()                
            elif op < 0 or op > 11:
                print('\nERRO! Favor informar um valor entre 0 e 11.\n')

        except ValueError:
            print('\nFavor informar um valor válido.\n')
        

main()

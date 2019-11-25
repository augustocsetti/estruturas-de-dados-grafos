# bibliotecas utilizdas para redirecionar o output (print) do método grade
import sys, os
from operator import itemgetter
from Node import *


# definição de estados para busca em profundidade
WHITE = 0
GRAY = 1
BLACK = 2


class Graph():  # classe para o grafo e seus métodos

    def __init__(self, nodes='', edges='', edgesW=[]):

        self.nodes = []
        self.directed = True

        # percorre os nodos e encontra os que ele tem conexão
        for node in nodes:
            tempD = []
            tempND = []
            tempWPrim = []
            tempComplete = [] # Kruskal, Dijkstra, Bellman-Ford

            for edge in edges:
                
                # descreve relação para direcionado ou não direcionado
                if edge[0] == node:
                    tempD.append(edge[1])
                    tempND.append(edge[1])
                
                if edge[1] == node:
                    tempND.append(edge[0])

            # Prim, Kruskal, Dijkstra, Bellman-Ford
            for edgeW in edgesW:
                if edgeW[0] == node:
                    tempWPrim.append([edgeW[1], edgeW[2]])
                    tempComplete.append([edgeW[0], edgeW[1], edgeW[2]])
                if edgeW[1] == node:
                    tempWPrim.append([edgeW[0], edgeW[2]])

            # cria nodo e adiciona a lista de nodos
            self.nodes.append(Node(node, tempD, tempND, tempWPrim, tempComplete))

    #==== NODOS E ARESTAS ====#    

    # insere nodo
    def push(self, label):
        for i in range(len(self.nodes)):
            if label == self.nodes[i].label:
                print('\nERRO! Este nodo já existe.\n')
                return

        self.nodes.append(Node(label, [], []))
       
        print('\nOperação bem sucedida.\n')

    # remove nodo
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
            print('\nNodo excluido com sucesso. Operação bem sucedida.\n')
        else:
            print('\nERRO! Nodo não existe no grafo.\n')

    # insere arestras
    def insert(self, edge):  
        # verifica se existem nodos no grafo
        if len(self.nodes) == 0:
            print('\nERRO! Não existem nodos neste grafo.\n')
            return

        edge = edge.split(" ")
        if len(edge) != 3:
            print('\nERRO! Favor verificar os dados para a inserção de arestas: [nodo1] [nodo2] [peso]\n')
            return

        # procura pelos índices dos nodos
        self.exitNodeIndex = self.index(edge[0])
        self.entryNodeIndex = self.index(edge[1])
        self.edgeWeight = edge[2]
        
        # se um deles não existir mostra mensagem de erro
        # -1 é o retorno da função que indica que o nodo em questão não foi encontrado
        if self.entryNodeIndex == -1 or self.exitNodeIndex == -1:
            print('\nERRO! Um dos nodos não existe.\n')
            return

        # veririca se a aresta já existe e, caso não exista, adicioná-las ao nodo
        if edge[1] not in self.nodes[self.exitNodeIndex].edgesD:
                # grafo orientado - arestas sem peso
                self.nodes[self.exitNodeIndex].edgesD.append(edge[1])
                # grafo não orientado - arestas sem peso
                self.nodes[self.exitNodeIndex].edgesND.append(edge[1])
                self.nodes[self.entryNodeIndex].edgesND.append(edge[0])

                # grafo orientado - completo [nodo1] [nodo2] [peso]
                self.nodes[self.exitNodeIndex].edgesComplete.append(edge)

                # grafo não orientado - [nodo2] [peso]
                self.nodes[self.exitNodeIndex].edgesWH.append([edge[1], edge[2]])
                self.nodes[self.entryNodeIndex].edgesWH.append([edge[0], edge[2]])

                
                print('\nOperação bem sucedida.\n')
        else:
            print('\nERRO! Esta aresta já existe.\n')

    # remove arestas
    def remove(self, edge):
        # verifica se o grafo não está vazio
        if len(self.nodes) == 0:
            print('\nERRO! Não existem nodos no grafo.\n')
            return
            
        # trata entrada
        edge = edge.split(" ")
        label, edge = edge[0], edge[1]

        self.indLabel = self.index(label)
        self.indEdge = self.index(edge)

        if self.indLabel == -1 or self.indEdge == -1:
            print('\nERRO! Um dos nodos não não existe.\n')
            return              

        # percorre os nodos
        for i in range(len(self.nodes)):

            # busca label em nodos
            if self.nodes[i].label == label and edge in self.nodes[i].edgesD:
                # remoção da aresta simples (sem peso) do grafo direcionado
                self.nodes[i].edgesD.remove(edge)
                self.nodes[i].edgesND.remove(edge)
                # remoção da aresta simples (sem peso) do grafo não direcionado
                self.nodes[self.indEdge].edgesND.remove(label) 

                # remoção da aresta na variável que contém a informação ['nodo2', 'peso']
                for edges in self.nodes[i].edgesWH:                    
                    if edges[0] == edge:           
                        self.nodes[i].edgesWH.remove(edges)
                        self.nodes[self.indEdge].edgesWH.remove([label, edges[1]]) 
                        break 

                # remoção da aresta na variável que contém a informação ['nodo1', 'nodo2', 'peso']
                for edges in self.nodes[i].edgesComplete: 
                    if edges[0] == label and edges[1] == edge:                        
                        self.nodes[i].edgesComplete.remove(edges)                        
                        break
                
                print('\nAresta excluida com sucedida.\n')           
                return           

        print('\nERRO! A aresta não existe.\n')

    #==== PRINT ====#

    # mostra lista com os nodos e suas arestas
    def view(self):
        print()
        for i in range(len(self.nodes)):
            print(f'{self.nodes[i].label}: ', end='')

            if self.directed:
                if self.nodes[i].edgesD:
                    for j in range(len(self.nodes[i].edgesD)):
                        print(f'--> {self.nodes[i].edgesD[j]}', end='  ')
            else:
                if self.nodes[i].edgesND:
                    for j in range(len(self.nodes[i].edgesND)):
                        print(f'--> {self.nodes[i].edgesND[j]}', end='  ')
            print()
        print()

    # mostra lista com os nodos, suas arestas e pesos
    def view2(self):
        print()
        for i in range(len(self.nodes)):
            print(f'{self.nodes[i].label}: ', end='')
            if self.nodes[i].edgesWH:                
                for j in range(len(self.nodes[i].edgesWH)):
                    print(f'{self.nodes[i].edgesWH[j]} ', end='  ')

            print()
        print()

    # mostra a matriz de adjacência do grafo
    def adjacencyMatrix(self):
        print()

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

    #==== GRAUS E ORIENTAÇÃO ====#

    # identifica fontes e sumidouros
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
            if  self.nodes[i].gradeIn == 0 and self.nodes[i].gradeOut == 0:
                continue
            else:
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
            else:
                self.exit = len(self.nodes[self.indexTemp].edgesND)
                self.entry = len(self.nodes[self.indexTemp].edgesND)
            
            # salvando informação de grau na classe nodo
            self.nodes[self.indexTemp].gradeIn = self.entry
            self.nodes[self.indexTemp].gradeOut = self.exit

            print(f'\nGrau de entrada do nodo {label}: {self.entry}')
            print(f'Grau de saída do nodo {label}: {self.exit}\n')

    # muda orientação do grafo
    def guidance(self):        
        self.directed = not self.directed

        if self.directed:
            print('\nGrafo orientado.\n')
        else:
            print('\nGrafo não orientado.\n')

    #==== BUSCA ====#

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
        time = 0
        while(len(line) != 0):
            # define primeiro valor da fila para analisar arestas
            u = line[0]

            line.pop(0)

            # processa(u) faz alguma coisa com o nodo percorrido
            # aqui apenas adicionaremos um contador 
            self.nodes[u].time = time
            time += 1

            # funciona para orientado ou não orientado
            if self.directed:
                # percorre arestas do nodo u e checa se já foram setadas
                # se não seta e adiciona a fila
                for i in range (len(self.nodes[u].edgesD)):
                    indexTemp = self.index(self.nodes[u].edgesD[i])
                    if self.nodes[indexTemp].set == False:
                        self.nodes[indexTemp].set = True
                        self.nodes[indexTemp].father = self.nodes[u].label
                        line.append(indexTemp)
            else:
                for i in range (len(self.nodes[u].edgesND)):
                    indexTemp = self.index(self.nodes[u].edgesND[i])
                    if self.nodes[indexTemp].set == False:
                        self.nodes[indexTemp].set = True
                        self.nodes[indexTemp].father = self.nodes[u].label
                        line.append(indexTemp)

        # printa informações de cada nodo pós busca por profundidade
        for elem in self.nodes:
            print()
            print(f'Nodo: {elem.label}')
            print(f'Pai: {elem.father}')
            print(f'Tempo: {elem.time}')
            print(f'Set: {elem.set}')

    # algoritmo de busca em largura DFS-1
    def depthSearch(self):
        # bibliografia https://www.youtube.com/watch?v=0B6VfRbppkE

        # inicializa set de todos elementos
        for elem in self.nodes:
            elem.set = WHITE
            elem.time = []
        
        # tempo de abertura e fechamento
        self.time = 0
        # percorre todos os nodos
        for i in range(len(self.nodes)):
            if self.nodes[i].set == WHITE:
                self.depthSearchVisit(i)

        # printa informações de cada nodo pós busca por profundidade
        print()
        for elem in self.nodes:
            print(f'Nodo: {elem.label}')
            print(f'Pai: {elem.father}')
            print(f'Tempo (Abertura): {elem.time[0]}')
            print(f'Tempo (Fechamento): {elem.time[1]}')
            if elem.set == 0:
                print(f'Cor: White')
            elif elem.set == 1:
                print(f'Cor: Gray')
            else:
                print(f'Cor: Black')
            print()

    # algoritmo de busca em largura DFS-2
    def depthSearchVisit(self, u):
        # marca primeira passagem sobre o nodo (cinza)
        self.nodes[u].set = GRAY

        # incrementa e adiciona tempo de entrada do nodo
        self.time += 1
        self.nodes[u].time.append(self.time)

        # funciona para orientado ou não
        if self.directed:
            # busca nodos vizinhos
            for i in range(len(self.nodes[u].edgesD)):
                indexTemp = self.index(self.nodes[u].edgesD[i])
                # se não tiver sido 'aberto' (nodo branco) acessa e chama recursão
                if self.nodes[indexTemp].set == WHITE:
                    # define pai do nodo encontrado
                    self.nodes[indexTemp].father = self.nodes[u].label
                    self.depthSearchVisit(indexTemp)

        else:
            for i in range(len(self.nodes[u].edgesND)):
                indexTemp = self.index(self.nodes[u].edgesND[i])
                if self.nodes[indexTemp].set == WHITE:
                    self.nodes[indexTemp].father = self.nodes[u].label
                    self.depthSearchVisit(indexTemp)


        # fecha nodo (seta cor preto) e adiciona tempo de saída
        self.nodes[u].set = BLACK
        self.time += 1
        self.nodes[u].time.append(self.time)

    #==== CAMINHOS ====# 

    # algoritmo que procura o menor caminho entre os nodos de um grafo
    def prim(self):
        if self.directed:
            print('\nERRO! O grafo precisa ser não orientado.\n')
            return
        else:
            # veriricando se o grafo possui arestas com pesos negativos
            # este algoritmo não funciona caso elas existam
            for i in range(len(self.nodes)):
                for edge in self.nodes[i].edgesComplete:
                    if int(edge[2]) < 0:
                        print('\nERRO! O grafo não pode possuir arestas com peso negativo.\n')
                        return

            # resetando os valores dos atributos dos nodos
            self.nodeResetter() 

            # variável do nodo inicial - escolhida arbitrariamente        
            self.indice = 0
            
            # a chave do nodo de partida é sempre 0
            self.nodes[self.indice].key = 0  
            
            # lista auxiliar para garantir que não haverá desconexão entre os nodos
            self.minPath = []
            self.size = len(self.nodes)
                    
            while self.size > 0:
                self.size -= 1

                # percorrendo as arestas do nodo indicado
                for edgeW in self.nodes[self.indice].edgesWH:
                    # procuramos o índice do nodo que forma a aresta
                    edgeIndex = self.index(edgeW[0])

                    # formamos o par de nodos para fazer a verificação se já pertecem ao menor caminho
                    aresta = [self.nodes[self.indice].label, edgeW[0]]

                    if int(edgeW[1]) < self.nodes[edgeIndex].key and aresta not in self.minPath and self.nodes[edgeIndex].done != True:
                        # acessamos o nodo na posição encontrada e setamos o pai e o valor da chave (peso da aresta)
                        self.nodes[edgeIndex].parent = self.nodes[self.indice].label
                        self.nodes[edgeIndex].key = int(edgeW[1])
                        self.minPath.append([self.nodes[self.indice].label, edgeW[0]])
                
                self.nodes[self.indice].done = True

                # procuramos o índice do próximo nodo com menor chave
                self.indice = self.extractMin()
                if self.indice == -1:
                    break
            
            total = 0
            # mostra o nodo, seu pai e o peso da ligação até este
            for i in range(len(self.nodes)):
                print(f'Nodo = {self.nodes[i].label}')
                print(f'Pai = {self.nodes[i].parent}')
                print(f'Chave = {self.nodes[i].key}')
                total += self.nodes[i].key
                print()
            
            print(self.minPath)
            print(total)
            print()

    # método auxiliar para Prim
    def extractMin(self):

        self.indiceMenor = -1
        self.menor = float('inf')

        for node in self.nodes:
            
            if node.key < self.menor and node.done == False:                
                self.menor = node.key
                self.indiceMenor = self.index(node.label)
                
        return self.indiceMenor

    def kruskal(self):
        # vai formando árvores (neste caso, pares de nodos) até terminar

        if self.directed:
            print('\nERRO! O grafo precisa ser não orientado.\n')
            return
        else:
            # veriricando se o grafo possui arestas com pesos negativos
            # este algoritmo não funciona caso elas existam
            for i in range(len(self.nodes)):
                for edge in self.nodes[i].edgesComplete:
                    if int(edge[2]) < 0:
                        print('\nERRO! O grafo não pode possuir arestas com peso negativo.\n')
                        return
                        
            # resetando os valores dos atributos dos nodos
            self.nodeResetter() 

            # listas auxiliares para guardar as listas em ordem de peso e o resultado final, respectivamente
            self.ordenadas = []
            self.minimum = []

            # guardamos todas as arestas
            for i in range(len(self.nodes)):
                for edge in self.nodes[i].edgesComplete:
                    self.ordenadas.append(edge)

            # e as ordenamos por peso
            self.ordenadas = sorted(self.ordenadas, key=itemgetter(2))

            # percorremos as arestas ordenadas e utilizamos o índice do primeiro elemento
            for edge in self.ordenadas:
                self.indice = self.index(edge[0])
                
                # percorrendo todas as arestas no índice encontrado
                for edgesK in self.nodes[self.indice].edgesComplete:

                    # agora pegamos o índice no segundo elemento da aresta para verificar se ele já tem pai
                    # caso não tenha ela será definido - isto evita que o grafo fique um ciclo
                    edgeIndex = self.index(edgesK[1])
                
                    if self.nodes[edgeIndex].parent == None:
                        self.nodes[edgeIndex].parent = edgesK[0]
                        self.minimum.append(edgesK)

            print(self.minimum)
        
    def dijkstra(self):
        # https://www.youtube.com/watch?v=ovkITlgyJ2s&t=0s
        # o grafo deve ser direcionado!
        if self.directed:

            # veriricando se o grafo possui arestas com pesos negativos
            # este algoritmo não funciona caso elas existam
            for i in range(len(self.nodes)):
                for edge in self.nodes[i].edgesComplete:
                    if int(edge[2]) < 0:
                        print('\nERRO! O grafo não pode possuir arestas com peso negativo.\n')
                        return
            
            # resetando os valores dos atributos dos nodos
            self.nodeResetter()

            # indíce no nodo inicial - distância = zero
            self.indice = 0
            self.nodes[self.indice].distance = 0
            self.nodes[self.indice].done = True

            self.nodosAPercorrer = []

            # adicionando os nodos que ainda não foram finalizados - ou seja, todos menos o nodo de partida
            for i in range(len(self.nodes)):
                if not self.nodes[i].done:
                    self.nodosAPercorrer.append(self.nodes[i])

            while len(self.nodosAPercorrer) > 0:            

                # percorremos os nodos ligados ao nodo com índice self.indice
                # este valor começa em zero e o atualizamos após o relaxamento de todos os nodos adjacentes
                for edge in self.nodes[self.indice].edgesComplete:
                    
                    # pegamos o índice da aresta ligada ao nodo
                    edgeIndex = self.index(edge[1])
                    
                    # "relaxamento" dos nodos adjacentes               
                    # verificamos se a distância atual do nodo é menor do que o caminho já percorrido mais o peso da aresta
                    if self.nodes[edgeIndex].distance > self.nodes[self.indice].distance + int(edge[2]):
                        self.nodes[edgeIndex].parent = self.nodes[self.indice].label
                        self.nodes[edgeIndex].distance = self.nodes[self.indice].distance + int(edge[2])

                # procuramos o nodo com menor distância percorrida para servir como o próximo nodo de partida
                self.minimum = float('inf')
                for i in range(len(self.nodosAPercorrer)):
                                
                    if self.nodosAPercorrer[i].distance < self.minimum:
                        self.minimum = self.nodosAPercorrer[i].distance
                        self.indice = self.index(self.nodosAPercorrer[i].label)
                        self.removeIndex = i

                # remoção do nodo já finalizado
                self.nodosAPercorrer.pop(self.removeIndex)        
            
            print()    
            for i in range(len(self.nodes)):
                print(f'label: {self.nodes[i].label}')
                print(f'parent: {self.nodes[i].parent}')
                print(f'distance: {self.nodes[i].distance}')
                print()
        else:
            print('\nERRO! O grafo precisa ser orientado.\n')

    def bellmanFord(self, s):
        # https://www.youtube.com/watch?v=vEztwiTELWs

        if self.directed:
            # resetando os valores dos atributos dos nodos
            self.nodeResetter() 
            
            # atribui distância zero ao primeiro termo do grafo
            s = self.index(s)
            self.nodes[s].distance = 0

            # conta as repetições de relaxamento de nodos
            for i in range(len(self.nodes) - 1):

                # percorre nodos
                for j in range(len(self.nodes)):

                    # percorre arestas           
                    for edge in self.nodes[j].edgesComplete:  

                        # pegamos o índice da aresta ligada ao nodo
                        edgeIndex = self.index(edge[1])

                        # RELAXA
                        # se a distância entre o nodo e seu vizinho é menor que a atual
                        # guarda a nova dsitância e altera pai
                        if self.nodes[edgeIndex].distance > self.nodes[j].distance + int(edge[2]):
                            self.nodes[edgeIndex].parent = self.nodes[j].label
                            self.nodes[edgeIndex].distance = self.nodes[j].distance + int(edge[2])

            # repete-se o processo para averiguar se há ciclos negativos
            # o que causaria sempre novos. Retorna False se há
            for j in range(len(self.nodes)):
                for edge in self.nodes[j].edgesComplete:  
                    edgeIndex = self.index(edge[1])
                    if self.nodes[edgeIndex].distance > self.nodes[j].distance + int(edge[2]):
                        print('\nERRO! O grafo não pode possuir ciclo negativo.\n')
                        return False

            # se não há ciclo negativo imprimi-se os parâmetros
            print()    
            for i in range(len(self.nodes)):
                print(f'Nodo = {self.nodes[i].label}')
                print(f'Pai = {self.nodes[i].parent}')
                print(f'Distância = {self.nodes[i].distance}')
                print()  

            return True
          
        else:
            print('\nERRO! O grafo precisa ser orientado.\n')
            return False

    # auxilia a resetar atributos dos nodos do grafo
    def nodeResetter(self):
        for i in range(len(self.nodes)):
            self.nodes[i].parent = None
            self.nodes[i].key = float('inf')
            self.nodes[i].done = False
            self.nodes[i].distance = float('inf')     

    #==== AUXILIAR ====#

    # retorna índice (da lista self.grafos) de algum nodo
    def index(self, label):
        for i in range(len(self.nodes)):
            if self.nodes[i].label == str(label):
                return i
        
        # caso não encontre o elemento procurado
        return -1
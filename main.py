'''
    Tarefa sobre Grafos
    Augusto
    Murilo
'''

class Graph():  # classe para o grafo e seus métodos

    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges                       
 
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
        # print os nodos na horizontal - primeira linha
        print('  ', end='')
        for i in range(len(self.nodes)):
            print(f'{self.nodes[i]} ', end='')
        
        print()

        # procura pelas nodos que possuem arestas entre si
        for i in range(len(self.nodes)):
            print(f'{self.nodes[i]} ', end='')
                        
            for j in range(len(self.nodes)):
                # a comparação abaixo é feita com or para garantir que
                #  tanto (1, 5) quanto (5, 1) sejam registdas correntamente
                if list([self.nodes[i], self.nodes[j]]) in self.edges or list([self.nodes[j], self.nodes[i]]) in self.edges:
                    print('1 ', end='')
                else:
                    print('0 ', end='')
            print()
        

# função para receber entrada - sugestão: mover para main
def readFile():  
    with open('entrada.txt') as file:        
        lines = [line.rstrip() for line in file]  

    return lines


def main():    
    
    # lê os dados do arquivo de entrada
    data = readFile()

    # cria uma lista com os nodos a partir da primeira linha lida do arquivo de entrada
    nodes = []
    for char in data[0]:
        nodes.append(char)

    # as linhas seguintes são as arestas
    #edges = data[1:]
    edges = []
    for linha in data[1:]:
        edges.append([linha[0], linha[1]])
    
    
    # cria o objeto passando como parâmetro os nodos e arestas
    g = Graph(nodes, edges)    

    # testes
    g.view()
    for node in nodes:
        g.grade(node)
    g.adjacencyMatrix()

main()

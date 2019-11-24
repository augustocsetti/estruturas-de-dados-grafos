'''
    Tarefa sobre Grafos

    Augusto Cardoso Setti - Matrícula 119994
    Murilo Vitória da Silva - Matrícula 124816

QUESTÕES EM ABERTO

- Acertar buscas com edgesD edgesND;
- Criar classes específicas para buscas e caminhos;
- Melhorar mostra informações com busca por profundidade e largura;

- Aconteceu um erro quando estava testando várias maneiras de busca por largura
uma erro de char~int com uma lista. Testar!

'''

from Grafo import *                
              
def readFile(): # função para receber entrada do arquivo
    with open('entrada.txt') as file:
        lines = [line.rstrip() for line in file]
    for i in range(len(lines)):
        lines[i] = lines[i].split(" ")   

    return lines[0], lines


def menu(): # menu do programa
    print('==================================Opções==================================')
    print('1 - Mostrar lista de adjacências   ---   2 - Mostrar matriz de adjacências')
    print('3 - Inserir um nodo                ---   4 - Remover um nodo')
    print('5 - Inserir uma aresta             ---   6 - Remover uma aresta')
    print('7 - Informar o grau de um nodo     ---   8 - Fontes e sumidouros do grafo')
    print('9 - Muda direcionamento do grafo   ---   10 - Breadth First Search')
    print('11 - Depth First Search            ---   12 - Prim')
    print('13 - Kruskal                       ---   14 - Dijkstra')
    print('15 - Bellman-Ford                  ---   16 - Arestas com pesos')
    print('0 - Encerra o programa')
    print('===========================================================================')
    option = input('Opção: ')

    return option


#==== MAIN ====#

def main():

    # lê os dados do arquivo de entrada e cria uma lista com
    # os nodos na posição 0 e as arestas nas posições seguintes
    nodes, data = readFile()

    # as linhas seguintes são as arestas
    edges = []
    edgesW = []

    for linha in data[1:]:
        edges.append([linha[0], linha[1]])
        edgesW.append([linha[0], linha[1], linha[2]])

    # cria o objeto passando como parâmetro os nodos e arestas
    g = Graph(nodes, edges, edgesW)
    
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
                g.insert(input('Informe a aresta a ser incluída ([nodo1] [nodo2] [peso]): '))
            elif op == 6:
                g.remove(input('Informe a aresta a ser excluída ([nodo1] [nodo2]): '))
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
            elif op == 12:                
                g.prim()
            elif op == 13:                
                g.kruskal()
            elif op == 14:
                g.dijkstra()
            elif op == 15:
                g.bellmanFord(input('Insira o nodo para iniciar o caminho: '))
            elif op == 16:
                g.view2()
            elif op < 0 or op > 16:
                print('\nERRO! Favor informar um valor entre 0 e 16.\n')

        except ValueError:
            print('\nFavor informar um valor válido.\n')
        

main()

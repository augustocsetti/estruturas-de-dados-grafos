class Node():  # classe para os nodos e suas características

    def __init__(self, label='', edgesD='', edgesND='', edgesWH=[]):
        self.label = label # valor do nodo
        self.edgesD = edgesD # arestas direcionadas
        self.edgesND = edgesND # arestas não direcionadas
        self.gradeIn = 0 # grau de entrada
        self.gradeOut = 0 # grau de saída
        self.edgesWH = edgesWH

        # infos para funções de busca
        self.set = False # usado para marcar nodo em buscas
        self.father = None # marcação do nodo pai na busca por profundidade
        self.time = [] # tempo de abertura e fechamento na busca por profundidade
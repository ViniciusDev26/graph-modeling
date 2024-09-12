# Classe de representação do grafo
class Grafo:
    # Função de inicialização do grafo como um dicionário vazio (chave: nó, valor: lista de nós vizinhos (arestas))
    def __init__(self):
        self.grafo = {}


    # Função de criação de uma aresta, ligando 2 nós
    def adicionar_aresta(self, origem, destino):
        # Verifica se o nó de origem já existe no grafo. Se não existir, cria uma nova lista vazia para nós vizinhos
        if origem not in self.grafo:
            self.grafo[origem] = []
        # Caso o nó de destino já exista, adiciona-se o nó de destino à lista de vizinhos
        self.grafo[origem].append(destino)


    def carregar_estrutura(self, estrutura):
        # Para cada nó de origem e seus respectivos destinos na estrutura
        for origem, destinos in estrutura.items():
            # Adiciona uma aresta (ligação) para cada destino
            for destino in destinos:
                self.adicionar_aresta(origem, destino)


    # Função de verificação de ciclos no grafo e na árvore de decisão, usando busca em prufundidade
    def dfs_verifica_ciclo(self):
        # Lista para armazenar nós já visitados
        visitado = set() 
        # Pilha de nós atuais na recursão
        recursao_pilha = set() 

        # Para cada nó no grafo
        for no in self.grafo:
            # Se o nó ainda não foi visitado, iniciamos a busca em profundidade a partir dele
            if no not in visitado:
                # Chamamos a função recursiva _dfs e, se detectarmos um ciclo, retornamos False
                if self._dfs(no, visitado, recursao_pilha):
                    print("Ciclo detectado!")
                    return False
        # Se não detectamos ciclos, retornamos True
        print("Nenhum ciclo detectado!")
        return True


    def _dfs(self, no, visitado, recursao_pilha):
        # Marca o nó atual como visitado, adicionando-o a lista de visitados
        visitado.add(no)
        # Adiciona o nó atual à pilha de recursão para controlar o caminho atual
        recursao_pilha.add(no)

        # Verifica todos os vizinhos do nó atual
        for vizinho in self.grafo.get(no, []):
            # Se o vizinho não foi visitado, fazemos a busca recursiva nele
            if vizinho not in visitado:
                # Se encontrarmos um ciclo na recursão, retornamos True
                if self._dfs(vizinho, visitado, recursao_pilha):
                    return True
            # Se o vizinho já está na pilha de recursão, detectamos um ciclo
            elif vizinho in recursao_pilha:
                return True

        # Remove o nó da pilha de recursão ao terminar de explorar todos os seus vizinhos
        recursao_pilha.remove(no)
        # Não encontramos um ciclo, retornamos False
        return False  


    def imprimir_estrutura(self):
        print("\n")
        print("Estrutura do Grafo:")
        # Para cada nó (node) no grafo, imprimimos seus vizinhos
        for node, vizinhos in self.grafo.items():
            # Se o nó não tiver vizinhos, imprimimos "Nenhum vizinho"
            vizinhos_texto = ', '.join(vizinhos) if vizinhos else 'Nenhum vizinho'
            print(f"  {node} -> {vizinhos_texto}")
        print("\n\n")


# Fluxo de atendimento (com ciclos)
fluxo_atendimento_com_ciclo = {
    'Recepção': ['Triagem'],
    'Triagem': ['Consulta'],
    'Consulta': ['Exame', 'Tratamento'],
    'Exame': ['Resultado'],
    'Resultado': ['Consulta'],  # ciclo
    'Tratamento': []
}


# Fluxo de atendimento (sem ciclo)
fluxo_atendimento = {
    'Entrada': ['Triagem'],
    'Triagem': ['Consulta'],
    'Consulta': ['Exame', 'Tratamento'],
    'Exame': ['Resultado'],
    'Resultado': ['Tratamento'],
    'Tratamento': ['Alta'],
    'Alta': []
}

# Fluxo de atendimento (com ciclos)
fluxo_atendimento_com_ciclos = {
    'Entrada': ['Triagem'],
    'Triagem': ['Consulta'],
    'Consulta': ['Exame', 'Tratamento'],
    'Exame': ['Resultado'],
    'Resultado': ['Tratamento', 'Consulta'],  # ciclo com Consulta de retorno
    'Tratamento': ['Alta'],
    'Alta': []
}


# Árvore de decisão de anamnese (sem ciclo)
arvore_anamnese = {
    'Febre': ['Dor de garganta', 'Dor no peito'],
    'Dor de garganta': ['Tratamento A', 'Tosse'],
    'Tosse': ['Tratamento B', 'Tratamento C'],
    'Dor no peito': ['Tratamento D', 'Tratamento E'],
    'Tratamento A': ["Alta"],
    'Tratamento B': ["Alta"],
    'Tratamento C': ["Alta"],
    'Tratamento D': ["Alta"],
    'Tratamento E': ["Alta"],
    'Alta': []
}


# Árvore de decisão de anamnese (com ciclo)
arvore_anamnese_com_ciclo = {
    'Sintoma A': ['Exame 1', 'Exame 2'],
    'Exame 1': ['Diagnóstico 1'],
    'Exame 2': ['Diagnóstico 2'],
    'Diagnóstico 1': ['Sintoma A'],  # ciclo
    'Diagnóstico 2': []
}


# Criação dos grafos para cada estrutura
def runGraph(flow_name, graph_data):
    print("--------------------------------------------------\n")
    print(f"Verificação para {flow_name}:")
    print("\n")

    grafo = Grafo()
    grafo.carregar_estrutura(graph_data)
    grafo.dfs_verifica_ciclo()
    grafo.imprimir_estrutura()


# Verificação do fluxo de atendimento (sem ciclo)
runGraph("o Fluxo de Atendimento", fluxo_atendimento)

# Verificação do fluxo de atendimento (com ciclo)
runGraph("o Fluxo de Atendimento com ciclo", fluxo_atendimento_com_ciclos)

# Verificação da árvore de anamnese (sem ciclo)
runGraph("a Árvore de Anamnese (sem ciclo)", arvore_anamnese)

# Verificação da árvore de anamnese (com ciclo)
runGraph("a Árvore de Anamnese (com ciclo)", arvore_anamnese_com_ciclo)

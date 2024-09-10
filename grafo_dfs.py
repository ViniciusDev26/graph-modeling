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
        print("\nEstrutura do Grafo:")
        # Para cada nó no grafo, imprimimos seus vizinhos
        for no, vizinhos in self.grafo.items():
            # Se o nó não tiver vizinhos, imprimimos "Nenhum vizinho"
            vizinhos_texto = ', '.join(vizinhos) if vizinhos else 'Nenhum vizinho'
            print(f"{no} -> {vizinhos_texto}")


# Fluxo de atendimento (sem ciclos)
fluxo_atendimento = {
    'Recepção': ['Triagem'],
    'Triagem': ['Consulta'],
    'Consulta': ['Exame', 'Tratamento'],
    'Exame': ['Resultado'],
    'Resultado': ['Tratamento'],
    'Tratamento': []
}

# Árvore de decisão de anamnese (sem ciclos)
arvore_anamnese = {
    'Sintoma A': ['Exame 1', 'Exame 2'],
    'Exame 1': ['Diagnóstico 1'],
    'Exame 2': ['Diagnóstico 2'],
    'Diagnóstico 1': [],
    'Diagnóstico 2': []
}

# Árvore de decisão de anamnese com ciclo (para testar o ciclo)
arvore_anamnese_com_ciclo = {
    'Sintoma A': ['Exame 1', 'Exame 2'],
    'Exame 1': ['Diagnóstico 1'],
    'Exame 2': ['Diagnóstico 2'],
    'Diagnóstico 1': ['Sintoma A'],  # ciclo
    'Diagnóstico 2': []
}

# Criação dos grafos para cada estrutura
grafo_fluxo = Grafo()
grafo_anamnese = Grafo()
grafo_anamnese_com_ciclo = Grafo()

# Verificação do fluxo de atendimento
print("Verificação para o Fluxo de Atendimento:")
grafo_fluxo.carregar_estrutura(fluxo_atendimento) 
grafo_fluxo.dfs_verifica_ciclo() 
grafo_fluxo.imprimir_estrutura() 

# Verificação da árvore de anamnese (sem ciclos)
print("\nVerificação para a Árvore de Anamnese (sem ciclo):")
grafo_anamnese.carregar_estrutura(arvore_anamnese) 
grafo_anamnese.dfs_verifica_ciclo() 
grafo_anamnese.imprimir_estrutura()  

# Verificação da árvore de anamnese (com ciclo)
print("\nVerificação para a Árvore de Anamnese (com ciclo):")
grafo_anamnese_com_ciclo.carregar_estrutura(arvore_anamnese_com_ciclo)  
grafo_anamnese_com_ciclo.dfs_verifica_ciclo()  
grafo_anamnese_com_ciclo.imprimir_estrutura()  

class Grafo:
  def __init__(self):
    self.grafo = {}

  def adicionar_aresta(self, origem, destino):
    if origem not in self.grafo:
      self.grafo[origem] = []
  self.grafo[origem].append(destino)


  def carregar_estrutura(self, estrutura):
    for origem, destinos in estrutura.items():
      for destino in destinos:
        self.adicionar_aresta(origem, destino)

  def dfs_verifica_ciclo(self):
    visitado = set() 
    recursao_pilha = set() 

    for no in self.grafo:
      if no not in visitado:
        if self._dfs(no, visitado, recursao_pilha):
          print("Ciclo detectado!")
          return False
    print("Nenhum ciclo detectado!")
    return True


  def _dfs(self, no, visitado, recursao_pilha):
    visitado.add(no)
    recursao_pilha.add(no)

    for vizinho in self.grafo.get(no, []):
      if vizinho not in visitado:
        if self._dfs(vizinho, visitado, recursao_pilha):
            return True
      
      elif vizinho in recursao_pilha:
        return True
    recursao_pilha.remove(no)
    return False  


  def imprimir_estrutura(self):
    print("\n")
    print("Estrutura do Grafo:")

    for node, vizinhos in self.grafo.items():
      vizinhos_texto = ', '.join(vizinhos) if vizinhos else 'Nenhum vizinho'
      print(f"  {node} -> {vizinhos_texto}")
    print("\n\n")

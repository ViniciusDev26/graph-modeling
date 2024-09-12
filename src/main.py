from graph import Grafo
from flows import *

# Criação dos grafos para cada estrutura
def runGraph(flow_name, graph_data):
  print("--------------------------------------------------\n")
  print(f"Verificação para {flow_name}:")
  print("\n")

  grafo = Grafo()
  grafo.carregar_estrutura(graph_data)
  grafo.dfs_verifica_ciclo()
  grafo.imprimir_estrutura()

# Verificação do fluxo de atendimento
runGraph("o Fluxo de Atendimento", fluxo_atendimento)

# Verificação do fluxo de atendimento com ciclo
runGraph("o Fluxo de Atendimento com ciclo", fluxo_atendimento_com_ciclos)

# Verificação da árvore de anamnese (sem ciclos)
runGraph("a Árvore de Anamnese (sem ciclo)", arvore_anamnese)

# Verificação da árvore de anamnese (com ciclos)
runGraph("a Árvore de Anamnese (com ciclo)", arvore_anamnese_com_ciclo)

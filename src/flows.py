# Fluxo de atendimento (sem ciclos)
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

# Árvore de decisão de anamnese (sem ciclos)
arvore_anamnese = {
  'Sintoma A': ['Exame 1', 'Exame 2'],
  'Exame 1': ['Diagnóstico 1'],
  'Exame 2': ['Diagnóstico 2'],
  'Diagnóstico 1': [],
  'Diagnóstico 2': []
}

arvore_anamnese_com_ciclo = {
  'Sintoma A': ['Exame 1', 'Exame 2'],
  'Exame 1': ['Diagnóstico 1'],
  'Exame 2': ['Diagnóstico 2'],
  'Diagnóstico 1': ['Sintoma A'],  # ciclo
  'Diagnóstico 2': []
}
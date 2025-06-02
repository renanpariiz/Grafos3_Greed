import json
import heapq

def interval_partitioning(atividades):
    atividades_ordenadas = sorted(atividades, key=lambda x: x['inicio'])

    salas_heap = []
    alocacao_salas = {}
    proxima_sala = 1

    for atividade in atividades_ordenadas:
        if salas_heap and salas_heap[0][0] <= atividade['inicio']:
            fim_anterior, sala = heapq.heappop(salas_heap)
        else:
            sala = proxima_sala
            proxima_sala += 1

        if sala not in alocacao_salas:
            alocacao_salas[sala] = []
        alocacao_salas[sala].append(atividade['id'])

        heapq.heappush(salas_heap, (atividade['fim'], sala))

    return alocacao_salas


# Leitura do arquivo JSON (sem verificação de JSON válido)
with open('aulas.json', 'r') as f:
    dados = json.load(f)
    lista_aulas = dados.get('aulas', [])  # Se 'aulas' não existir, vai ser lista vazia

# Não há verificação se lista_aulas está vazia
# Executa direto
alocacao = interval_partitioning(lista_aulas)

print("Alocação de aulas por sala (Interval Partitioning):")
for sala, aulas_ids in sorted(alocacao.items()):
    print(f"\nSala {sala}:")
    for aula_id in aulas_ids:
        detalhes_aula = next((aula for aula in lista_aulas if aula['id'] == aula_id), None)
        if detalhes_aula:
            print(f"- {aula_id} (Início: {detalhes_aula['inicio']}, Fim: {detalhes_aula['fim']})")
        else:
            print(f"- {aula_id}")

print(f"\nNúmero mínimo de salas necessárias: {len(alocacao)}")

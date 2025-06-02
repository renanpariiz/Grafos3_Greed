import json
import heapq

def interval_partitioning(atividades):
    """Distribui todas as atividades em diferentes salas sem conflitos, minimizando o número de salas.

    Args:
        atividades (list): Uma lista de dicionários, onde cada dicionário representa
                           uma atividade e contém 'id', 'inicio' e 'fim'.

    Returns:
        dict: Um dicionário onde as chaves são números de salas e os valores são listas de IDs de atividades alocadas.
    """
    # Ordena as atividades pelo horário de início
    atividades_ordenadas = sorted(atividades, key=lambda x: x['inicio'])

    # Heap (fila de prioridade) para controlar o horário de término das salas
    salas_heap = []  # Cada elemento: (fim_da_ultima_atividade, numero_sala)
    # Dicionário para armazenar a alocação de atividades por sala
    alocacao_salas = {}
    proxima_sala = 1

    for atividade in atividades_ordenadas:
        if salas_heap and salas_heap[0][0] <= atividade['inicio']:
            # Reutiliza a sala que terminar antes
            fim_anterior, sala = heapq.heappop(salas_heap)
        else:
            # Cria uma nova sala
            sala = proxima_sala
            proxima_sala += 1

        # Aloca a atividade na sala
        if sala not in alocacao_salas:
            alocacao_salas[sala] = []
        alocacao_salas[sala].append(atividade['id'])

        # Atualiza o heap com o novo horário de término dessa sala
        heapq.heappush(salas_heap, (atividade['fim'], sala))

    return alocacao_salas

# Leitura do arquivo JSON com as aulas
try:
    with open('aulas.json', 'r') as f:
        dados = json.load(f)
        lista_aulas = dados.get('aulas', [])
except FileNotFoundError:
    print("Erro: Arquivo 'aulas.json' não encontrado no diretório atual.")
    exit()
except json.JSONDecodeError:
    print("Erro: O arquivo 'aulas.json' não contém um JSON válido.")
    exit()

if not lista_aulas:
    print("Nenhuma aula encontrada no arquivo JSON.")
else:
    # Executa o algoritmo de Interval Partitioning
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

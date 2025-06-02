import json

def interval_scheduling(atividades):
    """Seleciona o número máximo de atividades não conflitantes usando uma abordagem gulosa.

    Args:
        atividades (list): Uma lista de dicionários, onde cada dicionário representa
                           uma atividade e contém 'id', 'inicio' e 'fim'.

    Returns:
        list: Uma lista de IDs das atividades selecionadas.
    """
    # Ordena as atividades pelo tempo de término (fim)
    atividades_ordenadas = sorted(atividades, key=lambda x: x['fim'])

    atividades_selecionadas = []
    ultimo_fim = 0

    for atividade in atividades_ordenadas:
        if atividade['inicio'] >= ultimo_fim:
            atividades_selecionadas.append(atividade['id'])
            ultimo_fim = atividade['fim'] # Atualiza o tempo de término da última atividade selecionada

    return atividades_selecionadas

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
    # Executa o algoritmo de Interval Scheduling
    aulas_selecionadas = interval_scheduling(lista_aulas)

    print("Aulas selecionadas (Interval Scheduling):")
    if aulas_selecionadas:
        for aula_id in aulas_selecionadas:
            # Encontra os detalhes da aula selecionada para exibição 
            detalhes_aula = next((aula for aula in lista_aulas if aula['id'] == aula_id), None)
            if detalhes_aula:
                print(f"- {aula_id} (Início: {detalhes_aula['inicio']}, Fim: {detalhes_aula['fim']})")
            else:
                 print(f"- {aula_id}") # Caso não encontre detalhes
    else:
        print("Nenhuma aula pôde ser selecionada.")

    print(f"\nTotal de aulas selecionadas: {len(aulas_selecionadas)}")



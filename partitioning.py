import json
from collections import defaultdict

# Classe que representa a rede social como um grafo (estrutura de nós e conexões)
class RedeSocial:
    def __init__(self):
        # Utilizamos um dicionário onde cada usuário é uma chave
        # e seu valor é uma lista de amigos (vizinhos no grafo)
        self.grafo = defaultdict(list)

    # Adiciona um novo usuário à rede, caso ainda não exista
    def adicionar_usuario(self, usuario):
        if usuario not in self.grafo:
            self.grafo[usuario] = []

    # Cria uma amizade (conexão bidirecional) entre dois usuários
    def adicionar_amizade(self, usuario1, usuario2):
        self.grafo[usuario1].append(usuario2)
        self.grafo[usuario2].append(usuario1)

    # Busca em profundidade para encontrar "componentes conexas"
    # Ou seja, grupos de usuários que estão todos conectados de alguma forma
    def encontrar_componentes_conexas(self):
        visitado = set()     # Conjunto para marcar usuários já visitados
        componentes = []     # Lista de todos os grupos encontrados

        # Função recursiva de busca em profundidade (DFS)
        def dfs(usuario, componente):
            visitado.add(usuario)         # Marca o usuário como visitado
            componente.append(usuario)    # Adiciona ao grupo atual
            for vizinho in self.grafo[usuario]:  # Percorre os amigos
                if vizinho not in visitado:
                    dfs(vizinho, componente)

        # Verifica cada usuário da rede
        for usuario in self.grafo:
            if usuario not in visitado:
                componente = []           # Cria um novo grupo
                dfs(usuario, componente)  # Inicia a DFS a partir dele
                componentes.append(componente)  # Salva o grupo encontrado

        return componentes

# Leitura do arquivo JSON com os dados da rede social 
with open("rede_social.json", "r") as arquivo:
    dados = json.load(arquivo)

rede = RedeSocial()

# Adiciona todos os usuários presentes no JSON à rede
for u in dados["usuarios"]:
    rede.adicionar_usuario(u)

# Adiciona todas as amizades (conexões) entre os usuários
for u1, u2 in dados["amizades"]:
    rede.adicionar_amizade(u1, u2)

# Exibição dos grupos (componentes conexas)
componentes = rede.encontrar_componentes_conexas()

# Mostra cada grupo encontrado, com os nomes dos membros
for i, grupo in enumerate(componentes, start=1):
    membros = ", ".join(grupo)  # Junta os nomes separados por vírgula
    print(f"Grupo {i}: {membros}")

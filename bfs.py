import json  # Importa a biblioteca para leitura de arquivos JSON
from collections import deque, defaultdict  # deque: fila eficiente; defaultdict: dicionário com valor padrão (lista)

# Classe que representa a rede social usando o algoritmo de BFS
class RedeSocialBFS:
    def __init__(self):
        # O grafo é representado como um dicionário onde cada chave é um usuário, e o valor é a lista de amigos (vizinhos)
        self.grafo = defaultdict(list)

    # Adiciona um novo usuário ao grafo, garantindo que ele tenha uma lista de amigos
    def adicionar_usuario(self, usuario):
        if usuario not in self.grafo:
            self.grafo[usuario] = []

    # Cria uma amizade bidirecional entre dois usuários (ou seja, adiciona as arestas nos dois sentidos)
    def adicionar_amizade(self, usuario1, usuario2):
        self.grafo[usuario1].append(usuario2)
        self.grafo[usuario2].append(usuario1)

    # Algoritmo de busca em largura (BFS) para encontrar o grau de separação entre dois usuários
    def grau_de_separacao(self, origem, destino):
        visitado = set()  # Conjunto de usuários já visitados
        fila = deque([(origem, 0)])  # Fila de tuplas: (usuário, grau de separação)

        while fila:
            atual, grau = fila.popleft()  # Pega o próximo usuário da fila
            if atual == destino:
                return grau  # Encontrou o destino, retorna o grau

            if atual not in visitado:
                visitado.add(atual)  # Marca como visitado
                # Adiciona os amigos (vizinhos) na fila para continuar a busca
                for vizinho in self.grafo[atual]:
                    if vizinho not in visitado:
                        fila.append((vizinho, grau + 1))
        
        return -1  # Caso não exista caminho entre origem e destino

# --- Leitura do JSON ---
# Abre o arquivo 'rede_social.json' e carrega os dados de usuários e amizades
with open("rede_social.json", "r") as arquivo:
    dados = json.load(arquivo)

# Cria uma instância da rede social
rede = RedeSocialBFS()

# Adiciona todos os usuários da lista no grafo
for u in dados["usuarios"]:
    rede.adicionar_usuario(u)

# Adiciona todas as amizades no grafo (arestas)
for u1, u2 in dados["amizades"]:
    rede.adicionar_amizade(u1, u2)

# --- Teste com dois usuários qualquer ---
# Aqui estamos consultando o grau de separação entre "Ana" e "Felipe"
print("Grau de separação entre Carlos e Felipe:", rede.grau_de_separacao("Carlos", "Felipe"))
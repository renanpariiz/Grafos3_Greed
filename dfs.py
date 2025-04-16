import json  # Importa a biblioteca para leitura de arquivos JSON
from collections import defaultdict  # defaultdict: dicionário com valor padrão (lista)

# Classe que representa a rede social usando o algoritmo de DFS
class RedeSocialDFS:
    def __init__(self):
        self.grafo = defaultdict(list)

    def adicionar_usuario(self, usuario):
        if usuario not in self.grafo:
            self.grafo[usuario] = []

    def adicionar_amizade(self, usuario1, usuario2):
        self.grafo[usuario1].append(usuario2)
        self.grafo[usuario2].append(usuario1)

    # Algoritmo de busca em profundidade (DFS) para encontrar o grau de separação
    def grau_de_separacao(self, origem, destino):
        visitado = set()
        return self._dfs(origem, destino, visitado, 0)

    def _dfs(self, atual, destino, visitado, grau):
        if atual == destino:
            return grau

        visitado.add(atual)

        for vizinho in self.grafo[atual]:
            if vizinho not in visitado:
                resultado = self._dfs(vizinho, destino, visitado, grau + 1)
                if resultado != -1:
                    return resultado

        return -1  # Caso não encontre caminho

# --- Leitura do JSON ---
with open("rede_social.json", "r") as arquivo:
    dados = json.load(arquivo)

# Cria uma instância da rede social com DFS
rede = RedeSocialDFS()

# Adiciona usuários e amizades
for u in dados["usuarios"]:
    rede.adicionar_usuario(u)

for u1, u2 in dados["amizades"]:
    rede.adicionar_amizade(u1, u2)

# Teste: grau de separação entre dois usuários
print("Grau de separação entre Carlos e Felipe:", rede.grau_de_separacao("Carlos", "Felipe"))

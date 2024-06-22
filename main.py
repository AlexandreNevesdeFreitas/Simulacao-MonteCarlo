import numpy as np
import time
import matplotlib.pyplot as plt
from metodos import *



inicio = time.time()
raio = 10
centro = np.array([0, 0, 0])

eixo_cone = np.array([0, 0, 1])

theta = np.pi / 4
sorteios = [10**3, 10**4, 10**6]

resultados = []

for i, qtde_sorteios in enumerate(sorteios):
    pts_no_angulo_solido = sortea_pontos(qtde_sorteios, raio, centro, eixo_cone, theta)

    novo_resultado = {
        "Pontos no ângulo sólido: ": pts_no_angulo_solido, 
        "Valor do ângulo sólido": ((4 * np.pi) * pts_no_angulo_solido) / qtde_sorteios
    }
    resultados.append(novo_resultado)

    obter_resultados(pts_no_angulo_solido, qtde_sorteios)

fig, axs = plt.subplots(1, len(resultados), figsize=(18, 6))

# Plotagem dos gráficos para cada resultado
for i, resultado in enumerate(resultados):
    pts_no_angulo_solido = resultado["Pontos no ângulo sólido: "]
    qtde_sorteios = sorteios[i]
    obter_resultados(pts_no_angulo_solido, qtde_sorteios, ax=axs[i])

# Ajustes de layout e exibição final dos gráficos
plt.tight_layout()
plt.show()

fim =  time.time()

tempo_execucao = fim - inicio
print("Tempo: ", tempo_execucao)
print(resultados)
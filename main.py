# O algoritmo Simulated Anneling substitui a solução atual por uma solução próxima escolhida de acordo com uma função objetivo
# e com uma variável TEMP (Temperatura).
# À medida que o algoritmo progride, o valor de T é decrementado, começando o algoritmo a convergir para uma solução ótima

import time
from SimulatedAnnealing import SimulatedAnnealing

QUEENS = 40 # Numero de Rainhas no Tabuleiro
TEMP = 3000 # Quanto maior for TEMP (Temperatura), maior a componente aleatória que será incluída na próxima solução escolhida.

def CalculateTime(StartTime):
    print("Tempo de execução do algoritmo: " + str(time.time() - StartTime) + "s")

def main():
    StartTime = time.time()
    SimulatedAnnealing(QUEENS, TEMP)
    CalculateTime(StartTime)

if __name__ == "__main__":
    main()

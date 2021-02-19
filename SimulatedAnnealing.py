import random
from math import exp
from copy import deepcopy

### Funções Auxiliares ###

def AuxAdjustBoard(temp, chessboard):
    if temp in chessboard:
        chessboard[temp] += 1
    else:
        chessboard[temp] = 1

    return chessboard

def AuxAdjustThreat(chessboard):
    threat = 0
    for i in chessboard:
        threat += AuxThreatCalculate(chessboard[i])

    return threat

def AuxThreatCalculate(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    
    return (n - 1) * n / 2

### Funções Intermediárias ###

# função de custo para contar o total de pares de rainhas ameaçadas
def Cost(chessboard):
    m_chessboard = {}
    a_chessboard = {}
    
    threat = 0

    for column in chessboard:
        temp_m = column - chessboard[column]
        m_chessboard = AuxAdjustBoard(temp_m, m_chessboard)

        temp_a = column + chessboard[column]
        a_chessboard = AuxAdjustBoard(temp_a, a_chessboard)

    threat += AuxAdjustThreat(m_chessboard) 
    threat += AuxAdjustThreat(a_chessboard)

    del m_chessboard
    del a_chessboard

    return threat

def CreateBoard(N_QUEENS):
    chessBoard = {}
    boardSize = list(range(N_QUEENS))
    random.shuffle(boardSize)
    column = 0
 
    while len(boardSize) > 0:
        row = random.choice(boardSize)
        chessBoard[column] = row
        boardSize.remove(row)
        column += 1

    del boardSize
    return chessBoard

def PrintBoard(board):
    i = 1
    for column, row in board.items():
        print("> Rainha {}\n Coluna: {} - Linha: {}".format(i, column, row))
        i += 1

### Algoritmo ###

def SimulatedAnnealing(N_QUEENS, TEMPERATURE):
    answer = CreateBoard(N_QUEENS) # Começa a busca a partir de uma solução inicial qualquer. 
    CostAnswer = Cost(answer)

    t = TEMPERATURE
    sch = 0.99

    # Cada geração de um novo vizinho s’ de s, é testada a variação ∆ do valor da função objetivo, isto é, ∆ = f (s’) – f (s),
    while t > 0:
        t *= sch
        successor = deepcopy(answer)

        while True:
            index_1 = random.randrange(0, N_QUEENS - 1)
            index_2 = random.randrange(0, N_QUEENS - 1)

            if index_1 != index_2:
                break

        successor[index_1], successor[index_2] = successor[index_2], \
            successor[index_1]

        delta = Cost(successor) - CostAnswer

        # ∆ = 0: Caso de estabilidade
        if delta < 0 or random.uniform(0, 1) < exp (-delta / t):
            answer = deepcopy(successor)
            CostAnswer = Cost(answer)

        if CostAnswer == 0:
            PrintBoard(answer)
            return
        

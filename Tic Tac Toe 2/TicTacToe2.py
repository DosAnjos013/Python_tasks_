import random

jogadorAtual = "X"
gameRunnig = True
winner = None
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 1° Passo: Imprimir o tabuleiro;
# 2° Passo: Receber a jogada;
# 3° Passo: verificar vitória ou empate;
# 4° Passo: trocar jogador.


# !!!! 1° passo !!!!

def displayBoard(board):
    print (" +-------+-------+-------+\n",
    "|       |       |       |\n",
    "|  ",board[2][0],"  |  ",board [2][1],"  |  ",board [2][2],"  |\n",
    "|       |       |       |\n",
    "+-------+-------+-------+\n",
    "|       |       |       |\n",
    "|  ",board [1][0],"  |  ",board [1][1],"  |  ",board [1][2],"  |\n",
    "|       |       |       |\n",
    "+-------+-------+-------+\n",
    "|       |       |       |\n",
    "|  ",board [0][0],"  |  ",board [0][1],"  |  ",board [0][2],"  |\n",
    "|       |       |       |\n",
    "+-------+-------+-------+")


#   !!!! 2° passo !!!!
    
def playerInput (board):
    inp = int(input("\nDigite sua jogada (escolha um número 1~9): "))
    if inp >= 1 and inp <= 3:
        board [0][inp-1] = jogadorAtual
    elif inp >= 4 and inp <= 6:
        board [1][inp-4] = jogadorAtual
    elif inp >= 7 and inp <= 9:
        board [2][inp-7] = jogadorAtual
    else:
        print ("Essa posição não está disponível !!!!")

#   !!!! 3° passo !!!!
def verificarHorizontal(board):
    global winner
    if board [0][0] == board [0][1] == board [0][2] and board [0][0] != 1:
        winner = board [0][0]
        return True
    elif board [1][0] == board [1][1] == board [1][2] and board [1][0] != 4:
        winner = board [1][0]
        return True
    elif board [2][0] == board [2][1] == board [2][2] and board [2][0] != 7:
        winner = board [2][0]
        return True
    
def verificarColunas(board):
    global winner
    if board [0][0] == board [1][0] == board [2][0] and board [0][0] != 1:
        winner = board [0][0]
        return True
    elif board [0][1] == board [1][1] == board [2][1] and board [0][1] != 4:
        winner = board [1][0]
        return True
    elif board [0][2] == board [1][2] == board [2][2] and board [0][2] != 7:
        winner = board [0][2]
        return True
    
def verificarDiagonal(board):
    global winner
    if board [0][0] == board [1][1] == board [2][2]:
        winner = board[0][0]
        return True
    elif board [2][0] == board [1][1] == board [0][2]:
        winner = board [2][0]
        return True

def verificarEmpate (board):
    global gameRunnig
    if board [0][0] != 1 and board [0][1] != 2 and board[0][2] != 3 and board [1][0] != 4 and board [1][1] != 5 and board[1][2] != 6 and board [2][0] != 7 and board [2][1] != 8 and board[2][2] != 9:
        print ("O jogo terminou empatado")
        displayBoard(board)
        gameRunnig = False

def verificarVitoria():
    global gameRunnig
    if verificarColunas(board) or verificarDiagonal(board) or verificarHorizontal(board):
        print(f"O vencedor é {winner}")
        displayBoard(board)
        gameRunnig = False

def trocarJogador():
    global jogadorAtual
    if jogadorAtual == "X":
        jogadorAtual = "@"
    else:
        jogadorAtual = "X"

def computador(board):
    while jogadorAtual == "O":
        position = random.randint (0,2) and (0,2)
        if board[position] != "X":
            board[position] = "O"
            trocarJogador()


while gameRunnig:
    displayBoard(board)
    playerInput(board)
    verificarVitoria()
    verificarEmpate(board)
    trocarJogador()
    #computador(board)
    #verificarVitoria()
    #verificarEmpate(board)
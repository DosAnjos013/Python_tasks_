#Para iniciar o projeto, começaremos com o passo a passo.

import random

board =["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"] # foi criada uma tuple que servira como os espaços em branco do tabuleiro.

currentPlayer = "X"
winner = None
gameRunnig = True
check = 0

#passo/step 1: imprimir o tabuleiro/ print the game board

def printBoard(board): # criamos a função responsável por imprimir o tabuleiro.
    print(board [6] + " | " + board[7] + " | "+ board[8]) #acrescentamos as barras que compõe o tabuleiro formando uma # e definimos seus componentes
    print ("--+---+--")
    print(board [3] + " | " + board[4] + " | "+ board[5])
    print ("--+---+--")
    print(board [0] + " | " + board[1] + " | "+ board[2])




#passo/step 2: receber a jogada do jogador / take player input
while check == 0:
    def playerInput (board):
        inp = int(input("\nDigite sua jogada (escolha um número 1~9): "))
        if inp >= 1 and inp <= 9 and board[inp-1] == "-" :
            board [inp-1] = currentPlayer
            check += 1
        else:
            print ("\n                           OOPS\n            PLAYER IS ALREADY IN THAT SPOT!!!!!!!!!\n")

            
check = 0


#Passo/Step 3: verificar vitória ou empate / check win or tie

def checkHorizontle(board):
    global winner
    if board [0] == board[1] == board [2] and board[1] != "-":
        winner = board[0]
        return True
    elif board [3] == board[4] == board [5] and board[3] != "-":
        winner = board[3]
        return True
    elif board [6] == board[7] == board [8] and board[6] != "-":
        winner = board[6]
        return True
    
def checkRow(board):
    global winner
    if board [0] == board[3] == board [6] and board[0] != "-":
        winner = board[0]
        return True
       
    elif board [1] == board[4] == board [7] and board[1] != "-":
        winner = board[1]
        return True
       
    elif board [2] == board[5] == board [8] and board[2] != "-":
        winner = board[2]
        return True
        

def checkDiag(board):
    global winner
    if board [0] == board [4] == board [8] and board [0] != "-":
        winner = board [0]
        return True
       
    elif board [2] == board [4] == board [6] and board [2] != "-":
        winner = board [2]
        return True
        

def checkTie(board):
    global gameRunnig
    if "-" not in board:
        printBoard(board)
        print ("it's a tie!")
        gameRunnig = False

def checkWin():
    global gameRunnig
    if checkDiag(board) == True or checkHorizontle(board) == True or checkRow(board) == True:
        printBoard (board)
        print ("\nIT'S OVER")
        print(f"\nThe winner is {winner}")
        gameRunnig = False


#Passo/Step 4: trocar de jogador / switch the player
def switchPlayer ():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer ="O"
    else:
        currentPlayer = "X"

#Computer
def computer(board):
    while currentPlayer == "O":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()

#Passo/Step 5: verificar vitória ou empate dnv / check win or tie again


while gameRunnig:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    if  checkDiag(board) or checkHorizontle(board) or checkRow(board) or checkTie(board):
        break
    switchPlayer()
    computer(board)
    checkWin()
    checkTie(board)
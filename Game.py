import random
import os
import math

class Game:
    def __init__(self):
        self.board = ["-"for i in range(16)]
        #self.board = ['X', '-', '-', 'O', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
        #self.winner = False
        self.numberMoves = 0
        self.turn = ""
        self.play()

    def play(self):
        while(True):
            while(True):
                self.printBoard()
                self.switchPlayer()

                self.insertPiece()

                if self.isFull():
                    self.printBoard()
                    print("EMPATE, el tablero está lleno")
                    break

                if self.verifyWinner():
                    self.printBoard()
                    print(f"{self.turn} ha ganado")
                    break
                    #self.winner = True

            if not self.playAgain():
                break
    
    #def printBoard(self):

    def printBoard(self):
        print("Tablero:")
        for i in range(4):
            for j in range(4):
                cell = self.board[i * 4 + j]
                if j < 3:
                    print(f"{cell} |", end=" ")
                else:
                    print(cell, end=" ")
            print()  # Nueva línea después de cada fila
            if i < 3:
                print("─" *14)  # Línea divisoria entre filas
        print()  # Línea en blanco para separar el tablero


    def verifyWinner(self):
            firstcell= 0
            secondCell = 4
            thirdCell = 5

            while(True):
                if thirdCell > 15:
                    break
                for i in range(3):
                    if (self.board[firstcell] == self.board[secondCell] and
                       self.board[secondCell] == self.board[thirdCell] and
                       self.board[firstcell] != "-"
                       ):
                        return self.board[firstcell]
                    firstcell+=1
                    secondCell+=1
                    thirdCell+=1
                
                firstcell+=1
                secondCell+=1
                thirdCell+=1
            
            return False

    def isFull(self):

        for i in range(16):
            if self.board[i]== "-":
                return False
        #self.printBoard()
        #print("EMPATE, el tablero está lleno")
        return True


    def playAgain(self):
        play = input("Escribe R para reiniciar el juego, de lo contrario ingresa cualquier caracter para salir")

        if play == "R" or play == "r":
            self.board = ["-"for i in range(16)]
            #self.winner = False
            self.turn = ""
            os.system('cls')
            return True
        else:
            print("Juego Finalizado")
            return False



    def switchPlayer(self):
        if self.turn == "" or self.turn == "AI":
            self.turn = "player"
            print("Turno del jugador")
            
        else:
            self.turn = "AI"
            print("Turno de la maquina")



    def insertPiece(self):
        piece =  self.requestMove()

        if self.turn == "player":
           self.board[piece] = "X"
           
        else:
           self.board[piece] = "O"
           

    def requestMove(self):
        if self.turn == "player":

            while(True):
                try:
                    piece = int(input("Selecciona la casilla:"))
                    if (0 <= piece <16 and self.board[piece]== "-"):
                        break
                    else:
                        print("\nPosicion invalida. Ingresala nuevamente\n")
                except ValueError:
                    print("Caracter invalido")

        else:
            #supongo que aqui iria el min max para que escoja la posicion
            piece = self.bestMove(self.board,"O")

        return piece
    
    def minimax(self,board,alpha,beta, maximizing,):
        if self.verifyWinner() == "O":
            return 1
        elif self.verifyWinner() == "X":
            return -1
        elif self.isFull():
            return 0

        
        if maximizing:
            bestScore = -math.inf
            for i in range(16):
                if board[i] == "-":
                    board[i] = "O"
                    score = self.minimax(board,alpha,beta,False)
                    board[i] = "-"
                    bestScore = max(bestScore,score)

                    alpha = max(alpha,bestScore)
                    if (alpha >= beta):
                        print("PODA ALFA")
                        break #alpha-beta-pruning
            return bestScore
        else:
            bestScore = math.inf
            for i in range(16):
                if board[i] == "-":
                    board[i] = "X"
                    score = self.minimax(board,alpha,beta,True)
                    board[i] = "-"
                    bestScore = min(bestScore,score)

                    beta = min(beta,bestScore)
                    if (alpha >= beta):
                        print("PODA BETA")
                        break #alpha-beta-pruning
            return bestScore


    def bestMove(self,board,AI):
        bestScore = -math.inf
        
        for i in range(16):
            if board[i] == "-":
                board[i]= "O"

                score = self.minimax(board,-math.inf,math.inf,False)
                board[i] = "-"
                print("Score es: ",score)
                if (score > bestScore): 
                    bestScore = score
                    move = i
        
        print("Score fuera fue:",score)
        print("BestScore fuera fue:",score)
        
        print("Aqui retorno move",move)
        return move


            
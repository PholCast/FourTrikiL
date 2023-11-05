import random
class Game:
    def __init__(self):
        self.board = ["-"for i in range(16)]
        #self.winner = False
        self.turn = ""
        self.play()

    def play(self):
        while(True):
            while(True):
                self.printBoard()
                self.switchPlayer()

                self.insertPiece()

                if self.isFull():
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
                        return True
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
        self.printBoard()
        print("EMPATE, el tablero está lleno")
        return True


    def playAgain(self):
        play = input("Escribe R para reiniciar el juego, de lo contrario ingresa cualquier caracter para salir")

        if play == "R" or play == "r":
            self.board = ["-"for i in range(16)]
            #self.winner = False
            self.turn = ""
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
                piece = int(input("Selecciona la casilla:"))
                if (0 <= piece <16 and self.board[piece]== "-"):
                    break
                else:
                    print("\nPosicion invalida. Ingresala nuevamente\n")

        else:
            #supongo que aqui iria el min max para que escoja la posicion
            while(True):
                piece = random.randint(0,15)
                
                if self.board[piece]== "-":
                    break
                else:
                    pass

        return piece


            
import random
class Game:
    def __init__(self):
        self.board = ["-"for i in range(16)]
        #self.winner = False
        self.turn = ""

    def play(self):
        while(True):
            while(True):
                self.switchPlayer()

                self.insertPiece()

                if self.isFull():
                    break

                if self.verifyWinner():
                    break
                    #self.winner = True

            if not self.playAgain():
                break


    def verifyWinner(self):
        pass
        #p1 = 

    def isFull(self):

        for i in range(16):
            if self.board[i]== "-":
                return False
        
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
        listMove =  self.requestMove()

        if self.turn == "player":
           self.board[listMove[0]][listMove[1]] = "X"
           
        else:
           self.board[listMove[0]][listMove[1]] = "O"
           

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


            
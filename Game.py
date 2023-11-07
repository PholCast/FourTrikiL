import random
class Game:
    def __init__(self):
        self.board = ["-"for i in range(16)]
        #self.board = ["X", "-", "-", "-", "-", "O", "-", "-", "-", "X", "-", "O", "O", "-", "-", "X"]
        #self.winner = False
        self.turn = ""
        self.first = True
        self.play()

    def play(self):
        while(True):
            while(True):
                self.printBoard()
                self.switchPlayer()

                self.insertPiece()

                if self.verifyWinner():
                    self.printBoard()
                    print(f"{self.turn} ha ganado")
                    break
                if self.isFull():
                    self.printBoard()
                    print("EMPATE, el tablero está lleno")
                    break

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
            
            return

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
            self.first = True
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
            while True:
                try:
                    piece = int(input("Selecciona la casilla: "))
                    if 0 <= piece < 16 and self.board[piece] == "-":
                        return piece  # Devuelve el número de la casilla seleccionada por el jugador humano
                    else:
                        print("\nPosición inválida. Ingrésala nuevamente\n")
                except:
                    print("Entrada invalida")
        else:
            bestMove = -1
            bestValue = -float('inf')
            for i in range(16):
                if self.board[i] == "-":
                    self.board[i] = "O"  # Simula el movimiento del jugador AI
                    moveValue = self.minimax(False)
                    self.board[i] = "-"  # Deshacer el movimiento
                    if moveValue > bestValue:
                        bestValue = moveValue
                        bestMove = i
            self.first = False
            return bestMove  # Devuelve el número de la casilla seleccionada por la IA  # Devuelve el número de la casilla seleccionada por la IA
            """bestMove = -1
            bestValue = -float('inf')
            for i in range(16):
                if self.board[i] == "-":
                    self.board[i] = "O"  # Simula el movimiento del jugador AI
                    moveValue = self.minimax(False)
                    self.board[i] = "-"  # Deshacer el movimiento
                    if moveValue > bestValue:
                        bestValue = moveValue
                        bestMove = i
            return bestMove"""  # Devuelve el número de la casilla seleccionada por la IA

        #supongo que aqui iria el min max para que escoja la posicion
        """
        while(True):
            piece = random.randint(0,15)
            
            if self.board[piece]== "-":
                break
            else:
                pass
        """
        
    def minimax(self, maximizingPlayer, depth = 10, alpha = -float('inf'), beta = float('inf')):
        
        if self.first and depth == 0:
            return self.StaticEvaluation()

        result = self.verifyWinner()
        if result == "O":
            return 1
        if result == "X":
            return -1
        
        if self.isFull():
            return 0  # Empate

        if maximizingPlayer:
            maxEval = -float('inf')
            for i in range(16):
                if self.board[i] == "-":
                    self.board[i] = "O"  # Simula el movimiento del jugador AI
                    eval = self.minimax(False, depth - 1, alpha, beta)
                    self.board[i] = "-"  # Deshacer el movimiento
                    maxEval = max(maxEval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
            return maxEval
        else:
            minEval = float('inf')
            for i in range(16):
                if self.board[i] == "-":
                    self.board[i] = "X"  # Simula el movimiento del jugador humano
                    eval = self.minimax(True, depth - 1, alpha, beta)
                    self.board[i] = "-"  # Deshacer el movimiento
                    minEval = min(minEval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
            return minEval

    def StaticEvaluation(self):
        ListBadMoves = [3, 7, 11, 12, 13, 14, 15] #🤮
        index = self.board.index("O")
        
        if index in ListBadMoves:
            return 0
        else:
            return 1
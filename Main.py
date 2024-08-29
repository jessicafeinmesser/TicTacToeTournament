class Player:

    def __init__(self, name):
        self.name = name
        self.gamesPlayed, self.wins, self.losses, self.draws = 0, 0, 0, 0

    def __str__(self):
        s = "{}"
        return s.format(self.name)

    '''def addWin(self):
       self.wins += 1

    def addLoss(self):
        self.losses += 1

    def addDraw(self):
        self.draws += 1

    def addGamePlayed(self):
        self.gamesPlayed += 1'''

    def calcWinPercentage(self):
        if self.gamesPlayed == 0 or self.wins + self.draws + self.losses == 0:
            return 0
        else:
            winPercentage = 100 * (self.wins / (self.wins + self.draws + self.losses))
            round(winPercentage, 2)
            return winPercentage

    def resetStatistics(self):
        self.wins, self.losses, self.draws = 0, 0, 0
        return self.wins, self.losses, self.draws

class TicTacToe:

    def __init__(self):
        self.board = type(list)
        self.winner = False
        self.playerList = []
        self.size = 3

    def displayMenu(self):
        print(" \nWelcome to Tic Tac Toe! \n")
        print("""Menu 
------------------------
1. Play New Game
2. Change Board Size
3. Add New Player 
4. Display Leaderboard
5. Reset Player Statistics 
6. Instructions
0. Exit Program""")

    def isNameInList(self, player):
        nameInList = False
        for person in self.playerList:
             if player.name == person.name:
                nameInList = True
        return nameInList

    def updateLeaderboard(self,player1,player2):
        for person1 in self.playerList:
           if player1.name == person1.name:
               person1.wins += player1.wins
               person1.losses += player1.losses
               person1.draws += player1.draws
               person1.gamesPlayed += player1.gamesPlayed
        for person in self.playerList:
           if player2.name == person.name:
               person.wins += player2.wins
               person.losses += player2.losses
               person.draws += player2.draws
               person.gamesPlayed += player2.gamesPlayed
        return self.playerList

    def displayLeaderboard(self):
        self.playerList.sort(key=Player.calcWinPercentage, reverse=True)
        for player in self.playerList:
            print(format("Name: ", '<10s'), format(player.name, '<10s'), format("Wins/Losses/Draws: ", '<10s'),
                  player.wins, player.losses, player.draws, format("Win Percentage: ", '<15s'),
                  round(player.calcWinPercentage(),2))

    def RunProgram(self):
        choice = 1
        while choice >= 1:
            self.displayMenu()
            choice = int(input("Please enter your selection: "))
            while choice < 0 or choice > 6:
                choice = int(input("Invalid choice. Enter again: "))
            if choice == 2:
                self.size = int(input("Enter new board size between 3 and 6 (board will be n x n): "))
                while self.size < 3 or self.size > 6:
                    self.size = int(input("Sorry, size must be between 3 and 6: "))
                self.initializeBoard(self.size)
            elif choice == 1:
                player1name = input("Enter player 1's name: ").strip().capitalize()
                player1name = Player(player1name)
                player2name = input("Enter player 2's name: ").strip().capitalize()
                player2name = Player(player2name)
                if self.isNameInList(player1name) == False:
                    print("\n Sorry, Player 1 is not in player list.\n Make sure to add player in menu (Option 3).")
                elif self.isNameInList(player2name) == False:
                    print("\n Sorry, Player 2 is not in the player list.\n Make sure to add player in menu (Option 3).")
                else:
                    self.playGame(player1name,player2name)
                    self.updateLeaderboard(player1name, player2name)
            elif choice == 3:
                newPlayer = input("Enter player's name: ").strip().capitalize()
                newPlayer = Player(newPlayer)
                if len(self.playerList) == 0:
                    self.playerList.append(newPlayer)

                if not self.isNameInList(newPlayer):
                    self.playerList.append(newPlayer)
            elif choice == 4:
                self.displayLeaderboard()
            elif choice == 5:
                for player in self.playerList:
                    player.resetStatistics()
            elif choice == 6:
                print("""\nTic Tac Toe Instructions
-------------------------------------------------------------
Enter coordinates for column then row, separated by a space.
The object of the game is to get 3 (or more, depending on 
the board size) of your markers in a row- 
either horizontally, vertically, or diagonally.
Good luck and enjoy!""")

    def initializeBoard(self, size):
        self.boardSize = size
        self.board = []
        for i in range(size):
            self.board.append([])
            for j in range(size):
                self.board[i].append(" ")
        return list(self.board)

    def displayBoard(self):
        for num in range(1, self.boardSize + 1):
            print("    ", num, end="    ")
        print()
        print(" ", "----------" * self.boardSize)
        side = 1
        for row in self.board:
            print(side)
            side += 1
            for col in row:
                print("    ", col, "  |", end='')
            print()
            print(" ", "----------" * self.boardSize)

    def playTurn(self, player, marker):
        def validateTurn():
            try:
                print("Enter coordinates for column then row, separated by a space.")
                coordinates = (input("Enter your move: ")).split()
                col, row = coordinates
                row = int(row) - 1
                col = int(col) - 1
                if row > (self.boardSize - 1) or col > (self.boardSize - 1) or row < 0 or col < 0:
                    coordinates = False
                    print("Out of bounds.")
                elif self.board[row][col] != " ":
                    coordinates = False
                    print("Spot Taken.")
                if coordinates == False:
                    validateTurn()
                else:
                    self.board[row][col] = marker
                    self.displayBoard()
            except ValueError:
                print("Input entered incorrectly. Try again.")
                validateTurn()

        validateTurn()

    def playGame(self, player1, player2):
        player1.wins, player2.wins, player1.losses, player2.losses, player1.gamesPlayed, player2.gamesPlayed,\
        player1.draws, player2.draws = 0,0,0,0,0,0,0,0
        playAgain = "y"
        while playAgain == "y":
            self.initializeBoard(self.size)
            self.displayBoard()
            self.winner = False
            moves = 0
            print("Time to play! ", player1, "vs.", player2)
            while moves < (self.boardSize ** 2):
                print(player1, ", it is your turn!")
                self.playTurn(player1, "X")
                self.checkForWin()
                if self.winner == True:
                    print("Congratulations,", player1, "won!")
                    player1.wins += 1
                    player2.losses +=1
                    player1.gamesPlayed +=1
                    player2.gamesPlayed +=1
                    break
                moves += 1
                if moves == (self.boardSize ** 2):
                    print("Looks like we have a tie! Good job.")
                    player1.draws +=1
                    player2.draws +=1
                    player1.gamesPlayed +=1
                    player2.gamesPlayed +=1
                    break
                print(player2, ", it is your turn!")
                self.playTurn(player2, "O")
                self.checkForWin()
                if self.winner == True:
                    print("Congratulations,", player2, "won!")
                    player2.wins += 1
                    player1.losses +=1
                    player1.gamesPlayed +=1
                    player2.gamesPlayed +=1
                    break
                moves += 1
                if moves == (self.boardSize ** 2):
                    print("Looks like we have a tie! Good job.")
                    player1.draws +=1
                    player2.draws +=1
                    player1.gamesPlayed +=1
                    player2.gamesPlayed +=1
                    break
            playAgain = input("To play again, enter 'y': ").lower()
        '''if playAgain.lower() == "y":
            self.playGame(player1, player2)'''

    def checkForWin(self):
        self.winner = False

        def checkForWin_Horiz():
            self.winner = False
            for row in self.board:
                if row[0] != " ":
                    if all(elem == row[0] for elem in row):
                        self.winner = True
            return self.winner

        def checkForWin_Diag1():
            if self.board[0][0] != " ":
                for i in range(1, self.boardSize):
                    if self.board[i][i] == self.board[0][0]:
                        cont = True
                    else:
                        cont = False
                        break
                if cont == True:
                    self.winner = True  # Diagonal Left to Right Down Win
                else:
                    self.winner = False
                return self.winner

        def checkForWin_Diag2():
            if self.board[0][self.boardSize - 1] != " ":
                for i in range(1, self.boardSize):
                    if self.board[i][self.boardSize - 1 - i] == self.board[0][self.boardSize - 1]:
                        cont = True
                    else:
                        cont = False
                        break
                if cont == True:
                    self.winner = True  # Diagonal Right to Left Down Win
                else:
                    self.winner = False
                return self.winner

        def checkForWin_Vert():
            self.winner = False
            for i in range(self.boardSize):
                good = 0
                j = 0
                while j < self.boardSize:
                    if self.board[j][i] != " " and (self.board[j][i] == self.board[0][i]):
                        good += 1
                    j += 1
                if good == self.boardSize:
                    self.winner = True
                    return self.winner
            return self.winner

        checkForWin_Horiz()
        if self.winner == True:
            return
        checkForWin_Diag1()
        if self.winner == True:
            return
        checkForWin_Diag2()
        if self.winner == True:
            return
        checkForWin_Vert()
        if self.winner == True:
            return

game = TicTacToe()
game.RunProgram()

import time, random, os
os.system("cls")

class TicTacToe():
    def __init__(self, p1, p2):
        self.grid = [[" "]*3 for i in range(3)]
        self.player1, self.player2 = p1, p2

    def clear_screen(self):
        os.system("cls")

    def print_board(self):
        print("\n    1   2   3\n    ---------",sep='')
        for i in range(3):
            print(i+1,"  ", end="")
            for j in range(3):
                print(self.grid[i][j], end="")
                if j != 2:
                    print(" | ", end="")
            print()
            if i != 2:
                print("    ---------")

    def make_move(self, symbol):
        while True:
            row = input("Enter row [1 - 3]: ")
            col = input("Enter column [1 - 3]: ")
            if row.lower() in ["cls", "clear"] or col.lower() in ["cls", "clear"]:
                self.clear_screen()
                return 0
            row, col = int(row), int(col)
            if row not in [1,2,3] or col not in [1,2,3]:
                print("\nInvalid input. Try again.")
                continue
            if self.grid[row-1][col-1]==" ":
                self.grid[row-1][col-1] = symbol
                return 1
            else:
                print("\nGridspace (",row,", ",col,") is already taken. Try again.", sep='')
                
    def has_winner(self):
        for i in range(3):
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] != " ":
                return self.grid[i][0]
            elif self.grid[0][i] == self.grid[1][i] == self.grid[2][i] != " ":
                return self.grid[0][i]
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != " ":
            return self.grid[0][0]
        elif self.grid[0][2] == self.grid[1][1] == self.grid[2][0] != " ":
            return self.grid[0][2]
        return None

    def play_game(self):
        symbol = 'X'
        print("\nDeciding who goes first...")
        time.sleep(1.5)
        names = [self.player1.title(), self.player2.title()]
        turn = random.choice(names)
        print("\n",turn," has won the toss", sep='')
        while True:
            self.clear_screen()
            self.print_board()
            print("\n",turn,"'s turn:", sep='')
            move = self.make_move(symbol)
            if move==0:
                break
            winner = self.has_winner()
            if winner:
                self.clear_screen()
                self.print_board()
                print("\nCongratulations,", turn,"has won!")
                break
            game_is_draw = True
            for row in self.grid:
                if " " in row:
                    game_is_draw = False
                    break
            if game_is_draw:
                self.clear_screen()
                self.print_board()
                print("\nThe game is a draw.")
                break
            else:
                symbol = "O" if symbol=="X" else "X"
                turn = self.player2.title() if turn==self.player1.title() else self.player1.title()


print("\t"*4,"Welcome to World Championship Tic-Tac-Toe\n\nRULES for the game: \
\n\n1. Player 1 is 'X', Player 2 is 'O'.\n2. Enter row and column numbers (1 - 3) in your turn to place your \
symbols in corresponding gridspace.\n3. First player to get three of their symbols in a row \
(horizontally, vertically, or diagonally) wins the game.\n4. If all 9 gridspaces are filled and \
no player has won, the game ends in a draw.\n5. No take backs allowed.\n6. Type 'cls' or 'clear' \
clear the screen.\n7. Arbitrator is GOD.")

p1 = input("\nEnter name for player 1: ")
p2 = input("Enter name for player 2: ")

obj = TicTacToe(p1, p2)
obj.play_game()
print()
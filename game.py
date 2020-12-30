from player import HumanPlayer,RandomComputerPlayer ,GeniusComputerPlayer
import time
import os

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # we will use a single list to represent 3x3 board
        self.current_winner = None


    def print_board(self):
        #this is just getting the rows 
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('')
            print(' | '+ ' | '.join(row) +' | ')



    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (tells us what number corresponding to what box)
        number_board = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| '+ ' | '.join(row) +' |')



    def available_moves(self):
        return [i for i,spot in enumerate(self.board) if spot == ' ']
        # moves = []   // we can wrap all this in comprehension loop
        # for (i,spot) in enumerate(self.board):  
        #     if spot = ' ':
        #         moves.append(i)
        # return moves



    def empty_squares(self):
        return ' ' in self.board



    ## return the number of empty squares
    def num_empty_squares(self):
        ##return len(self.available_moves()) another way is
        return self.board.count(' ')
    


    def make_move(self,square,letter):
        #if valid move , then make a move assign square to letter
        #then return True , if Invalid move return False
        if self.board[square] == ' ':
            self.board[square] = letter

            if self.winner(square,letter):
                self.current_winner = letter

            return True

        return False
    


    def winner(self,square,letter):
        ##check the rows for win
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]

        if all([spot == letter for spot in row]):
            return True

        ## check columns for win
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]

        if all([spot == letter for spot in column ]):
            return True

        ## check diagonals 
        if square % 2 == 0: ## if square is an even number(0,2,4,6,8),all possible move to win in diagonals

            diagonal1 = [self.board[i] for i in [0,4,8]]

            if all([spot == letter for spot in diagonal1]):
                return True

            diagonal2 = [self.board[i] for i in [2,4,6]]

            if all([spot == letter for spot in diagonal2]):

                return True
        ## if all fail then no winner
        return False





def play(game,x_player,o_player,print_game=True): # print_game is used when a human play the game (set False if computer vs computer) 
    
    #returns the winner of the game!(the letter) , or None for tie

   
    ## if print_game is set to True print the valid numbers to move
    if print_game:
        game.print_board_nums()

    letter = 'X' #starting letter
    #iterate while the game still have empty squares
    #(we don't have to worry about winners because we will return the player who breaks the loop)
    while game.empty_squares():
        #lets get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        ## lets define a function to make a move
        if game.make_move(square,letter):
            if print_game:
                print(letter + ' makes a move in square {}'.format(square))
                game.print_board()
                print('') # empty new line
            if game.current_winner:
                if print_game:
                    print(letter + ' Wins!!!!')
                return letter



            # after the move , alternate letters
            letter = 'O' if letter == 'X' else 'X' #switch players

        ## little break between move to make things bit easier to read
        if print_game:
            time.sleep(0.7)
    if print_game:
        print('It\'s a Tie')

if __name__ == "__main__":
    ## incase you want to see computer vs computer assing print_game to False and uncomment
    # x_wins = 0
    # o_wins = 0
    # ties = 0
    # count = 0
    # for _ in range(100):
        # count+=1
        os.system('cls' if os.name == 'nt' else 'clear')
        x_player = HumanPlayer('X') ## change to computer player
        o_player = GeniusComputerPlayer('O')
        t = TicTacToe()
        result = play(t,x_player,o_player,print_game=True) # change False for computer vs computer
        # if result == 'X':
        #     x_wins += 1
        # elif result == 'O':
        #     o_wins += 1
        # else:
        #     ties += 1
    #   print(count)    
    # print('After 1000 iterations, we have {} X wins, {} o_wins and {} ties'.format(x_wins,o_wins,ties))
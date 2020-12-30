from player import HumanPlayer,RandomComputerPlayer ,GeniusComputerPlayer
import time
import os

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # 3x3 board
        self.current_winner = None


    def print_board(self):
        
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('')
            print(' | '+ ' | '.join(row) +' | ')



    @staticmethod
    def print_board_nums():
        
        number_board = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| '+ ' | '.join(row) +' |')



    def available_moves(self):
        return [i for i,spot in enumerate(self.board) if spot == ' ']
     

    def empty_squares(self):
        return ' ' in self.board



    ## return the number of empty squares
    def num_empty_squares(self):
        return self.board.count(' ')
    


    def make_move(self,square,letter):
        #assign square to letter
        #return True , if Invalid  return False
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
        if square % 2 == 0: ##(0,2,4,6,8)

            diagonal1 = [self.board[i] for i in [0,4,8]]

            if all([spot == letter for spot in diagonal1]):
                return True

            diagonal2 = [self.board[i] for i in [2,4,6]]

            if all([spot == letter for spot in diagonal2]):

                return True
       
        return False





def play(game,x_player,o_player,print_game=True): 
    
    
    if print_game:
        game.print_board_nums()

    letter = 'X' #starting letter
    
    while game.empty_squares():
        
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        if game.make_move(square,letter):
            if print_game:
                print(letter + ' makes a move in square {}'.format(square))
                game.print_board()
                print('') # newline
            if game.current_winner:
                if print_game:
                    print(letter + ' Wins!!!!')
                return letter



            #switch players
            letter = 'O' if letter == 'X' else 'X' 

       
        if print_game:
            time.sleep(0.7)
    if print_game:
        print('It\'s a Tie')

if __name__ == "__main__":
    ## if computer vs computer assing print_game to False and uncomment
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
    # print('1000 times, we have {} X wins, {} O wins and {} Ties'.format(x_wins,o_wins,ties))

import math
import random

class Player:

    def __init__(self,letter):
        # letter x or o
        self.letter = letter
    

    ## we want all players to get their next move in given game
    def get_move(self, game):
        pass




class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)


    def get_move(self,game):
        square = random.choice(game.available_moves())
        return square





class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    

    def get_move(self,game):
        valid_square = False
        val = None

        while not valid_square:
            square = input(self.letter + "'s turn, Input a move (0-8):\n>> ")
            #we're are trying to check if it's a correct values 
            #by trying to cast it to an intergier , if it's not then we raise valueError 
            #if spot if not available then we also raise an Error

            try:
                val = int(square)

                if val not in game.available_moves():
                    raise ValueError

                valid_square = True # if success then change to True (exit the loop)

            except ValueError:

                print('Invalid square, Try again')

        return val   

class GeniusComputerPlayer(Player):
    def __init__ (self,letter):
        super().__init__(letter)
    
    def get_move(self,game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            ## get the square based on minimax algorithms
            square = self.minimax(game,self.letter)['position']
        return square

    def minimax(self, state,player):
        max_player = self.letter ## youself
        other_player = 'O' if player == 'X' else 'X' ## other player , opposite whatever player you are

        ##check if previous move is a winner
        if state.current_winner == other_player:
            ## we return the position AND score because we want to keep track of the score for minimax to word
            return {'position':None,
                    'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)
            }
        elif not state.empty_squares(): ## no empty squares
            return {'position':None , 'score':0}

        #initialize some dictionaries
        if player == max_player:
            best = {'position':None,'score': -math.inf} ## each score should maximize (be larger)
        else:
            best = {'position':None,'score': math.inf} ## each score should be minimize  
        
        for possible_move in state.available_moves():

            # step 1 : make a move , try that spot

            state.make_move(possible_move,player)

            # step 2 : recurse using minimax to simulate a game after making that move

            sim_score = self.minimax(state,other_player) ## we alternate players

            # step 3 : undo the move

            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            # step 4 : update the dictionary if possible

            if player == max_player: ## we are trying to maximize the max_player

                if sim_score['score'] > best['score']:
                    best = sim_score ## replace best

            else: ## but minimize the other player

                if sim_score['score'] < best['score']:
                    best =  sim_score
        return best







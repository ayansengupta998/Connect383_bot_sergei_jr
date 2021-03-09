import random
import math


BOT_NAME = "Sergie_jr"


class RandomAgent:
    """Agent that picks a random available move.  You should be able to beat it."""
    def __init__(self, sd=None):
        if sd is None:
            self.st = None
        else:
            random.seed(sd)
            self.st = random.getstate()

    def get_move(self, state):
        if self.st is not None:
            random.setstate(self.st)
        return random.choice(state.successors())


class HumanAgent:
    """Prompts user to supply a valid move."""
    def get_move(self, state, depth=None):
        move__state = dict(state.successors())
        prompt = "Kindly enter your move {}: ".format(sorted(move__state.keys()))
        move = None
        while move not in move__state:
            try:
                move = int(input(prompt))
            except ValueError:
                continue
        return move, move__state[move]


class MinimaxAgent:
    """Artificially intelligent agent that uses minimax to optimally select the best move."""

    def get_move(self, state):
        """Select the best available move, based on minimax value."""
        nextp = state.next_player()
        best_util = -math.inf if nextp == 1 else math.inf
        best_move = None
        best_state = None

        for move, state in state.successors():
            # print(state.successors(),"boiiii")
            util = self.minimax(state)
            if ((nextp == 1) and (util > best_util)) or ((nextp == -1) and (util < best_util)):
                best_util, best_move, best_state = util, move, state
        return best_move, best_state
    
    #function that bubbles up the value from the terminal nodes
    #function also determines if sergei_jr is player1 or player2
   


    def minimax(self, state):
        ply = state.next_player()#gives us what player goes next 
       #if terminal node return util val right away 
        if(state.is_full()==True):
            return state.utility()
        if (ply == 1):
            bestval = -math.inf 
            for move, state_cur in state.successors(): #generates all legal successors 
                bubble = self.minimax(state_cur) #recursive call to get utility of the state
                bestval = max(bestval,bubble)#compare best value found so far and update if new util val is better
        else:
            bestval = math.inf
            for move, state_cur in state.successors():
                bubble = self.minimax(state_cur)
                bestval = min(bestval,bubble)
        return bestval
           
class MinimaxHeuristicAgent(MinimaxAgent):
    """Artificially intelligent agent that uses depth-limited minimax to select the best move."""

    def __init__(self, depth_limit):
        self.depth_limit = depth_limit

    def minimax(self, state):
        """Determine the heuristically estimated minimax utility value of the given state.

        The depth data member (set in the constructor) determines the maximum depth of the game 
        tree that gets explored before estimating the state utilities using the evaluation() 
        function.  If depth is 0, no traversal is performed, and minimax returns the results of 
        a call to evaluation().  If depth is None, the entire game tree is traversed.

        Args:
            state: a connect383.GameState object representing the current board

        Returns: the minimax utility value of the state
        """
        if state.is_full():
            return self.evaluation(state)

        if self.depth_limit == 0:
            return self.evaluation(state)
        
        bestVal = None
        if state.next_player() == 1:
            bestVal = -(math.inf)
            for move, state in state.successors():
                if self.depth_limit == None:
                    value = self.minimax(state)
                else:
                    value = self.minimax(state)
                bestVal = max(bestVal, value)
        else:
            bestVal = math.inf
            for move, state in state.successors():
                if self.depth_limit == None:
                    value = self.minimax(state)
                else:
                    value = self.minimax(state)
                bestVal = min(bestVal, value)
        return bestVal 

    def evaluation(self, state):
        """Estimate the utility value of the game state based on features.

        N.B.: This method must run in O(1) time!

        Args:
            state: a connect383.GameState object representing the current board

        Returns: a heusristic estimate of the utility value of the state
        """
        flag = 0 #initialzing a flag to keep track of score
        for x in state.get_rows()+state.get_cols()+state.get_diags(): #get all the rows,cols and diagonals and iterate over them
            flag = flag + self.true_eval(x)
        return flag
    def true_eval(self,run): #function that calculates the evaluation function
        """Instead of adding score when the streak length is 3 or more we look at any instance where 2 similar symbol (X or 0)"""
        rets = []  
        prev = run[0]
        curr_len = 1
        p1_score = 0
        p2_score = 0
        for curr in run[1:]:
            if curr == prev:
                curr_len += 1
            else:
                if curr_len > 2:
                    rets.append((prev, curr_len))
                    if prev == 1:
                        p1_score += curr_len**2
                    elif prev == -1:
                        p2_score += curr_len**2
                prev = curr
                curr_len = 1
        if curr_len > 2:
            rets.append((prev, curr_len))
            if prev == 1:
                p1_score += curr_len**2
            elif prev == -1:
                p2_score += curr_len**2
        return p1_score - p2_score

     

class MinimaxHeuristicPruneAgent(MinimaxHeuristicAgent):
    """Smarter computer agent that uses minimax with alpha-beta pruning to select the best move."""
    

    def minimax(self, state, depth, alpha, beta):
        ply = state.next_player()#gives us what player goes next 
       #if terminal node return util val right away 
        if(state.is_full()==True or depth == 0):
            return state.utility()
        if (ply == 1):
            bestval = -math.inf 
            for move, state_cur in state.successors(): #generates all legal successors 
                bubble = self.minimax(state_cur, depth-1, alpha, beta) #recursive call to get utility of the state
                bestval = max(bestval,bubble)#compare best value found so far and update if new util val is better
                alpha = max(alpha, bestval)
                if beta <= alpha:
                    break
        else:
            bestval = math.inf
            for move, state_cur in state.successors():
                bubble = self.minimax(state_cur, depth-1, alpha, beta)
                bestval = min(bestval,bubble)
                beta = min(beta, bestval)
                if beta <=alpha:
                    break
        return bestval



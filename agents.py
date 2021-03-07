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
            util = self.minimax(state)
            if ((nextp == 1) and (util > best_util)) or ((nextp == -1) and (util < best_util)):
                best_util, best_move, best_state = util, move, state
        return best_move, best_state

    def bubble_up(self, parents, popped, state):
        # print("Test", state, type(state))
        utility = popped[0].utility()
        print("Utility", utility)
        minimax = popped[1]
        print(minimax,"mini")
        current_child = popped[0]
        # print("current_child", current_child, type(current_child))
        parents[current_child] = (parents[current_child][0],utility)
        # print("Testing Testing", type(parents[current_child][0]))
        current_parent= parents[popped[0]][0]
        # print("Parent", current_parent[0], type(current_parent[0])
        while(current_child != state):
            if minimax == 1:
                #update parent with min of the values
                if parents[current_parent][1] == 0 or parents[current_parent][1] == 123456789:
                    parents[current_parent] = (parents[current_parent][0], utility)
                else:
                    parents[current_parent] = (parents[current_parent][0], min(parents[current_parent][1],utility))
            else:
                #update parent with max of the values
                if parents[current_parent][1] == 0 or parents[current_parent][1] == 123456789:
                    parents[current_parent] = (parents[current_parent][0], utility)
                else:
                    parents[current_parent] = (parents[current_parent][0], max(parents[current_parent][1],utility))
            
            utility = parents[current_parent][1]
            minimax =  minimax*-1
            current_child = current_parent
            current_parent = parents[current_child][0]

        return utility
#issue facing is that the states in the dicitonary seem to be behaving erratically. can't seem to find the key stored even though it is in the dict
#mismatch of object types
# The utility function should ideally be returning a non zero value

    def minimax(self, state):
        # print("TESTER", state, type(state))
        stack = []
        visited = dict()
        parents = dict()
        parents[state] = ('',123456789)
        stack.append((state, 1))    
        utility = 0
        while(len(stack) != 0):
            popped = stack.pop(len(stack)-1)
            # print("Popped:", popped[0], type(popped[0]))
            visited[popped[0]] = ""
            if(popped[0].is_full()==True):
                print(popped[0].is_full(),"TESTING")
                utility = self.bubble_up(parents, popped, state)
            else:
                successors = popped[0].successors()
                for succ in successors:
                    # print("BIGGER TEST:", succ, succ[1], type(succ[1]))
                    if succ[1] not in visited:
                        stack.append((succ[1], popped[1]*-1))
                        parents[succ[1]] = (popped[0], 0)
        print("Utility:", utility)
        return utility


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
        #
        # Fill this in!
        #
        return 9  # Change this line!

    def evaluation(self, state):
        """Estimate the utility value of the game state based on features.

        N.B.: This method must run in O(1) time!

        Args:
            state: a connect383.GameState object representing the current board

        Returns: a heusristic estimate of the utility value of the state
        """
        #
        # Fill this in!
        #
        return state.utility() # Change this line!


class MinimaxHeuristicPruneAgent(MinimaxHeuristicAgent):
    """Smarter computer agent that uses minimax with alpha-beta pruning to select the best move."""

    def minimax(self, state):
        """Determine the minimax utility value the given state using alpha-beta pruning.

        The value should be equal to the one determined by MinimaxAgent.minimax(), but the 
        algorithm should do less work.  You can check this by inspecting the value of the class 
        variable GameState.state_count, which keeps track of how many GameState objects have been 
        created over time.  This agent should also respect the depth limit like HeuristicAgent.

        N.B.: When exploring the game tree and expanding nodes, you must consider the child nodes
        in the order that they are returned by GameState.successors().  That is, you cannot prune
        the state reached by moving to column 4 before you've explored the state reached by a move
        to to column 1.

        Args: 
            state: a connect383.GameState object representing the current board

        Returns: the minimax utility value of the state
        """
        #
        # Fill this in!
        #
        return 13  # Change this line!



# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions, GameStateData
import random
import util

from game import Agent


class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """

    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(
            gameState, action) for action in legalMoves]
        # print "---------------------------------"
        bestScore = max(scores)
        bestIndices = [index for index in range(
            len(scores)) if scores[index] == bestScore]
        # Pick randomly among the best
        chosenIndex = random.choice(bestIndices)

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.


        python pacman.py -p ReflexAgent -l testClassic
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [
            ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        if action == "Stop":
            return 0

        nearestGhost = min([manhattanDistance(newPos, ghost.getPosition())
                            for ghost in newGhostStates])  
        if newFood.asList():

            nearestFood = min([manhattanDistance(newPos, food)
                               for food in newFood.asList()])
        else:
            nearestFood = 0

        score = (nearestGhost) / (nearestFood+1)

        return successorGameState.getScore() + score


def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()


class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn='scoreEvaluationFunction', depth='2'):
        self.index = 0  
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)


class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
        # util.raiseNotDefined()
        moves=gameState.getLegalActions(0)
        nextStates=[gameState.generateSuccessor(0,action) for action in moves]
        scores=[self.minimize(0,nextState,1) for nextState in nextStates]
        topScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index]==topScore]
        chosenIndex = random.choice(bestIndices)
        return moves[chosenIndex]

    def maximize(self,currentDepth,gameState):
    	if(self.depth==currentDepth or gameState.isLose() or gameState.isWin()):
    		return self.evaluationFunction(gameState)
    	legalMoves=gameState.getLegalActions(0)
    	resultStates=[gameState.generateSuccessor(0,action) for action in legalMoves]
    	scores=[self.minimize(currentDepth,state,1) for state in resultStates]
    	return max(scores)

    def minimize(self,currentDepth,gameState,ghostIndex):
    	if(self.depth==currentDepth or gameState.isLose() or gameState.isWin()):
    		return self.evaluationFunction(gameState)
    	
    	
    	legalMoves=gameState.getLegalActions(ghostIndex)
    	resultStates=[gameState.generateSuccessor(ghostIndex, action) for action in legalMoves]
    	
    	if (ghostIndex>=gameState.getNumAgents()-1):
    		scores=[self.maximize(currentDepth+1,state) for state in resultStates]
    	else:
    		scores=[self.minimize(currentDepth,state,ghostIndex+1) for state in resultStates]
    	return min(scores)


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        def maximizer(agent, depth, gameState, a, b):
          v = float("-inf")
          for newState in gameState.getLegalActions(agent):
            v = max(v, alphabetaprune(1, depth, gameState.generateSuccessor(agent, newState), a, b))
            if v > b:
              return v
            a = max(a, v)
          return v
        def minimizer(agent, depth, gameState, a, b):
          v = float("inf")
          nextAgent = agent + 1
          if gameState.getNumAgents() == nextAgent:
            nextAgent = 0
          if nextAgent == 0:
            depth += 1
          for newState in gameState.getLegalActions(agent):
            v = min(v, alphabetaprune(nextAgent, depth, gameState.generateSuccessor(agent, newState), a, b))
            if v < a:
              return v
            b = min(b, v)
          return v
        def alphabetaprune(agent, depth, gameState, a, b):
          if gameState.isLose() or gameState.isWin() or depth == self.depth: 
            return self.evaluationFunction(gameState)
          if agent == 0:
            return maximizer(agent, depth, gameState, a, b)
          else: 
            return minimizer(agent, depth, gameState, a, b)
        
        utility = float("-inf")
        action = Directions.WEST
        alpha = float("-inf")
        beta = float("inf")

        for agentState in gameState.getLegalActions(0):
          ghostValue = alphabetaprune(1, 0, gameState.generateSuccessor(0, agentState), alpha, beta)
          if ghostValue > utility or utility == float("-inf"):
            utility = ghostValue
            action = agentState
          if utility > beta:
            return utility
          alpha = max(alpha, utility)

        return action
      

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction
          
          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        #util.raiseNotDefined()
        def expectimax(agent, depth, gameState):
          if gameState.isLose() or gameState.isWin() or depth == self.depth: 
            return self.evaluationFunction(gameState)
          if agent == 0: 
            return max(expectimax(1, depth, gameState.generateSuccessor(agent, newState)) for newState in gameState.getLegalActions(agent))
          else: 
            nextAgent = agent + 1
            if gameState.getNumAgents() == nextAgent:
              nextAgent = 0
            if nextAgent == 0:
              depth += 1
            return sum(expectimax(nextAgent, depth, gameState.generateSuccessor(agent, newState)) for newState in gameState.getLegalActions(agent)) / float(len(gameState.getLegalActions(agent)))
          
        maximum = float("-inf")
        action = Directions.WEST
        for agentState in gameState.getLegalActions(0):
          utility = expectimax(1, 0, gameState.generateSuccessor(0, agentState))
          if utility > maximum or maximum == float("-inf"):
            maximum = utility
            action = agentState
        return action


def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    newPos = currentGameState.getPacmanPosition()
    newFood = currentGameState.getFood()
    newFoodList = newFood.asList()
    min_food_distance = -1
    for food in newFoodList:
      distance = util.manhattanDistance(newPos, food)
      if min_food_distance >= distance or min_food_distance == -1:
        min_food_distance = distance
    distance_to_ghosts = 1
    check_to_ghosts = 0
    for ghostState in currentGameState.getGhostPositions():
      distance = util.manhattanDistance(newPos, ghostState)
      distance_to_ghosts += distance
      if distance <= 1:
        check_to_ghosts += 1
    newBigDot = currentGameState.getCapsules()
    numberOfBigDots = len(newBigDot)

    return currentGameState.getScore() + (1 / float(min_food_distance)) - (1 / float(distance_to_ghosts)) - check_to_ghosts - numberOfBigDots
    


# Abbreviation
better = betterEvaluationFunction

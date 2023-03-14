import random

"""
Finds random a move from the list of valid moves
randint- returns a random integer between the given parameters
it is inclusive of both first and second parameter
"""
pieceScore = {"K": 0, "Q": 10, "R": 5, "B": 3, "N": 3, "p": 1}
CHECKMATE = 1000
STALEMATE = 0

def findRandomMove(validMoves):
    # [] brackets added to access validMoves
   return validMoves[random.randint(0, len(validMoves)-1)]

'''
Get opponent's move, set their maximum score to a very low value, then find the best/ highest value for score by selecting best moves possible.
then check score, if score is greater than ax val, set maximum score = score
'''
def findBestMove(gs, validMoves):
    turnMultiplier = 1 if gs.whiteToMove else -1
    opponentMinMaxScore = CHECKMATE
    bestPlayerMove = None
    random.shuffle(validMoves)
    for playerMove in validMoves:
        gs.makeMove(playerMove)
        opponentsMoves = gs.getValidMoves()
        opponentMaxScore = -CHECKMATE
        for opponentsMove in opponentsMoves:
            gs.makeMove(opponentsMove)
            if gs.checkmate:
                score = -turnMultiplier * CHECKMATE
            elif gs.stalemate:
                score = STALEMATE
            else:
                score = -turnMultiplier * scoreMaterial(gs.board)
            if score > opponentMaxScore:
                opponentMaxScore = score
            gs.undoMove()
        import random

        """
        Finds random a move from the list of valid moves
        randint- returns a random integer between the given parameters
        it is inclusive of both first and second parameter
        """

        def findRandomMove(validMoves):
            # [] brackets added to access validMoves
            return validMoves[random.randint(0, len(validMoves) - 1)]

        def findBestMove():
            return

        if opponentMaxScore < opponentMinMaxScore:
            opponentMinMaxScore = opponentMaxScore
            bestPlayerMove = playerMove
        gs.undoMove()
    return bestPlayerMove

'''
Score the board based on material
For white pieces score is positive, checkmate = 1000
For black pieces score is negative, checkmate = -1000
So basically in MinMax algorithm we start with the worst score then proceed towards the best score.
for black worst score = 1000, best = -1000
for white worst score = -1000, best = 1000
'''
def scoreMaterial(board):
    score = 0
    for row in board:
        for square in row:
            if square[0] == 'w':
                score += pieceScore[square[1]]
            elif square[0] == 'b':
                score -= pieceScore[square[1]]
    return score
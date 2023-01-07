import random

"""
Finds random a move from the list of valid moves
randint- returns a random integer between the given parameters
it is inclusive of both first and second parameter
"""
def findRandomMove(validMoves):
    # [] brackets added to access validMoves
   return validMoves[random.randint(0, len(validMoves)-1)]

def findBestMove():
    return
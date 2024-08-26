from Pieces import *

class Board:
    def __init__(self):
        self.board = [[0 for _ in range(8)] for _ in range(8)] 
        self.init() 
        self.turn = 0
        self.blackCapture = []
        self.whiteCapture = []
        self.checkMate = False

    def init(self):
        self.board[0][0] = Rook((0, 0), 'White')
        self.board[1][0] = Knight((1, 0), 'White')
        self.board[2][0] = Bishop((1, 0), 'White')
        self.board[3][0] = Queen((3, 0), 'White')
        self.board[4][0] = King((4, 0), 'White')
        self.board[5][0] = Bishop((5, 0), 'White')
        self.board[6][0] = Knight((6, 0), 'White')
        self.board[7][0] = Rook((7, 0), 'White')

        self.board[0][7] = Rook((0, 7), 'Black')
        self.board[1][7] = Knight((1, 7), 'Black')
        self.board[2][7] = Bishop((2, 7), 'Black')
        self.board[3][7] = Queen((3, 7), 'Black')
        self.board[4][7] = King((4, 7), 'Black')
        self.board[5][7] = Bishop((5, 7), 'Black')
        self.board[6][7] = Knight((6, 7), 'Black')
        self.board[7][7] = Rook((7, 7), 'Black')

        for col in range(8):
            self.board[col][1] = Pawn((col, 1), 'White')
            self.board[col][6] = Pawn((col, 6), 'Black')

    # White Turn = 0
    # Black Turn = 1
    def nextTurn(self):
        self.turn = 1 - self.turn

    def getTurn(self):
        return self.turn
    
    def getPiece(self, coordinates):
        y = coordinates[1]
        x = coordinates[0]
        piece = self.board[int(x)][int(y)]
        if piece != None:
            return piece

        return None
    
    def getPieceByName(self, name):
        for row in range(8):
            for col in range(8):
                if self.board[row][col].__str__() == name:
                    piece = self.board[row][col]
                    return piece
                
        return None
    
    def updateMove(self, piece, newMove):
        oldPosition = piece.getPosition()
        self.board[oldPosition[0]][oldPosition[1]] = 0
        piece.updateMove(newMove)
        self.board[newMove[0]][newMove[1]] = piece

    def capture(self, piece):
        position = piece.getPosition()
        piece.captured()
        self.board[position[0]][position[1]] = 0

        if piece.color == "White":
            self.blackCapture.append(piece)
        elif piece.color == "Black":
            self.whiteCapture.append(piece)

    def check(self):

        turn = self.getTurn()

        if turn:
            king = self.getPieceByName("King Black")
            color = "Black"
        elif not turn:
            king = self.getPieceByName("King White")
            color = "White"
        else:
            raise ValueError("Invalid turn value!")

        if king is None:
            raise ValueError(f"King not found on the board!")
        
        positionKing = king.getPosition()

        print(positionKing)

        for row in range(8):
            for col in range(8):
                piece = self.board[col][row]
                
                if piece and piece.color != color:
                    if piece.isPossibleMove(self.board, positionKing):
                        return True
                
        return False
    

    def checkmate(self):
        turn = self.getTurn()

        if turn:
            king = self.getPieceByName("King Black")
            color = "Black"
        elif not turn:
            king = self.getPieceByName("King White")
            color = "White"
        else:
            raise ValueError("Invalid turn value!")

        if king is None:
            raise ValueError(f"King not found on the board!")
        
        positionKing = king.getPosition()

        if not self.check():
            return False
        
        for row in range(8):
            for col in range(8):
                piece = self.board[col][row]
                if piece and piece.color == color:
                    possibleMoves = piece.getAllPossibleMoves(piece)
                    for move in possibleMoves:
                        old_position = piece.getPosition()
                        self.updateMove(piece, move)

                        if not self.check():
                            self.updateMove(piece, old_position)
                            return False
                        
                        self.updateMove(piece, old_position)

        self.board.checkMate = True
        return True
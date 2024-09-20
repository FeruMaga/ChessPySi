from copy import deepcopy
from Pieces import *

class Board:
    def __init__(self):
        self.board = [[0 for _ in range(8)] for _ in range(8)] 
        self.turn = 0
        self.blackCapture = []
        self.whiteCapture = []
        self.checkMate = False
        self.init() 

    def init(self):
        self.board[0][0] = Rook((0, 0), 'White')
        self.board[0][1] = Knight((0, 1), 'White')
        self.board[0][2] = Bishop((0, 2), 'White')
        self.board[0][3] = Queen((0, 3), 'White')
        self.board[0][4] = King((0, 4), 'White')
        self.board[0][5] = Bishop((0, 5), 'White')
        self.board[0][6] = Knight((0, 6), 'White')
        self.board[0][7] = Rook((0, 7), 'White')

        self.board[7][0] = Rook((7, 0), 'Black')
        self.board[7][1] = Knight((7, 1), 'Black')
        self.board[7][2] = Bishop((7, 2), 'Black')
        self.board[7][3] = Queen((7, 3), 'Black')
        self.board[7][4] = King((7, 4), 'Black')
        self.board[7][5] = Bishop((7, 5), 'Black')
        self.board[7][6] = Knight((7, 6), 'Black')
        self.board[7][7] = Rook((7, 7), 'Black')

        for col in range(8):
            self.board[1][col] = Pawn((1, col), 'White')
            self.board[6][col] = Pawn((6, col), 'Black')

        # Teste - Checkmate rápido
        self.updateMove(self.board[1][5], (2,5)) # f2 f3
        self.updateMove(self.board[6][4], (4,4)) # e7 e5
        self.updateMove(self.board[1][6], (3,6)) # g2 g4
        self.nextTurn()
        #self.updateMove(self.board[7][3], (3,7)) # d8 h4
        


    # White Turn = 0
    # Black Turn = 1
    def nextTurn(self):
        self.turn = 1 - self.turn

    def getTurn(self):
        return self.turn
    
    def getPiece(self, coordinates):
        piece = self.board[coordinates[0]][coordinates[1]]
        if piece != None:
            return piece

        return 0
    
    def getPieceByName(self, name):
        for row in range(8):
            for col in range(8):
                if self.board[row][col].__str__() == name:
                    piece = self.board[row][col]
                    return piece
                
        return 0
    
    def updateMove(self, piece, newMove):
        oldPosition = piece.getPosition()
        self.board[oldPosition[0]][oldPosition[1]] = 0
        piece.updateMove(newMove)
        self.board[newMove[0]][newMove[1]] = piece

    def capture(self, piece):
        if self.getTurn():
            if piece.color != "White":
                return False
        elif not self.getTurn():
            if piece.color != "Black":
                return False
            
        position = piece.getPosition()
        
        piece.captured()
        if piece.color == "White":
            self.blackCapture.append(piece)
        elif piece.color == "Black":
            self.whiteCapture.append(piece)

        return True

    def kingTurn(self):
        turn = self.getTurn()

        if turn:
            king = self.getPieceByName("King Black")
            color = "Black"
            return king
        elif not turn:
            king = self.getPieceByName("King White")
            color = "White"
            return king
        else:
            raise ValueError("Invalid turn value!")

        if king == 0:
            raise ValueError(f"King not found on the board!")
        

    def check(self):
        king = self.kingTurn()
        kingPosition = king.getPosition()

        print(f"King turno check: {king}")

        for row in range(8):
            for col in range(8):
                piece = self.getPiece((row, col))
                if piece != 0 and piece.color != king.color:
                    if piece.isPossibleMove(self, kingPosition):
                        print(f"Piece {piece} is checking the king {king.color}.")
                        return True
        return False
    

    def checkmate(self):
        king = self.kingTurn()
        kingPosition = king.getPosition()

        print(f"King turno check: {king}")

        if not self.check():
            return False
        
        board_copy = deepcopy(self)

        possible_moves = king.getAllPossibleMoves(self)

        print(f"Piece Moves: {possible_moves}")

        for move in possible_moves:
            board_copy = deepcopy(self)
            board_copy.updateMove(king, move)
            if not board_copy.check():
                return False

        for row in range(8):
            for col in range(8):
                piece = self.getPiece((row, col))

                if piece != 0 and piece.color == king.color:
                    possible_piece_moves = piece.getAllPossibleMoves(self)
                    for move in possible_piece_moves:
                        board_copy = deepcopy(self)
                        board_copy.updateMove(piece, move)
                        
                        if not board_copy.check():
                            return False

        return True
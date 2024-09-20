class Piece(object):
    def __init__(self, position, color):
        self.position = position
        self.color = color

    def __str__(self) -> str:
        return self.color
    
    def getPosition(self):
        return self.position
    
    def updateMove(self, coordinates):
        self.position = coordinates

    def captured(self):
        self.position = 0

    def isPathClear(self, board, start, end):
        startX, startY = start
        endX, endY = end
        if startX == endX:
            stepY = 1 if startY < endY else -1
            for y in range(startY + stepY, endY + stepY, stepY):
                print('y:')
                print(y)
                piece = board.getPiece((startX, y))
                if board.getPiece((startX, y)) != 0:
                    print("Path not clear.")
                    return False
        elif startY == endY:
            stepX = 1 if startX < endX else -1
            for x in range(startX + stepX, endX + stepX, stepX):
                if board.getPiece((x, startY)) != 0:
                    print("Path not clear.")
                    return False
        elif abs(startY - endY) == abs(startX - endX):
            stepX = 1 if startX < endX else -1
            stepY = 1 if startY < endY else -1
            currentX, currentY = startX + stepX, startY + stepY
            while currentX != endX and currentY != endY:
                if board.getPiece((currentX, currentY)) != 0:
                    print("Path not clear.")
                    return False
                currentY += stepY
                currentX += stepX
        else:
            return False

        print("Path clear")
        return True

    def getAllPossibleMoves(self, board):
        possibleMoves = []
        for x in range(8):
            for y in range(8):
                if (x, y) != self.getPosition():
                    if self.isPossibleMove(board,(x, y)):
                        possibleMoves.append((x, y))

        return possibleMoves

class Pawn(Piece):
    def __init__(self, position, color):
        super().__init__(position, color)

    def __str__(self) -> str:
        return 'Pawn ' + super().__str__()

    def isPossibleMove(self, board, positions):
        x, y = self.position
        newX, newY = positions
        if self.isPathClear(board,(x,y), (newX, newY)):
            if self.color == 'White':
                if newY == y and newX == x + 1:
                    return True
                elif newY == y and newX == x + 2 and x == 1:
                    return True
                elif abs(newY - y) == 1 and newX == x + 1 and board.getPiece(positions):
                    return True

            elif self.color == 'Black':
                if newY == y and newX == x - 1:
                    return True
                elif newY == y and newX == x - 2 and x == 6:
                    return True
                elif abs(newY - y) == 1 and newX == x - 1 and board.getPiece(positions):
                    return True
                
        return False

    
class Rook(Piece):
    def __init__(self, position, color):
        super().__init__(position, color)

    def __str__(self) -> str:
        return 'Rook ' + super().__str__()
    
    def isPossibleMove(self, board, positions):
        x, y = self.position
        newX, newY = positions

        if newX == x or newY == y:
            if self.isPathClear(board,(x,y), (newX, newY)):
                return True

        return False

class Knight(Piece):
    def __init__(self, position, color):
        super().__init__(position, color)

    def __str__(self) -> str:
        return 'Knight '+ super().__str__()
    
    def isPossibleMove(self, board, positions):
        x, y = self.position
        newX, newY = positions

        if self.isPathClear(board,(x,y), (newX, newY)):
            if (newX == x + 1 and newY == y + 2) or (newX == x + 1 and newY == y - 2) \
            or (newX == x -1 and newY == y + 2) or (newX == x - 1 and newY == y - 2) \
            or(newX == x+2 and newY == y+1) or (newX == x+2 and newY==y-1) \
            or(newX == x - 2 and newY == y+1) or (newX == x-2 and newY==y-1):
                return True
            
        return False
    

class Bishop(Piece):
    def __init__(self, position, color):
        super().__init__(position, color)

    def __str__(self) -> str:
        return 'Bishop ' + super().__str__()
    
    def isPossibleMove(self, board, positions):
        x, y = self.position
        newX, newY = positions
        dx = abs(newX - x)
        dy = abs(newY - y)
        if (dx == dy):
            if self.isPathClear(board,(x,y), (newX, newY)):
                return True


        return False

class Queen(Piece):
    def __init__(self, position, color):
        super().__init__(position, color)
    
    def __str__(self) -> str:
        return 'Queen ' + super().__str__()
    
    def isPossibleMove(self, board, positions):
        x, y = self.position
        newX, newY = positions
        dx = abs(newX - x)
        dy = abs(newY - y)
        if newX == x or newY == y or (dx == dy):
            if self.isPathClear(board,(x,y), (newX, newY)):
                return True
            
        return False

class King(Piece):
    def __init__(self, position, color):
        super().__init__(position, color)
              
    def __str__(self) -> str:
        return 'King ' + super().__str__()
    
    def isPossibleMove(self, board, positions):
        x, y = self.position
        newX, newY = positions

        if (newY - y == 1) or (newX - x == 1) or (abs(newX - x) == 1 and abs(newY - y)):
            if self.isPathClear(board, (x,y), (newX, newY)):
                return True
            
        return False

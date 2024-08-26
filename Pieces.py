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
        self.position = None

    def isPathClear(self, board, start, end):
        startY, startX = start
        endY, endX = end

        if startX == endX:
            stepY = 1 if startY < endY else -1
            for y in range(startY + stepY, endY, stepY):
                if board.getPiece([startX, y]) != 0:
                    print("Path not clear.")

                    return False
        elif startY == endY:
            stepX = 1 if startX < endX else -1
            for x in range(startX + stepX, endX, stepX):
                if board.getPiece([x, startY]) != 0:
                    print("Path not clear.")
                    return False
        elif abs(startY - endY) == abs(startX - endX):
            stepY = 1 if startY < endY else -1
            stepX = 1 if startX < endX else -1
            for i in range(1, abs(startY - endY)):
                if board.getPiece([(startX + i * stepX), (startY + i * stepY)]) != 0:
                    print("Path not clear.")
                    
                    return False
        print("Path clear")
        return True

class Pawn(Piece):
    def __init__(self, position, color):
        super().__init__(position, color)

    def __str__(self) -> str:
        return 'Pawn ' + super().__str__()

    def isPossibleMove(self, board, positions):
        y, x = self.position
        newY, newX = positions

        if self.color == 'White':
            if newX == x and newY == y + 1:
                return True
            elif newX == x and newY == y + 2 and y == 1:
                return True
            elif abs(newX - x) == 1 and newY == y + 1:
                return True

        elif self.color == 'Black':
            if newX == x and newY == y - 1:
                return True
            elif newX == x and newY == y - 2 and y == 6:
                return True
            elif abs(newX - x) == 1 and newY == y - 1:
                return True
            
        return False

    
class Rook(Piece):
    def __init__(self, position, color):
        super().__init__(position, color)

    def __str__(self) -> str:
        return 'Rook ' + super().__str__()
    
    def isPossibleMove(self, board, positions):
        y, x = self.position
        newY, newX = positions

        if newX == x or newY == y:
            if self.isPathClear(board, [y,x], [newY, newX]):
                return True

        return False

class Knight(Piece):
    def __init__(self, position, color):
        super().__init__(position, color)

    def __str__(self) -> str:
        return 'Knight '+ super().__str__()
    
    def isPossibleMove(self, board, positions):
        y, x = self.position
        newY, newX = positions

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
        y, x = self.position
        newY, newX = positions

        if abs(newX - x) == abs(newY - y):
            if self.isPathClear(board, [y,x], [newY, newX]):
                return True


        return False

class Queen(Piece):
    def __init__(self, position, color):
        super().__init__(position, color)
    
    def __str__(self) -> str:
        return 'Queen ' + super().__str__()
    
    def isPossibleMove(self, board, positions):
        y, x = self.position
        newY, newX = positions

        if newX == x or newY == y or abs(newX - x) == abs(newY - y):
            if self.isPathClear(board, [y,x], [newY, newX]):
                return True
            
        return False

class King(Piece):
    def __init__(self, position, color):
        super().__init__(position, color)
              
    def __str__(self) -> str:
        return 'King ' + super().__str__()
    
    def isPossibleMove(self, positions):
        y, x = self.position
        newY, newX = positions

        if newX == x + 1 or newY == y + 1 or newX == x - 1 or newY == y - 1 or abs(newX - x) == abs(newY - y):
            return True
            
        return False

class Piece(object):
    def __init__(self, position, color):
        self.position = position
        self.color = color

    def __str__(self) -> str:
        return self.color
    
    def getPosition(self):
        return position

class Pawn(Piece):
    def __init__(self, position, color):
        super().__init__(position, color)

    def __str__(self) -> str:
        return 'Pawn ' + super().__str__()

    def possibleMove(self, positions):
        x, y = self.position
        newX, newY = positions

        if self.color == 'White':
            if newX == x and (newY == y + 1 or newY == y+ 2):
                return True
            elif abs(newX - x) == 1 and newY == y + 1:
                return True

        elif self.color == 'Black':
            if newX == x and (newY == y - 1 or newY == y - 2):
                return True
            elif abs(newY - y) == 1 and newY == y - 1:
                return True
            
        return False
    
class Rook(Piece):
    def __init__(self, position, color):
        super().__init__(position, color)

    def __str__(self) -> str:
        return 'Rook ' + super().__str__()
    
    def possibleMove(self, positions):
        x, y = self.position
        newX, newY = positions

        if newX == x or newY == y:
            return True

        return False

class Knight(Piece):
    def __init__(self, position, color):
        super().__init__(position, color)

    def __str__(self) -> str:
        return 'Knight '+ super().__str__()
    
    def possibleMove(self, positions):
        x, y = self.position
        newX, newY = positions

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
    
    def possibleMove(self, positions):
        x, y = self.position
        newX, newY = positions

        if abs(newX - x) == abs(newY - y):
            return True

        return False

class Queen(Piece):
    def __init__(self, position, color):
        super().__init__(position, color)
    
    def __str__(self) -> str:
        return 'Queen ' + super().__str__()
    
    def possibleMove(self, positions):
        x, y = self.position
        newX, newY = positions

        if newX == x or newY == y or  abs(newX - x) == abs(newY - y):
            return True
            
        return False

class King(Piece):
    def __init__(self, position, color):
        super().__init__(position, color)
              
    def __str__(self) -> str:
        return 'King ' + super().__str__()
    
    def possibleMove(self, positions):
        x, y = self.position
        newX, newY = positions

        if newX == x + 1 or newY == y + 1 or newX == x - 1 or newY == y - 1 or abs(newX - x) == abs(newY - y):
            return True
            
        return False

from abc import ABC, abstractmethod

# Base Chess Piece Class (Abstract)
class BaseChessPiece(ABC):

    def __init__(self, color: str, name: str, symbol: str, identifier: int):
        self.color = color
        self.symbol = symbol
        self.name = name # The name to use for the Piece
        self.identifier = identifier # The identifier to use for the Piece in case there are more with the same name
        self.is_alive = True
        self.position = ""

    def __str__(self):
        return "{} {} {}".format(self.color, self.name, self.identifier)

    def __repr__(self):
        return "{} {} {}".format(self.color, self.name, self.identifier)

    # def __eq__(self, other):
    #     # Equals when the symbol, identifier and color are the same
    #     return self.symbol == other.symbol and self.identifier == other.identifier and self.color == other.color

    @abstractmethod
    def move(self, allowed_movement):
        print(allowed_movement)

    @abstractmethod
    def can_kill(self):
        pass

    def die(self):
        self.is_alive = False


class Pawn(BaseChessPiece):

    def __init__(self, color: str, identifier: int):
        super().__init__(color, 'Pawn', None, identifier)

    def move(self):
        movement = "Can only move forward"
        super().move(movement)

    def can_kill(self):
        print("Pawn can kill diagonally")
        # TODO: Implement to check if there is a unit forward diagonally and if it is an enemy unit
        # TODO: Kill that enemy

# The rook can move in a straight line, horizontally or vertically, any number of squares.
class Rook(BaseChessPiece):

    def __init__(self, color: str, identifier: int):
        super().__init__(color, 'Rook', 'R', identifier)
    
    def move(self):
        print("Rook moves forward, backward, left or right any number of squares")

    def can_kill(self):
        print("Rook can kill any unit in a straight line, horizontally or vertically")

# The knight moves to any of the closest squares that are not on the same rank, file, or diagonal, thus the move forms an "L"-shape: two squares vertically and one square horizontally, or two squares horizontally and one square vertically. The knight is the only piece that can leap over other pieces.
class Knight(BaseChessPiece):

    def __init__(self, color: str, identifier: int):
        super().__init__(color, 'Knight', 'N', identifier)
    
    def move(self):
        print("Knight moves in an L shape")

    def can_kill(self):
        print("Knight can kill any unit in an L shape")

# The bishop can move any number of squares diagonally, but cannot leap over other pieces.
class Bishop(BaseChessPiece):

    def __init__(self, color: str, identifier: int):
        super().__init__(color, 'Bishop', 'B', identifier)
    
    def move(self):
        print("Bishop moves diagonally any number of squares")

    def can_kill(self):
        print("Bishop can kill any unit in a diagonal line")

# The queen combines the power of a rook and bishop and can move any number of squares along a rank, file, or diagonal, but cannot leap over other pieces.
class Queen(BaseChessPiece):

    def __init__(self, color: str, identifier: int):
        super().__init__(color, 'Queen', 'Q', identifier)
    
    def move(self):
        print("Queen moves diagonally, horizontally or vertically any number of squares")

    def can_kill(self):
        print("Queen can kill any unit in a diagonal, horizontal or vertical line")

# The king moves one square in any direction, so long as that square is not attacked by an enemy piece.
class King(BaseChessPiece):

    def __init__(self, color: str, identifier: int):
        super().__init__(color, 'King', 'K', identifier)
    
    def move(self):
        print("King moves one square in any direction")

    def can_kill(self):
        print("King can kill any unit in a square adjacent to it")
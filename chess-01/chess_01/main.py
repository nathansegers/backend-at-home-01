from pieces import Pawn, King, Queen, Bishop, Knight, Rook
from board import Board

board = Board()

board.print_board()



# black_pawns = {
#     f"{chr(range(ord('a'), ord('i'))[i - 1])}2": Pawn('BLACK', i) for i in range(1, 9)
# }
# print(black_pawns)

# black_king: King = board.find_piece('K', 1, 'BLACK')
# print(black_king)

pawn_one_white = Pawn("WHITE", 1)
pawn_one_white.move()
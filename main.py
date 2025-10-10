class Tic_Toe:
    def __init__(self):
        self.board = [ " " for _ in range (9)]
        print(self.board)

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('|'+'|'.join(row)+ '|')

    @staticmethod
    def print_number():
        number_board= [[str(i) for i in range (j*3,(j+1)*3)] for j in range(3)]
        for row in number_board:
            print('|'+'|'.join(row)+'|')

    def available_moves(self):
        for(i,spot) in enumerate(self.board):
            moves= []
            if spot == '':
                moves.append(i)
        return moves





T= Tic_Toe()

num= T.print_number()
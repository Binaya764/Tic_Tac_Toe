class Tic_Toe:
    def __init__(self):
        self.board = [ " " for _ in range (9)]
        print(self.board)

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('|'+'|'.join(row)+ '|')
        
T= Tic_Toe()
create= T.print_board()
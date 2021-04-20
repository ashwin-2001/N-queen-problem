class Nqueen:
    def __init__(self, size):
        self.size = size
        self.board = [[0 for i in range(size)] for i in range(size)]
        self.Trials = 0

    def isSafe(self, row, col):
        for i in range(col):
            if self.board[row][i] == 1:
                return False

        diag1 = [self.board[row-i][col-i] for i in range(self.size) if row-i>=0 and col-i>=0]                   #Diagonal TopLeft to Bottom Down
        diag2 = [self.board[row-i][col+i] for i in range(self.size) if row-i>=0 and col+i<self.size]            #TopRight
        diag3 = [self.board[row + i][col - i] for i in range(self.size) if row + i <self.size and col - i >= 0] #BottomLeft
        if 1 in diag1: return False
        if 1 in diag2: return False
        if 1 in diag3: return False
        return True
    def place_queen(self,col):
        if col >= self.size:
            print("True",col)
            return True
        for row in range(self.size):
            if self.isSafe(row,col):
                #print(row,col)
                self.board[row][col]=1
                self.Trials+=1
                if self.place_queen(col+1):
                    return True
                self.board[row][col]=0

        return False
    def show(self):
        print(f"Total Trials : {self.Trials}")
        for i in range(self.size):print(self.board[i])

Count = 8 # Size of board / no.of Queens
sol = Nqueen(Count)
import time
start = time.time_ns()
sol.place_queen(0)
end = time.time_ns()
print("Time Take(ns) : {}".format(end-start))
sol.show()

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

class Array:
    def __init__(self,capacity):
        self.board = [None] * capacity
        self.size = 0
    def add(self,stu):
        self.board[self.size]=stu
        self.size+=1
    def sort(self):
        for i in range(self.size-1):
            for j in range(self.size-1-i):
                if self.board[j].score  <  self.board[j+1].score:
                    self.board[j],self.board[j+1]=self.board[j+1],self.board[j]
    
    def remove(self, name):
        i = 0
        while i < self.size:
            if self.board[i].name == name:
                for j in range(i, self.size - 1):
                    self.board[j] = self.board[j + 1]
                self.board[self.size - 1] = None
                self.size -= 1
            else:
                i += 1

    def show(self):
        for i in range(self.size):
            print(f"           {self.board[i].name} {self.board[i].score}")
        print()
if __name__== "__main__":
    pL= Array(50)
    while True:
        s= input()
        if s=="over": break
        if s=="disqualify": 
            S=input()
            pL.remove(S)
            pL.show()
        else:
            name, score= s.split()
            score=int(score)
            player= Player(name,score)
            pL.add(player)
            pL.sort()
            pL.show()
        
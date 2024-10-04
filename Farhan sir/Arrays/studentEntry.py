class Student:
    def __init__(self, name, id, marks):
        self.name=name
        self.id=id
        self.marks=marks
class Array:
    def __init__(self,capacity):
        self.board= [None]*capacity
        self.size= 0
    def add(self,stu):
        self.board[self.size]=stu
        self.size+=1
    def sort(self):
        for i in range(self.size-1):
            for j in range(self.size-1-i):
                if self.board[j].marks==self.board[j+1].marks:
                    if self.board[j].id  >  self.board[j+1].id:
                        self.board[j],self.board[j+1]=self.board[j+1],self.board[j]

                elif self.board[j].marks  <  self.board[j+1].marks:
                    self.board[j],self.board[j+1]=self.board[j+1],self.board[j]
    def show(self):
        if self.size<3:
            for i in range (self.size):
                print(f"{i+1}. Name: {self.board[i].name} Marks: {self.board[i].marks} Id: {self.board[i].id}")
        else :
            for i in range (3):
                print(f"{i+1}. Name: {self.board[i].name} Marks: {self.board[i].marks} Id: {self.board[i].id}")

if __name__== "__main__":
    stu_list= Array(50)
    while True:
        s= input("enter name , id , marks without space and 'over' to terminate : ")
        if s=="over": break
        name, id , marks= s.split()
        id=int(id)
        marks= int(marks)
        stu= Student(name,id,marks)
        stu_list.add(stu)
        stu_list.sort()
        stu_list.show()
    print("its over")
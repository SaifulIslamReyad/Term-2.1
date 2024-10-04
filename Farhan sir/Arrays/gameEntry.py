class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

class Array:
    def __init__(self, capacity):
        self.array = [None] * capacity
        self.size = 0

    def add(self, entry):
        new_score = entry.score

        if self.size < len(self.array):
            self.array[self.size] = entry
            self.size += 1
        elif new_score > self.array[self.size - 1].score:
            self.array[self.size - 1] = entry

        for i in range(self.size - 1):
            for j in range(self.size - 1 - i):
                if self.array[j].score < self.array[j + 1].score:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]

    def remove(self, i):
        if i < 0 or i >= self.size:
            raise IndexError(f"Invalid index: {i}")
        temp = self.array[i]

        for j in range(i, self.size - 1):
            self.array[j] = self.array[j + 1]
        self.array[self.size - 1] = None
        self.size -= 1
        return temp

    def show(self):
        for i in range(self.size):
            print(f"{i + 1}. Name: {self.array[i].name}, Score: {self.array[i].score}")
        print()


def main():
    scoreboard = Array(3)
    print("Game Start")

    while True:
        entry = input("Enter name and score (enter 'over' to stop the game): ")
        if entry == "over": break
        name, score = entry.split()
        score = int(score)
        game_entry = Player(name, score)
        scoreboard.add(game_entry)
        print("Current scoreboard")
        scoreboard.show()

    print("Game over")

if __name__ == "__main__":
    main()

#include <bits/stdc++.h>
using namespace std;

class Player
{
private:
    string name;
    int score;

public:
    Player() : name(""), score(0) {}

    Player(const string &name, int score) : name(name), score(score) {}

    string getName() const
    {
        return name;
    }

    int getScore() const
    {
        return score;
    }

    string toString() const
    {
        return name + ", " + to_string(score);
    }
};

class Array
{
private:
    vector<Player> array;
    int size;
    int capacity;

public:
    Array(int capacity) : size(0), capacity(capacity)
    {
        array.resize(capacity);
    }

    void add(const Player &entry)
    {
        int newScore = entry.getScore();

        if (size < capacity)
        {
            array[size] = entry;
            size++;
        }
        else if (newScore > array[size - 1].getScore())
        {
            array[size - 1] = entry;
        }

        for (int i = 0; i < size - 1; i++)
        {
            for (int j = 0; j < size - 1 - i; j++)
            {
                if (array[j].getScore() < array[j + 1].getScore())
                {
                    swap(array[j], array[j + 1]);
                }
            }
        }
    }

    Player remove(int i)
    {
        if (i < 0 || i >= size)
        {
            throw out_of_range("Invalid index: " + to_string(i));
        }

        Player temp = array[i];

        for (int j = i; j < size - 1; j++)
        {
            array[j] = array[j + 1];
        }
        array[size - 1] = Player("", 0);
        size--;

        return temp;
    }

    void show() const
    {
        for (int i = 0; i < size; i++)
        {
            cout << (i + 1) << ". Name: " << array[i].getName() << ", Score: " << array[i].getScore() << endl;
        }
        cout << endl;
    }
};

int main()
{
    Array scoreboard(3);
    string name;
    int score;

    cout << "Game Start" << endl;

    while (true)
    {
        cout << "Enter name and score (enter 'over' to stop the game): ";
        string entry;
        getline(cin, entry);

        if (entry == "over")
            break;

        size_t spacePos = entry.find(' ');
        if (spacePos != string::npos)
        {
            name = entry.substr(0, spacePos);
            score = stoi(entry.substr(spacePos + 1));
            Player gameEntry(name, score);
            scoreboard.add(gameEntry);
            cout << "Current scoreboard" << endl;
            scoreboard.show();
        }
    }

    cout << "Game over" << endl;
    return 0;
}

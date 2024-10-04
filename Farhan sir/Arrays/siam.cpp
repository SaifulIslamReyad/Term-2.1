#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Player 
{
private:
    string name;
    int score;

public:
    Player(string name, int score) : name(name), score(score) {}

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
    int capacity;

public:
    Array(int capacity) : capacity(capacity) {}

    void add(const Player& entry) 
    {
        if (array.size() < capacity) 
        {
            array.push_back(entry);
        } 
        else if (entry.getScore() > array.back().getScore()) 
        {
            array.back() = entry;
        }

        sort(array.begin(), array.end(), [](const Player& a, const Player& b) 
        {
            return a.getScore() > b.getScore();
        });
    }

    void remove(int i) 
    {
        if (i < 0 || i >= array.size()) 
        {
            cout << "Invalid index: " << i << endl;
            return;
        }
        array.erase(array.begin() + i);
    }

    void show() const 
    {
        for (int i = 0; i < array.size(); ++i) 
        {
            cout << (i + 1) << ". Name: " << array[i].getName() << ", Score: " << array[i].getScore() << endl;
        }
        cout << endl;
    }
};

int main() 
{
    Array scoreboard(3);
    cout << "Game Start" << endl;

    while (true) 
    {
        cout << "Enter name and score (enter 'over' to stop the game): ";
        string entry;
        getline(cin, entry);

        if (entry == "over")
            break;

        string name = entry.substr(0, entry.find(" "));
        int score = stoi(entry.substr(entry.find(" ") + 1));

        Player gameEntry(name, score);
        scoreboard.add(gameEntry);

        cout << "Current scoreboard" << endl;
        scoreboard.show();
    }

    cout << "Game over" << endl;

    return 0;
}

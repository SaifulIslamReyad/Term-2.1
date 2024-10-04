import java.util.*;

class Player 
{
    private final String name;
    private final int score;

    public Player(String name, int score) 
    {
        this.name = name;
        this.score = score;
    }

    public String getName() 
    {
        return name;
    }

    public int getScore() 
    {
        return score;
    }

    @Override
    public String toString() 
    {
        return this.name + ", " + this.score;
    }
}

class Array 
{
    private final Player array[];
    private int size;

    public Array(int capacity) 
    {
        array = new Player[capacity];
        size = 0;
    }

    public void add(Player entry) 
    {
        int newScore = entry.getScore();

        if (size < array.length) 
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
                    Player temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                }
            }
        }
    }

    public Player remove(int i) 
    {
        if (i < 0 || i >= size) 
        {
            throw new IndexOutOfBoundsException("Invalid index: " + i);
        }

        Player temp = array[i];

        for (int j = i; j < size - 1; j++) 
        {
            array[j] = array[j + 1];
        }
        array[size - 1] = null;
        size--;

        return temp;
    }

    public void show() 
    {
        for (int i = 0; i < size; i++) 
        {
            System.out.println((i + 1) + ". Name: " + array[i].getName() + ", Score: " + array[i].getScore());
        }
        System.out.println();
    }
}

public class gameEntry 
{
    public static void main(String[] args) {
        Array scoreboard = new Array(3);
        Scanner scanner = new Scanner(System.in);

        System.out.println("Game Start");

        while (true) {
            System.out.print("Enter name and score (enter 'over' to stop the game): ");
            String entry = scanner.nextLine();

            if (entry.equals("over"))
                break;

            String[] parts = entry.split(" ");
            String name = parts[0];
            int score = Integer.parseInt(parts[1]);
            Player gameEntry = new Player(name, score);
            scoreboard.add(gameEntry);

            System.out.println("Current scoreboard");
            scoreboard.show();
        }

        System.out.println("Game over");
        scanner.close();
    }
}

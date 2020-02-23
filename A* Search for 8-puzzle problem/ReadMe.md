
# Problem:

The 8-puzzle problem is played on a 3-by-3 grid with 8 square tiles labeled 1 through 8 and a
blank tile. Your goal is to rearrange the blocks so that they are in order. You are permitted
to slide blocks horizontally or vertically into the blank tile. For example, consider the given
sequence:

 

In this program, I am using A* Search using 2 different heuristics to solve this problem.

astar1: A* with Heuristic 1: Number of Misplaced Tiles
This Heuristic basically counts the number of tiles which are misplaced in the board configuration state at each iteration of the algorithm. It takes O(n) time.

astar2: A* with Heuristic 2: Manhattan Distance
The Heuristic basically calculates the distance between the desired goal position and the given input position for all elements in both x-axis and y-axis directions.
Thus, for each element, it checks twice and runs in O(n^2) time. 


# Instructions to run:

Assumed Dependencies: python 3.7.3 version

Just run on terminal:

**For A\* with Heuristic 1:**
> *python3 astar_.py astar1*

**For A\* with Heuristic 2:**
> *python3 astar_.py astar2*

The code asks you to enter the input configuration.

Just enter all 9 entries giving a space between each entry.
Press enter once you are done writing all 9 entries of your input configuration.

**For example:**
ananyabanerjee@Ananyas-MacBook-Pro Desktop % python3 astar_.py astar1

Enter the input state config 0 1 3 4 2 5 7 8 6

Do the same when asked for goal state

**For example:**
ananyabanerjee@Ananyas-MacBook-Pro Desktop % python3 astar_.py astar1

Enter the input state config 0 1 3 4 2 5 7 8 6
Enter the goal state1 2 3 4 5 6 7 8 0

Then Press enter.
You will be able to see all the required information including board configurations chosen, number of moves and sum of enqueued states.


# Sample Run Output for A* Search using Heuristic 1:

  
  0   1   3   Input State


  4   2   5


  7   8   6


-----------------
  1   0   3


  4   2   5


  7   8   6


-----------------
  1   2   3


  4   0   5


  7   8   6


-----------------
  1   2   3


  4   5   0


  7   8   6


-----------------
  1   2   3   (Goal State)


  4   5   6


  7   8   0


-----------------
Total Number of moves 4
Total Enqueued 11

# Sample Run Output for A* Search using Heuristic 2:

  
  
  0   1   3   Input State


  4   2   5


  7   8   6


-----------------
  1   0   3


  4   2   5


  7   8   6


-----------------
  1   2   3


  4   0   5


  7   8   6


-----------------
  1   2   3


  4   5   0


  7   8   6


-----------------
  1   2   3   (Goal State)


  4   5   6


  7   8   0


-----------------
Total Number of moves 4
Total Enqueued 13

Thank you!




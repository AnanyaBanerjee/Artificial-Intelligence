
# Problem:

The 8-puzzle problem is played on a 3-by-3 grid with 8 square tiles labeled 1 through 8 and a
blank tile. Your goal is to rearrange the blocks so that they are in order. You are permitted
to slide blocks horizontally or vertically into the blank tile. For example, consider the given
sequence:

 

In this program, I am using Iterative Deepening Search to solve this problem.

# Instructions to run:

Assumed Dependencies: python 3.7.3 version

Just run on terminal:

> **python3 ids_.py ids**

The code asks you to enter the input configuration.

Just enter all 9 entries giving a space between each entry.
Press enter once you are done writing all 9 entries of your input configuration.

**For example:**
ananyabanerjee@Ananyas-MacBook-Pro Desktop % python3 ids_.py ids

Enter the input state config 0 1 3 4 2 5 7 8 6

Do the same when asked for goal state

**For example:**
ananyabanerjee@Ananyas-MacBook-Pro Desktop % python3 ids_.py ids

Enter the input state config 0 1 3 4 2 5 7 8 6

Enter the goal state1 2 3 4 5 6 7 8 0

Then Press enter.
You will be able to see all the required information including board configurations chosen, number of moves and sum of enqueued states.






# Sample Run Output:
<pre>
  
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
Total Enqueued 24
</pre>
Thank you!



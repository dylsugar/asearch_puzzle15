Programming Language: Python 
Version: Python 3.8.5

Instructions:

 1) In the command line, type: "python3 ./thesolver.py 1 3 4 8 5 2 0 6 9 10 7 11 13 14 15 12"
   where the numbers after ./thesolver.py can be any of the 15 numbers
 
 (But if running in VS code, then it should just be python ./thesolver ...)
 
 2) Next user will be prompted with "Enter Heuristic either 'H' or 'M' (H is Hamming and M is Manhattan):" in which entering 'M' will make A* use a Manhattan Heuristic or entering     'H' will make A* use a Hamming Heuristic.
 
 
 3) This should give the output of:

          Enter Heuristic either 'H' or 'M' (H is Hamming and M is Manhattan): H
          Found Solution!
          Moves: R U L L D R D R D
          Number of Nodes expanded: 156
          Time Taken: 0.024
          Memory Used: 5760 kb

          ------------OR-----------------------------------------------

          Enter Heuristic either 'H' or 'M' (H is Hamming and M is Manhattan): M
          Found Solution!
          Moves: R U L L D R D R D
          Number of Nodes expanded: 36
          Time Taken: 0.001
          Memory Used: 1512 kb

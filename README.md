For this assignment you will have to complete an algorithm that computes a hierarchical clustering using the average distance heuristic.  This is very similar to the UPGMA algorithm (minus the calculation of branch lengths).  You may complete this assignment through Gradescope at: https://www.gradescope.com/courses/358896/assignments/1937380 (Links to an external site.) .  Also, this is equivalent to Rosalind's assignment BA8E: http://rosalind.info/problems/ba8e/ (Links to an external site.) , in case you need more details or want to pre-test yourself.

Your program should read a file called "input" that contains a header, consisting of a single integer (n) corresponding to the number of organisms being clustered, followed by an n x n distance matrix containing the pairwise distances between the organisms.  You may assume that the matrix is symmetrical.  An example is shown below:

7
0.00 0.74 0.85 0.54 0.83 0.92 0.89
0.74 0.00 1.59 1.35 1.20 1.48 1.55
0.85 1.59 0.00 0.63 1.13 0.69 0.73
0.54 1.35 0.63 0.00 0.66 0.43 0.88
0.83 1.20 1.13 0.66 0.00 0.72 0.55
0.92 1.48 0.69 0.43 0.72 0.00 0.80
0.89 1.55 0.73 0.88 0.55 0.80 0.00
Your code must produce as output a list of all possible clusters contained within the hierarchical clustering of the given set of organisms, using the "average distance/Davg" heuristic.  Within this output, each organism is represented by an integer, corresponding to the row/column (1-based) where the organism appears in the distance matrix provided as input.

Here is the matrix again, with the rows/columns numbered, and the corresponding output:

1    2    3    4    5    6    7
1  0.00 0.74 0.85 0.54 0.83 0.92 0.89
2  0.74 0.00 1.59 1.35 1.20 1.48 1.55
3  0.85 1.59 0.00 0.63 1.13 0.69 0.73
4  0.54 1.35 0.63 0.00 0.66 0.43 0.88
5  0.83 1.20 1.13 0.66 0.00 0.72 0.55
6  0.92 1.48 0.69 0.43 0.72 0.00 0.80
7  0.89 1.55 0.73 0.88 0.55 0.80 0.00
4 6
5 7
3 4 6
1 2
5 7 3 4 6
1 2 5 7 3 4 6
Each line represents the set of leaves within the subtree dominated by an internal node of the clustering tree:

rosalind-tree.png

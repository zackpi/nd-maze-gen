# nd-maze-gen
Generates a maze in arbitrarily many dimensions that is guaranteed to be solvable.

## Set up environment
    python 2d_maze.py [width height [gen_method]]
or use/extend the MazeGraphND code yourself

## Sample output demonstrating 5x3 maze using djs method
    (1, 0) -> (1, 1)
    (3, 1) -> (3, 2)
    (1, 2) -> (1, 1)
    (2, 0) -> (2, 1)
    (4, 1) -> (4, 2)
    (4, 1) -> (4, 0)
    (1, 1) -> (0, 1)
    (2, 0) -> (3, 0)
    (4, 0) -> (3, 0)
    (0, 0) -> (1, 0)
    (1, 1) -> (2, 1)
    (2, 2) -> (3, 2)
    (1, 2) -> (0, 2)
    (2, 2) -> (1, 2)
    ═╗╔═╗
    ═╬╝║║
    ═╩═╝╚
If you trace the steps on a paper grid, you'll see how the code works.
It initializes each junction as a disjoint set. Then it chooses a random edge between disjoint sets, 
unions the two sets, and adds a connection in the maze. This continues until there is only one set--that
is, every junction is a member of the same djs.

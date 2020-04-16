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

## How it works
### Disjoint Set Method
generates neighbors in this MazeGraphND such there is at least one path from the START to TERMINAL node. Uses a disjount set heuristic; initialize each node as a disjoint set. Place random edges until there is only one DJS covering all nodes. If a DJS covers nodes V' and u,v in V', then u->v. Then if G=(V,E) and DJS covers V, there must exist a path START->TERMINAL

### Prim's Method
generates neighbors in this MazeGraphND such there is at least one path from the START to TERMINAL node. Generates a random number for each edge in the network, then runs Prim's algorithm to create an MST. There is guaranteed to be a path u->v for all u,v in MST(G) for a connected undirected graph G. Then when Prim's terminates, there must exist a path START->TERMINAL.

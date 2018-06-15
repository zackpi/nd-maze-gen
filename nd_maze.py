import random


class MazeNodeND:
    def __init__(self, data):
        self.data = data
        self.edges = {}     # other_junc |-> edge_weight


class MazeGraphND:
    def __init__(self, dimension_vector, solve_method="prims"):
        """
        init() creates a new random MazeGraphND with dimensions of dimension_vector
        
        @param:     dimension_vector    the nd vector containing the size of MazeGraphND in each dimension
                                        must be of the form [n_0, n_1, n_2, n_3, ... n_(n-1)], n_i == int and n_1 > 1
                    solve_method        "prims" for a solution based on prims algorithm 
                                        or "djs" for a solution based on disjoint-set
        """
        
        # intialize the empty maze
        if any([type(d) != int or d < 1 for d in dimension_vector]):
            raise ValueError("Improper dimension vector passed to NDMazeGraph constructor")
        self.dims = dimension_vector
        self.junctions = self.init_grid()
        
        # create the connections in the maze
        # If there is a connection between two junctions,
        # the user can travel between them
        self.connections = []
        if solve_method == "prims":
            self.solve_prims()
        elif solve_method == "djs":
            self.solve_djs()
        else:
            raise ValueError("Invalid solve method. Choose one of 'prims' or 'djs'")


    def init_grid(self):
        """
        init_grid() generates an empty grid with dimensions corresponding to dimension_vector
                    represented as an n-dimensional lists-of-lists matrix
            
        @return:    the nd grid with dimensions of self.dims
        """
        
        def init_grid_recurse(d, i, p):
            if i == len(d)-1:
                return [MazeNodeND(p+(k,)) for k in range(d[0])]
            else:
                return [init_grid_recurse(d, i+1, p+(k, )) for k in range(d[-i-1])]
        return init_grid_recurse(self.dims, 0, tuple())


    def select_junction(self, pos):
        """
        select_junction() returns the value at pos in self.junctions. Implemented recursively.
            
        @param:     pos     the nd vector pointing to the junction in self.junctions to select
        
        @return:    val     the value at pos in self.junctions
        """
        
        val = self.junctions
        for p in pos:
            val = val[p]
        return val.data


    def get_adjacent(self, pos):
        """
        get_adjacent() returns a list of all junctions directly adjacent (not diagonal) to pos in nd space
            
        @return:    adj     the list of adjacent junctions
        """
        adj = []
        for i, p in enumerate(pos):
            pos[i] -= 1
            if pos[i] >= 0:
                adj.append(self.select_junction(pos))
            pos[i] += 2
            if pos[i] < self.dims[i]:
                adj.append(self.select_junction(pos))
            pos[i] -= 1
        return adj
    

    def solve_prims(self):
        """
        solve_prims() generates neighbors in this MazeGraphND such there is at least one path from 
                        the START to TERMINAL node. Generates a random number for each edge in the 
                        network, then runs Prim's algorithm to create an MST. There is guaranteed 
                        to be a path u->v for all u,v in MST(G) for a connected undirected graph G.
                        Then when Prim's terminates, there must exist a path START->TERMINAL
        """
        
        def randomize_edge_weights(d, i, p):
            if i < len(d)-1:
                for dim in range(d[i]):
                    randomize_edge_weights(d, i+1, p+(dim, ))
            else:
                for dim in range(d[i]):
                    junc = p+(dim, )
                    node = self.select_junction(junc)
                    nbrs = self.get_adjacent(junc)
                    for n in nbrs:
                        neighbor = select_junction(n)
                        node.edges[neighbor] = random.random()   
                    print(node.edges)              
        
        randomize_edge_weights(self.dims, 0, tuple())
        
        used_vertices = set()
        used_edges = set()
        avail_edges = []


    def solve_djs(self):
        """
        solve_djs() generates neighbors in this MazeGraphND such there is at least one path from 
                    the START to TERMINAL node. Uses a disjount set heuristic; initialize each node 
                    as a disjoint set. Place random edges until there is only one DJS covering all 
                    nodes. If a DJS covers nodes V' and u,v in V', then u->v. Then if G=(V,E) and 
                    DJS covers V, there must exist a path START->TERMINAL
        """
        pass


    def draw_junctions(self):
        """
        draw_junctions() returns a string representation of the junctions of this MazeGraphND.
                            and is called by the __str__ method. Only intended for debug purposes.
        
        String representation for dims == [x=3,y=4,z=2]:
        [ z	
        .	[ y	
        .	.	[ x	(0, 0, 0), (0, 0, 1), (0, 0, 2)], 
        .	.	[ x	(0, 1, 0), (0, 1, 1), (0, 1, 2)], 
        .	.	[ x	(0, 2, 0), (0, 2, 1), (0, 2, 2)], 
        .	.	[ x	(0, 3, 0), (0, 3, 1), (0, 3, 2)]
        .	], 
        .	[ y
        .	.	[ x	(1, 0, 0), (1, 0, 1), (1, 0, 2)], 
        .	.	[ x	(1, 1, 0), (1, 1, 1), (1, 1, 2)], 
        .	.	[ x	(1, 2, 0), (1, 2, 1), (1, 2, 2)], 
        .	.	[ x	(1, 3, 0), (1, 3, 1), (1, 3, 2)]
        .	]
        ]
        """
        def draw_junc_recurse(r, junc, n, i):
            r += "\n" + ".\t"*i + "[ i=" + str(i) + "\t"
            if i == n-1:
                for k, j in enumerate(junc):
                    r += str(j)
                    if k != len(junc)-1:
                        r += ", "
                r += "]"
            else:
                for k, j in enumerate(junc):
                    r = draw_junc_recurse(r, j, n, i+1)
                    if k != len(junc)-1:
                        r += ", "
                r += "\n" + ".\t"*i + "]"
            return r
        return draw_junc_recurse("Dimensions: " + str(self.dims), self.junctions, len(self.dims), 0)
   
    def __str__(self):
        return self.draw_junctions()
        


mazegraphnd = MazeGraphND([4,3,2])

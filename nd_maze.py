class MazeGraphND:
    def __init__(self, dimension_vector):
        """
        init() creates a new random MazeGraphND with dimensions of dimension_vector
        
        @param:     dimension_vector    the nd vector containing the size of MazeGraphND in each dimension
                                        must be of the form [n_0, n_1, n_2, n_3, ... n_(n-1)], n_i == int and n_1 > 1
        """
        
        if any([type(d) != int or d < 1 for d in dimension_vector]):
            raise ValueError("Improper dimension vector passed to NDMazeGraph constructor")
        self.dims = dimension_vector
        self.junctions = self.init_grid()
        self.s = MazeNodeND("START")
        self.t = MazeNodeND("TERMINAL")
        self.connections = []

    def init_grid(self):
        """
        init_grid() generates a empty grid with dimensions corresponding to dimension_vector
                    represented as n-dimensional lists-of-lists matrix
            
        @return:    the nd grid with dimensions of self.dims
        """
        
        def init_grid_recurse(d, i, p):
            if i == len(d)-1:
                return [p+(k,) for k in range(d[0])]
            else:
                return [init_grid_recurse(d, i+1, p+(k, )) for k in range(d[-i-1])]
        return init_grid_recurse(self.dims, 0, tuple())


    def select_junction(self, pos):
        """
        select_junction() returns the value at pos in self.junctions. Implemented recursively.
            
        @param:     pos     the nd vector pointing to the junction in self.junctions to select
        
        @return:    val     the value at pos in self.junctions
        """
        
        ret = self.junctions
        for p in pos:
            val = val[p]
        return val

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
        used_vertices = set()
        used_edges = set()
        avail_edges = []


    def solve_djs(self):
        pass

    def __str__(self):
        """
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
        def str_recurse(r, junc, n, i):
            r += "\n" + ".\t"*i + "[ i=" + str(i) + "\t"
            if i == n-1:
                for k, j in enumerate(junc):
                    r += str(j)
                    if k != len(junc)-1:
                        r += ", "
                r += "]"
            else:
                for k, j in enumerate(junc):
                    r = str_recurse(r, j, n, i+1)
                    if k != len(junc)-1:
                        r += ", "
                r += "\n" + ".\t"*i + "]"
            return r
        return str_recurse("Dimensions: " + str(self.dims), self.junctions, len(self.dims), 0)


class MazeNodeND:
    def __init__(self, data):
        self.data = data
        self.neighbors = []

n = MazeGraphND([3, 6, 4])
print(n, "\n")
print(str(n))
print(n.get_adjacent([0, 3, 1]))

class MazeGraphND:
    def __init__(self, dimension_vector):
        if any([type(d) != int or d < 2 for d in dimension_vector]):
            raise ValueError("Improper Dimension Vector passed to NDMazeGraph Constructor")
        self.dims = dimension_vector
        self.junctions = self.init_grid()
        self.s = MazeNodeND("START")
        self.t = MazeNodeND("TERMINAL")
        self.connections = []

    def init_grid(self):
        def init_grid_recurse(d, i, p):
            if i == len(d)-1:
                return [p+(k,) for k in range(d[0])]
            else:
                return [init_grid_recurse(d, i+1, p+(k, )) for k in range(d[-i-1])]
        return init_grid_recurse(self.dims, 0, tuple())

    def select_junction(self, pos):
        ret = self.junctions
        for p in pos:
            ret = ret[p]
        return ret

    def get_adjacent(self, pos):
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
print(n.get_adjacent([0, 3, 1]))

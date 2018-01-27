class NDMazeGraph:
    def __init__(self, dimension_vector):
        if any([type(d) != int or d < 2 for d in dimension_vector]):
            raise ValueError("Improper Dimension Vector passed to NDMazeGraph Constructor")
        self.dims = list(reversed(dimension_vector))
        self.junctions = self.init_grid()
        self.s = NDMazeNode("START")
        self.t = NDMazeNode("TERMINAL")
        self.edges = []

    def init_grid(self):
        def init_grid_recurse(d, i, p):
            if i == len(d)-1:
                return [p+(k,) for k in range(d[-1])]
            else:
                return [init_grid_recurse(d, i+1, p+(k, )) for k in range(d[i])]
        return init_grid_recurse(self.dims, 0, tuple())

    def select_junction(self, pos):
        ret = self.junctions
        for p in pos:
            ret = ret[p]
        return ret

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
        return str_recurse("Dimensions: " + str(list(reversed(self.dims))), self.junctions, len(self.dims), 0)


class NDMazeNode:
    def __init__(self, data):
        self.data = data
        self.neighbors = []

n = NDMazeGraph([3, 6])
print(n)

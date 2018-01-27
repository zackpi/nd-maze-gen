class DisjointSet:
    def __init__(self, data):
        self.data = data
        self.parent = self
        self.dim = 1

    def union(self, other):
        if self == other:
            return self.rep()
        self.parent = other
        other = self.rep()
        other.dim += self.dim
        return other

    def rep(self):
        A = self
        chain = [A]
        while A.parent != A:
            chain.append(A)
            A = A.parent
        for C in chain:
            C.parent = A
        return A

    def cardinality(self):
        return self.rep().dim

    def __str__(self):
        return "<" + str(self.rep().data) + ">"

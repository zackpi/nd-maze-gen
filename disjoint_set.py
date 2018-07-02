class DisjointSet:
    def __init__(self, data):
        self.data = data
        self.parent = self
        self.children = []
        self.dim = 1

    def union(self, other):
        if self == other:
            return self.rep()
        #self.parent = other     # wrong in some way
        other.children.append(self.rep())
        #other = self.rep()
        #other.dim += self.dim
        return other.rep()

    def rep(self):
        A = self
        chain = A.children
        while A.parent != A:
            A = A.parent
            chain.extend(A.children)
        for C in chain:
            C.parent = A
            C.children = []
        return A

    def cardinality(self):
        return self.rep().dim

    def __str__(self):
        return "<" + str(self.rep().data) + ">"
        
if __name__=="__main__":
    A, B, C = DisjointSet("A"), DisjointSet("B"), DisjointSet("C")
    D, E, F = DisjointSet("D"), DisjointSet("E"), DisjointSet("F")
    G, H, I = DisjointSet("G"), DisjointSet("H"), DisjointSet("I")
    
    print(A, B, C, D, E)
    print([str(a) for a in A.children], [str(b) for b in B.children], [str(c) for c in C.children], [str(d) for d in D.children], [str(e) for e in E.children])
    A.union(B)
    print(A, B, C, D, E)
    print([str(a) for a in A.children], [str(b) for b in B.children], [str(c) for c in C.children], [str(d) for d in D.children], [str(e) for e in E.children])
    B.union(C)
    print(A, B, C, D, E)
    print([str(a) for a in A.children], [str(b) for b in B.children], [str(c) for c in C.children], [str(d) for d in D.children], [str(e) for e in E.children])
    D.union(E)
    print(A, B, C, D, E)
    print([str(a) for a in A.children], [str(b) for b in B.children], [str(c) for c in C.children], [str(d) for d in D.children], [str(e) for e in E.children])
    C.union(D)
    print(A, B, C, D, E)
    print([str(a) for a in A.children], [str(b) for b in B.children], [str(c) for c in C.children], [str(d) for d in D.children], [str(e) for e in E.children])
    
    


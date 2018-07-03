class DisjointSet:
    def __init__(self, data):
        self.data = data
        self.parent = self
        self.dim = 1

    def union(self, other):
        # combines the djs containing self and other
        srep, orep = self.rep(), other.rep()
        if srep is orep:
            return
        srep.parent = orep
        orep.dim += srep.dim

    def rep(self):
        # returns the representative of the djs containing self
        # and compresses the path from self to the rep        
        A = self
        chain = [A]
        while A.parent is not A:
            A = A.parent
            chain.append(A)
        for C in chain:
            C.parent = A
        return A
    
    def __len__(self):
        return self.rep().dim

    def __str__(self):
        return "<" + str(self.rep().data) + ">"
    
    def __eq__(self, other):
        return self.rep() is other.rep()
        
if __name__=="__main__":
    A, B, C = DisjointSet("A"), DisjointSet("B"), DisjointSet("C")
    D, E = DisjointSet("D"), DisjointSet("E")
    
    print(A, B, C, D, E)
    print(len(A), len(B), len(C), len(D), len(E))
    print(A==B, A==C, A==D, A==E)
    A.union(B)
    
    print(A, B, C, D, E)
    print(len(A), len(B), len(C), len(D), len(E))
    print(A==B, A==C, A==D, A==E)
    B.union(C)
    
    print(A, B, C, D, E)
    print(len(A), len(B), len(C), len(D), len(E))
    print(A==B, A==C, A==D, A==E)
    D.union(E)
    
    print(A, B, C, D, E)
    print(len(A), len(B), len(C), len(D), len(E))
    print(A==B, A==C, A==D, A==E)
    C.union(D)
    
    print(A, B, C, D, E)
    print(len(A), len(B), len(C), len(D), len(E))
    print(A==B, A==C, A==D, A==E)
    
    


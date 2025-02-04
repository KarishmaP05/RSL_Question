def sorted_array(edges):
    n = len(edges)
    
    # Loop through all elements
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n-i-1):
            # Compare adjacent elements and swap if they are in the wrong order
            if edges[j][2] > edges[j+1][2]:
                edges[j], edges[j+1] = edges[j+1], edges[j]
    
    return edges


class Disjointset:
    def __init__(self,num_nodes):
        self.parent=[i for i in range(num_nodes)]
        self.rank=[0]*num_nodes



    def find(self,node):
        if self.parent[node]!=node:
            self.parent[node]=self.find(self.parent[node])
        return self.parent[node]
    
    def union(self,u,v):
        rootU=self.find(u)
        rootV=self.find(v)

        if rootU != rootV:
            if self.rank[rootU] > self.rank[rootV]:
                self.parent[rootV]=rootU
            elif self.rank[rootU] < self.rank[rootV]:
                self.parent[rootU]=rootV
            else:
                self.parent[rootV]=rootU
                self.rank[rootU]+=1

def Kruskal_algorithm(edges,num_nodes):
    # sort edges by weight

    # edges.sort(key=lambda x:x[2])
    edges=sorted_array(edges)

    ds=Disjointset(num_nodes)
    mst=[]
    total_wt=0

    for u,v,weight in edges:
        if ds.find(u)!=ds.find(v):
            ds.union(u,v)
            mst.append((u,v,weight))
            total_wt+=weight


        if len(mst)==num_nodes-1:
            break
    return mst,total_wt


edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]
num_nodes = 4

mst,total_wt=Kruskal_algorithm(edges,num_nodes)
print("mst",mst,"total_wt",total_wt)



# time c0mplexity:  O(E log E) E= numbner of edges

# overall time complexity of Kruskal's algorithm would improve to O(E log E + E α(n)), which simplifies to O(E log E) for most practical cases.
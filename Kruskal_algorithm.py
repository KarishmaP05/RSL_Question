
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

    edges.sort(key=lambda x:x[2])

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
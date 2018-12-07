from collections import defaultdict 
from sets import Set
import operator

#Class to represent a graph 
class Graph:   
    # function 
    def __init__(self,u,v):        
        self.edges={} #dictionary with all edges of the graph        
        self.vertices=defaultdict(set) #dictionary with neighbors
        
        #Parameters for DFS
        self.u=u #first node of the edge
        self.v=v #second node of the edge
        print("Edge to check %d-%d" % (u,v))
        self.w=None #contains the weigth of the  selected edge
        self.visited_vertices=set()
        self.not_in_mst=False
        
        #List for Kruskal
        self.graph = []
          
   
    # function to add an edge to graph 
    def addEdge(self,u,v,w):         
        #a frozenset can be used as dict's key 
        self.edges[frozenset([u,v])]=w
        #store a dict with neighbors
        self.vertices[u].add(v)
        self.vertices[v].add(u)
        
        #store for Kruskal
        self.graph.append([u,v,w]) #add as list

        
    def dfsTraversal(self,v,level=0):
        self.visited_vertices.add(v)
        print("%sVisiting : %d" % (''.join(['\t' for t in range(level)]),v))
        
        for z in self.vertices[v]:
            if not z in self.visited_vertices and self.edges[frozenset([v,z])] < self.w:
                if self.v == z:
                    self.not_in_mst=True
                    print("%sReached edge: %s" % (''.join(['\t' for t in range(level)]), self.v))
                else:
                    print("%s> %d --> %d" % (''.join(['\t' for t in range(level)]),v,z))
                    self.dfsTraversal(z, level+1)
        
            
    def isEdgeInMST(self):
        self.w=self.edges[frozenset([self.u, self.v])]
        self.dfsTraversal(self.u)
        return not self.not_in_mst

        
    # Search the set of an element
    def find(self, p, x): 
        if p[x] == x: 
            return x 
        return self.find(p, p[x]) 
  
    # An union of set
    def union(self, p, rank, x, y): 
        xr = self.find(p, x) 
        yr = self.find(p, y) 
  
        # Attach smaller rank tree under root of  
        # high rank tree (Union by Rank) 
        if rank[xr] < rank[yr]: 
            p[xr] = yr 
        elif rank[xr] > rank[yr]: 
            p[yr] = xr 
  
        # If ranks are same, then make one as root  
        # and increment its rank by one 
        else : 
            p[yr] = xr 
            rank[xr] += 1
  
    # The main function to construct MST using Kruskal's  
        # algorithm 
    def KruskalMST(self): 
        result =[] 
        parent = [];
        rank = [] 
        vertices_number=len(self.vertices)
        i = 0
        e = 0
  
        # sort all the edges
        #self.graph = sorted(self.graph, key=lambda item: item[2]) 
        self.graph = sorted(self.graph, key=operator.itemgetter(2)) 
        
        #remove the edge and insert at the head of the list
        #self.graph.remove([self.u, self.v, self.w])
        #self.graph.insert(0,[self.u, self.v, self.w])
        
  
        # for each vertice create elements
        for node in self.vertices: 
            parent.append(node) 
            rank.append(0) 
      
        # the number of the edge in MST cannot be > of number of vertices 
        while e < vertices_number -1 : 
  
            #pick the edge and its weight
            u,v,w =  self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent ,v) 
  
            #if we have not caused any cycle
            if x != y: 
                e = e + 1     
                result.append([u,v,w]) 
                self.union(parent, rank, x, y)             
    
        
        print "Edges in MST:"
        for u,v,weight  in result: 
            print ("%d -- %d == %d" % (u,v,weight)) 
def main():
    #Creates a graph and specify the edge to check
    g = Graph(1,3) 
    g.addEdge(0, 1, 9) 
    g.addEdge(0, 2, 3) 
    g.addEdge(0, 3, 2) 
    g.addEdge(1, 3, 11) 
    g.addEdge(1, 4, 7) 
    g.addEdge(2, 3, 4) 

    
    if g.isEdgeInMST():
        g.KruskalMST()


if __name__ == "__main__":
    main()  
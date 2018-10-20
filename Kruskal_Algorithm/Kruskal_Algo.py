# Kruskal Algorithm to find the Minimum Spanning Tree
# using Union Find Data Structure (Disjoint Set)

# Function to make ne Nodes/Vertex
# Vertex  in given Graph
class Vertex(object):
    def __init__(self, name):
        self.name = name
        # Node in the Disjoint Set
        self.node = None


# Nodes in the Disjoint Set
# In the begenning, we assign a Node in the Disjoint Set corresponding to each Vertex in the Graph
# Keep on Merging the Nodes in the Disjoint Set till only one Set is left with no more Nodes to be Merged.
# Rule to Merge: Merge if the starting Node and Target Node are in different Set.
# Skip the edges if Starting Edge and Target Edge are both in the same Set.
class Node(object):
    # height: height of Disjoint structure represented by a Tree
    # nodeId:
    def __init__(self, height, nodeId, parentNode):
        self.height = height
        self.nodeId = nodeId
        self.parentNode = parentNode


# Function to generate Edges between Vertex/Nodes in Graph
class Edge(object):
    def __init__(self, weight, startVertex, targetVertex):
        self.weight = weight
        self.startVertex = startVertex
        self.targetVertex = targetVertex

    # Compare two Edges According to Weight Parameter
    def __cmp__(self, otherEdge):
        return self.cmp(self.weight, otherEdge.weight)

    def __lt__(self, other):
        selfPriority = self.weight
        otherPriority = other.weight
        return selfPriority < otherPriority


# Define the Disjoint Set
class DisjointSet(object):
    # vertexList: contains list of Vertices in a given Graph as we need to map Nodes in Disjoint Set to Vertices
    def __init__(self, vertexList):
        self.vertexList = vertexList
        # rootNodes: Root of the Disjoint Sets
        # As many root Nodes as number of Nodes/Vertex in Graph
        self.rootNodes = []
        # Keep a count of number of nodes in the Set
        self.nodeCount = 0
        # Keep a count of number of sets of Nodes in a Disjoint Set
        self.setCount = 0
        # Make as many sets as the number of Vertex in Graph
        self.makeSets(vertexList)

    # Find Function of Disjoint Set DS
    # Go till the root Node (recursive(parent(currentNode))
    def find(self, node):
        currentNode = node
        while currentNode.parentNode is not None:
            currentNode = currentNode.parentNode
        root = currentNode
        currentNode = node

        # Path Compression
        while currentNode is not root:
            temp = currentNode.parentNode
            currentNode.parentNode = root
            currentNode = temp
        return root.nodeId

    # Function to Merge two Nodes
    def merge(self, node1, node2):
        # Returns node Id for node 1
        index1 = self.find(node1)
        index2 = self.find(node2)
        # The Nodes are in same Set; No need to merge them
        if index1 == index2:
            return
        root1 = self.rootNodes[index1]
        root2 = self.rootNodes[index2]
        # If root1 tree > root2 tree, merge them
        if root1.height < root2.height:
            root1.parentNode = root2
        elif root1.height > root2.height:
            root2.parentNode = root1
        else:
            root2.parentNode = root1
            root1.height = root1.height + 1

    # Function to Make Sets by merging nodes
    def makeSets(self, vertexList):
        for v in vertexList:
            self.makeSet(v)

    def makeSet(self, vertex):
        node = Node(0, len(self.rootNodes),None)
        vertex.node = node
        self.rootNodes.append(node)
        self.setCount = self.setCount + 1
        self.nodeCount = self.nodeCount + 1

# Kruksal Algorithm Implementation
class KruskalAlgorithm(object):
    def __init__(self, tong):
        self.__tong = tong
    #
    def set_tong(self, tong):
        self.__tong = tong
    #
    def get_tong(self):
        return self.__tong
    #
    def spanningTree(self, vertexList, edgeList):
        disjointSet = DisjointSet(vertexList)
        spanningTree = []
        # Sort the Edge list in Ascending Order
        edgeList.sort()

        for edge in edgeList:
            u = edge.startVertex
            v = edge.targetVertex
            # If both nodes are in distinct sets, we can use that edge
            if disjointSet.find(u.node) is not disjointSet.find(v.node):
                spanningTree.append(edge)
                disjointSet.merge(u.node, v.node)

        for edge in spanningTree:
            print(edge.startVertex.name," - ", edge.targetVertex.name)
            self.__tong += edge.weight




# --------------------- Testing ---------------------
if __name__ == '__main__':

    vertex1 = Vertex("a") #1
    vertex2 = Vertex("b") #2
    vertex3 = Vertex("c") #3
    vertex4 = Vertex("d") #4
    vertex5 = Vertex("e") #5
    vertex6 = Vertex("f") #6
    vertex7 = Vertex("g") #7
    vertex8 = Vertex("h") #8
    vertex9 = Vertex("i") #9
    vertex10 = Vertex("j") #10
    vertex11 = Vertex("k") #11
    vertex12 = Vertex("l") #12

    edge1 = Edge(2, vertex1, vertex2)
    edge2 = Edge(3, vertex2, vertex3)
    edge3 = Edge(1, vertex3, vertex4)
    edge4 = Edge(4, vertex5, vertex6)
    edge5 = Edge(3, vertex6, vertex7)
    edge6 = Edge(3, vertex7, vertex8)
    edge7 = Edge(3, vertex9, vertex10)
    edge8 = Edge(3, vertex10, vertex11)
    edge9 = Edge(1, vertex11, vertex12)
    edge10 = Edge(3, vertex1, vertex5)
    edge11 = Edge(4, vertex5, vertex10)
    edge12 = Edge(1, vertex2, vertex6)
    edge13 = Edge(2, vertex6, vertex10)
    edge14 = Edge(2, vertex3, vertex7)
    edge15 = Edge(4, vertex7, vertex11)
    edge16 = Edge(5, vertex4, vertex8)
    edge17 = Edge(3, vertex8, vertex12)

    vertexList = []
    vertexList.append(vertex1)
    vertexList.append(vertex2)
    vertexList.append(vertex3)
    vertexList.append(vertex4)
    vertexList.append(vertex5)
    vertexList.append(vertex6)
    vertexList.append(vertex7)
    vertexList.append(vertex8)
    vertexList.append(vertex9)
    vertexList.append(vertex10)
    vertexList.append(vertex11)
    vertexList.append(vertex12)

    edgeList = []
    edgeList.append(edge1)
    edgeList.append(edge2)
    edgeList.append(edge3)
    edgeList.append(edge4)
    edgeList.append(edge5)
    edgeList.append(edge6)
    edgeList.append(edge7)
    edgeList.append(edge8)
    edgeList.append(edge9)
    edgeList.append(edge10)
    edgeList.append(edge11)
    edgeList.append(edge12)
    edgeList.append(edge13)
    edgeList.append(edge14)
    edgeList.append(edge15)
    edgeList.append(edge16)
    edgeList.append(edge17)

    algorithm = KruskalAlgorithm(tong=0)
    algorithm.spanningTree(vertexList, edgeList)
    print ("Chi phí nhỏ nhất là: ", algorithm.get_tong())

# ----------------------------- EOC --------------------------------
# Dijkstra Algorithm using Python 3

import sys

# Import Heap Functions to get the Min. Heap Root Value
import heapq

# Edge in the Graph from one node to other
class Edge(object):
    # weight of each edge, starting Vertex and Target Vertex.
    # ex. Starting Vertex: A; End Vertex: G
    def __init__(self, weight, startVertex, targetVertex):
        self.weight = weight
        self.startVertex = startVertex
        self.targetVertex = targetVertex


# Function for Nodes in a Graph
class Node(object):
    def __init__(self, name):
        # Name of the Node (string)
        self.name = name
        # Boolean; check if node visited or not
        self.visited = False
        # Save the predecessor to each current node
        self.predecessor = None
        # List of neighbors to each node
        self.adjacencyList = []
        # Minimum Distance from starting node to other nodes in Graph
        self.minDistance = sys.maxsize

    # Function that defines on what basis we select a minimum Node: "minimum Distance"
    # Required to tell the Heap that which node is the minimum Node and that is the Root
    # Orders the nodes according to Minimum Distance before adding to the Heap.
    # A Node is selected if the distance between Current Node and Node to be reached is smaller than other Nodes.

    # Step where we check for smallest weight in Heap Content and select it for next step
    def __cmp__(self, otherVertex):
        return self.cmp(self.minDistance, otherVertex.minDistance)

    # Less than method to define on what basis a minimum Node is selected
    def __lt__(self, other):
        selfPriority = self.minDistance
        otherPriority = other.minDistance
        return selfPriority < otherPriority



# Dijkastra Algorithm Implementation
class DijkstraAlgorithm(object):

    # Function to Calculate the Shortest Path
    # Requires List of Vertex and the starting Vertex "A".
    def calculateShortestPath(self, vertexList, startVertex):
        # Implementing Heap using 1-D array
        q = []
        # The min Distance of the starting vertex "A" is "0".
        startVertex.minDistance = 0
        # Push the Heap: "q" and the item: startVertex "A" onto the Heap
        heapq.heappush(q, startVertex)

        # While the heap "q" has items in it
        while q:
            # Pop the item from heap, it pops the Root Node
            # Since, we use the cmp and lt functions to get only the minimum node,
            # so the minimum Node is Popped out of Heap.
            actualVertex = heapq.heappop(q)

            for edge in actualVertex.adjacencyList:
                u = edge.startVertex
                v = edge.targetVertex
                # Calculate weight from A -> B, A -> E, A -> H
                newDistance = u.minDistance + edge.weight

                # Since, initially all Nodes except the start node have a weight of Infinity
                # Hence, A=0, B=infinity, A -> B, edge weight: 5, so weight of B = 0+5 = 5
                if newDistance < v.minDistance:
                    v.predecessor = u
                    v.minDistance = newDistance
                    # Update the Heap with new weights of eaach node
                    heapq.heappush(q,v)

    def getShortestPath(self, targetVertex):
        print('Shortest Path to vertex is: ', targetVertex.minDistance)
        # Target Vertex Node
        node = targetVertex
        # Backtrack from the Target Node to the starting node using Predecessors
        while node is not None:
            print('%s' % node.name)
            node = node.predecessor



# -------------------------- Testing ------------------------------
if __name__ == '__main__':
    # Create Nodes
    node1 = Node('A')
    node2 = Node('B')
    node3 = Node('C')
    node4 = Node('D')
    node5 = Node('E')
    node6 = Node('Z')


    # Create Edges
    # Edge Weight, Starting Vertex, Ending Vertex
    edge1 = Edge(4,node1, node2)
    edge2 = Edge(2, node1, node3)
    edge3 = Edge(1, node2, node3)
    edge4 = Edge(5, node2, node4)
    edge5 = Edge(8, node3, node4)
    edge6 = Edge(10, node3, node5)
    edge7 = Edge(2, node4, node5)
    edge8 = Edge(6, node4, node6)
    edge9 = Edge(3, node5, node6)
    edge10 = Edge(1, node3, node2)

    # Adjacency List, append edges
    node1.adjacencyList.append(edge1)
    node1.adjacencyList.append(edge2)
    node2.adjacencyList.append(edge3)
    node2.adjacencyList.append(edge4)
    node2.adjacencyList.append(edge10)
    node3.adjacencyList.append(edge3)
    node3.adjacencyList.append(edge5)
    node3.adjacencyList.append(edge6)
    node2.adjacencyList.append(edge10)
    node4.adjacencyList.append(edge4)
    node4.adjacencyList.append(edge5)
    node4.adjacencyList.append(edge7)
    node4.adjacencyList.append(edge8)
    node5.adjacencyList.append(edge6)
    node5.adjacencyList.append(edge7)
    node5.adjacencyList.append(edge9)
    node6.adjacencyList.append(edge8)
    node6.adjacencyList.append(edge9)
    # Vertex List
    vertexList = (node1, node2, node3, node4, node5, node6)

    algorithm = DijkstraAlgorithm()
    # Calculate Shortest Path with start Vertex node1 : "A"
    algorithm.calculateShortestPath(vertexList, node1)
    # Get the Shortest Path from node1: "A" to node6: "Z"
    algorithm.getShortestPath(node6)


# ----------------------------- EOC -------------------------------
import math
import copy

graph = {}
#nodes
graph["Start"] = {}
graph["A"] = {}
graph["B"] = {}
graph["End"] = {}
#node connections
graph["Start"]["A"] = 6
graph["Start"]["B"] = 2
graph["A"]["End"] = 1
graph["B"]["A"] = 3
graph["B"]["End"] = 5


#2/5/18
def DijstrasAlgo(graph, startNode):
    parents = {}
    shortest = {}
    solved = []
    solved.append(startNode)

    #creating the shortest dict
    for x in graph:
        shortest[x] = math.inf

    #adding costs for start node
    shortest[startNode] = 0
    for y in graph[startNode]:
        shortest[y] = graph[startNode][y]

    #creating parents
    parents = {}
    for z in graph:
        parents[z] = None
        
    #adding all known node parents
    for c in graph[startNode]:
        parents[c] = startNode

    nextNode = startNode
    for l in graph:
        proCheck = False
        #shortest from node
        while proCheck == False:
            nextNodeList = copy.deepcopy(graph[nextNode])
            node = min(nextNodeList, key=nextNodeList.get)
            print("Lowest cost from", startNode, "to node", node, "is", graph[startNode][node])
            if node in solved:
                proCheck = False
                nextNodeList[node] = math.inf
            else:
                proCheck = True
        #neighbours of node
        neighbours = graph[node]
        print("Node", node, "is neighbours with", neighbours)

        #updating shortest path from node
        for x in neighbours:
            print("node", x, graph[node][x])
            currentNodeCost = shortest[node]
            newCost = currentNodeCost + graph[node][x]
            if newCost < shortest[x]:
                shortest[x] = newCost
                parents[x] = node
        print(shortest)
        
        solved.append(node)
        
    print(shortest)
        






DijstrasAlgo(graph, "Start")
























'''
#display
print(graph.keys())
for x in graph:
    print("Node: ", x)
    print("Connected to")
    for y in graph[x]:
        print(y, "distance =",graph[x][y])
    print("\n")


#path
infinity = math.inf #float("inf")
shortest = {}
for x in graph:
    shortest[x] = infinity #infinity as no path found as of yet

current_node = None # current node of iteration
next_nodes = []

order = ["Start","A","B","End"]
startNode = order[0]


for x in order:
    for y in graph[x]:
        if len(next_nodes) == 0 or graph["Start"][next_nodes[len(next_nodes)-1]] > graph["Start"][y]:
            next_nodes.insert(0, y)
        else:
            pass

    
print(min(graph[startNode], key=graph[startNode].get)) #gets shortest from nbode
print(shortest)
'''

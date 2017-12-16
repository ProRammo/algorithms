## DIJKSTRA'S ALGORITHM
## Mostapha Rammo
## 2017.12.10

## Before beginning I need to think about what king of data structures I'm going
# to need to implement this and how I want to represent my graph.

## When implementing Dijkstra's we're going to need to keep track of:
	# the CURRENT shortest path to every node
	# the nodes who have a FINAL shortest path
	# every nodes parent
	# all of the unvisited nodes (Priority Queue)


## We define our graph variables

# the weighted graph is set up like so
# { node : {weights : [int], adjacents : [int]} }
graph = {
	"A": {
		"weights": [1, 5],
		"adjacents": ["B", "C"]
	},
	"B": {
		"weights": [1, 6, 9, 7],
		"adjacents": ["A", "C", "D", "E"]
	},	
	"C": {
		"weights": [5, 6, 3, 8],
		"adjacents": ["A", "B", "D", "E"]
	},
	"D": {
		"weights": [9, 3, 2],
		"adjacents": ["B", "C", "E"]
	},
	"E": {
		"weights": [7, 8, 2],
		"adjacents": ["B", "C", "D"]
	}
}

## current shortest path to every node
# should be initialized to infinity for all nodes
# {node: shortest path}
d = {}

# Final shortest paths to every node
# {node: shortest path}
S = {}

## @params: node, adj
# @return: weight between nodes
def weight(node, adj):
	index = graph[node]["adjacents"].index(adj)
	return graph[node]["weights"][index]

## extract value from queue
def q_extract_min(array):
	minVal = None
	for node in array:
		if (d[node] == -1):
			continue
		if (minVal == None or minVal > d[node]):
			minVal = d[node]
			index = array.index(node)
	tmp = array[index]
	del array[index]
	return tmp
		
	

def dijkstra(graph, startNode):
	## initialize variables
	queue = []
	prev = {}	# {node: prev. node}
	for node in graph:
		## We're initializing all nodes to -1, here we're assuming there
		# are no negative weights
		d[node] = -1
		## we want to initialize the queue with all our vertices (nodes)
		queue.append(node)
	d[startNode] = 0
	prev[startNode] = None
	S = []

	while ( not len(queue) == 0):
		u = q_extract_min(queue)
		S.append(u)
		for v in graph[u]["adjacents"]:
			if (v in S):
				continue
			## now we need to check for a shorter path to each adjacent
			if (d[v] == -1 or d[v] > d[u] + weight(v,u)):
				d[v] = d[u] + weight(v,u)
				prev[v] = u


dijkstra(graph, "A")
print(d)







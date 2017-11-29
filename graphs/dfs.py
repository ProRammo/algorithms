
# Mostapha Rammo
# 2017.11.29
# My implementations of depth-first search

################################
### RECURSIVE IMPLEMENTATION ###
################################

## This implementation includes a parent variable, and always checks every node in the graph.
# Here I also try starting from every node in the graph to cover disconnected nodes, this can also
# be done in my other method.  I'm showing both ways for sake of example and need.

## checking for cycles part is disbled, uncomment below to enable
def dfs_visit2(graph, startNode, parent, visited):
	#visited.append(startNode)	## cycle detection
	for adj in graph[startNode]:
		#if adj in visited:		## cycle detection
			#print("cycle")		## cycle detection
		if (adj not in parent):
			parent[adj] = startNode
			dfs_visit2(graph, adj, parent, visited)

def dfs_r2(graph):
	parent = {}	## Parent should have all nodes that have been globally visited
			# at the end of this function

	visited = [] 		## This is used when looking for a cycle,
				# we need to keep track of visited nodes from each outer
				# start node.

	for node in graph:
		if (node not in parent):
			parent[node] = None
			dfs_visit(graph, node, parent, visited)


## Here I only explicitly keep track of what's visited, we need a dfs_visit function because
# the visited list needs to be initialized to [] at every dfs call.  It is of my knowledge that there
# is no C like static variables in python that keep their values over recurrent function calls and
# global variables introduce many other problems
def dfs_visit(graph, currentNode, visited):
	print(currentNode)
	visited.append(currentNode)
	for adj in graph[currentNode]:
		if (adj not in visited):
			dfs_visit(graph, adj, visited)
			

def dfs_r(graph, startNode):
	visited = []
	dfs_visit(graph, startNode, visited)


################################
### ITERATIVE IMPLEMENTATION ###
################################

def dfs(graph, startNode):
	visited = []	
	stack = []
	stack.insert(0, startNode)
	while (len(stack) > 0):
		currentNode = stack.pop(0)
		if (currentNode not in visited):
			visited.append(currentNode)
			print(currentNode)
			for adj in graph[currentNode]:
				stack.insert(0, adj)

#################
### MAIN CODE ###
#################

G = {1: [2,3,4], 2: [], 3: [1,3,4], 4: [1, 2]}

dfs_r(G,1)






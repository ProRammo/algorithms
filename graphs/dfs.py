
# Mostapha Rammo
# 2017.11.29

###############################
### RECURSIVE IMPLEMENTATION###
###############################

## checking for cycles part is disbled, uncomment below to enable
def dfs_visit(graph, startNode, parent, visited):
	#visited.append(startNode)	## cycle detection
	for adj in graph[startNode]:
		#if adj in visited:		## cycle detection
			#print("cycle")		## cycle detection
		if (adj not in parent):
			parent[adj] = startNode
			dfs_visit(graph, adj, parent, visited)


def dfs_r(graph):
	parent = {}	## Parent should have all nodes that have been globally visited
			# at the end of this function

	visited = [] 		## This is used when looking for a cycle,
				# we need to keep track of visited nodes from each outer
				# start node.

	for node in graph:
		if (node not in parent):
			parent[node] = None
			dfs_visit(graph, node, parent, visited)
	
	print(parent)


################################
### ITERATIVE IMPLEMENTATION ###
################################

def dfs(graph):
	parent = {}		## Parent should have all the nodes that have been globally visited
				# at the end of this function
	for node in graph:
		if (node not in parent):
			stack = [node]
			while (len(stack) > 0):
				currentNode = stack.pop(0)
				if (currentNode not in parent): parent[currentNode] = None
				for adj in graph[currentNode]:
					if (adj not in parent):	 
						parent[adj] = currentNode
						stack.insert(0, adj)

	print(parent)				


G = {5: [1], 4: [1], 1: [5], 3:[]}

dfs(G)


# Mostapha Rammo
# 2017.11.29
# Topological sort is done using depth-first search, if there is any confustion go check dfs.py

## topological sort only works on directed acyclic graphs, here I am assuming that's what I'm given

## We want to visit every node in the graph unconditionally, so we'll do it recursively with
# a ts_visit function

def ts_visit(graph, currentNode, visited, stack):
	visited.append(currentNode)
	for adj in graph[currentNode]:
		if (adj not in visited):
			ts_visit(graph, adj, visited, stack)
	stack.insert(0, currentNode)

def t_sort(graph):
	visited = [] 		## Use this now to also keep track of order !
	stack = []	

	for node in graph:
		if (node not in visited):
			ts_visit(graph, node, visited, stack)

	print(stack)
	return stack

####################
### TESTERS CODE ###
####################



#G = {8:[],1: [2], 2: [], 3: [2,4], 4:[5], 5:[], 6: [4,7], 7: [5]}
G = {2: [], 6: [4,7], 8:[], 5:[], 4:[5], 1:[2], 3:[2,4], 7:[5]}

t_sort(G)



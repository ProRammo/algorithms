# Mostapha Rammo
# 2017.11.28
# My implementation of breadth-first search

################################
### ITERATIVE IMPLEMENTATION ###
################################

def bfs(graph, startNode):
	queue = []
	visited = []
	
	queue.append(startNode)
	while (len(queue) > 0):
		currentNode = queue.pop(0)
		if (currentNode not in visited): 
			visited.append(currentNode) 
			print(currentNode)

			for adj in graph[currentNode]:
				queue.append(adj)


G = {1: [2,3,4], 2: [], 3: [4,1,3], 4: [2,1]}

bfs(G, 1)

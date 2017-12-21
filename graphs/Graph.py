## GRAPH.PY
## MOSTAPHA RAMMO
## Semi generic graph class, I'm making this keep making the graph less of a hassle
# and focus more on the fun algorithms.  Works with integer keys.

## Basic node class, a node will have a key and a set of adjacent nodes
class Node:
	def __init__(self, key):
		self.key = key
		self.adjacents = []
		## Dictionary of weights, { node_key : corresponding edge weight }
		self.weights = {}

class Graph:

	## Theoretically a graph can't exist without any nodes, however I can see
	# advantages in implementiation if I set it up without an initial node.
	## We'll call the graph a null-graph if it has no nodes.
	def __init__(self):
		self.nodes = []

	## Let's create a method to check whether our graph is null or not
	def isNull(self):
		if (len(self.nodes) == 0): return True
		return False

	## We should be able to check if a node is in the graph
	## For now we will check by key, until I figure out a better way
	def hasNode(self, key):
		for node in self.nodes:
			if (node.key == key):
				return True
		return False

	## Also need to be able to get the node obj based on its key
	def getNode(self, key):
		for node in self.nodes:
			if (node.key == key):
				return node
		return None   ## no node found

	## Now we need to be able to add a node to our graph. Should the user input
	# an actual node object, or just its key?
	## I've decided to go with inputing a key as a parameter to make it
	# more abstract
	def addNode(self, key):
		## For now, we will assume each node needs a unique key
		if (self.hasNode(key)):
			return False
		newNode = Node(key)
		self.nodes.append(newNode)
		return True

	## When adding edges, we should input either two existing nodes(keys) or 
	# one existing node(key) and one new node(key) respectively.
	## Weights are default 1 when not specified.
	## Edge is undirected by default
	def addEdge(self, a, b, w=1):

		## check if first node doesn't exist, this takes care of the case
		# where both don't exist and the case where only the second
		# one exists, both cases result in error
		if (not self.hasNode(a)):
			return False

		## Since our addNode function already checks if a node exists and
		# only adds it otherwise, we can just try to add node b.
		self.addNode(b);

		## At this point we know both nodes exist
		## Add an edge between them
		a = self.getNode(a)
		b = self.getNode(b)
		a.adjacents.append(b)
		a.weights[b.key] = w
		b.adjacents.append(a)
		b.weights[a.key] = w

		return True

	## find the weight between two edges
	def weight(self, a, b):
		a = self.getNode(a)
		b = self.getNode(b)
		if (not b.key in a.weights):
			return false
		return a.weights[b.key]

	## I want to be able to see how the graph looks, going to implement a 
	# print function
	def print(self):
		print("================")
		print("---------------")
		for node in self.nodes:
			print(node.key, "is adjacent to", node.weights)
			print("----------------")
		print("================")

	
	######################
	## GRAPH ALGORITHMS ##
	######################

	## extracts element with minimal dist.
	def __queue_extract_min(self, q, d):
		minimal = None
		for node in q:
			if (d[node] == -1):
				continue
			if (minimal == None or minimal > d[node]):
				minimal = d[node]
				index = q.index(node)
		tmp = q[index]
		del q[index]
		return tmp

	## finds the shortest path length between two nodes using dijkstra's
	def dijkstra(self, a, b):
		a = self.getNode(a)
		b = self.getNode(b)

		## make sure nodes exist
		if (a == None or b == None):
			return False
		
		## current shortest path for every node
		# { node : distance}	
		d = {}

		## Final shortest path for every node
		# { node.key : distance }
		S = {}

		## Queue of all current nodes
		queue = []
		for node in self.nodes:
			## init distances to -1 (representing infinity)
			d[node] = -1
			## init queue with all nodes
			queue.append(node)
		d[a] = 0
		
		while (not len(queue) == 0):
			u = self.__queue_extract_min(queue, d)
			S[u.key] = d[u]
			if (u.key == b.key):
				return S[u.key]
				
			for v in u.adjacents:
				if (v.key in S):
					continue
				if (d[v] == -1 or d[v] > d[u]+ self.weight(v.key, u.key)):
					d[v] = d[u] + self.weight(v.key, u.key)	

G = Graph()

G.addNode("A")
G.addNode("B")
G.addNode("C")
G.addNode("D")
G.addNode("E")

G.addEdge("A", "B", 1)
G.addEdge("A", "C", 5)

G.addEdge("B", "A", 1)
G.addEdge("B", "C", 6)
G.addEdge("B", "D", 9)
G.addEdge("B", "E", 7)

G.addEdge("C", "A", 5)
G.addEdge("C", "B", 6)
G.addEdge("C", "D", 3)
G.addEdge("C", "E", 8)

G.addEdge("D", "B", 9)
G.addEdge("D", "C", 3)
G.addEdge("D", "E", 2)

G.addEdge("E", "B", 7)
G.addEdge("E", "C", 8)
G.addEdge("E", "D", 2)

G.print()

for node in G.nodes:
	print(G.dijkstra("A", node.key))




	

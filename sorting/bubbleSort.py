## BUBBLE SORT
## MOSTAPHA RAMMO	
## 2017.12.16

array = [9,6,1,5,37,1,5241,32]

def swap(array, a, b):
	tmp = array[a]
	array[a] = array[b]
	array[b] = tmp

def bubble(array):
	sorted = False
	for i in range(0, len(array)-1):
		sorted = True
		for j in range(0, len(array)-1-i):
			if (array[j] > array[j+1]):
				swap(array, j, j+1)
				sorted = False
		if (sorted):
			break;
print(array)
bubble(array)
print(array)

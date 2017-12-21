

array = [7, 2, 5, 1, 10, 9, 1, 3]


def swap(array, a, b):
	tmp = array[a]
	array[a] = array[b]
	array[b] = tmp

def selectionSort(array):
	for i in range(0, len(array)-1):
		for j in range(i, len(array)):
			if (array[j] < array[i]):
				swap(array, i, j)

print(array)
selectionSort(array)
print(array)


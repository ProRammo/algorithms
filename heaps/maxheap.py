
class MyHeap:

    ############################
    ######### HELPERS ##########
    ############################

    def __isLeaf(self, array, position):
        if (position*2 >= len(array)):
            return True
        return False

    def __hasRightChild(self, array, position):
        if ( 1+position*2 < len(array) ):
            return True
        return False

    def __getRightChild(self, array, position):
        if (self.__hasRightChild(array, position)):
            return array[1+position*2]
        return None

    def __getLeftChild(self, array, position):
        if (not self.__isLeaf(array, position)):
            return array[position*2]
        return None

    def __getParent(self, array, position):
        return array[position//2]

    def __swap(self, array, pos1, pos2):
        tmp = array[pos1]
        array[pos1] = array[pos2]
        array[pos2] = tmp
        return array

    ############################
    ######### METHODS ##########
    ############################

    # O(lg n)
    def __heapify(self, array, position):

        # BASE CASE for recursive calls
        # if no left child (node is a leaf), return 
        if (self.__isLeaf(array, position)):
            return

        childPos = position*2
        if (self.__hasRightChild(array, position) and self.__getRightChild(array, position) > self.__getLeftChild(array, position)):
            childPos += 1

        # compare node with larger child
        if ( array[position] < array[childPos] ):
            self.__swap(array, position, childPos)
            self.__heapify(array, childPos)

        return array

    def is_max_heap(self, array):
        return self.__is_max_heap(array, 1)

    def __is_max_heap(self, array, position):
        if (self.__isLeaf(array, position)):
            return True
        if ( self.__getLeftChild(array, position) > array[position] ):
            return False
        if ( self.__hasRightChild(array, position) and self.__getRightChild(array, position) > array[position] ):
            return False

        if (self.__hasRightChild(array, position)):
            return self.__is_max_heap(array, 1+position*2) and self.__is_max_heap(array, position*2)
        else:
            return self.__is_max_heap(array, position*2)

    # 0(n)
    def build_max_heap(self, array):
        for i in range(len(array)//2, 0, -1):
                self.__heapify(array, i)
        return array

    def extract_max(self, array):
        val = array[1]
        del array[1]
        self.build_max_heap(array);
        return val

    def sort(self, a):
        array = [0] + a
        a = []
        self.build_max_heap(array)
        while (len(array) > 1):
            a.append(self.extract_max(array))
        return a


    def insert(self, array, item):
        array[0] += 1
        array.append(item)
        position = len(array)-1
        while ( position > 1 and array[position] > self.__getParent(array, position) ):
            self.__swap(array, position//2, position)
            position = position//2
        return array





heap = MyHeap()

array = [3, 6, 1, 10, 20, 14]

array = heap.sort(array)
print(array)
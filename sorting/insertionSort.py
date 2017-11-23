# Mostapha Rammo
#

def swap(i, list):
    tmp = list[i-1]
    list[i-1] = list[i]
    list[i] = tmp
    return list


# This uses O(n^2), which is fine assuming
# swapping costs and comparing costs are O(1).
# However, comparing some records may be cost heavy,
# so we want to improve the sort, or more specifically
# improve the amount of times we need to compare.
# Do this using binary search to find the correct position,
# instead of constant comparing
def insertionSort(list):
    for i in range(1, len(list)):
        pos = i
        while ( list[pos] < list[pos-1] ):
            if (pos == 0): break
            list = swap(pos, list)
            pos = pos - 1

    return list;



#####################
###### MAIN #########
#####################

list = [5,2,4,6,1,3]
print(rightShift(2, list))



def swap(positions, list):
    x, y = positions
    tmp = list[x]
    list[x] = list[y]
    list[y] = tmp
    return list
    
def twoFinger(list1, list2):
    p1, p2 = (0,0)
    newList = []

    while( p1 < len(list1) and p2 < len(list2) ):
        if (list1[p1] > list2[p2]):
            newList.append(list2[p2]);
            p2 += 1
        else:
            newList.append(list1[p1]);
            p1 += 1

    if ( p1 < len(list1) ):
        newList += list1[p1:]
    elif ( p2 < len(list2) ):
        newList += list2[p2:]

    return newList
            
            

def mergeSort(list):
    # BASE CASES   

    if (len(list) == 1):
        return list
    
    # RECURSIVE LOOP

    mid = len(list)//2
    list1 = list[0:mid]
    list2 = list[mid:]

    return twoFinger(mergeSort(list1), mergeSort(list2))
    


list = [5,2,4,6,1,3]
print(mergeSort(list))  
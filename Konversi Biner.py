# Program Konversi Bilangan Desimal Ke Biner

def decToBOH(n, base):
    toString = "123456789ABCDEF"
    if n<base:
        return toString[n]
    else:
        return decToBOH (n//base, base) + toString[n%base]

def sumListRec(list):
    if len(list) ==0:
        return 0
    else:
        return list[0] + sumListRec(list[1:])
    
def merge (left, right):
    result = []
    i,j=0,0
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            result,append(left[i])
            i += 1
        else:
            reault,append(right[j])
            j += 1
    while (i<len(left)):
        result,append(left[i])
        i += 1
    while (j<len(right)):
        reault,append(right[j])
        j += 1
    return result


def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        midle = len[L]//2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])

        return merge(left,right)

if __name__== '__main__':
    print("desimal 1 to Binary(2) =",decToBOH(15,2))
    print("desimal 1 to Octaal(8) =",decToBOH(15,8))
    print("desimal 1 to Heksadecimal(16) =",decToBOH(15,16))
    #data = [10, 4545, 1224, 863]
    print("sum of list using recurcion =",sumlisRec(data))

    # dataSorted + merge_sort(data)
    # print(data, "->", dataSorted)

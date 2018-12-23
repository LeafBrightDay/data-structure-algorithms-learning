def merge(items, p, q, r):
    L = items[p:q+1]
    R = items[q+1:r+1]
    i = j = 0
    k = p ##start from 1st element of subarray.
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            items[k] = L[i]
            i+= 1
        else:
            items[k] = R[j]
            j+= 1
        k+= 1
    if j == len(R):
        items[k:r+1] = L[i:]  ##copy remained array


def mergesort(items, p, r):
    if p < r:
        q = int((p+r)/2)   ###ensure integer for odd array
        mergesort(items, p, q)
        mergesort(items, q+1, r)
        merge(items, p, q, r)

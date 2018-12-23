####Insertion sort
def insertion(l,seq='DESC'):
    order=seq
    if isinstance(l,list):
        length=len(l)
        for j in range(1, length):
            key=l[j] #temp store
            # insertion A[j] to the sorted seq A[1,j-1]
            i=j-1
            if order=='DESC':
                while i>=0 and l[i]<key:
                    l[i+1]=l[i] #swap
                    i-=1
                l[i+1]=key
            if order=='ASC':
                while i>=0 and l[i]>key:
                    l[i+1]=l[i] #swap
                    i-=1
                l[i+1]=key
        return l

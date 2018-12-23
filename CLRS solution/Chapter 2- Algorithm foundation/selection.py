def selection(l,seq='ASC'):
    order=seq
    length=len(l)
    if order=='ASC':
        for j in range(length-1):
            min_index=j
            for i in range(j+1,length):
                if l[i]<l[min_index]:
                    min_index=i
            temp=l[j]
            l[j]=l[min_index]
            l[min_index]=temp
        return l
    if order=='DESC':
        for j in range(length-1):
            max_index=j
            for i in range(j+1,length):
                if l[i]>l[max_index]:
                    max_index=i
            temp=l[j]
            l[j]=l[max_index]
            l[max_index]=temp
        return l

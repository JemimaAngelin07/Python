def bubbleSort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i] > nlist[i+1]:
                temp = nlist[i]
                nlist[i]=nlist[i+1]
                nlist[i+1]=temp

nlist=[12,34,5,6,89,90,34,23,12]
bubbleSort(nlist)
print(nlist)                
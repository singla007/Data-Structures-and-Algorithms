import random
size = 10000000
arr = [random.randint(1,size) for _ in range(size)]

def quicksort(arr,l,r):
    if l<r:
        p = partition(arr,l,r)
        quicksort(arr,l,p-1)
        quicksort(arr,p+1,r)
    return arr

def partition(arr,l,r):
    i = l-1
    pivot = arr[r]
    for j in range(l,r):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[r] = arr[r],arr[i+1]
    return i+1

# print(quicksort(arr,0,size-1))

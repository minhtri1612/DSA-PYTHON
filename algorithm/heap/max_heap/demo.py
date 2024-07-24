array = [10, 20, 15, 30, 40]
n = len(array)

def makeMaxHeap(arr, n):
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    return arr

def heapify(arr, n, i):
    largest = i 
    left = 2 * i + 1 
    right = 2 * i + 2 
    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] # swap

        heapify(arr, n, largest)

print(makeMaxHeap(array, n))

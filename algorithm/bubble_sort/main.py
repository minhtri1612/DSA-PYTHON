arr = [7, 3, 1, 5, 8, 9, 10, 56,21, 33]
print(arr)
n=len(arr)
def bubble_sort(arr,n):
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                tmp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=tmp
bubble_sort(arr,n)
print("sau khi thay doi:")
print(arr)
arr = [12, 11, 13, 5, 6]
print(arr)
n=len(arr)
def insertSort(arr,n):
    for i in range(1,n):
        temp=arr[i]
        j=i-1
        while j>=0 and arr[j]>temp:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=temp
insertSort(arr,n)
print("after edit:")
print(arr)
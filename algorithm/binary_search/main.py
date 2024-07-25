arr = [7, 3, 1, 5, 8, 9, 10, 22, 33]
arr.sort()
n=len(arr)
def binary_search(arr,left,right,x):
    if left<=right:
        middle=left+(right-left)//2
        if arr[middle]==x:
            return middle
        elif arr[middle]>x:
            return binary_search(arr,left,middle-1,x)
        elif arr[middle]<x:
            return binary_search(arr,middle+1,right,x)
        else:
            return -1
x=int(input("nhap so can tim:"))
index_x=binary_search(arr,0,len(arr)-1,x)
print(f"index cua {x}:",index_x)
            
arr=[4,1,3,5,7,8,9,22,13,42]
n=len(arr)
def linearSearch(arr,n,target):
    for i in range(n):
        if arr[i]==target:
            return True
        
    return False
print(arr)
target=int(input("nhap tu khoa can tim:"))
res=linearSearch(arr,n,target)
print(f"co {target} khong?:",res)
arr=[3,2,5,0,1,8,7,6,9,4]
def merge_sort(arr):
    if len(arr)>1:
        left_arr=arr[:len(arr)//2]
        right_arr=arr[len(arr)//2:]
        
        merge_sort(left_arr)
        merge_sort(right_arr)  
        
        i=0 #index for left array
        j=0 #index for right array
        k=0 #index for merge sort
        
        while i<len(left_arr) and j<len(right_arr):
            if left_arr[i]<right_arr[j]:
                arr[k]=left_arr[i]
                i+=1
                k+=1
            else:
                arr[k]=right_arr[j]
                j+=1
                k+=1

            
        while i<len(left_arr):
            arr[k]=left_arr[i]
            i+=1
            k+=1
            
        while j<len(right_arr):
            arr[k]=right_arr[j]
            j+=1
            k+=1

merge_sort(arr)
print(arr)    

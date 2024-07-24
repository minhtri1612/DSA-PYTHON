arr=[3,2,5,0,1,8,7,6,9,4]
def merge_sort(arr):
  if(len(arr)>1):
    left_array=arr[:len(arr)//2]
    right_array=arr[len(arr)//2:]
    
    merge_sort(left_array)
    merge_sort(right_array)

    i=0
    j=0
    k=0

    while i<len(left_array) and j <len(right_array):
      if arr[left_array] <arr[right_array]:
        arr[k]=arr[left_array]
        i+=1
        k+=1
      else:
        arr[k]=arr[right_array]
        j+=1
        k+=1
    
    if i<len(left_array):
      arr[k]=arr[left_array]
      i+=1
      k+=1

    if j<len(right_array):
      arr[k]=arr[right_array]
      j+=1
      k+=1

  merge_sort(arr)
  print(arr)

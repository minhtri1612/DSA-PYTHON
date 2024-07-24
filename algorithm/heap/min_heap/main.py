import heapq

data=[10,20,31,22,90,5]
heapq.heapify(data) #biến 1 danh sách thành 1 heap
print(data)
print(heapq.heappop(data))#pop phần tử đầu cũng như là phần tử nhỏ nhất
print(data)
heapq.heappush(data,3)#push 1 phần tử r heap
print(data)

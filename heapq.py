Usefull:
    
http://stackoverflow.com/questions/33024215/built-in-max-heap-api-in-python

import heapq

def _heappush_max(heap, item):
    heap.append(item)
    heapq._siftdown_max(heap, 0, len(heap)-1)

def _heappop_max(heap):
    lastelt = heap.pop() 
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        heapq._siftup_max(heap, 0)
        return returnitem
    return lastelt

h=[]
n = int(input())
i = 0
heapq._heapify_max(h)
while i<n:
        s = str(input())
        if s.split()[0] =='ExtractMax':
            print(_heappop_max(h))
        elif s.split()[0] =='Insert':
            _heappush_max(h,int(s.split()[1]))
        i = i + 1

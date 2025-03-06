from random import shuffle
# Merge Sort

test_list = [n for n in range(10)]
shuffle(test_list)
print(f"Test list is: {test_list}")

def heap_sort(l):
    # phase 1
    for i in range(len(l)):
        bubble_up(l, i)



def bubble_up(heap, index):
    while index > 0:
        parent = (index - 1) // 2
        if heap[index] > heap[parent]:
            heap[index], heap[parent] = heap[parent], heap[index]
            index = parent
        else:
            break

def bubble_down(heap, index):
    while index > len(heap)-1:
        left = (index * 2) + 1 
        right = (index * 2) + 2
        biggest = 0
        if left > len(heap)-1 and right <= len(heap)-1:
            biggest = right
        elif right > len(heap)-1 and left <= len(heap)-1:
            biggest = left
        elif right > len(heap)-1 and left > len(heap)-1:
            break
        else:
            biggest = left if heap[left] > heap[right] else right

        if heap[biggest] > heap[index]:
            heap[index], heap[biggest] = heap[biggest], heap[index]
            index = biggest
        else:
            break
        

heap_sort(test_list)
print(f"Heap sort: {test_list}")
shuffle(test_list)
    

def mergesort(l) -> list:
    n = len(l)
    if n > 1:
        l1 = l[:n//2]
        l2 = l[n//2:]
        mergesort(l1)
        mergesort(l2)
        merge(l1, l2, l)

def merge(l1, l2, l):
    f1 = 0
    f2 = 0
    while f1 + f2 < len(l):
        if f1 == len(l1):
            l[f1+f2] = l2[f2]
            f2 += 1
        elif f2 == len(l2):
            l[f1+f2] = l1[f1]
            f1 += 1
        elif l2[f2] < l1[f1]:
            l[f1+f2] = l2[f2]
            f2 += 1
        else:
            l[f1+f2] = l1[f1]
            f1 += 1

mergesort(test_list)
print(f"Merge sort: {test_list}")
shuffle(test_list)

# Quick Sort

def partition(l):
    pivot = l[0]
    bigger = -1
    smaller = len(l)

    while True:

        while True:
            bigger += 1
            if l[bigger] >= pivot:
                break

        while True:
            smaller -= 1
            if l[smaller] <= pivot:
                break

        if bigger <= smaller:
            l[smaller], l[bigger] = l[bigger], l[smaller]
        
        break

def insertion_sort(l):
    i = 1
    while i < len(l):
        j = i - 1
        while l[i] < l[j] and j > -1:
            j -= 1
        temp = l[i]
        k = i - 1
        while k > j:
            l[k+1] = l[k]
            k -= 1
        l[k+1] = temp
        i += 1

insertion_sort(test_list)
print(f"Insertion sort: {test_list}")
shuffle(test_list)


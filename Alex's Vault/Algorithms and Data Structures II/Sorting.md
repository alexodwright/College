## Bubble Sort

```Python
def bubble_sort(mylist):
	n = len(mylist)
	for i in range(n-1):
		for j in range(0, n-i-1):
			if mylist[j] > mylist[j+1]:
				mylist[j], mylist[j+1], mylist[j+1], mylist[j] 
```

- Worst case comparisons: (n-1) + (n-2) + ... + 1 = $0.5\times(n-1)\times n$ which is O($n^2$)
- Worst case number of swaps: initial list ordered in reverse requires a swap for each comparison so O($n^2$)

## Sorting using Priority Queue

A priority queue is a data structure to which we can add items, and from which we can remove the item with the top priority.

```python
def pq_sort(mylist):
	pq = Priority
```

*todo*

### Sorting with an unsorted linked list PQ

Selection sort: main task is selecting the next smallest item

Adding an item to the PQ is O(1), so cost of first loop is O(n)

Removing top item requires linear search over all items in the list, so n-1 comparisons.
Each time we remove an item, the list shrinks by 1, and we make 1 assignment back into our original (array-based) list.

So removing n items takes (n-1) + (n-2) + ... + 1 comparisons.
O($n^2$) comparisons, and n assignments

The base case is the same, as we have to search the entire doubly linked list for the smallest item, no guarantee of the position of the smallest element.

## In-place sorting

Sorting using a separate Priority Queue requires extra space.
An input list of size n will require a PQ implementation of size n as it operates.

In many applications, space in memory is restricted, and so we want to sort using only a small amount of extra space over the original input array.
- This is called in-place sorting.

Here we treat the unsorted input array as the PQ list implementation (so no build cost).
Instead of removing the top item, swap it to the correct cell, and shrink the 'view' of the PQ.

Firstly, find the smallest item and swap it with cell 0, then shrink the view of the PQ to not account for the first cell since we know it's the smallest of the original input array. Repeat.

```python
def selection_sort(mylist):
	n = len(mylist)
	i = 0
	while i < n:
		smallest = i
		j = i + 1
		while j < n:
			if mylist[j] < mylist[smallest]:
				smallest = j
			j += 1
		mylist[i], mylist[smallest] = mylist[smallest], mylist[i]
		i += 1
```

Here the worst and best cast are both O($n^2$) comparisons, and n swaps.

## Sorting with a sorted linked list PQ

Insertion sort: main task is inserting each item in the right place.

Adding an item to a sorted linked list of length n takes at most n comparisons, and if we are lucky, just 1 comparison. It takes 1 assignment (since this is a linked list).
So adding n items into an initially empty PQ takes 0 + 1 + 2 + ... + (n-1) = $0.5 \times (n-1) \times n$ = O($n^2$).

Removing top item is O(1).

Best case is O(n) comparisons.

### In-place insertion sort

Treat the unsorted input array as the stream of items to be added to the PQ list implementation, and gradually expand the sorted list from the front (i.e. growing the 'view' of the PQ).
Search the PQ to find the insertion place.
Copy the new item, shuffle the others down one place, insert the new item.

```python
def insertion_sort(mylist):
	n = len(mylist)
	i = 1
	while i < n:
		j = i - 1
		while mylist[i] < mylist[j] and j > -1:
			j -= 1
		# insert i in the cell after j
		temp = mylist[i]
		k = i - 1
		while k > j:
			mylist[k + 1] = mylist[k]
			k -= 1
		mylist[k + 1] = temp
		i += 1
```

Worst case is completely reverse sorted list: O($n^2$) comparisons, and O($n^2$) swaps.

Best case is O(n) comparisons and 0 swaps.

## Sorting with a Binary Heap PQ

Heap sort: all the action takes place with heap operations.

Adding an item to a binary heap which has n items takes O(log n) comparisons and swaps. So adding all n items takes log(2) + log(3) + ... log(n-1).
Each of these <= log(n), and there are <= n, so $n \times O(log n) = O(n \times log n)$ to build the PQ.

Removing the top item from the binary heap with n items takes O(log n), so by the same argument, to rebuild the array takes O(n log n) comparisons, and swaps.

So O(n log n) to sort using a binary heap.

## In-place Heap Sort

Treat the unsorted input array as the stream of items to be added to the PQ, like insertion sort, and gradually expand an array-based heap from the front (growing the 'view' of the PQ).

Next item added to the heap goes into the last position, so it is already in the right starting place. Now bubble up to find its correct position.

We want to use a max heap instead of a min heap.

### Phase 1

Treat the unsorted input array as the stream of items to be added to the PQ, like insertion sort, and gradually expand an array-based max heap from the front.

Next item added to the heap goes into the last position, so it is already in the right starting place. Now bubble up to find its correct position.

### Phase 2

At the end of phase 1, we have an array based max heap, with the biggest number at the front.

In the final output, we want the biggest item at the end. So remove it from the heap, copy the last item and then bubble it down, leaving the last place free to re-insert the biggest item.
Iterate until the (virtual) heap is empty, and we have a sorted list.

## Heap Sort Complexity

The same analysis as for the heap sort with separate PQ works again.

O(n log n) comparisons and swaps to build the max heap in the array.
O(n log n) comparisons and swaps to turn the max heap into the sorted list.

Note: If we start with a complete unsorted array, the bound on building the array-based heap can be reduced to O(n), but overall complexity remains O(n log n), but we still have to turn it into a max heap.
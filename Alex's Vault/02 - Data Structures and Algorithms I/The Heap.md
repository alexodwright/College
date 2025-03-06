## The Priority Queue ADT

add(key, value) - adds a new element into the priority queue
min() - return the value with the minimum key
remove_min() - remove and return the value with the minimum key
length() - return the number of items in the priority queue.

## Priority Queue: Informal Analysis

Fully sorted gives low access time (since we know where min is), but expensive insertion, since we need to find the exact position.
- Do we need to find the exact place in the order
- Precise order of x and y only needed when identifying the min.
Unsorted gives cheap insertion (we just add at the end), but expensive access, since we need to find the lowest item by linear search.
- Should we be less lazy, and find a good position for new items?
- After removing min, check a few close items and identify next min?
Keep multiple sorted chains? No relationship between items in different chains. Next min is always the front of the chain.
- Each of its successor much have a higher key.
Keep chains in a binary tree? Each path is a sorted chain from root to leaf (so each parent has a lower key than its children).

### Maintaining the PQ data.

A binary tree where every node has lower key than its children?

![[Pasted image 20241111101904.png]]

Where do we add a new element? E.g. an element with key 26. How do we reorganise the tree when we remove the top node?

## The Binary Heap

A binary tree where:
- Every node has lower (or equal) key than its children
- Every level (except maybe the last) is complete
- The lowest level, counting from the left has nodes in every position up to some point, and then no more nodes.
![[Pasted image 20241111102523.png]]

### Adding to a binary heap

Create Element Object
Add element in last position.
Bubble element up heap
Update last position
Update heap size

Bubble element up (recursive):
	if key < parent key
	swap element with parent
	bubble parent element up heap

Bubble element up (iterative):
	while this key < this.parent key
	swap this and this.parent
	set this to parent.

Each swap is O(1). At most O(log n) swaps. So add is O(log n).

### Removing top from binary heap

Apply the same reasoning- we know what the tree shape will be, so do the minimal change, then recursively move the key that changed position until the heap is restored?

![[Pasted image 20241111102818.png]]

Extract the root value.
Copy the last element into the root
Remove last node.
Bubble root element down.
Update last position
Update Size

Bubble element down (recursive)
	if children
	target = child with the min key
	if this key > target key
		swap element with the target
		bubble element down the heap

Finding min key is O(1)
Swap is O(1)
O(log n) swaps
So remove is O(log n)

## Do we have to use a linked tree?

![[Pasted image 20241111103152.png]]

### Represent the tree using an array-based list.

Root node is at index 0.
Next item to be added is at index size.
Last item is at index size-1.

left(i) = 2*i + 1
right(i) = 2*i + 2
parent(i) = (i-1)//2

![[Pasted image 20241111103414.png]]

## Priority Queue: Implementation Complexity

![[Pasted image 20241111103445.png]]

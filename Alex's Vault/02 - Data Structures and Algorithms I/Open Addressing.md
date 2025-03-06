---
cssclasses:
  - center-table-contents
---
## Flat arrays and open addressing

The separate chaining method and the bucket array requires the use of additional data structures (e.g. lists) for the buckets, which take up extra space.

In open addressing, we store each element in a separate cell in the list. The cell cannot be uniquely determined by the compressed hash because of collisions (so the address must be open). So how do we determine the address?

We need to find a policy that will:
- Determine where we put a new (k, v) pair in all cases
- Allow us to find a (k, v) pair if it is already in the structure
- Do this efficiently - i.e. maintain expected O(1) complexity.

We need a policy that can be applied in all cases, and that allows us to find items on lookup, while avoiding efficiency problems.

Where do we setitem('CS2510', ...), which hashes & compresses to 4?
![[Pasted image 20241028220025.png]]

## Linear Probing (?)

To set an element, we search right from the compressed hash value until:
- We find the key, and we update the value, or
- We find an empty cell, and we add the new element.

To delete an element, we search right from the compressed hash until:
- We reach an empty cell, and do nothing (element not in map), or
- We find the key, and we delete the element.

![[Pasted image 20241028220221.png]]
setitem('CS1111', q), which hashes & compresses to 5.
delitem('CS2510'), which hashes and compresses to 4.
![[Pasted image 20241028220302.png]]
But what happens now when we do getitem('CS1111')?
![[Pasted image 20241028220343.png]]
What happens in these two slightly different cases?
![[Pasted image 20241028220403.png]]
setitem('CS1111', q), which hashes & compresses to 5.
delitem('CS2510'), which hashes & compresses to 5.
setitem('CS1111', s)
![[Pasted image 20241028220448.png]]
setitem('CS1111', q), which hashes & compresses to 5.
delitem('CS2510'), which hashes & compresses to 5.
setitem('CS2995', z), which hashes and compresses to 4.
## Linear Probing

To set an element, we search right from the compressed hash value, remembering the first **available** cell, until:
- We find the key, and we update the value, or
- We find an empty cell, and we add the new element in what was the first **available** cell, or in the empty cell if no **available**s found

To delete an element, we search right from the compressed hash until:
- We reach an empty cell, and do nothing (element not in map), or
- We find the key, and we delete the element
	- **Replacing it with a special 'available' marker**

![[Pasted image 20241028220733.png]]
## Linear Probing (2)

All values must get the same opportunity to be added.
- 'Search right' must wrap round the end of the list and continue from the beginning, for up to n steps in total.
- Use modular arithmetic
	- comphash(k) % N, then (comphash(k) + 1) % N, comphash((k) + 2) % N
The load factor (i.e. n/N) must never get above 1
- Why not?
- Standard practise is to grow the list when n/N = 0.5
- Instead of doubling the size, grow to 2N-1, or 2N+1
	- More chance of new size being a prime number...
- Should also shrink when more space than needed
- As with bucket array, all items must be re-hashed & compressed.
## Implementations (III)

Version 3: open addressing, linear probing, dynamic size
```Python
comphash(key) = hash(key) % len(list)

getitem(key):  
	if there is something in list[comphash(key)]  
		search & wrap from there for the key and return value or None  
	return None  
	
setitem(key, value):  
	if there is something in list[comphash(key)]  
		search & wrap from there for the key, and remember “available”  
		if key found, update with new value  
		else insert in first available or none; increment size  
	else insert and increment size  
	if size > f(len(list))  
	resize by factor c  
	
resize(c):  
	oldlist = list  
	list = new list with c None items  
	for each cell in oldlist  
		if cell has (k,v) insert (k,v) into the (list) hash table  
			size +=1

delitem(key):  
	if there is something in list[comphash(key)]  
		search & wrap from there, using probing scheme, for the key  
		if key found  
			replace with “available”; decrement size  
	if size < g(len(list))  
		resize by factor c  
#Note – not particularly efficient – list can get filled up with  
#”available” markers – should also maintain a count of them, and  
# when too many, re-compress all entries, removing ‘available
```
## Other probing schemes

Linear probing tends to produce long chains of occupied cells, and so searching tends to O(n)

Quadratic probing tries the cell
	(comphash(k) + $i^2$) % N for each search step i
Double hashing tries the cell
	(comphash(k) + $i \times h$'(k)) % N for each search step i, where h'() is another hash function

The python dict uses open addressing with pseudo-random probing

Pseudo-random probing tries the cell
	(comphash(k) + f(i)) % N, for each search step i, where f(i) is determined by a pseudo-random number generator.

### Complexity

|              | getitem(k) | contains() | setitem(k, v) | delitem() | build full map |
| ------------ | ---------- | ---------- | ------------- | --------- | -------------- |
| Unsorted ist | O(n)       | O(n)       | O(n)          | O(n)      | O($n^2$)       |
| Sorted List  | O(log n)   | O(log n)   | O(n)          | O(n)      | O($n^2$)       |
| Hash Table   | O(n)       | O(n)       | O(n)          | O(n)      | O($n^2$)       |
| Expected     | O(1)       | O(1)       | O(1)          | O(1)      | O(n)           |
Note: for most applications in Python, just use Python's dict - it is almost always faster
But maybe we want to keep the keys in sorted order? Are we forced back to the sorted list implementation?
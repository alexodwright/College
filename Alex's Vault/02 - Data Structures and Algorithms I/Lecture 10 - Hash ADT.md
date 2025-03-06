## Initial Hash Table

Use an array of known size N for storage

Generate a unique integer for each key, using a hash function.

Compress (i.e. reduce) the hash number to an integer in [0, N-1] by taking the hash number modulo N

index = hash(key)

### Separate Chaining

Each cell in the list will maintain its own list of values known as a bucket array.

## Implementation

```Python
comphash(key) = hash(key) % len(list)

getitem(key)
setitem(key, value)
delitem(key)

# creating a list of a known size
self.mylist = [None] * size

for sublist in mylist:
	for item in sublist:
		if item.key == key
			return item.value
return None

cell = comphash(key)
sublist = mylist[cell]
for item in sublist:
	if item.key == key
		return item.value
return None
```

## Search complexity in bucket arrays

To find an item in a bucket array, we have to compute the hash, then the compressed location (both O(1)), but then search the bucket (i.e. the list) - which is O(length of bucket).

If we are unlucky, all of our items could end up being sent to the same bucket, and so search is O(n)

If we have n items to insert into a bucket array of size N, and we can distribute the items fairly across the buckets, then we can expect n/N items in any given bucket, and so the expected complexity is O(n/N).But we were aiming for O(1).

### How can we bring O(n/N) closer to O(1)?

If we have n items to insert into a bucket array of size N, and we can distribute the items fairly across the buckets, then we can expect n/N items in any given bucket, and so the expected complexity is O(n/N).

## Dynamic Bucket Arrays

We have already seen dynamic arrays

- When we need more space, create bigger list storage and copy elements across

We can do the same for hash tables, and thus increase the value of N

If we can guarantee that n/N will always be less than some constant c, then we have an expected search time of O(c), which is O(1)

But each time we resize, we must compute new locations, since the original locations were based on the old N.
- So that if we now add an item equivalent to one already in the map, it will be assigned the same bucket

map.setitem('g', '...')

![[Pasted image 20241028234513.png]]

## How do we obtain the expected complexity?

By using bucket arrays with dynamic list sizes, we get a complexity of expected O(1) for lookup, insertion and deletion.
"Expected" in this case does **not** mean "average", and it is **not** the same as the term in probability / statistics.
- On most occasions, for most buckets, it is O(1)

It assumes an even spread of items across the buckets.

To get close to an even spread, we need to pay attention to:
- The hash function
- The compression function
## Hash function properties

We would like to avoid collisions as far as possible
- Distinct items should get distinct hashes, so we should use as much of the content as possible.
- With a fixed size output, some collisions are inevitable.

Simple hash function:
- For integers that fit into 32 bits, hash to their own value
	- Integers in larger bit size should hash to exclusive-or of first half and the second half..
- Don't hash floats
- Hash strings by polynomial sum of the characters, using a fixed constant integer c
	- $x_0c^{n-1} + x_0c^{n-2} + x_0c^{n-3} x_0c^{n-1} + ... + x_{n-2}c + x_{n-1}c$
## Compression

Main aim is to distribute the compressed hash values as evenly as possible across the range.
- We used h % N, where N is the size of the list.

This works, but if a sequence of values has a pattern related to N, many will end up colliding.
e.g. compressing the numbers in the sequence.
10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50

mod 12 gives buckets: [10,22,34,46], [14,26,38,50], [18,30,42]  
(the numbers increase by 4, which is a factor of 12)
mod 13 gives: [10],[14],[18],[22],[26],[30],[34],[38],[42],[46],[50]
## Multiply, Add and Divide

MAD_hash(key) = ((a$\times$hash(key) + b) % p) % N

where
	p is a prime number > N
	0 < a < p
	0 <= b < p
can be shown (using Group Theory) that this gives us a better distribution of compressed values than simple % N
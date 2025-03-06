## Algorithms

- An algorithm is a set of instructions which state how a task is to be performed. 
- It is an ordered, deterministic, executable, terminating set of instructions. 
- Algorithms process information maintained in data structures, and produce actions and results.

## Data Structures

- Data structures are the frameworks we use to maintain the data that are processed by the algorithms.

## Abstract Data Types

- Higher level patterns for interacting with data structures - patterns for reading data from the structure, for removing data, and for adding new data.
- An ADT does not specify how an underlying data structure should be implemented.
## O(n) Notation

- Consider two functions f and g, mapping positive integers to positive integers.
- We will say f(x) is O(g(x)) if there are two constant values k and C so that whenever x is bigger than k, f(x) <= C x g(x).
- This means that when x is big enough, f(x) is never more than some constant multiple of g(x), and so f(x) will not become drastically worse than g(x).

- We use O(n) notation to restrict the functions we need to deal with.
- Any polynomial with highest degree k is O($n^k$).
- It gives an upper bound on the growth rate of the function.

Standard worst-case upper bound functions:
- Constant - O(1)
- Logarithmic - O(log(n))
- Linear - O(n)
- Log Linear - O(n log(n))
- Quadratic - O($n^2$)
- Cubic - O($n^3$)
- Exponential - O($c^n$)

![[Pasted image 20241215154740.png]]

## Arrays

An array is a single block of memory of fixed size (determined when it is created), conceptually divided into cells packed one after another with no gaps, where we store data in each cell.

- Each cell is exactly the same size.
- If we know the address of the start of the array, and we know the size of each cell, we can use simple arithmetic to jump to any numbered cell.
- Address of cell i = address of cell 0 + ($i * size$)
- Therefore it is O(1) to access a cell by index.

## Tuples

A tuple is a sequence of references to objects. The length and content of a tuple cannot change (i.e. it is immutable).

### Space Required for a List

Since a python list is a sequence of references, the amount of space required for a list depends on the number of elements, and not on the space required for the basic objects.

### Searching for an Element

Finding an element in a list takes time O(n), where n is the length of the list.

### Increasing list size

If we already have space reserved at the end of the list, use it.
If not, it may require reservation of new area in memory for the entire list, and time to copy the list elements across.

![[Pasted image 20241215155247.png]]

Each time we must grow the list, double its size.
Each time we grow it, we request new space, and copy old data across.

Doubling the size each time space is needed takes O(n) to build a list of size n.

Average cost of a single append is then O(1).

### Cost of popping an element

Python's lists have no spaces - when we pop an element, the list must close up, pushing space to the end.

- For a list of length n, pop(i) takes (n-1-i) copies.
- pop(0) takes n-1 copies
- pop is O(n)

### The remove(...) method

`mylist.remove(x)` will remove the first occurrence of x that it finds in a list.

### Deleting an element: space

del, pop and remove all create empty cells at the end of the reserved space for the list.

Python will manage that space, and when the proportion of empty space exceeds a limit, Python will release the space for other uses.

## Stack

A stack is last-in, first-out (LIFO).
### ADT in Python

`push(element)`: add element onto the stack
`pop()`: remove and return the element that was added to the stack most recently (return None if empty)
`top()`: report the element that was added to the stack most recently (None if empty)
`length()`: return the number of elements in the stack

To add and delete on a Python list most efficiently, we should do it at the end of the list
- The end of our list will be the 'top' of the stack.
- Use `.append()` to push, and `pop()` to pop

### Complexity of Operations

- List creation is O(1)
- List.append is O(1) on average
- List.pop is O(1) on average - always pop the last element, so no copying, unless resizing the list
- List index lookup is O(1)
- List length is O(1)

## Queue

A queue is first-in, first-out (FIFO).
### ADT in Python

`enqueue(element)`: add element to the queue
`dequeue()`: remove and return the element that has been in the queue for the longest time (None if empty)
`front()`: report element that has been int he queue for the longest time (None if empty)
`length()`: return the number of elements in the queue

Avoid using `list.pop(0)`.
- Instead, maintain internal reference to the first element in the list, called the head.
- To dequeue, record the element which is referred to by head, reassign None to that cell, update the head pointer to the next index, and return the recorded element.
- To fix `length()`, subtract head.
- These operations take constant time, so `dequeue()` is O(1), and we haven't changed `enqueue()`

### Exploding the Space

- If we do many enqueue and dequeue operations we will have a short queue, but with Python maintaining space for a very large list.
- When we reach the end of the list, we will wrap around, placing new items at the front.
- Only expand the list space when all cells are filled.
- Must maintain a head and tail.
- Each operation will be slower than before, but still O(1), and we will only require space for the biggest queue we have maintained at any one time.

![[IMG_0019.jpeg]]

`dequeue()` is now O(1) on average and our space requirement is determined by the biggest number of elements ever stored in our queue at any one time (and not by the number of `enqueue()` method calls).


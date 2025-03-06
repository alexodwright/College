## Arrays

An array is a single block of memory of fixed size (determined when it is created), conceptually divided into cells packed one after another with no gaps, where we store data in each cell. Standard in many languages.

Each cell is exactly the same size. In most languages, the data stored in the cells must all be of the same data type.

![[image 23.png|image 23.png]]

If we know the address of the start of the array, and we know the size of each cell, we can use simple arithmetic to jump to any numbered cell.

Address of cell i = address of cell 0 + (i*size).

It is constant time (O(1)) to access an element at a specific index at a list.

## Everything in Python is an Object

```Python
x = 3
y = 3
z = y
y = 4
```

Is implemented as follows:

- 3 is an integer object, stored in memory,
- x is a variable, which references that object.
- y is a variable, which references the same object - only 1 copy of a basic type
- z is a variable, which references the same object.
- y is then changed to refer to a different object.

The reference maintains the memory address of the object.

Same for Boolean and floating point types.

## User-Defined Classes and Objects

Each time we create an object from a class, Python creates a new object in memory (Python decides where it is stored)

## Python lists are array-based lists

A list in Python is a sequence of refences to objects. The references in the list are maintained internally in an array.

Array contains refences, so all of the same type and size.

## Tuples

A tuple is a sequence of refences to objects. The length and content of a tuple cannot change (i.e. it is immutable)

Implementation is similar to lists, but is able to take advantage of the fact that they are immutable.

## Space required for a list

Since a python list is a sequence of references, the amount of space required for a list depends on the number of elements, and not on the space required for the basic objects.

## Sequence Operations

![[image 1 20.png|image 1 20.png]]

## Naïve Append

If python added one new cell into the list each time we append, each append would require a full copy of the current list

For a list that may grown to size n, using naïve append takes O($n^2$﻿) to build the whole list.

$\displaystyle\sum_{i=1}^n$﻿

## Complexity of List Doubling

Policy: Each time we must grow the list, double its size.

Each time we grow it, we request new space, and copy old data across.

To create a list that reaches size n, this will take:

1 assignment +

1 copy op + 1 assignment +

2 copy ops + 2 assignments +

4 copy ops + 4 assignments +

…

n/2 copy ops + n/2 assignments - up to n elements

1+2+4+…+(n/2) copies + 1+1+2+4+…+(n/2) assignments

==*** ***==

## Cost of Popping an Element

Python’s lists have no spaces- when we pop an element, the list must close up, pushing space to the end, moving each element back to fill the gap. (n-1 copies)

For a list of length n pop(i) takes O(n-i-1)

## The remove(…) method

```Python
myList.remove(x) 
```

Removes the first occurrence of x that it finds in the list.

## Deleting an element: space

del, pop and remove all create empty cells at the end of the reserved space for the list.

Python will manage that space, and when the proportion of empty space exceeds a limit, Python will release the space for other uses.
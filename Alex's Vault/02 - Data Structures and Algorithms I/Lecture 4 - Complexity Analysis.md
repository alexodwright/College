1. Comparison requires full implementation of each algorithm (and development of a test framework)
2. Performance depends on the implementation in a particular language.
    1. Underlying language constructs may introduce hidden complexity.
3. Comparison requires testing in same software and hardware environment.
4. Results are dependent on the test cases selected.

## Counting Basic Steps

We will consider the following to be basic steps

- Reading the value of a variable
- Assigning a value to a variable
- Simple arithmetic operations (e.g. addition)
- Comparing the values of two values.
- Calling a function
- Returning a value
- Reading the value at a given index in a Python list.

We expect each of these steps to take (approximately) a constant time to complete, regardless of the value.

### Worst-Case Upper Bound

The number of steps for an algorithm will vary depending on the precise values in the input, but may grow in a pattern dependent on the size of the input.

As the inputs grows past a certain size, we want a guarantee that the number of steps will be less than some function of the input size.

## Big-Oh Notation

![[image 22.png|image 22.png]]

![[image 1 19.png|image 1 19.png]]

For all values of x > k, f(x) will be below the red line.

### Big-Oh is an upper bound…

We use the Big-Oh notation to restrict the functions we need to deal with.

Any polynomial with highest degree k is O($n^k$﻿)

Note Big Oh gives an upper bound on the grown rate of the function.

- Any function that is O($n^k$﻿) is also O($n^{k+1}$﻿)

We will consider 7 standard functions to describe the worst-case upper bounds:

- Constant
- Logarithmic
- Linear
- Log Linear
- Quadratic
- Cubic
- Exponential

### Constant

If f(.) specifies the runtime of a function on input of size n, and f(n) = c for some fixed constant value c, then the runtime is independent of the size of the input.  
For example: a function which returns the value in the first position in a list - doesn’t matter how long the list is.  

Note: we say such a function is O(1)

### Logarithmic

f(n) = $\log_bn$﻿ , for some fixed constant value b

The log of a number is the power to which the base must be raised to give the number.

$\log_bn$﻿ = x if and only if $b^x = n$﻿

### Binary Search

Worst case analysis: each time round the loop, we cut the list in half.

How many times can you divide by 2 until you reach a value of 1 or less?

$\log_2n$﻿

We will do this operation (repeatedly dividing by 2) so often, that we will stop writing the base = 2.

For this $\log n$﻿ means $\log_2n$﻿

### Linear

f(n) = n

Typically, this comes from an algorithm with a single loop that iterates over each element of an input list. (could be multiple loops, but NOT nested.

### Log Linear

f(n) = n$\log n$﻿

Typically, the algorithm is doing something like binary search, but repeating it once for each position in the list.

### Quadratic

f(n) = $n^2$﻿

Typically this comes from algorithms with a nested loop where we are iterating over the same structure.

### Cubic

f(n) = $n^3$﻿

Typically this comes from algorithms with a doubly nested loop where we are iterating over the same structure.

We can go higher, to any arbitrary degree.

### Exponential

f(n) = $c^n$﻿, for some constant c.

Typically, this comes from algorithms with a loop where the number of operations increases by a factor of c each time round the loop.

Algorithms with exponential running time are considered inefficient, although we will see some practical algorithms of this sort later in the degree program.

## Runtimes

![[image 2 12.png|image 2 12.png]]
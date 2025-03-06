
## Question 1
### i)

Array based lists are implemented by reserving blocks of consecutive memory addresses. We get constant time to access an arbitrary index in the list by performing simple arithmetic. Since we know how big the cell size is and we know the start address of the first cell (index 0), we can get the address of an arbitrary index using the following formula: $A_0 + (i \times S)$ where $A_0$ is the start address, i is the index we want to access and S is the size of a cell.

### ii)

An append method can be implemented so that the average time complexity is O(1). Since array based lists reserve consecutive memory addresses there is nearly always space for an element so the append just adds to the end. On the occasion that the list is full and we need to create more space we double the size of the list. Even through this is an expensive operation O(n), it averages out because the list can now contain another n elements. This time complexity averages out over the next n append operations.


### iii)

#### Stack

```Python
8
8 3
8
8 9
8 9 5
8 9
8 9 6
8 9 6 7
8 9 6
8 9
8 9 2
8 9
```

#### Queue

```Python
8
3 8
3
9 3
5 9 3
5 9
6 5 9
7 6 5 9
7 6 5
7 6
2 7 6
2 7
```

### iv)


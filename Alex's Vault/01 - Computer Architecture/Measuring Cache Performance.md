## Cache Performance Analysis

CPU time = (# CPU execution cycles + CPU stall cycles) x cycle period

Memory-stall clock cycles = (read-stall cycles + write-stall cycles)

Read-stall cycles = reads/program x read miss rate x read miss penalty

Write-stall cycles = (writes/program x write miss rate x write miss penalty + write buffer stalls)

Write buffer stalls can be ignored with sufficiently deep buffer and/or fast writing procedures.

Memory-stall clock cycles = memory accesses/program x miss rate x miss penalty

## Performance Concerns

What happens when CPU performance increased?
- R
== *** ***==

## How does block size impact Memory Performance?

### Average Memory Access Time

#### Good memory performance

1. A small hit time
2. A low miss ratio
3. A small miss penalty

#### Larger Blocks
- Should reduce miss rate due to spatial locality
- Larger miss penalty
- Higher miss rate (fewer blocks in a fixed cache size)

## Improving Cache Performance

### Example: Direct Mapped Cache has high miss rate

Consider a system with a 4-block cache using Direct mapped memory organisation.
- Block access sequence: 0, 8, 0, 6, 8 (Memory block ID)
- Initially, we assume all cache entries are empty

## Reducing Miss Rate

Flexible block location to reduce the competition for cache blocks -> Associative Caches

Fully associative caches:
- Any memory block can go to any cache block (less competition)
- Simple flexible placement
- More complex search - should be designed to ensure small hit time.

n-way set-associative caches
- A memory block can be located to a set of n cache blocks.
- Which set? (Memory block number) % sets in cache
- Which block? Any block in the set.
- How to search? Search all possible n entries in a given set at once.

## Set associative cache organisation

Remember:
Direct mapped organisation -> Searches one location.

4-way set

Each block may be in a different location
Additional Hardware to support simultaneous search in all locations to ensure that the HIT performance is not affected.

### N-set Associativity Example

Consider a system with a 4-block cache using 2-way set associative memory organisation.
- Block access sequence: 0, 8, 0, 6, 8

Increased associativity decreases miss rate but with diminishing returns
Performance-cost trade off: better performance requires additional hardware for speeding hit time.

## Replacement Policy

Direct mapped: no
Choice set associative:
- Prefer non-valid entry, if there is one
- Otherwise, choose among entries in the set.

- Least-recently used (LRU).
- Random
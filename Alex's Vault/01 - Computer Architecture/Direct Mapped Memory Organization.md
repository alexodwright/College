## Direct Mapped Cache Organization

### Where can a block be placed?

Each physical address is mapped to only one cache location.
Physical address is split into 3 parts


| Mem Block ID |                        | Block Offset |
| ------------ | ---------------------- | ------------ |
| TAG          | Cache block identifier | Block Offset |
Tag is used to determine which memory block is actually in the cache

The cache block identifier bits define which cache block should be used.

The block offset represents the bits used for block offset (>= 0).

## Larger Block Size

Consider a 64-block cache with 16 bytes/block.
To which cache block does address 1202 belong?

Method #1.
- Memory Block = byte address/byte per block = [1202/16] = 75
- Direct-Mapped Cache Block = Mem Blk ID % (# cache blks) = 75 % 16 = 11
Method #2.
- 64 Blocks = 2 $blocks^6_4$ -> n = 6
- 16 byte/block = 2 bytes/block
  MIPS TAG size = 32 - (6 + 4) = 20 bit

1200 = 0..1 TAG
001011 Blk Idx
0000 Block Offset

Once the address is calculated all the fields are known.

## Direct Mapped Cache Block Search

Cache memory stores the block content + tag + valid bit.
- Valid bits are set by the OS when valid data is moved to the cache block (initialized to 0).
Search is performed using hardware.
1. The CPU calculates the address
2. The address tag is compared to the stored tag at the cache block.
== *** ***==

## Block Replacement Strategies

### What block is replaced on a miss

In direct-mapped memory, there is only one possible place for every block.
A trivial question

## Handing Cache Writes

write hit (Block in cache)

Write-through technique: Update both cache and next lower level memory hierarchy

Write-back technique: Update slower memory level when the entire block is replaced.

When to update the main memory? Consistent vs. speed.

Write miss (Block is not in cache)

Write-allocate: load the block in the cache and update in the cache.

No write allocate: update the written address using write through without loading the block.

### Write-through technique

Pros:
- Consistent
Cons:
- Slow
Write-through ensures consistent data but is slow.

E.g. If base CPI = 1, 10% of instructions are stores, write to memory takes 100 cycles.
- Effective CPI = 1 + 0.1*100 = 11 (Big Problem)

Solution: Speeding write-through using a write buffer
- A buffer holds data waiting to be written to memory.
- CPU continues immediately (no delay)

Only stalls on write if write buffer is already full (not bad at all)

### Write-back

Fast writes but a higher miss penalty
- Write every block back to main memory.
Problem: Doubles a miss penalty.

Solution: Reducing miss penalty.
- A dirty bit is set whenever a cache block is updated
- When an updated (dirty) block is replaced
	- Write it back to memory
	- Can use a write buffer to allow replacing block to be read first.




## Memory Technologies

### SRAM

- Uses more transistors per bit and keeps the data as long as it is powered

### DRAM

- Keeps the charge for a few milliseconds -> needs periodic refresh (dynamic!).
- Organized in banks that can be accessed simultaneously
- DDR (Double Data Rate) (Transfer on rising and falling clock edges)

### Flash Memory (EEPROM)

- Avoid wears by distributing dispersing the written blocks

### Magnetic Disk

- Platters having tracks split into sectors
- Large access time (seek delay + rotational delay + transfer time)

## Memory Hierarchy

**Cache** makes slow MAIN MEMORY appear faster.

**Virtual Memory** makes small MAIN MEMORY appear bigger.

![[Pasted image 20241106131227.png]]

### Why caching work for memory organization?

#### Principal of locality

- Programs access a small proportion of their address space at any time.
#### Temporal Locality

Items accessed recently are likely to be accessed again soon; e.g., instructions in a loop, induction variables.

#### Spatial Locality

Items near those accessed recently are likely to be accessed soon; E.g., sequential instruction access, array data.

## Memory Basics

## Memory Operation

- The CPU calculates the memory address
- The CPU activates read/write signal and puts the address on the signal bus.
- The memory accesses the activated location and read/write data bus depending on the operation

The max memory size depends on the size of the address bus.
### Memory Blocks (Definition)

#### Main Memory Blocks

- Storage data unit for active applications stored in units called **blocks**

#### Cache Blocks

- Contains a subset of the main memory blocks (some text call them lines)
- Data transfer between cache and main memory is based on entire **blocks**

*Processors only interact with cache memory.*

## Memory Address

- The processor requests **data/code words** using their **physical memory address** when calculated in memory instructions.
- The physical memory address depends on the processor architecture (e.g. 32-bit address in MIPS 32, can be smaller or larger for other architectures.)
- The memory address (n-bit) has two parts.

![[Pasted image 20241106132719.png]]

- The block offset address part depends on the block size.
	- 1 KB block has 10-bit offset
	- 512 KB block needs 9-bit offset.

## Example 1A

Consider a processor with 16-bit address using a block size of 16 words.

*How many lines are used for block offset and identifier?*

16 words/block = 64 bytes/block = $2^6$ bytes/block

==*** ***==

### Cache Hit and Miss

The processor needs to access data in block X.

**Memory hit:** processor finds block X in the cache.

**Memory Miss:** block X is not currently in the cache.
- Block X should be copied from the main memory to the cache to continue operation (delay penalty).

## What happens on cache misses?

1. Stall the CPU pipeline
	1. Send original PC value to memory i.e., current PC-4
2. Fetch block from lower level of hierarchy
	1. Instruct memory to perform a read and wait for memory to complete access.
	2. Cache update
		1. Put data from memory into data portion of entry
		2. Update some cache control bits (later)
3. Resume execution
	1. Instruction cache miss: restart instruction fetch
	2. Data cache miss: complete data access (read or write)

## Memory Performance Measures

Hit/miss ration ($\alpha$)

- Percentage of memory accesses that results in a memory hit/miss
- Higher ratio is better.

Average memory access time ($t_a$)

- $t_a = \alpha \times t_h + (1-\alpha) \times t_m$
	- A high hit ratio is desireable
	- A small hit time ($t_h$) is desired
	- A smaller miss penalty ($t_m$) is also desirable

## Example

Consider a MIPS processor with 64-block cache with 16 bytes/block

*What is the cache size?*

*How many address lines are used for the block offset?*

*How many address lines are used for the memory block index?*

*To which memory block does address 1202 belong?*

**Memory Block** = Byte Address/ Bytes per block
= 1202/16 = 75.125 = 75

1202 = 1001011 | 0010 $_2$


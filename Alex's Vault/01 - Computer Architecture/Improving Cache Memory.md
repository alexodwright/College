## Reducing the Miss Penalty

### Multi-Level Cache

- Level 1 cache (primary cache): service the CPU, small (~KB), but fast.
- Level 2 cache (~MB): services misses from primary cache still faster than main memory.

## Multi Level Cache Considerations

### Primary Cache
- Focus on minimal hit time

### L-2 Cache
- Focus on low miss rate to avoid main memory access
- Hit time has less overall impact

### Results
- L-1 Cache usually smaller than a single cache
- L-1 Block size smaller than L-2 block size

## Memory Organisation & Performance

### Memory Hierarchy is transparent to programmer!
- Machine AUTOMATICALLY assigns locations, depending on runtime usage patterns.
- Programmer doesn't (cannot) know where the data is actually stored!

### Memory Organisation impacts the computer performance.
- Organisation refers not only to the hierarchy but also to the involved read and write operations to different parts of the hierarchy.

Caching is an IMPORTANT concept to improve the performance of computing systems.
Beyond the CPU, caching is used at application-level, database-level, network-level and the Internet level.

## Virtual Memory

The physical address may be limited by the installed memory or connected HW address lines.
- Virtual memory enables extending the memory size beyond main memory.
- Virtual memory extends the physical memory to the HDD
- Virtual memory is managed jointly by CPU

== *** *** ==

Programs share main memory:
- Each gets a private virtual address space holding its code and data
- Physical memory is used as a 'cache' for the virtual memory file
- Virtual memory block is called a page
- Virtual memory 'miss' is called a page fault
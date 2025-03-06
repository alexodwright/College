## Key Performance Metrics

When we say computer A is better than Computer B?

Response time:
- Also referred to as **execution time**
- Measure the time needed by the machine to complete a task (or tasks)
- Performance benchmarks measure the time needed to complete a set of divers tasks (compression, decoding, ...)

Throughput:
- Number of tasks completed per unit time
- **Relevant to servers**

## Response Time Analysis

Time is the only complete and reliable measure of perform

CPU Time = $\frac{Instructions}{Program}\times\frac{Clock \space Cycles}{Instruction}\times\frac{Seconds}{Clock \space Cycle}$

What factors impact the response time?
- Algorithm: Affects IC, possibly CPI
- Compiler: affects IC, CPI
- Instruction set architecture: affects IC, CPI, Tc

## Two Cores or one Faster Core?

### HW impact on performance

How are response time and throughput affected by.
1. Replacing the processor with a faster version?
2. Adding more processors?

### Why speeding processor is challenging?

In CMOS IC technology:
- Complementary Metal Oxide Semiconductor (CMOS)
	- $Power = Capacitive\space Load \times Voltage^2 \times Frequency$

### Is multi-core processor useful for a single program?

It is difficult because it needs
- Partitioning the work into parallel pieces
- Scheduling (Balancing the load evenly between the workers)
- Synchronization
- Minimize overhead communications

Amdahl's Law
Speed-up = $1 \div ((1-\alpha) + \alpha\div n )$
N: Number of cores
$\alpha$ : percentage of parallelized code

### Parallel Processing Benefit (Single Task)

Increasing the size of the parallelizable jobs increases the speed up (Check 100 Tasks $\rightarrow$ 400 tasks)

**Unbalanced** processor load reduces the speed-up factor



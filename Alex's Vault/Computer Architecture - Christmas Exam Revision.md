- [ ] 
Executing a Binary file:
1. Binary file format:
- Header - Describes size and position of other sections
- Text - Machine code for routines.
- Data - Binary representation of data in source file
- Relocation - Instructions and data words that depend on absolute addresses.
- Symbol - Associates addresses with labels and lists unresolved references.
- Debug Info - Description of the way the program compiled.
2. Steps:
- Reads header
- Creates address for program
- Copies text and data to respective memories
- Copies passed program arguments to the stack.
- Initializes CPU registers.
- Runs program's first instruction.

Role of ISA:
- Abstraction
- Compatibility - Different generations of processors with the same ISA

Key Components:
- Data types
- Registers
- Instruction Set
- Instruction Formats
- Addressing Modes
- Memory Architecture

RISC:
- Reduced Instruction Set Computer
- Simple instructions taking around 1 clock cycle.
- Primitive and reduced instruction set.
- Small Execution time
- ARM, MIPS, ARC, AVR.
- Average CPI = 1.5
- Software Centric Design

CISC:
- Complex Instruction Set Computer
- Complex instructions that take up multiple clock cycles.
- Variety and complex instruction set.
- Very high execution time
- AMD, x86 Intel, VAX, PDP-11
- Average CPI: 2-15
- Hardware Centric Design

## Integer Arithmetic Instructions

Unsigned: 0-$2^n-1$
Signed: $-2^{n-1} - 2^{n-1}-1$

Most Positive number: 0111 1111 .... 1111
Most Negative number: 1000 0000 .... 0000

There is no subi instruction -> addi $t1, $t1, -3
- Registers are faster to access than memory
- Operating on memory requires load and store
- MIPS is big-endian -> MSB at least address of word

## Signed Extension
8 -> 16 bit
+2: 0000 0010 -> 0000 0000 0000 0010 - 0's to the left
-2: 1111 1110 -> 1111 1111 1111 1110 - 1's to the left

j(goto), jal(jump and link), jr(return)
Only use j for conditional logic (if and loop)

## Bitwise Operations

sll = x2
slr = /2

AND - Mask to check values of bits
OR - change bits that should be 1's to 1's without altering other its
NOR - invert bits in a word

## Procedures

Name used as a label -> pointer mapped by the assembler.
jal: $PC = address of first instruction in the procedure
$ra = stores address of the next instruction after jal (return address)

jr $ra -> unconditional jump to instruction after jal.

### Rules for Procedures
$a0 - $a3 -> Argument Registers
$v0, $v1 -> Result Registers
$t0 - $t9 -> Temporaries which can be overwritten by callee
$s0 - $s7 -> Saved registers cannot be overwritten by callee - must be saved / restored by callee
- Use stack to save / restore data
- $SP points to most recently allocated address in the stack
- MIPS stack managed manually; grows in decreasing address direction.
- Leaf-Procedure -> Procedure that doesn't call another procedure (no jal).
- Non-Leaf-Procedure -> Procedures that call other procedures (including recursive)
	- Should save $ra
	- Save arguments needed after call
	- Restore saved from stack after call.

## MIPS Instructions Encoding
R - Format Instructions -> (ALU)
I - Format Instructions -> (lw, sw, addi)
J - Format (j)

Fields for R-Format:
- Opcode
- First source register number
- Second source register number
- Destination register number
- Shift amount (0000 for now)
- Function code (extends opcode)

MIPS has 32 register (32 = $2^5$ -> 5 bits to identify every register.)

I-Format Instructions

- op - 6 bits
- rs - 5 bits
- rt - 5 bits
- constant or address - 16 bits
Immediate arithmetic / load / store / branch instructions

## Arithmetic

Binary Division

![[Pasted image 20241204131541.png]]

## Floating Point Standard

Single Precision (32-bit) -> Float
Double Precision (64-bit) -> Double

### Single Precision

- Total length - 32 bits
- sign bit - 1 bit
- exponent - 8 bits
- mantissa - 23 bits

Excess Representation
- Exponent = yyyy + Bias
- 127 for single
- 1023 for double
- Biased exponent is unsigned

Double Precision $\approx$ 16 digits
Single Precision $\approx$ 7 digits 

## FP Instructions in MIPS

Separate FP processor (CP1)

Separate FP registers:
- 32 single-precision: $f0, $f1, ... $f31
- Paired for double-precision $f0 / $f1 , $f2 / $f3

FP instructions operate only on FP registers

Conversion:
cvt.to.from

### FP Arithmetic Hardware

- FP multiplier is of similar complexity to FP adder
	- But uses a multiplier for significands instead of an adder

# Processor Design

- A processor is the HW that facilitate executing the processor instruction set.
- The processor has two key elements
1. Data path: fetch, decode, execute instructions
2. Control path: orchestrate the instruction cycle (fetch, decode, execute)
- There exist multiple implementations for the same instruction set.

Two MIPS processor implementations:
- A simplified single clock cycle processor where the whole instruction is processed (fetch + decode + execute) in one clock cycle.
- A pipelined version that speeds program execution but should overcome other complexities.

MIPS Control decodes the instruction to define control signals and ALU operations.

### Performance Issues

- All instructions operate at the speed of the slowest one (Violates making the common case fast)
- Not feasible to vary period for different instructions.
- A solution to improve performance is by pipelining.

The critical path is the instruction that has the longest execution time.

# Pipelined Processor

### MIPS Pipeline

Five stages, one step per stage.
1. IF: instruction fetch from memory
2. ID: instruction decode & register read
3. EX: execute operation or calculate address
4. MEM: access memory operand (not always)
5. WB: write result back to register (not always)

### Pipelining and MIPS ISA Design

- MIPS ISA designed for pipelining
	- One instruction size 32-bits (4 bytes)
		- Easier to fetch in one cycle
		- c.f. x86: 1 to 17 byte instructions
	- Few and regular instruction formats
		- Can decode and read registers in one step
	- Simple load / store addressing
		- Can calculate address in 3rd stage, access memory in 4th stage
	- Alignment of memory operands.

### Pipeline Speedup

If all stages are balanced.
- Balanced -> all N pipeline stages take the same time T and we have I instructions (millions) in our program
Single clock cycle execution time I * (NT)

Pipelined processor execution time = NT + (I-1)T # first vs subsequent inst.

Speedup factor = INT / (N + I - 1)T ~ N

Pipeline speeding factor is proportional to the number of stages

Reality: not balanced -> speedup gain drops
Speedup due to increased throughput
Instruction latency (time for each instruction) does not increase.

### Pipeline Hazards

Situations that prevent starting the next instruction in the next cycle

The processor needs to fetch an instruction from the memory at stage 1 and you need to execute a memory load instruction <-> Structure hazard: conflict on hW resources

Data Hazard: Operand needed by a instruction has not exited the pipeline <-> Considering dependent instruction sequence:
```Assembly
add $s0, $t0, $t1
sub $t2, $s0, $t3
```

Executing instructions that changes the program counter (beq, j, jal, jr, ...) <-> Control Hazard: Flow control may waste fetch and decode of subsequent instructions

Problem: Hazard reduces the pipeline architecture design again.

#### Structure Hazard - Conflict on HW resources

In MIPS pipeline with a single memory:
- Load / store requires data access
- Instruction fetch would have to stall for that cycle
	- Would cause a pipeline 'bubble'

#### Data Hazards

- An instruction depends from a previous instruction that is still in the pipeline.
```Assembly
add $s0, $t0, $t1 # the value of $s0 will be updated after 2 clock cycles
sub $t2, $s0, $t3 # wrong result if read from $s0
```

#### MIPS Pipelined Processor

Buffers introduced as interfaces between stages to keep the state of instructions as they propagate in the pipeline.

#### Solution 1: Forwarding (aka Bypassing)

HW connections that allow the data when it is available (after computing or memory load)
- Don't wait for it to be stored in a register.
- Requires extra connections in the datapath + additional control (later)
Forward implies reading ALU operands from a source other than the register file.
- Multiplexers are needed at the ALU I/P
- A forwarding unit determines the multiplexer control signal.

#### Forwarding Unit Output

![[Pasted image 20241204153716.png]]

When does forwarding fail?
- Loaded data won't be available before 2 cc
- Can't always avoid bubble / stalls by forwarding
- Can't forward backward in time!

### Code Scheduling
- Reorder instructions to avoid use of load result in the next instruction
- Code for A = B + E; C = B + F

![[Pasted image 20241204153839.png]]

### Hazard Detection Unit

Identify unresolvable hazards and stall the pipeline (bubbles)

Memory Load-use Hazard Detection 
- Check when an instruction is decoded in ID stage
- If ALU operand register numbers in ID stage are given by and target a preceding load.
- If detected, stall and insert bubble.

How to stall the pipeline.
1. Force control values in ID / EX register to 0
	1. EX, MEM and WB do nop (no operation)
2. Prevent update of PC and IF / ID register
	1. Fetch and decoding work is repeated
	2. E.g. load use case.
	   Stall 1 - cycle allows MEM to read data for lw and subsequently proceed to EX stage.

Pipelined MIPS and inter-stage buffers are used to maintain the state of both data and control paths.

#### Handling Control Hazards
- More challenging than data and structure hazards
- We will explore some solutions
	- Stall on branch (do nothing - BAD - no solution)
	- Optimized waiting
	- Delayed branch slot
	- Prediction
		- Static
		- Dynamic

Optimized stall on branch
- Decide while decoding (additional HW)
	- Not while executing - reduce one wait cycle.
HW:
Equality check: XOR then ORing bits for equality
If branching, the fetched instruction is flushed to a nop

Delayed Branch slot:
- Schedule an instruction after the branch instead of the wait cycle
- The instruction should have no impact on the branch instruction
- If compiler can not find an instruction, it just uses nop

Typical compiler strategies:
- From before - performance is always improved
- From target - performance gain if branch is taken
- From fall-through - performance gain if branch is not taken
Require complex compilers.

Branch Prediction
- Adopted by most architectures
	- Only stall if prediction is wrong
	- Accurate prediction -> high performance
- In simpler pipelines (e.g. MIPS), simple prediction policies are highly efficient.
- In longer pipelines, complex HW but necessary due to the high penalty
- Prediction policies may be dynamic or static.

### Branch Prediction Strategies

Static branch prediction:
- Based on typical branch behaviour
		- Backward Taken Forward Not Taken (BTFNT)
		- Example: loop and if-statement branches
Dynamic branch prediction
- Hardware track branch behaviour (taken or not)
- Assume future behaviour will continue the trend.

#### Dynamic Branch Prediction

Branch prediction buffer (aka branch history table)
- Indexed by branch instruction addresses
- Stores outcome (taken / not taken)
To predict a branch
- Check table, predict the outcome (repeat the last action)
- Start fetching from fall-through or target
- If wrong, flush pipeline and flip prediction.

#### 2-Bit Predictor

Only change prediction on two successive mispredictions.

## Interacting Hazards

### Double Data Hazard

![[Pasted image 20241204155418.png]]

Data hazards for branches
- If a comparison register is a destination of 2nd or 3rd preceding ALU instruction

![[Pasted image 20241204155510.png]]

Branch operands can be resolved using forwarding.

- If a comparison register is a destination of preceding ALU instruction or 2nd preceding load instruction
	- Need 1 stall cycle

![[Pasted image 20241204155602.png]]

- If a comparison register is a destination of immediately preceding load instruction.
	- Need 2 stall cycles

![[Pasted image 20241204155643.png]]

### Pipeline Summary

- Pipeline clock cycle is determined by the longest stage.
- Pipelining improves performance by increasing instruction throughput by a factor of # pipeline stages.
- Hazards may reduce pipeline again:
	- Structure Hazard (Conflict at HW resources) -> adding HW
	- Data Hazards (Dependency between pipeline instructions) -> mostly avoided by forwarding and code scheduling
	- Control (Deviating from sequential execution) -> wait, optimized wait, predict, delay slot.

# Exceptions and Interrupts

'Unexpected' events requiring change the instruction sequence of the user software.

Exception
- Arises within the CPU
	- e.g., undefined opcode, overflow, divide by zero, address error, syscall.
Interrupt
- From an external I/O controller
	- E.g., keyboard, mouse, printer, network card, power failure..

Traps are special instructions used to trigger an interrupt (AKA SW interrupts.)
Handling exceptions always reduces the performance.

## Common Exception Causes

- Arithmetic overflow occurs when the absolute value of the result is too large for the format.
- Arithmetic underflow occurs when the absolute value of a result is too small for the format (e.g., floating point)
- Divide by 0 exception is self-explanatory.
- Illegal instruction may happen if program counter or the memory was corrupted.
- Bus error for inaccessible resources.
- Segmentation fault is an attempt to access memory in an illegal way.

### More on Interrupts

- Interrupts are hardware-triggered events to handle IO
	- Remember: Handling I/O with busy waiting or polling wastes CPU time.
- IO devices indicate the need of service by raising a flag (changing a bit value)
- A special hardware (interrupt controller) is responsible for communicating interrupt to the CPU
- On interrupt detection, it is up to software to actually perform the I / O transaction.

### Interrupt Controller

A generic interrupt controller takes interrupts from peripherals, prioritizes them and delivers them to the appropriate processor core.

## Handling Exceptions / Interrupts

- A special OS (kernel) program that is executed in the event of exception or interrupt
- Reaching ISR(s)
1. Interrupt Vector Table (IVT)
   OS maintains a table that maps the interrupt reason to an address to its service routine (handler). When an interrupt occurs, the CPU jumps to the address specified in the IVT for that interrupt.
2. Single Entry Point
   OS has a single ISR for all interrupts and the cause is examined in this code (MIPS).
   - In MIPS, the exception handler is always located at 0x80000180
   - When an exception occurs, the processor always jumps to this instruction address, regardless of the cause.

Actions implemented by the handler
- Fatal problem (e.g., segmentation or bus errors)
	- The running program may be terminated and the offending instruction should be reported for debugging.
- Recoverable Issue (e.g. IO operation)
	- Continue the execution of the current program after handling the interrupt.

### Handling Exceptions / Interrupts
1. Hardware saves current PC in a special register
2. CPU jumps to an exception handler, which
	1. Save the current processor state (registers)
	2. Take appropriate internal action for an exception, or deal with the external source of the interrupt
	3. Restores the previous processor state
	4. Resumes user program execution (if possible) from step 1.
Exception handler resides in kernel memory (ktext not text)
- In any OS, kernel code has extra privileges and protection over use code (this is not simulated in MARS).


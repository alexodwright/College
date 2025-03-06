A processor is the hardware that facilitates executing the processor instruction set.

The processor has two key elements

1. **Data path**: fetch, decode, execute instructions
2. **Control path**: orchestrate the instruction cycle (fetch, decode, execute)

There exist multiple implementations for the same instruction set.

## CPU Overview

Can’t just join wires together.

We must use multiplexers

Multiplexers enable selecting an input from a group of sources

Most control signals are determined as the instruction is encoded.

![[image 11.png|image 11.png]]

## How a processor is designed?

- **Processor hardware** should be capable of executing the instruction set (shows most aspects)
    - Memory reference: lw, sw
    - Arithmetic/logical: add, sub, and, or, slt
    - Control transfer: beq, j, jal
    - Processors are designed to execute binary (machine) instructions.
- We will example two MIPS implementations
    - A simplified single clock cycle processor
        - The whole instruction is processed (fetch + decode + execute) in one clock cycle.
    - A pipelined version
        - A new design that speeds program execution but should overcome other complexities.

## MIPS Datapath

**Datapath:** Components that process data and addresses in the CPU (e.g., registers, ALU’s, mux’s, memories, …)

We will build a MIPS data path incrementally:

==*** ***==

### Building the Data Path

Each processor performs three key operations.

### Instruction Fetch.

1. Read the instruction @PC from the instruction memory
2. Update PC to PC + 4

### Instruction Decode

1. Prepare operands
2. Configure ALU

### Instruction Execution

1. Use ALU to calculate:
    1. Arithmetic result
    2. Memory address for load/store
    3. Branch target address
2. Possibly memory R/W or update registers (including PC)

## Instruction Fetch Component

![[image 1 8.png|image 1 8.png]]

## R-Format Instructions

Decode: Latches the content of two register operands to the output registers + config ALU

Execute: Perform arithmetic/logical operation + store results to the destination register.

## Load/Store Instructions

Decode: Read register operands

Execute: Calculate address using 16-bit offset.

- Use ALU, but sign-extend offset

Load: Ready memory and update register.

## Branch Instructions

Read register operands

Compare operands

- Use ALU, subtract and check zero output.

Calculate target address

1. Sign-extend displacement
2. Shift left 2 places (word displacement)
3. Add to PC + 4
    1. Already calculated by instruction fetch.

## Integrated Datapath with Control Unit

![[image 2 8.png|image 2 8.png]]

Control Unit is the circuit that manages instruction fetch-execution by decoding instruction bits into relevant control signals.

## Implementing Jumps

Jump uses word address

Update PC with concatenation of

- Top 4 bits of old PC
- 26-bit jump address
- 00

Need an extra control signal decoded from opcode

- Called a jump control
- Asserted (set) only when opcode has the value of 2

PC - Program Counter which allows the CPU to fetch instructions from memory in a sequential manner.

## MIPS Control

### ALU Control

ALU is used for various instructions

- Load/store: F = add
- Branch: F = subtract
- R-type: F depends on func field

Assume a 2-bit ALU Op derived from the opcode

- Combinatorial logic derives ALU control.
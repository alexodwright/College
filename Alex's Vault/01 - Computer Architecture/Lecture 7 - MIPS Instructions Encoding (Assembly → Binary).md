MIPS instructions have a fixed size of 32 bits

The layout of the 32 bits is defined as the ==Instruction format==

Basic MIPS Instructions have three key instruction formats:

- R-format (ALU, …)
- I-format (lw, sw, addi)
- J-format (j)

## MIPS R-format Instructions

Fields for ==Register Instruction format==

- op: operation code(opcode)
- rs: first source register number
- rt: second source register number
- rd: destination register number
- shamt: shift amount (00000 for now)
- funct: function code(extends opcode)

ALU instructions, others later.

Remember that MIPS has 32 registers (32 = $2^5$﻿) → 5 bits are needed to identify every register in the register file.

![[image 8.png|image 8.png]]

## MIPS I-format Instructions

![[image 1 5.png|image 1 5.png]]

Immediate arithmetic, load/store, branch instructions

- rs: source register
- rt: target register
- Constant: $-2^{15}$﻿ to $2^{15}$﻿-1

Example: lw $t0, 1200($t1)

## Signed Extension (revisited)

Signed extension is also used for extending:

- immediate values (e.g., addi, …)
- OFFSET (16 bits) of lw, sw, …

## Supporting Large Constants

Most constants are small

- 16-bit immediate is sufficient (make common case fast)

For the occasional 32-bit constant (large constant) [2 steps]

1. lui $at, constant
    1. Copies most significant 16-bit constant to the left by 16 bits of $at
    2. Clears right 16 bits of $at to 0
    3. $at (register \#1): **assembler temporary**
2. ori lower half
    1. Example: li $t0, 0x 007D 0900
    2. lui $at, 0x7d
    3. ori $t0, $at, 0x900

## MIPS Addressing Mode Summary

==Addressing modes== refers to the way in which the operand of an instruction is specified.

![[image 2 5.png|image 2 5.png]]

## Remarks on MIPS ISA Design

- The design of instruction set requires a delicate balance among
    - The number of instructions needed to execute a program
    - The number of clock cycles needed by an instruction
    - The speed of the clock
- MIPS achieves this balance by following some design principles
    1. Make the common case fast
    2. Simplicity favours regularity
    3. Smaller is faster.

## MIPS ISA Design Principles

- Design Principle 1: Smaller is faster
    - Desire to maintain fast execution time
    - Number of registers. More registers mandates longer identifier
    - Instruction size. One word instructions enables fetching the instruction in one step
- Design Principle 2: Simplicity favours regularity
    - Regularity makes implementation simpler → higher performance at lower cost
    - Instruction format layout is similar → simplifies the HW implementation
- Design Principle 3: Make the common case fast (design for common case)
    - Small constants are common (small immediate values)
    - Small loops are more common (small immediate values)
    - Immediate operand avoids a load instruction (addi, …)**
## MIPS Integer Arithmetic Instructions

### Integer Arithmetic

Processors may have different capabilities: data unit (e.g., 8-bit, 16-bit, 32-bit, ..) and types of operands (integer only, any numbers)

MIPS can process both integer and floating-point numbers

- A special coprocessor is used for floating point operations
- MIPS also has both 32-bit and 64-bit architectures (but we only focus on 32-bit MIPS architecture)

Integers: negative-0-positive

We consider sign-bit representation for negative numbers (simpler ALU HW)

|   |   |   |
|---|---|---|
||Unsigned|Signed|
|Range|0 to (2n – 1)  <br>32-bit (0 to +4,294,967,295)|(–2n-1) to (2n-1-1)  <br>32-bit (–2,147,483,648 to  <br>+2,147,483,647)|

## 2s - Complement Signed Integers

Bit 31 is a sign bit

- 1 for negative numbers
- 0 for non-negative numbers

Non-negative numbers have the same unsigned and 2s-complement representation

Some specific numbers:

- 0: 0000 0000 … 0000
- -1 1111 1111 … 1111
    - Most-positive: 0111 1111 … 1111
    - Most-negative: 1000 0000 … 0000

## MIPS Arithmetic Operations

E.g. add, subtract

Exactly three ==operands==

- Two sources and one destination

```Assembly
Ins $result, $operand1, $operand2
add $t0, $S1, $S2 # t0 = S1 + S2
a = b + cz 
```

MIPS Arithmetic instructions only use register operands

Other processors may use memory or an implied register

Assembly instructor operands are either ==registers== or ==memory== operands.

## Key Integer MIPS Instructions

![[image 6.png|image 6.png]]

## Immediate Operands

Constant data specified in an instruction

![[image 1 3.png|image 1 3.png]]

==No subtract immediate== instruction

Just use a negative constant (remember RISC)

```Assembly
addi $s2, $s1, -1
```

## The Zero Register

MIPS register 0 ($zero) is the constant 0

- Hardwired (Cannot be overwritten)

Useful for common operations

```Assembly
add $t2, $s1, $zero # no need for move instruction
addi $t2, $zero, 5 # a new load immediate (li) instruct
# can be used for variable initialization
```

## Memory Related Instructions

### (Read from and write to memory)

![[image 2 3.png|image 2 3.png]]

1. CPU puts the memory location address on the address bus
2. CPU activates control line to indicate whether it is a read or write operation
3. CPU puts (reads) data on (from) the data bus from (to) one of its registers.

### Register vs Memory Performance

- Registers are faster to access than memory
- Operating on memory data requires ==load== and ==store==
    - More instructions to be executed
- Programmer (Compiler) must use registers for variables as much as possible
    - Only spill to memory for less frequently used variables
    - Register optimization is important!

### Memory Operands

Main memory used for composite data

- Arrays, structures, dynamic data

Data transfer instructions

- Load values from memory into registers
- Store result from register to memory

MIPS Memory is ==byte-addressed==

→ you can read/write byte or larger data unit

MIPS words are ==aligned== in memory

- Word can be only accessible at an address that is a multiple of 4
- Half-word address @ multiple of 2

MIPS is Big Endian

Most-significant byte at least address of a word

c.f. Little Endian: least-significant byte at least address

![[image 3 3.png|image 3 3.png]]

### Memory Operand Example 1

Base address:

- A reference for array start
- 0x1001000 in this example
- Typically obtained using load address (la $s3, A)

![[image 4 3.png|image 4 3.png]]

```Assembly
la $s3, A # load base address
lw $t0, 12($s3) # load 4 bytes starting at 12+[$s3]
```

12 is the offset: byte offset from the array start

$s3 is the base register: the address of the first item in the array.

An array index 3 requires an offset of 12 (i.e., 4 * 3 = 12) - 4 bytes per word.

![[image 5 2.png|image 5 2.png]]

![[image 6 2.png|image 6 2.png]]

## What does every load instruction mean?

la $t4, label → loads memory address instruction of a label.

- After execution: $t4 = 0x10001000 (address of the first array element)
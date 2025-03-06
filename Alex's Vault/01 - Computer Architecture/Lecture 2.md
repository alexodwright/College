### HLL vs Assembly

|   |   |   |
|---|---|---|
|**Feature**|**High-Level Language**|**Assembly Language**|
|**Abstraction Level**|High|Low|
|**Readability**|Easy to understand|Difficult to read|
|**Portability**|High|Low|
|**Efficiency**|Generally slower|Generally faster|
|**Complexity**|Simpler to learn|Complex to learn|
|**Control**|Less control over hardware|More control over hardware|

## What happens when you execute a binary (executable) file?

### First: Binary File Format [Unix]

- **Header** describes the size and position of the other pieces of the file.
- **Text segment** contains the machine language code for routines in the source file (text section in assembly).
- **Data segment** contains a binary representation of the data in the source file (data section in assembly).
- **Relocation information** identifies instructions and data words that depend on absolute addresses.
- **Symbol table** associates addresses with external labels in the source file and lists unresolved references.
- **Debugging information** contains a concise description of the way in which the program was compiled.

## Binary File Loading

![[image 4.png|image 4.png]]

In Unix, the operating system performs the following steps:

- Reads the file’s header to determine the size of the text and data segments.
- Creates a new address space for the program.
- Copies text and data to respective memories.
- Copies passed program arguments to the stack.
- Initializes the CPU registers (IP, SP, …)
- Runs the program’s first instruction.

![[image 1 2.png|image 1 2.png]]

## MARS: (MIPS Assembler and Runtime Simulator)

MARS is a lightweight interactive development environment (IDE)

# Instruction Set Architecture

The ISA defines how the CPU is controlled by the software.

SW Analogy: ISA is similar to a library API that is used without understanding the implementation.

==Common ISA’s:== 80 x 86, ARM, MIPS

Software:

- Application
- Operating System
- Device Drivers

Hardware:

- Processor
- Memory
- I/O
- Circuits
- Devices
- Materials

### Role of ISA

Abstraction: It provides an abstraction layer between hardware and software, enabling programmers to write code without needing to understand the intricacies of the underlying hardware.

Compatibility: The ISA allows software to be compatible with different generations of processors that support the same ISA.

## ISA Key Components

Data Types: supported by the CPU (n-bit integer, float, double …)

Registers: The ISA specifies the number, size, and types of registers (small, fast CPU data storage locations).

Instruction Set: All operations that a particular CPU can execute (add, sub, mul, div, and, or, lw, lb, se, sb, j, jal, beq, …)

Instruction Formats: The layout of the binary instructions, including fields for the operation code (opcode), operand(s), and other necessary information.

Addressing Modes define how the CPU access operands (register vs memory operands)

Memory Architecture: How memory is organized and accessed, including memory addressing modes, stack management.

## MIPS Instruction Set Architecture

### MIPS Registers

Main CPU Registers

- Integer Operations
- Control Registers

Floating Point Registers

- FP coprocessor

Exception Coprocessor

## MIPS Main CPU Registers

32x32-bit register file

Registers are almost the variables.

![[image 2 2.png|image 2 2.png]]

## MIPS Register Functions

==*** REGISTER FUNCTIONS ***==

## Instruction Set

Instruction sets of different processors perform similar functions:

1. Arithmetic & logical operations (add, sub, mul, div, and, or, ..)
2. Memory and port transfers move data between the CPU and other computer elements
3. Flow control. (j, beq, jal, …)

Each instruction involves ==operands== that could be processor specific registers and/or memory content.

![[image 3 2.png|image 3 2.png]]

## Instruction Set Design Approaches

|Basis|RISC|CISC|
|---|---|---|
|Full Form|Stands for Reduced Instruction Set Computer|CISC stands for Complex Instruction Set Computer|
|Type of Instruction|RISC processors have simple instructions taking about one clock cycle|CISC processor has complex instructions that take up multiple clocks for execution|
|Instruction Set|The instruction set is reduced i.e. it has only a few instructions in the instruction set. Many of these instructions are very primitive.|The instruction set has a variety of different instructions that can be used for complex operations.|
|Execution Time|In RISC Execution time is relatively small.|In CISC Execution time is very high.|
|Examples|The most common RISC microprocessors are Alpha, ARC, ARM, AVR, MIPS, PA-RISC, PIC, Power Architecture, and SPARC.|Examples of CISC processors are the System/360, VAX, PDP-11, Motorola 68000 family, AMD and Intel x86 CPUs.|
|Average CPI|The average CPI _(Cycle Per Instruction)_ is 1.5 in RISC|The average CPI is in the range of 2 and 15.|
|Focus On|Software Centric Design|Hardware Centric Design|

## MIPS Instruction Set: An Overview

![[image 4 2.png|image 4 2.png]]

## Data Section

- Is used to declare and initialize global variables.
- Starts by .data ==assembler directive== in the code

Examples:

```Assembly
.data
count: .word 5 # integer initialized to 5
piVal: .float 5 # floating point number initialized to 3.14
array: .word 1, 2, 3, 4, 5 # integer array initialized to 1, 2, 3, 4, 5
msg: .asciiz "Hello, world!\n" # string initialized with the value
```

- Line 1: instructs the assembler to store the following in the program data segment
- Line 2: instructs the assembler to reserve 4 bytes and store the binary equivalent of 5 in these bytes.
- Line 3: instructs the assembler to reserve 4 bytes and stores the binary representation of floating point number 5.0 in these bytes.
- Line 4: instructs the assembler to reserve 20 bytes and store the binary equivalent of 1, 2, 3, 4, 5 in these bytes (each in 4 bytes)
- Line 5: instructs the assembler to reserve _____ bytes and store the binary representation of the string “Hello, world!” in these bytes

## I/O Syscalls in MIPS

- Any assembly will rely on OS code (device drivers) to deal with I/O operation (Similar to import OS)
- ==syscall== instruction is used to execute such OS code.
- syscall needs procedure ID and may need procedure arguments

1. syscall ID is stored in $v0
2. syscall arguments should be in $a0, $a1, … before executing syscall instruction
3. syscall outcome is typically stored in $v0 register

## Example \#1 Syscall to print string

```Assembly
.data 
	prompt1: .asciiz "Enter first integer: "
	
	li $v0, 4 # syscall code for print_string
	la $a0, prompt1 # load address of prompt1 into $a0
	syscall
	
	li $v0, 5 # syscall code for read_int
	syscall
	move $t0, $v0 # move the first integer into $t0
```

- loads print string syscall ID 4 in $v0
    - it uses load immediate (li) instruction
- loads the address (la) of the string to be displayed in $a0
    - after executing this instruction, the address of prompt1 will be stored in $a0.

Everything is ready to execute in the system with the last line - syscall

loads read an integer syscall ID 5 in $v0

No arguments are needed here →

==*** ***==

## Syscall Service References

![[image 5.png]]
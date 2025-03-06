## Signed Extension

- Needed when loading a byte, or half-word to MIPS 32-bit registers.
    - Unsigned values: extend with 0s.
    - Signed numbers: replicate the sign bit to the left.
- Examples: 8-bit to 16-bit.
    - +2: 0000 0010 → 0000 0000 0000 0010
    - -2: 1111 1110 → 1111 1111 1111 1110
- In MIPS instruction set.
    - lb, lh: extend loaded byte/half-word in the register.

## Branching (Flow Control)

### Conditional Branching

- HLL: if, case, loop
- MIPS Assembly: beq, bne, bgtz, bltz, bgez, blez

### Unconditional Branching

- HLL: break, Function calls
- Assembly: j (goto), jal (=call), jr (=return)

Branch instructions may only change then program counter new PC =/= PC + 4

## Key Branching Instructions

```Python
beq rs, rt, L1 # if (rs == rt) branch to instruction labelled
\#L1 otherwise proceed to next instruction

j mytarget # branch to isntruction at mytarget.
```

HLL code:

```Python
if (i==j):
f = g + h
else:
f = g - h
```

|   |   |
|---|---|
|f|$s0|
|g|$s1|
|h|$s2|
|i|$s3|
|j|$s4|

Compiled MIPS code:

```Assembly
beq $s3, $s4, if # start of it state
else: sub $s0, $s1, $s2 # else block start
j endif # else block end
if: add $s0, $s1, $s2 # if block start
endif: subsequent instructions after
```

line 3 ensures that only one block (if or else) is executed.

**Other Instructions:** bne, bgtz, bltz, bgez, blez

## MIPS Instruction Offset

```Assembly
beq rs, rt, L1
j mytarget
```

- The offset is signed (goes up or down)
- The offset represents how many ==instructions== is the target far ==from the next instruction.==
- 16-bit in branch / 26 bits in jump
- Remember: MIPS has a fixed size instruction (4 bytes)

beq (condition in general) —> new PC = (PC + 4) + offset x 4*[label value]

j instruction

==Unconditional== branch instruction

```Assembly
j Label # jump to instruction at Label:
```

==ONLY Use== J to build conditional logic (if and loop)

==Do NOT use jump== for function calls or alternating between code blocks

|   |   |
|---|---|
|2|10000|
|6-bits|26-bits|

New PC —> j instruction enables performing ==FAR== jumps 26 bit —> -+ 32M instructions —> 128 Mbytes

This is how big your if block could be.

## Adding Array Elements Using a Loop

```Assembly
.data
array: .word 5, 10, 15
.text
.globl main
main: la $t4, array # load the base address of the array into $t4
	li $t5, 0 # initialize loop counter
	li $t3, 0 # initialize sum of array elements
	li $t6, 3 # load the number of elements (3) into $t6
loop: li $t0, 0 ($t4) # load the element at offset 0
	add $t3, $t3, $t0 # add the current element to the sum
	addi $t4, $t4, 4 # increment by 4 bytes to move to the next element
	addi $t5, $t5, 1 # increment the loop counter
Loop: bne $t5, $t6, loop # 
	move $a0, $t3
	li $v0, 1
	syscall
	# exit the program
	li $v0, 10
	syscall
```

  
  

## Pseudo Branching Instructions

BLT is not a basic MIPS instruction, why?

It’s too complicated to implement —> Design Decision

Would stretch the clock cycle time

==**Solution:**== use two basic instructions to execute its logic.

### Set Instructions

```Assembly
slt rd, rs, rt # if (rs < rt) rd = 1; else rd = 0
slti, rt, rs, const # if (rs < constant) rt = 1; else rt = 0

BLT

slt $t0, $s1, $s2 # if ($s1 < $s2) --> t0 = 1
bne $t0, $zero, L # branch to L if $s2 < $s2
```

Yes, you can write blt in the editor

But it will be translated into 2 instructions.

## Signed vs. Unsigned

Signed comparison: slt, slti

Unsigned comparison: sltu, sltui

## Example

- $s0 = 1111 1111 1111 1111 1111 1111 1111 1111
- $s1 = 0000 0000 0000 0000 0000 0000 0001

```Assembly
slt $t0, $s0, $s1 # signed
-1 < +1 --> $t0 = 1
sltu $t0, $s0, $s1 # unsigned
```

## MIPS Logic Instructions

### Logical Operations

- Instructions for bitwise manipulation
- Bit is the smallest data unit (used in real applications)

|Operation|C|Java|MIPS|
|---|---|---|---|
|Shift Left|<<|<<|sll|
|Shift Right|>>|>>>|slr|
|Bitwise AND|&|&|and, andi|
|Bitwise OR|\||\||or, ori|
|Bitwise NOT|~|~|nor|
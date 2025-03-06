## Bitwise Operations - Relevant Applications

- Embedded Systems:
    - Bitwise operations are heavily used in embedded systems for controlling hardware. For example, setting, clearing, toggling, or checking the status of individual bits in hardware registers.
- Fast Arithmetic Operations
    - sll one position is same x2
    - slr one position is the same as /2
- Networking and Communication Processing
- Data compression and encryption

## I/O Big Picture

![[image 7.png|image 7.png]]

I/O device appears as a set of special-purpose registers to the CPU

- Status registers: usually read-only to determine the state of the device
- Configuration/control registers → configuration registers are usually read-only while control can be read/write.

![[image 1 4.png|image 1 4.png]]

## MIPS I/O addressing

![[image 2 4.png|image 2 4.png]]

MIPS uses memory mapped I/O addresses

- Registers have memory addresses

MIPS I/O uses memory instructions (e.g., lw, lb, …) to transfer data between I/O registers (RISC)

- Intel has in and out instructions (CISC)

## AND Example: Keyboard Interaction

### Receiver control register

@0xffff0000

Bit 0 (R) is the **ready bit:**

- Set to 1 by the keyboard controller when a key is pressed
- Cleared automatically when the receiver data register is read.

### Receiver data register

@0xffff0004

The low bits of this register contain the ASCII/ISO code of the last key that was pressed.

![[image 3 4.png|image 3 4.png]]

```Assembly
getChar:
	lui $t0, 0xffff # address of keyboard control register 0xffff 0000
	li  $t1, 1 # ready bit MASK (least significant bit) 0x0000 0001
key_wait:
	lbu $t2, ($t0) # read keyobard control register at xffff 0000
	and $t2, $t2, $t1 # apply ready bit mask
	beqz $t2, key_wait # 0 no key press --> busy waiting, 1 a key is pressed
	lbu $v0, 4($t0) # load RECEIVER_DATA to $v0
```

## Multi-bit AND Operations

- Useful to checking/testing the value of specific bit(s)

### Steps

1. The data is loaded to a register $t2
2. A mask (test pattern) is loaded in an arbitrary register $t1
3. and mask with data and store in result
4. Check result and take actions

Applications:

- Is a button pressed?
- Read a sensor from multiple bits.

![[image 4 4.png|image 4 4.png]]

![[image 5 3.png|image 5 3.png]]

## Multi-bit Example

OX7800 = 0B 0111 1000 0000 0000

```Assembly
.text
main:
	lw $t0, 0xFFFFFFF0 # read the i/o register (at address 0xFFFFFFF0)
	lw $t1, 0x7800 # mask to extract bits 11-14
		and $t1, $t0, $t1 # test by mask and register
	srl $t1, $t1, 10 # shift the result to the right by 10 bits
	move $a0, $t1 # move the value of $t1 to $a0 for pri
	li $v0, 1 # load the print integer syscall code
	syscall # print the integer reading
	li $v0, 10 # load the exit syscall code
	syscall # exit the program
```

NOTE: MIPS use same memory instructions to read I/O ports (RISC instruction set)

## OR Operation

Useful to set one or more bits to 1 in a word and leave others unchanged.

- e.g., switch a LED on, set on a HW switch, set a configuration bit in an I/O control register.

### Steps

1. The port is read to register $t2
2. Relevant bits are set in another register ($t1)
3. OR two registers
4. Send the result to the target port

![[image 6 3.png|image 6 3.png]]

## NOT Operations

Useful to invert bits in a word

- Change 0 to 1, and 1 to 0

MIPS use NOR instruction for not

- a NOR 0 == NOT (a) (remember A or Zero = A)
- NOR $t0, $t1, $zero ($t0 = not($t1))

![[image 7 2.png|image 7 2.png]]

Remember: MIPS is a RISC processor.
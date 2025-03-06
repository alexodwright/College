`## Exceptions and Interrupts

- "Unexpected" events requiring change the instruction sequence of the user software

- Exception
	- Arises within the CPU
		- e.g., undefined opcode, overflow, divide by zero, address error, syscall, ...

- Interrupt
	- From an external I/O controller
		- E.g., keyboard, mouse, printer, network card, power failure.

**Traps** are special instructions used to trigger an interrupt (AKA, SW interrupts)

Different ISAs use the terms differently.
Handling exceptions always reduces the performance.

## Common Exception Causes

- **Arithmetic overflow** occurs when the absolute value of a result is too large for the format.
- **Arithmetic underflow** occurs when the absolute value of a result is too small for the format (e.g., floating point)
- **Divide by 0** exception is self-explanatory.
- **Illegal instruction** may happen if program counter or the memory was corrupted.
- **Bus error** for inaccessible resources
- **Segmentation fault** is an attempt to access memory in an illegal way.

## More on Interrupts

- Interrupts are hardware-triggered events to handle IO.
	- Remember: Handling I/O with **busy waiting** or **polling** wastes CPU time.

```Assembly
getChar:
	lui $t0, 0xffff
	li $t1, 1
key_wait:
	lbu $t2, ($t0)
	and $t2, $t2, $t1
	beqz $t2, key_wait
	lbu $v0, 4($t0)
```

- IO devices indicate the need of service by raising a **flag** (changing a bit value)
- A special hardware (Interrupt Controller) is responsible for communicating interrupt to the CPU
- On interrupt detection, ==*** ***==

## Interrupt Controller

A Generic Interrupt Controller (GIC) takes interrupts from peripherals, prioritizes them, and delivers them to the appropriate processor core.

![[Pasted image 20241104101259.png]]
## Handling Exceptions and Interrupts

### Interrupt service routine(s) (ISR)

- A special OS (kernel) program that is executed in the event of exception or interrupt
- Reaching ISR(s)
	1. Interrupt Vector Table (IVY)
	   OS maintains a table that maps the interrupt reason to an address to its service routine (handler). When an interrupt occurs, the CPU jumps to the address specified in the IVT for that interrupt.
	2. Single Entry Point
	   OS has a single ISR for all interrupts and the cause is examined in this code (MIPS).
	   - In MIPS, the exception handler is always located at 0x80000180.
	   - When an exception occurs, the processor always jumps to this instruction address, regardless of the cause.

### What are the actions implemented by the handler?

- Fatal problem (e.g., segmentation or bus errors)
	- The running program may be terminated and the offending instruction should be reported for debugging.
- Recoverable issue (e.g., IO operation)
	- Continue the execution of the current program after handling the input.

### Handling Exceptions / Interrupts

1. Hardware saves current PC in a **special register**
2. CPU jumps to an exception handler, which
	1. Saves the current processor state (registers)
	2. Take appropriate internal action for an exception, or deal with the external source of the input.
	3. Restores the previous processor state
	4. Resumes user program execution (if possible) from step 1.

Exception handler resides in **kernel memory** (ktext not text)
- In any OS, kernel code has extra privileges and protection over user code (this is not simulated MARS).

## Handling Exceptions in MIPS

### MIPS HW for Exceptions

MIPS uses **coprocessor 0** for exception/interrupt handling.
The following registers are simulated in MARS.

![[Pasted image 20241104102242.png]]

### Status Register (**MIPS $12@C0**)

- Interrupt enable bit: global interrupt enable (or disable)
- Exception level bit: automatically set during an exception.
	- Can be used to prevent handling itself being interrupted
- User mode bit: 1 for user code - 0 when executing ktext.
	- MARS does not implement this change (always 1).
- Interrupt mask: which of the 8 inputs are allowed
	- Eight interrupt bits: 6 hardware, 2 software levels.

![[Pasted image 20241104102600.png]]

## Cause Register (MIPS $13@C0)

- **Mostly read-only** register whose value is set by the system.

![[Pasted image 20241104102654.png]]
#### Common Exception codes:

![[Pasted image 20241104102719.png]]

**Code = 0 for interrupts**
- **Which one?** Pending interrupts is bit-field of the 8 interrupts.

## MIPS Coprocessor0 Instructions

Special Register Instructions (**mfc0** and **mtc0**)

```Assembly
# move from coprocessor 0

mfc0 $reg, $regC0 # $reg << $regC0

# move to coprocessor 0

mtc0 $reg, $regC0 # reg << $regC0

# example: allow all hardware interrupts

mfc0 $t0, $12
ori $t0, $t0, 0xff01
mtc0 $t0, $12
```

lwc0 and swc0 are other coprocessor 0 instructions.
- lwc0 c0Reg, address
- swc0 c0Reg, address

## MIPS Interrupt/Exception Handler

- Handler always at address 0x80000180 in kernel memory
	- Use the .ktext 0x80000180
- Mut not change any register except $k0 and $k1 can be freely used.
	- Including $at
	- Should not use stack to save register values.
	- Solution: Temporarily spill used registers to reserved memory in kdata.

Return control to the user program with eret
Jumps to EPC, and resets Exception level in Status
- Handler must increment EPC by 4 to proceed to the next instruction.



## Procedure (functions)

```Assembly
sum_list: li $v0, 0 # initialize the sum to 0
loop: beqz $a1, done # if the size is 0, exit the loop
	lw $t0, 0($a0) # load the current integer into $t0
	add $v0, $v0, $t0 # add the current integer to the sum
	addi $a0, $a0, 4 # move to the next integer
	subi $a1, $a1, 1 # decrement the size
	j loop # repeat the loop
done: jr $ra # return to the calling function
```

Procedure name is used as a label (remember that labels are just pointers to be mapped by the assembler.

MIPS procedures end with the jr instruction.

## MIPS Procedure Call and Return

## **Procedure call:** jump and link (==jal==)

jal sum_list

- Instructs the processor to branch to the instruction at sum_list label with a return status. → This status stores the address of the first instruction in the procedure [jump] = $PC
    
    $ra ← stores the address of the next function after jal [link]
    

## Procedure return: jump register (==jr==)

jr $ra

- $PC ← $ra Unconditional jump to the next instruction in the calling code → Execute the instruction after jal.

We can’t use two jumps at the end of the procedure as you can only jump back to one label at a time.

## MIPS Register Rules for Procedures

$a0 - $a3: arguments registers for passing parameters (reg’s 4-7)

$v0, $v1: registers for result values (reg’s 2 and 3)

## Register Rules

- $t0-$t9: temporaries which can be overwritten by callee >> must not be saved by caller if needed.
- $s0-$s7: saved registers can not be overwritten by callee >> must be saved/restored by callee.

We use the stack to save and restore data.

## Stack

- A last-in-first-out (LIFO) queue for storing register content.
    - Stack pointer ($SP) points to the most recent allocated address in the stack.
    - MIPS stack is managed manually
    - The stack grows in a decreasing address direction.

```Assembly
addi $sp, $sp, -4 # save s0 on stack before using it in the procedure
sw $s0, 0($sp)
```

```Assembly
lw $s0, 0($sp) # restore $s0 before exiting the procedure
addi $sp, $sp, 4
```

## String Copy Procedure

### Arguments

- Addresses of strings are in $a0, $a1 - Null Terminated String
- i in $s0

### MIPS code

```Assembly
strcpy:
	addi $sp, $sp, -4 # adjust stack for 1 item
	sw $s0, k0($sp) # save $s0
	add $s0, $zero, $zero # i = 0
next: add $t1, $s0, $a1 # addr of y[i] in $t1
	lbu $t2, 0($t1) # $t2 = y[i]
	add $t3, $s0, $a1 # addr of x[i] in $t3
	sb $t2, 0($t3) # x[i] = y[i]
	beq $t1, $zero, exitloop # exit loop if y[i] = 0
	addi $s0, $s0, 1 # i = i+1
	j NEXT # next iteration of the loop
exitloop: lw $s0, 0 ($sp) # restore saved $s0
addi $sp, $sp, 4 # pop 1 item from the stack
jr $ra # and return 
```

Leaf Procedure: A procedure that does NOT call another procedure (i.e., do the job and return to caller - do not use ==jal==)

## Non-Leaf Procedures

- Procedures that call other procedures (including recursive calls)
- Every non-leaf procedure should
    - save the return address register (every jal will change $ra)
    - save any argument and temporaries needed after the call
    - restore saved from the stack after the call

| Preserved                     | Not preserved                   |
| ----------------------------- | ------------------------------- |
| saved registers: $s0-$s7      | temporary registers: $t0-$t9    |
| stack pointer register: $sp   | argument registers: $a0-$a3     |
| return address register: $ra  | return value registers: $v0-$v1 |
| stack above the stack pointer | stack below the stack pointer   |

## Non-Leaf Procedure Example

Write a procedure that calculate factorial n in a recursive fashion.

### Arguments

- Argument n in $a0
- Result in $v0

*** Code in the lab ***
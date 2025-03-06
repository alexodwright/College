## Sample Exam

![[CS2507Winter2023_24.pdf]]

### Identify three differences between RISC and CISC instruction set architectures.
[[01 - Computer Architecture/Lecture 2]]

### Considering the following MIPS assembly code
```Assembly
.data
Z: .word 65
X: .double 65
```
1. How many bytes are reserved in the memory?
2. Write down the binary representation of the stored numbers (show your steps).

Answers:
1. 12 - word(4) + double(8)
2. ...01000001 - 64 + 1 = 65

### Your friend claimed that doubling the processor speed is better than using two identical cores. Do you agree or disagree? Explain.
[[Computer Performance]]

### Name hazard types in pipelined processor architectures and identify the cause of them.

[[Lecture 11]]

### Increasing the pipeline stages has benefits and drawbacks. Discuss this statement based on your understanding of a pipelined processor.

### Associative memory has advantages and disadvantages. Explain.

Multiple locations are searched at a fast rate, by doing the comparison in parallel. Needs more hardware which is more expensive, which requires more power to run.

## Question 2

### Write the code needed to call this function with $a0=-2 and $a1=6

```Assembly
li $a0, -2
li $a1, 6
jal test_proc
```

### What would be the value in $a0, $a1, $v0 after executing calling the procedure with the values in part (i)

```Assembly
$a0 = 4
$v0 = 4
$a1 = 6
```

### Can you reduce the number of procedure instructions without impacting the functionality?

No need to push the value of $ra to the stack as we are not calling (jal) to any other function.

## Identify 2 standard (basic) and 2 pseudo-MIPS instructions in the procedure code.

Standard:
- addi
- sub
Pseudo:
- blt
- bge

### What would the instruction offset stored in `j label3` instructions when the instruction is encoded?

1. 3
2. 1

### Which register(s) may change after executing the procedure in comparison to before calling the procedure?

- $a0
- $v0
- $ra
- $sp
- $pc

### Does the "test_proc" procedure follow MIPS convention? If yes, why? If not, how can you fix it?

Yes it follows MIPS convention.

### What does "test_proc" do?

This procedure adds $a1 to $a0 if $a0 is less than 0
This procedure subtracts $a1 from $a0 if $a0 is greater than $a1

### Identify two pipelining hazards of distinct types in the code. For each one, identify the instruction(s) and hazard type.

- Line 2, 3, could cause a data hazard
- Line 5 could cause a control hazard with the branching instruction.

### Does the code have a double data hazard? If yes, identify the instructions, otherwise explain why?


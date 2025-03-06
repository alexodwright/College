## MIPS Pipelined Processor

Buffers introduced as interfaces between stages to keep the state of instructions as they propagate in the pipeline.

## Pipeline Hazards

	Situations that prevent starting the next instruction in the next cycle.

The processor needs to fetch an instruction from the memory at stage 1 and you need to execute a memory load instruction —> ==Structure Hazard *** ***==

### Structure Hazard - Conflict on HW Resources

In MIPS pipeline with a single memory:

- Load/store requires data access
- Instruction fetch would have to stall that cycle
    - Would cause a pipeline ‘bubble’

Solution:

- Pipelined datapaths require separate instruction and data memories

## Data Hazards

An instruction depends on data from a previous instruction that is still in the pipeline.

```PowerShell
add $s0, $t1, $t1 # the value of $s0 will be updated after 2 clock cycles
sub $t1, $s0, $t3 # wrong result if read from $s0
```

Trivial solution: Delay the dependant instruction.

## Solution 1: Forwarding (aka Bypassing)

HW connections that allow using the data when it is available (after computing or memory load)

Don’t ~~wait~~ for it to be stored in a register

==*** ***==

### Forwarding Unit

Forward implies ALU operands from a source other than the register-file

- Multiplexers are needed at the ALU I/P
- A forwarding unit determines the multiplexer control signal

![[image 12.png|image 12.png]]

### When does forwarding fail?

Load-Use data Hazard.

- Loaded data won’t be available before 2 cc.
- Can’t always avoid bubble/stalls by forwarding.
- Can’t forward backward in time.

## Code Scheduling

Reorder instructions to avoid the use of load result in the next instruction.

Code for A = B + E; C = B + F

## Hazard Detection Unit

Identify unresolvable hazards and stall the pipelines (bubbles)

### Memory Load-use Hazard Detection

Check when an instruction as decoded in ID stage

- If the ALU operand register numbers in ID stage are given by are target for a preceding load
- If detected, stall and insert bubble.

![[image 1 9.png|image 1 9.png]]

## Stall/Bubble in the Pipeline

### How to stall the pipeline?

1. Force control values in ED/EX register to 0
    1. EX, MEM and WB do nop (no operation)
2. Prevent update of PC and IF/ID register
    1. Fetch and decoding work is repeated.
    2. e.g., load-use case.  
        Stall 1 - cycle allows MEM to read data for lw and subsequently proceed to EX stage  
        

## Double Data Hazard

Consider the sequence:

```PowerShell
add $1, $1, $2
add $1, $1, $3
add $1, $1, $4
```

Solution: In this case, the processor should use the most recent result by properly designing the forwarding unit.

## Data Hazards for Branches

If a comparison register is a destination of 2nd or 3rd preceding ALU instructions

Branch operands can be resolved using forwarding.
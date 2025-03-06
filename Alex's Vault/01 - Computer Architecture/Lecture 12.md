## Handling control hazards

More challenging than data and structure hazards

We will explore some solutions:

- Stall on branch (do nothing - ==BAD== - no solution)
- Optimized waiting
- Delayed branch slot
- Prediction
    - Static Dynamic

## Stall on Branch

Wait until branch outcome is determined before fetching the next instruction.

A trivial solution - Always increases the CPI (Cycle per Instruction)

## Optimized Stall on Branch

Decide while decoding (additional HW)

- Not while executing - reduce one wait cycle.

### Optimized Stall on Branch HW

Equality check:

XOR then ORing bits for equality

If branching, the fetched instruction is flushed to a ==nop==.

## Delayed Branch Slot

- Schedule an instruction after the branch instead of the wait cycle
- The instruction should have no impact on the branch instruction.
- If compiler can not find an instruction, it just uses nop

Typical compiler strategies:

- From before - performance is always improvided
- From target - performance gain if branch is taken
- From fall through - performance gain if branch is not taken

Require complex compilers

## Branch Prediction

Adopted by most architectures

- Only stall if prediction is wrong
- Accurate prediction → high performance.

In simpler pipelines (e.g. MIPS), simple prediction policies are highly efficient.

In longer pipelines, complex HW but necessary due to high penalty.

Prediction policies may be dynamic or static.

### Branch Prediction Strategies

- Static branch prediction
    - Based on typical branch behaviour
        - Backward Taken Forward Not Taken (BTFNT)
        - Example: loop and if-statement branches
- Dynamic branch prediction
    - Hardware track branch behaviour (Taken or not)
    - Assume future behaviour will continue the trend.

## Dynamic Branch Prediction

Branch prediction buffer (aka branch history table)

- Indexed by branch instruction addresses
- Stores outcome (taken/not taken)

To predict a branch

- Check table, predict the outcome [repeat the last action]
- Start fetching from fall-through or target
- If wrong, flush pipeline and flip prediction.

## 2-Bit Predictor

Only change prediction on two successive mispredictions.
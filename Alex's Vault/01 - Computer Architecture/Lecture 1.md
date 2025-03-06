Computer Organization and Design - David Patterson

![[image.png]]

Computers are designed to serve different purposes.

The application domain defines the computer design goals that could be a combination of ==performance==, cost, energy consumption, and many other aspects.

  

Same components for all computers:

1. Inputs/Outputs
2. Memory/Storage
3. Processor

These components would have distinct physical and logical implementations

- The HW choice depends on many factors such as usage, cost, and energy efficiency.

# Computer Architecture

Computer architecture is the science and art of designing hardware components to create computers that meet functional, performance and cost goals.

1. Design Goals
    1. Performance
    2. Cost
    3. Energy Efficiency
    4. Reliability
    5. Time-to-market
2. Technology
    1. Circuit
    2. Packaging
    3. Memory
3. Domains
    1. PMD
    2. Server
    3. Game Consoles

### Key Decisions in Computer Architecture Design

**Instruction Set Architecture (ISA) -** Supported data types, instructions, addressing modes, instruction format.

**Processor Design -** One or more cores, supporting multiple instructions simultaneously

**Memory Design -** Cache memory and virtual memory.

**System Design -** I/O CPU interaction, bus design, power management.

  

High level language statements forming the needed logic to receive the input, process it, and generate output.

## Code Execution

The code runs in a CPU that only deal with binary instructions and data

The HLL statements should be encoded to equivalent CPU specific binary instructions.

![[image 1.png]]

**Datapath:** Is where data is processed (fetch, decode, execute)

**Control Unit:** Controls the CPU behaviour.

![[image 2.png]]

## Code Transformation

Instruction Elements

- Operation: Arithmetic, logic, memory.
- Operands: Data in registers and memory.
- Binary instructions encoding the operation and operands.
- CPU decode the instruction sand execute them to generate the desired output.

![[image 3.png]]

## Machine vs Assembly Instructions

Machine instructions are the Binary commands that tell the CPU what operations to perform, such as arithmetic operations, data movement, and control flow management.

Assembly Instructions are a more human-readable version of machine instructions of a particular CPU.

- Each assembly language command corresponds directly to a machine instruction.
- Assembly language uses mnemonic codes (like mov, add, sub, etc.) to represent the binary machine instructions.

Assembly is not easy to interpret as it is Hardware Specific

The code contains implied information about the processor like register names.

The instructions are defined by the instruction set architecture of the target processor e.g. Intel or ARM.
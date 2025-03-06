# Preliminaries: Computer System

## Conceptual View of a Computer System

A computer system can be divided roughly into three components: the hardware, the operating system, and the application programs.

## Operating System

An operating system (OS) is a program/software that manages the computer hardware.

The OS provides the means for proper use of resources in the operation of the computer system.

The OS provides a basis for application program sand act as an intermediary between user and hardware.

## Computer System

A modern general-purpose computer system consists of one or more CPU’s and a number of device controllers connected through a common bus that provides access to shared memory.

Each device controller is in charge of a specific type of advice.

### Some Important Terms

**Kernel**

- A kernel is a central component of an operating system that manages the operations of computer hardware's.

**Bootstrap Program**

- The first program that runs when a computer power-on is powered on or rebooted.
- It loads the operating system.

**Interrupts**

- The occurrence of an event is usually signalled by an Interrupt from Hardware or Software.
- Hardware may trigger an interrupt at any time by sending a signal to the CPU, usually through the system bus.
- Software may trigger an interrupt by executing a special operation called the System Call.

**Process**

- A process is a running program.

## Storage Device

![[image 14.png|image 14.png]]

## The Trade-Off

|   |   |   |
|---|---|---|
|Cell Type|Area|Typical Latency|
|Master Slave D flip flop|0.8$\mu m^2$|Less than nano sec|
|SRAM cell in an array|0.08$\mu m^2$|1-5 nano sec|
|DRAM cell in an array|0.005$\mu m^2$|50-100 nano sec|
|SSD|0.001$\mu m^2$|10-100 micro-sec|

### Faster is More Expensive

- SRAM, ~$1000 per GB
- DRAM, ~$20 per GB
- Hard Disk, ~$0.01 per GB

### Larger is Slower

## Memory Hierarchy

### Why Memory Hierarchy?

- We want both fast and large
- But we cannot achieve both with a single level of memory
- Idea: Have multiple levels of storage (progressively bigger and slower as the levels are farther from the processor).

![[image 1 11.png|image 1 11.png]]

## The Caches

The L1 Cache is a small memory (8-64 KB) composed of SRAM cells

The L2 Cache is larger and slower (128KB - 4MB) SRAM cells)

The main memory is even larger (1-64 GB) DRAM cells)

![[image 2 10.png|image 2 10.png]]

## Textbooks

Operating System Concepts 10th Edition - Abraham Silberschatz, Peter B Galvin, Greg Gagne
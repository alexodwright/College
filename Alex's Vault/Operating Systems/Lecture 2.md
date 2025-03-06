## OS Timeline

![[Pasted image 20250120131155.png]]

## Computer Hardware

- An operating system is intimately tied to the hardware
- Simple computer: I/O devices are all connected by a system bus.

## CPU - Instructions and Registers

- 'Brain' of the computer is the CPU
- CPU fetches instructions from memory and executes
- CPUs contain some registers to hold key variables
- Each CPU has a specific set of instructions
	- The instruction set contains instructions to load a word from memory into a register, and store a word from register into memory
	- Other instructions combine two operands from registers into a result and storing the result in a register.
- In addition to the general registers computers have special registers
	- Program counter: memory address of the next instruction to be fetched
	- Stack pointer: points to the top of the current stack in memory.

### Multiplexing

- The OS must be fully aware of all the registers
- When time multiplexing
	- The OS will stop the running program to (re)start another one
	- The OS saves all the registers so they can be restored when the program runs again

- Standard execution: Fetching, Decoding and Executing
- Superscalar: Multiple execution units are present

## User Mode and Kernel Mode

- CPUs have two modes: kernel mode and user mode
- Kernel Mode:
	- CPU can execute every instruction and use every feature of the hardware
	- OS runs in kernel mode, giving it access to the complete hardware.
- User mode:
	- User programs run in user mode, which permits only a subset of the instructions
	- Provides isolation between programs and also protection/security
	- User programs make system calls, which traps into the kernel and invokes the OS
	- The TRAP switches from user mode to kernel mode and starts the OS
	- When the work has been completed, the control is returned to the user program at the instruction following the system call.

## Multithreaded and Multicore Chips

- Multithreading or Hyperthreading
	- Holds the state of two different threads, switching on nanosecond time scale
	- If one process needs to read from memory (which takes many clock cycles), a multithreaded CPU can just switch to another thread
	- No true parallelism, only one process at a time is running
	-> Multithreading has implications for the operating system because each thread appears to the operating system as a different CPU!
- Multicore
	- Many CPU chips now have four, eight, or more complete processors or cores on them (each core may perform multithreading).
- GPU (Graphics Processing Unit):
	- A GPU is a processor with thousands of tiny cores.
	- Good at small parallel tasks, not so 'good at serial tasks.


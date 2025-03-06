The OS provides you with an interface for you as a user to interact with the computer.
It managers all the hardware and software in your computer.

## OS Purpose

The operating system as a resource manager.

Top-down view:
- Provide abstractions to application programs
Bottom-up view:
- Manage pieces of complex systems
- Provide orderly, controlled allocation of resources.

## Kernel and User Mode

The operating system runs in kernel mode (also called supervisor mode).
- Has access to all the hardware and can execute any instruction the machine is capable of.
The rest of the software runs in user mode
- Only a subset of the machine instructions is available
- Instructions that affect control of the machine or do I/O (Input/Output) are forbidden.
If a user doesn't like a particular email reader, he is free to get a different one or write his own if he so chooses; he is not free to write his own clock interrupt handler, which is part of the operating system as is protected by hardware against attempts by users to modify it.

Distinction of user mode and kernel mode is sometimes blurred.
- Embedded systems may not have kernel mode.
- Interpreted systems use interpretation, not hardware, to separate the components.
- Programs that run in user mode but help the operating system or perform privileged functions (e.g. passwd).
- In some systems, system kernel programs (such as the file system) run in user space.

## Where the Operating System fits?
![[Pasted image 20250114171959.png]]

## Abstractions

![[Pasted image 20250114172044.png]]


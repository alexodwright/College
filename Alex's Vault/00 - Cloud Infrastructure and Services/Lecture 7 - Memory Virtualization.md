- Memory virtualization allows a computer to run multiple operating systems (OS) or virtual machines (VMs) on the same physical memory.
- Each virtual machine thinks it has its own memory, but in reality, the actual memory is shared
- The hypervisor controls multiple operating systems running at the same time and manages how these systems use the computer’s real memory.
- Hypervisor maps each VM’s virtual memory to the real physical memory on the hardware.
- Requires multiple levels of mapping.

## Virtualizing Other Resources: I/O Virtualization

- The hypervisor provides virtual I/O devices (e.g., virtual hard drives, virtual network interfaces) to virtual machines (VM’s)
- The VM thinks it’s using real hardware, but the hypervisor is translating those requests to the actual physical hardware on the host machine.

How it works:

- The VM makes requests to virtual devices (e.g., to read/write data)
- The hypervisor intercepts those requests and passes them to the physical hardware.
- The physical device performs the task, and the hypervisor returns to the result to the VM as if it came from the virtual device.

### Example: Virtualizing Hard Drive

- Each guest OS thinks it “owns” the disk.
- Hypervisor creates “virtual disks”
    - Large empty files on the physical disk that appear as “disks” to the guest OS
- Stored as virtual disk or vmdk files.

## Virtual Machine (VM) Migration

VMs can be migrated from one physical machine to another

Why migrate VMs?

- Distribute VM load efficiently across servers in a cloud
- System Maintenance

What needs to be migrated?

- Memory (RAM)
- Storage (Disk)
- CPU State
- Network State

## Pre-Copy VM Migration

1. Enable dirty package tracking
2. Copy all memory pages to destination
3. Copy memory pages dirtied during the previous copy again.
4. Repeat the third step until the specified number of iterations is reached or the number of dirty pages falls below a certain threshold
5. Stop VM
6. Copy the rest of memory pages
7. Resume VM at destination.

## Downtime and Migration Time

1. Stop and Copy (Downtime): The downtime is primarily the time required to transfer the remaining dirty page sin the final round, when the VM is stopped.
    
    $T_{Downtime}=\frac{Remaining\space Dirty\space Pages}{B}$﻿
    
    If after n iterations, there are $D_n$﻿ dirty pages remaining, the downtime is:
    
    $T_{downtime}=\frac{D_n}{B}$﻿
    
2. Total Migration Time: The total migration time is the sum of all the iterations plus the downtime

==*** ***==
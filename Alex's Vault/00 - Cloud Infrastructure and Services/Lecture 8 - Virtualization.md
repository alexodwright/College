Virtualization is the process of creating a virtual version of something, such as a computer, server, or device, by using software to divide the physical resources into multiple virtual environments.

Introduced in 1970’s: Run legacy software on newer mainframe hardware.

## Types of Virtualization

Hardware Virtualization

- Virtualizes the physical hardware into multiple virtual machines (VMs)
- Example: VMware, Hyper-V

Operating System Virtualization

- Virtualizes the OS kernel to allow multiple isolated user-space instances (containers) to run at the same time.
- Example: LXC, Docker containers

Network Virtualization

- Abstracts physical network resources into virtual networks
- Example: Software-Defined Networking (SDN), Virtual LAN (VLAN)

## Hypervisors

![[image 19.png|image 19.png]]

Hypervisor runs on “bare metal”

Acts like a lightweight operating system and runs on hardware. This is the optimal solution for large production environments.

Examples: Xen, VMware ESXi

![[image 1 16.png|image 1 16.png]]

Runs on a host OS as an additional software layer

Guest OS runs inside hypervisor

Latency is higher

Example: VirtualBox, VMWare Workstation

## Types of Virtualization

Full Virtualization:

- The hypervisor provides a virtual hardware environment to the guest operating system (OS), making the guest OS believe it’s running on real, physical hardware
- The hypervisor handles all the hardware calls and translates them for the physical machine.

Para-Virtualization

- The guest OS is modified to be aware that it’s running on a hypervisor. Instead of making hardware calls as if it were running on bare metal, the guest OS directly interacts with the hypervisor using special APIs.
- Example: Xen with para-virtualized guests.

Emulation:

- The hypervisor emulates different hardware than what is physically present, allowing an OS designed for a different hardware architecture to run.
- Hardware and architecture do not need to match between the host and the guest.
- Example: QEMU.

## Benefits of Virtualization

Resource sharing - an increased use of resources by reducing the idle time

- Reduce hardware costs
- Power saving

Flexibility and scalability - multiple software running on the same computing platform

Isolation - protection from other tenants.

Simple Management - Easy distribution, deployment, testing and automation.

## Use of Virtualization Today

Data centres:

- Server consolidation: pack multiple virtual servers onto a smaller number of physical servers
- Saves hardware costs, power and cooling costs

Cloud Computing:

- Rent virtual servers
- Cloud providers control physical machines and mapping of virtual servers to physical hosts.
- User gets root access on virtual server
- Desktop Computing.

## Features of Interest

Shared folders provide the mechanism to exchange files between a host (OS) and a guest OS. Shared folders are available in VirtualBox, VMWare Workstation, Player and Fusion.

Snapshots save a VM state at a moment in time. Then, it is possible to roll back a VM to one of the snapshots to restore the VM state. When a snapshot of a running VM is taken, the virtual memory is also saved to a file.
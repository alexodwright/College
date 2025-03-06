
A computer system can be divided into 3 components:
1. Hardware
2. OS
3. Application Programs

## Operating System (OS)

An operating system (OS) is a program / software that manages the computer hardware.
The OS provides the means for proper use of resources in the operation of the operating system.
The OS provides a basis for application programs and acts as an intermediary between the user and the hardware.

## Computer System

A modern general-purpose computer system consists of one or more CPUs and a number of device controllers connected through a common bus that provides access to shared memory.
Each device controller is in charge of a specific type of device.

## Important Terms

Kernel: A central component of an OS that manages the operations of computer hardware.

Bootstrap Program: The first program that runs when a computer is powered on or rebooted. It loads the OS.

Interrupts: The occurrence of an event is usually signalled by an interrupt from hardware or software. Hardware may trigger an interrupt at any time by sending a signal to the CPU, usually through the system bus. Software may trigger an interrupt by executing a special operation called System Call.

Process: A process is a running program.

![[Pasted image 20241201143724.png]]

## Why a Memory Hierarchy

- We want both fast and large
- But we cannot achieve both with a single level of memory.

### The Caches

- The L1 cache is a small memory (8-64 KB) composed of SRAM cells
- The L2 cache is larger and slower (128 KB -4 MB) composed of SRAM cells
- The main memory is even larger (1-64 GB) composed of DRAM cells

# Networks

## What is a network

- A system of 'links' that interconnect 'nodes' in order to move 'information' between nodes.

### Nodes and Links

Channels = Links
Peer entities = Nodes

![[Pasted image 20241201144117.png]]

- Bandwidth (capacity): 'width' of the links
	- Number of bits sent (or received) per unit time (bits/sec or bps)

- Link Latency: 'length' of the link
	- Propagation time for data to travel along the link (seconds)
	- Also known as propagation delay
	- Propagation delay = $\frac{Distance}{LightSpeed}$

Packet Delay = $\frac{PacketSize}{LinkCapacity} + LinkLatency$

### Switched Networks

This is a network where nodes share network link resources

![[Pasted image 20241201144404.png]]

### Circuit Switching (Old Way)

- Establishes a dedicated communication path
- Allocated channel remains reserved

### Packet Switching

- No dedicated communication path
- Data is broken down into small packets, each of which can take different routes.

- Data is sent as chunks of formatted bits (Packets)
- Packets consist of a 'header' and a 'payload'
	- Payload is the data being carried
	- Header holds instructions to the network for how to handle the packet.
	- Headers may include:
		- Destination address
		- How this traffic should be handled
		- Who signed for it?
		- Are the contents OK?

### Layered Internet Protocol Stack

- Application: supporting network applications
	- HTTP, IMAP, SMTP, DNS
- Transport: end-end data transfer
	- TCP, UDP
- Network: routing of datagrams from source to destination
	- IP, routing protocols
- Link: Data transfer between neighbouring network elements
	- Ethernet, 802,11 (WiFi)
- Physical: bits 'on the wire'

### Network Devices

- Hubs:
	- Hub is a physical layer device i.e. Layer 1
	- Broadcast: All frames are sent out all physical ports
- Switches:
	- Switch is a data link layer device, i.e. Layer 2.
	- Only send frames to selected physical port based on destination MAC address
- Routers:
	- Router is a network layer device i.e. Layer 3
	- Only send packet to selected physical port based on destination IP address.

### Packet Loss in Communication Network

When accessing the internet, ethernet, LAN, or any other network, data packets are sent and received.
If one of these packets fails to reach its intended destination, what's known as 'packet loss' occurs.

What causes packet loss?:
- Network Congestion
- Issues with the networking hardware
- Loss in the communication channel (especially in wireless channel)

# Distributed Computer Systems

A distributed computing system:
- Multiple connected computing devices working together
- A collection of computers that usually appears to its users as a single coherent system
- Consists of 'nodes' (computer, phone, car, robot, ...)
- A distributed application in computing is a software application that runs on multiple computers within a network simultaneously.

- Some systems are inherently distributed
	- Accessing a shared document stored on a cloud service from multiple devices.
- For better reliability
	- Even if one node fails, the system as a whole keeps functioning.
- For better performance.
	- Get data from a nearby node rather than one halfway round the world.
- To solve bigger problems:
	- Huge amounts of data, can't fit on one machine.

- The trouble with distributed systems:
	- Communication may fail (and we might not even know it has failed)
	- Processes might crash (and we might not know)
- Fault tolerance
	- We want the system as a whole to continue working, even when some parts are faulty. This is hard.
- Writing a program to run on a single computer is comparatively easy.

## Cluster Computing

Cluster computing involves a group of interconnected computers working together as a single system, often within a single data center.

The computers are generally connected through fast local area networks (LANs)

It can be used as part of the underlying infrastructure in cloud computing environments, especially for high-performance tasks.

Usage example: Scientific simulations.

## Grid Computing

Grid computing is a distributed architecture that combines computer resources from different locations to achieve a common goal.

It can also be utilized in cloud computing to allocate resources from multiple locations for large-scale computations.

Usage example: Large-scale computations (e.g., SETI@home, CERN)

## Distributed Computing Model: Parallel Computing

The most common computing model is the farm model, where a central controller (like a 'farmer') distributes tasks or computations to a set of workers (PCs or nodes), ensuring the load is balanced across them.

Alternatively, the application can manage its own components, where individual parts of the job are run on different PC's./

The operation of the PCs is continuously monitored for failures. If a PC fails, it is automatically replaced by another available PC from a free pool of resources.

## Amdahl's Law

Consider an application with total workload W and execution time T when running on a single PC. A fraction of the workload denoted by p, can be parallelized across multiple PC's, say n PC's. The new execution time when using n Pc's is given by:

$T_{par} = (1-p)T + \frac{pT}{n}$

where $(1-p)T$ represents the portion that cannot be parallelized
$\frac{pT}{n}$ represents the portion that can be parallelized across n pC's.

The speedup, defined as the ratio of the original execution time to the parallelized execution time, is calculated as: 

![[Pasted image 20241201171228.png]]

Amdahl's Law provides a limit or upper bound on the achievable speedup in a parallel computing system.
- No communication Overhead
- Uniform Processing Power
- Ignores Memory Constraints.

## Distributed System Design Goals & Architectures

- An important goal of a distributed system is to hide the fact that its processes and resources are physically distributed across multiple computers, possibly separated by large distances.
- In other words, it tries to make the distribution of processes and resources transparent, that is, invisible, to end users and applications.

### Transparency in a Distributed System


![[Pasted image 20241201205625.png]]

### Openness in Distributed Systems

An open distributed system is essentially a system that offers components that can be easily used by, or integrated into other systems.
- Interoperability: Two implementations of systems or components from different manufacturers can co-exist and work together by following a common standard.
- Portability: An application developed for a distributed system A can be executed, without modification, on a different distributed system B.
- Extensible: It should be easy to add components or replace existing ones without affecting those components that stay in place.

### Dependability in Distributed Systems

Dependability refers to the degree that a computer system can be relied upon to operate as expected.

It covers several useful requirements:
- Availability is defined as the property that a system is ready to be used immediately.
- Reliability refers to the property that a system can run continuously without failure.
- Fault tolerance, meaning that a system can provide its services even in the presence of faults.
- Maintainability refers to how easily a failed system can be repaired.

### Security in Distributed Systems

A distributed system that is not secure, is not dependable.

- Data confidentiality:
	- Protect sensitive data during transmission and storage using encryption.
- Authentication and Authorization
	- Verify user identities and grant appropriate access levels using secure authentication methods.
- Secure Communication:
	- Use secure communication channels between distributed notes to prevent unauthorized access.
- Intrusion Detection:
	- Employ real-time monitoring and intrusion detection systems to detect malicious activity across the network.

### Scalability in Distributed Systems

Scalability of a system can be measured along the following dimensions:

- Size scalability: A system can be scalable regarding its size, meaning that we can easily add more users and resources to the system without any noticeable loss of performance.
- Geographical Scalability: A geographically scalable system is one in which the users and resources may lie far apart, but the fact that communication delays may be significant is hardly noticed.
- Administrative scalability: An administratively scalable system is one that can still be easily managed even if it spans many independent administrative organizations.

## Analysing Size Scalability

![[Pasted image 20241202145304.png]]

Arrival Rate ($\lambda$): The rate at which jobs or requests arrive in the system (requests per second).
Service rate ($\mu$): The rate at which jobs are processed by servers (requests processed per second).
Utilisation ($\rho$): $= \frac{\lambda}{\rho}$

Utilisation $\rho$ is the ratio of the arrival rate to the service rate, which represents the system's load. Utilisation tells us how busy the system is. Ideally, $\rho$ should be less than 1 for stable systems (where the service rate exceeds the arrival rate).

Utilisation $\rho_m$ considering multiple servers:
$\rho_m = \frac{\lambda}{m.\mu}$ where m is the number of servers (or cloud instances).

### Value of $\rho$

A utilisation of 100% (i.e. $\rho$ = 1) means that the system is fully utilised, but it leaves no room for handling bursts in traffic or unexpected demand spikes.

A too-low utilisation (e.g. $\rho$ < 0.5) means that the system is underused, which can result in wasted resources and unnecessary costs.

For most practical systems, an ideal utilisation falls in the range of 70% to 85%.

### What if the arrival rate is greater than the service rate?

- Growing Queue: Requests will start to queue indefinitely.
- High Latency: Users experience significant delays, as their requests take longer to be processed.
- Unstable System: Potential system failures due to overload or run into performance bottlenecks.
Solution: To prevent this, cloud computing systems typically implement scaling mechanisms (such as auto-scaling) that dynamically increase the service capacity (increase $\rho$) by adding more servers or processing power when the load becomes too high.

## Distributed System Architectures

### Client-Server Architectures

In a client-server system within a distributed system, clients request services or resources from servers over a network.

Clients initiate communication, send requests, and handle user interfaces, while servers listen for requests, perform tasks and manage resources.

Most common style: client-server architecture
- User-interface level
- Processing level
- Data level.

#### Multi-tiered approach

The simplest client-server architecture can be composed of:
- A client machine containing only the programs implementing (part of) the user interface level.
- A server machine containing the rest,
	- The programs implementing the processing and data level.

#### Edge-Server Systems

Edge servers: from client-server to client-proxy-server
- Content distribution networks: proxies cache web.
Content near the edge
- Evolved into edge computing model.

# Distributed System Architectures Peer-to-Peer (P2P)

In p2p systems, interconnected nodes directly communicate and collaborate without centralized control.
- Removes distinction between a client and a server.
Each node can act as both a client and a server, sharing resources and services with other nodes.

### File Transfer using Client/Server

![[Pasted image 20241202151243.png]]

![[Pasted image 20241202151255.png]]

### Client/Server vs P2P

- Clients request data or functionality from a server

Advantages:
- Easy to control access to resources and functionality (including providing security)
- Simple and efficient algorithms

Disadvantages:
- Single point of failure - if the server fails, the entire service is unusable.
- Bandwidth bottlenecks at the server.

- No distinction between clients and servers
- Individual peers can cooperate with each other.

Advantages:
- No longer depend on a single server (no single point of failure)
- Addition of new users, leads to new server and clients.

Disadvantages:
- Complex algorithms needed
- Hard to control access and provide security.

### P2P Implementation Choices

Unstructured versus Structured

- Unstructured: Peers connect randomly, with no predefined structure, making search and data retrieval less efficient.
- Structured: Peers and resources are organized in a specific topology.

Flat vs Hierarchical

- Flat: all nodes are equivalent (play same role)
- Hierarchical: some nodes have special functionality: e.g. only some nodes can search.

### Structured P2P System: Chord

Chord utilises a Distributed Hash Table (DHT), which distributes both the hash values and the keys across different nodes to store and retrieve key-value pairs efficiently.

N nodes in network:
- Aim to distribute files amongst the nodes, and locate the files

Hashing is used to assign ID's to nodes and resources (e.g. files).
- SHA-1 hash of node properties (e.g. IP address) produces 160-bit ID
- SHA-1 hash of file properties (e.g. name, type) produces 160-bit key, k

Visualise nodes as circle ordered by ID

Resource with key k is stored at node with ID = k
- If node with ID = k does not exist, resource is stored at node with the next highest ID.
- Consistent hashing

Node n joins the network
- Need to reassign keys from successor node.

Node n leaves the network:
- Need to reassign keys to successor node.

To insert data, insert(data)
- Node calculates hash of data (e.g. the file) to get k
- Routing is used to find the node that responsible for key (e.g., node k or > k)
- Data is stored on the node.

To search for data, search(k)
- Node calculates hash of data to get k
- Routing is used to find the node that stores k
- Any access method (e.g. HTTP) is used to retrieve data from node k.

# Chord: Searching/Routing

Simple routing:
- Each node n maintains route to successor:
	- Node n knows the IP address/port number of successor
- A simple (but naive) approach is to then try find the key by checking each subsequent successor
	- Example: node 0 knows the IP address/port of node 1; node 1 knows IP address/port of node 3 and so on
	- But may have to traverse all nodes to find the key
- But can provide more efficient search than this (at expense of maintaining more connections)

Routing in Chord:
- Each node maintains a routing table (also called a finger table)
- The routing table contains up to m entries considering the size of the keyspace is $2^m$.
- The $i^{th}$ entry in the finger table of a node with ID n points to the first node that succeeds $n + 2^{i-1}$ in the identifier space.
	- Example: node 0 knows route to 1, 2, 4, 8 (or next subsequent node if it does not exist); node 1 knows the route to 2, 3, 5, 9; and so on.
- The worst-case maximum number of hops (or lookup steps) required to locate a specific key in the Chord ring is $log_2(N)$ where N is the total number of possible nodes (or identifiers) in the system.

# Virtualization

Virtualization is the process of creating a virtual version of something, such as a computer, server, or storage device, by using software to divide the physical resources into multiple virtual environments.

Introduced in 1970's: Run legacy software on newer mainframe hardware.

### Types of Virtualization

Hardware Virtualization:
- Virtualizes the physical hardware into multiple virtual machines (VM's).
- Example: VMware, Hyper-V
Operating System Virtualization:
- Virtualizes the OS kernel to allow multiple isolated user-space instances (containers) to run.
- Example: LXC, Docker containers.
Network Virtualization:
- Abstracts physical network resources into virtual networks.
- Example: Software-Defined Networking (SDN), Virtual LAN (VLAN).

### Hypervisors

Type 1

- Hypervisor runs on 'bare metal'.
- Acts like a lightweight operating system and runs on hardware. This is the optimal solution for large production environments.
- Examples: Xen, VMware ESXi

Type 2

- Runs on a host OS as an additional software layer.
- Guest OS runs inside hypervisor
- Latency is higher.
- Example: VirtualBox, VMWare Workstation.

### Types of Virtualization

Full virtualization
- The hypervisor provides a virtual hardware environment to the guest operating system (OS), making the guest OS believe it's running on real, physical hardware
- The hypervisor handles all the hardware calls and translates them for the physical machine.

Para-Virtualization:
- The guest OS is modified to be aware that it's running on a hypervisor. Instead of making hardware calls as if it were running on bare metal, the guest OS directly interacts with the hypervisor using special API's.
- Example: Xen with para-virtualized guests.

Emulation:
- The hypervisor emulates different hardware than what is physically present, allowing an OS designed for a different hardware architecture to run.
- Hardware and architecture do not need to match between the host and guest.
- Example: QEMU.

### Benefits of Virtualization:

- Resource sharing - an increased use of resources by reducing the idle time.
	- Reduce hardware costs.
	- Power saving
- Flexibility and scalability - multiple software running on the same computing platform.
- Isolation - protection from other tenants.
- Simple management- easy distribution, deployment, testing and automation.

### Uses Today

- Data centers
	- Server consolidation: pack multiple virtual servers onto a smaller number of physical servers
	- Saves hardware costs, power and cooling costs.
- Cloud Computing:
	- Rent virtual servers
	- Cloud provider controls physical machines and mapping of virtual servers to physical hosts.
	- User gets root access on virtual server
- Desktop Computing

Features of Interest
- Shared Folders
- Snapshots and Rollback.


# Memory Virtualization

Memory virtualisation allows a computer to run multiple operating systems (OS) or virtual machines (VM's) on the same physical memory.
Each virtual machine thinks it has it's own memory, but in reality, the actual memory is shared.
The hypervisor controls multiple operating systems running at the same time and manages how these systems use the computer's real memory.
Hypervisor maps each VM's virtual memory to the real physical memory on the hardware.
It requires multiple levels of mapping.

## VM Migration

VM's can be migrated from one physical machine to another.
Why migrate VM's?
- Distribute VM load efficiently across servers in a cloud
- System maintenance.
What needs to be migrated?
- Memory (RAM)
- Storage (Disk)
- CPU state
- Network State

###  Types of Migration Techiniques

Pure Stop-and-Copy: The VM is stopped, all its information is sent to the new location, and then the VM restarts there.
Pre-Copy: Most of the VM's information is sent to the new location while it's still running, and then there's a short stop-and-copy phase to send any remaining data.
Post-Copy: The VM is stopped, and only the essential information needed to start it up is sent to the new location. The rest of the data is brought over as needed while the VM is running at the new place.
Hybrid: This method combines both pre-copy and post-copy. Some information is sent over while the VM is still running, then it stops to send more data, and finally, any remaining data is pulled as needed.

#### Pre-Copy VM Migration

1. Enable dirty page tracking
2. Copy all memory pages to destination
3. Copy memory pages dirtied using the previous copy again
4. Repeat the third step until the specified number of iterations is reached or the number of dirty pages falls below a certain threshold.
5. Stop VM
6. Copy the rest of the memory pages
7. Resume VM at destination.

#### Pre-Copy VM Migration: Downtime and Migration Time

M: Total memory size of the VM
D: Rate of dirty pages (pages modified per second)
B: Network Bandwidth
n: Number of iterations.

1.  Data transferred per Iteration: Each iteration transfers the dirty pages from the previous round.
- First iteration data transfer: All memory is copied
	- $Data_{Iteration1} = M$ 
- Subsequent iterations: After each iteration, dirty pages are recopied. For iteration i, assuming a fixed dirty page rate:
	- $Data_{Iteration_i} = D . T_{i-1}$
The time for the previous iteration depends on how long it took to send the previous round's dirty pages over the network.

2. Stop-and-Copy (Downtime): The downtime is primarily the time required to transfer the remaining dirty pages in the final round, when the VM is stopped:
   $T_{downtime} = \frac{Remaining\space Dirty \space Pages}{B}$
	If after n iterations, there are $D_n$ dirty pages remaining, the downtime is:
	$T_{downtime} = \frac{D_n}{B}$

3. Total Migration Time: The total migration time is the sum of all iterations plus the downtime.
	![[Pasted image 20241202163843.png]]


### Post-Copy VM Migration

- Avoid multiple transfers of same page as happens in pre-copy
- Prepare target, stop VM, copy CPU context and minimum memory to target
- Start VM at target, pull memory from source via demand paging.
	- Memory access at target causes page fault, page fetched from source.
### VM Migration Time
![[Pasted image 20241203141938.png]]

# Containers

### Why don't we use virtual environments

They only solve part of the problem by isolating dependencies, but they don't solve system issues (like operating system differences.)
They may not work across different operating systems.

- VM's are heavy because they need to boot up an entire operating system.
- This makes them slow to start and requires a lot of system resources like CPU and memory.

- Containers virtualize the operating system and do not require dedicated pieces of hardware because they share the same kernel of the hosting system.
- Containers give the impression of a separate operating system however, since they're sharing the kernel, they are much lighter than a virtual machine.
- OS provides resource isolation and necessary support.

### Containers - Benefits

- Fast provisioning, fast performance, lightweight, extremely portable
- Fully packaged software with all dependencies included
- Containers instantiate in seconds
- Can run many containers in a laptop
- Multiple containers can be started from the same image.
- Orchestration/Scaling of multiple containers can be easily managed.
- Containers are best suited to deliver microservices.

### VM vs Containers

![[Pasted image 20241203150753.png]]

### Main Tricks Behind Containers

Isolation via Namespaces

- Containers leverage Linux namespaces to isolate system resources like processes (PID), file systems (mnt), networking (net), etc.
- Namespaces restrict what a container see.
- Each container gets its own isolated environment but runs on the same OS instance, allowing fast spin-up

Resource Management via Control Groups (cgroups):

- Control groups manage resources, (CPU, memory, network bandwidth) for each container.
- What and how much can a container use.
- Containers can efficiently share system resources without the need to allocate fixed amounts like in VM's.

## Image Registries

- Containers are built form images and can be saved as images
- Images are stored in registries
	- Local registry on the same host
	- Docker Hub Registry: Globally shared
	- Private registry
- Any component not found in the local registry is downloaded from specified location.
- Official Docker Registry: Images vetted by Docker
- Unofficial Registry: Images not vetted
- Each image has several tags, e.g., v2, latest

## Layers in Docker Image

- Each image has many read only layers
- Image is built layer by layer
- Layers in an image can be inspected by Docker commands
- Each layer has its own 256 bit hash
- E.g.
	- Ubuntu OS is installed then,
	- Python package is installed, then
	- A security patch to the Python is installed
- Whenever we create/run a docker container a Read-Write layer is created on top of the docker image.

# Kubernetes

Limitations of Docker
- Single host issue
- No auto healing
- No auto scaling
- Limited load balancing
- No enterprise level support

- Open-source orchestration platform that manages applications and services deployed and scaled up/down in containers
- Architecturally, Kubernetes is a set of services.
- Orchestration: Planning and coordinating to achieve a goal.
- Developed by Google, it was brought into the open-source domain in 2014.

## Cluster in Kubernetes

- The main concept used is the cluster: when Kubernetes is deployed, a cluster is created. The cluster is made of nodes, each node is a computing host, physical or virtual.
- There is a master node and one or more worker nodes. There must be a minimum of one master node and one worker node for a Kubernetes cluster to be operational.

## Pod & Kectlub

Pod
- A pod is the smallest deployable unit in Kubernetes. It can have one or more conatiners.
- One container can be the main application, and the other containers (sidecars) can provide complementary services like logging, monitoring or data synchronisation.
- Containers in a pod share the same network and storage resources
- Pods are temporary; they can be created, destroyed, and replaced by Kubernetes as needed.

Kutectl
- Kubectl is the command-line tool to interact with a Kubernetes cluster
- It allows you to create, manage, and monitor Kubernetes resources like Pods, Services and Deployments.
- Kubectl interacts with the Kubernetes API server to perform actions.

![[Pasted image 20241203151900.png]]

![[Pasted image 20241203151910.png]]

## YAML Manifestation

YAML file in Kubernetes is used for defining configurations for various Kubernetes objects. Kubernetes reads this file and uses it to create, update, or manage resources in the cluster.

Key Fields in the YAML File:
- apiVersion: this field specifies the version of the Kubernetes API you're using.
- kind: it tells kubernetes what kind of object or resource you are dealing with, such as a pod, service, deployument or replicaset.
	- pod: represents a single instance of an application (or group of containers running together).
	- Deployment: Manages ReplicaSets and provides mechanisms for updates, rollbacks, and scaling.
	- Service: A way to expose a set of pods as a network service.
- Metadata: This section contains data that helps identify the object. Typically, this includes:
	- Name: The name of the resource (e.g., my-pod or my-service).
	- Labels: Key-value pairs that help in grouping or selecting objects.
- Spec: This is the specification of the desired state of the object. The content under spec varies depending on the kind of object.
	- For example, in a pod configuration, the spec would define the containers, their images, environment variables, and ports.
	- In a deployment, the spec would define how many replicas to run and which pods to manage.

## MiniKube

- Minikube is a tool that lets you run a single-node Kubernetes cluster on your local machine.
- It's perfect for testing and learning Kubernetes on your own computer.
- Minikube runs lightweight VM's that mimic a Kubernetes cluster, allowing you to try out kubectl commands and deploy applications.

# Data Centers

- A data center is a facility that houses many servers and massive storage systems to store, process, and manage cast amounts of data.
- These centres are designed to handle many terabytes or petabytes of data.
- Used for
	- Data processing
	- Web sites
	- Business apps

Types of Data Centers
- Specialized data centers built for one or a few bit apps
- "Cloud" data centers

## Server Racks

- Servers are arranged into racks
	- Some people call the individual server in a rack a blade
	- Each slot also called a pizza box or 1U ('1 unit')
	
Rack Standards

- Width
	- The standard width of data center racks is 19 inches, which refers to the horizontal space between the mounting rails.
- Height (Measured in U):
	- Rack height is measured in rack units (U), where 1U = 1.75 inches.
	- Common rack heights include 42U, 45U, and 48U, allowing multiple pieces of equipment to be stacked vertically.
- Depth:
	- There is no strict standard for depth, but common depths are between 600mm to 1200mm.

### Networking - Recap

- Internet protocol stack (layers): application, transport, network, link, physical.
- Switch (data link layer): multi-port device that switches data packets from input ports to output ports (using MAC addresses).
- Routing: required for multi-hop networks. Routers determine the path from the sender to the destination according to an algorithm.

## Data Center: Network Models

- Historically, data center networks has been based on a three-tier architecture that facilitated the communication with correspondents outside the data center - "North-South communication".
- However, the distributed applications running in the data center ("East-West") require shorter latency and predictable communication that can be achieved by reducing the data center design to two tiers.
- With two tiers, the network becomes more resilient and scalable. The traffic complexity is lowered as communication patterns between endpoints become more predictable. Also, the number of components to manage and monitor is lower.

## Spine/Leaf Architecture

- Spine-leaf architecture consists of leaf switches and spine switches for efficient data centre networking.
- Leaf switches are positioned at the top of racks and connect directly to the servers.
- Spine switches are centrally located and connect to all the leaf switches, forming a backbone neetwork.
- Each leaf switch connects to multiple spine switches to ensure redundancy and fault tolerance.
- The architecture supports high volumes of east-west traffic between servers.
- There is a maximum of two hops for any east to west packet flow, so ultra-low latency comes as standard.

## ToR & EoR Design

Top-of-Rack (ToR) Design
- Placement: Switches are located at the top of each server rack.
- Advantages
	- Simplified cabling: Fewer, shorter cables needed within the rack.
	- Easier maintenance: Access to network equipment is within the rack.
	- Supports leaf-spine architecture, which optimizes east-west traffic (inter-server communication).
- Disadvantages:
	- More switches required overall (one for each rack).
	- Higher power consumption due to more switches.

End-of-Row (EoR) Design
- Placement: A single switch (or a pair for redundancy) at the end of each row of racks.
- Advantages:
	- Fewer switches need: Centralized switching for multiple racks.
	- Reduced management complexity with fewer devices to monitor.
- Disadvantages
	- Longer cabling between servers and swtiches.
	- More complex cabling layout (can lead to higher cable management costs).
	- Less optimal for modern data centers with high east-west traffic.

## Data Center Network Design Issue: Oversubscription

- Oversubscription is the ratio of all active incoming (input, ingress) bandwidth to maximum outgoing (output/ outgoing) bandwidth in a network. It shows how much the traffic is being shared or aggregated across the network.
	- Oversubscription Ration = $\frac{Max \space Incoming \space Bandwidth}{Max \space Outgoing \space Bandwidth}$
- Consider a setup where 10 servers are connected to a leaf-switch, each with a 10GbE connection. On the other hand, the leaf switch is connected to the next layer (the spine switches) via 2 uplink connectoins, each with 40 GbE capacity.
- The oversubscription ratio is calculated by dividing the total incoming traffic by the total outgoing capacity, which in this case is 100/80 = 1.25
- This means the incoming traffic slightly exceeds the outgoing capacity, but it's not usually an issue.

## Switch Oversubscription

- Switch oversubscription refers to the ratio of the maximum incoming traffic (from connected devices) to the switch's internal capacity to handle and forward that traffic.
Leaf Switch:
- A 48 port leaf switch, with each port supporting 10GbE, handles a total of 480 GbE of incoming traffic from servers.
Switch Capacity:
- The leaf switch's internal capacity can support a maximum of 240GbE of traffic at any time.
	- Oversubscription Ratio = $\frac{480 GbE \space (incoming)}{240 GbE \space (Switch \space capacity)} = 2$
This means the switch has a 2:1 oversubscription ratio, where it can only handle half of the incoming traffic load.

### Problem: Designing a Data Center Network with a Target Oversubscription Ratio

Data center network configuration:
- 10 racks
- 14 servers per rack.
- Each server has 3x 10 GbE fiber connections
Switches:
- Each leaf switch has multiple 10GbE ports and four 40 GbE uplink ports to the spine.
- Each switch has 40GbE ports only.
- One connection from each leaf switch to each spine switch.
Requirement:
- Achieve a target oversubscription ratio of 4:1 or lower
- Try different numbers of spine switches to find the best configuration.


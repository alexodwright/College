  

A distributed computing system:

- Multiple connected computing devices working together
- A collection of computers that usually appears to its users as a single coherent system.
- Consists of “nodes” (computer, phone, car, robot, …)
- A distributed application in computing is a software application that runs on multiple computers within a network simultaneously.

## Why Make a System Distributed?

Some systems are inherently distributed:

- Accessing a shared document stored on a cloud service from multiple devices.

For better reliability:

- Even if one node fails, the system as a whole keeps functioning.

For better performance:

- Get data from a nearby node rather than one halfway round the world.

To solve bigger problems:

- Huge amounts of data, can’t fit on one machine.

## Why Not Make a System Distributed?

The trouble with distributed systems:

- Communication may fail (and we might not even know it has failed)
- Processes may crash (and we might not know)

Fault tolerance:

- We want the system as a whole to continue working, even when some parts are faulty, this is hard.

Writing a program to run on a single computer is comparatively easy.

## Computing Paradigm Shift

![[image 16.png|image 16.png]]

## Distributed System Examples

Cluster computing systems

- LAN with a cluster of servers + storage

Grid computing systems:

- Cluster of machines connected over a WAN
- WAN-based data centres.
- Google, Amazon

Cloud Computing

## Cluster Computing

Cluster Computing involves a group of interconnected computers working together as a single system, often within a single data center.

The computers are generally connected through fast local area networks (LANs)

It can be sued as part of the underlying infrastructure in cloud computing environments, especially for high-performance tasks.

Usage example: Scientific Simulations.

## Grid Computing

Grid computing is a distributed architecture that combines computer resources from different locations to achieve a common goal.

It can also be utilized in cloud computing to allocate resources from multiple locations for large-scale computations.

Usage Example: Large-scale computations (e.g., SETI@home, CERN)

## Emerging Distributed Systems

Distributed Pervasive Systems

- “Smaller” nodes with networking capabilities
- Home networks
- Mobile computing: smart phones, cares
- Sensor networks

## Distributed Computing Model: Parallel Computing

The most common computing model is the farm model, where a central controller (like a “farmer”) distributes tasks or computations to a set of workers (PCs or nodes), ensuring the load is balanced across them.

Alternatively, the application can manage its own components, where individual parts of the job are run on different PCs.

The operation of the PCs is continuously monitored for failures. If a PC fails, it is automatically replaced by another available PC from a free pool of resources.

## Matrix Multiplication Problem (Distributed Computation)

![[image 1 13.png|image 1 13.png]]

## Parallel Computing: Expected Speedup

Consider an application with total workload W and execution time T when running on a single PC. A fraction of the workload, denoted by p, can be parallelized across multiple PCs, say n PCs, The new execution time when using n PCs is given by.

$T_{par} = (1-p)T + \frac{pT}{n}$﻿

Where (1-p)T represents the portion that cannot be parallelized

$\frac{pT}{n}$﻿ represents the portion that can be parallelized across n PCs.

The speedup, defined as the ration of the original execution time to the parallelized execution time, is calculated as:

$S = \frac{T}{T_{par}} = \frac{1}{(1-p)+\frac{p}{n}}$﻿

This is known as Amdahl’s Law.

It provides a limit or upper bound on the achievable speedup in a parallel computing system.

- No communication overhead
- Uniform Processing Power
- Ignores Memory Constraints.
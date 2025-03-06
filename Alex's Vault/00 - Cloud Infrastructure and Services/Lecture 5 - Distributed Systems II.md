## Scalability in Distributed Systems

Scalability of a system can be measured along the following dimensions:

- Size scalability: A system can be scalable regarding its size, meaning that we can easily add more users and resources.

==*** ***==

## Analysing Size Scalability

![[image 17.png|image 17.png]]

- Arrival Rate ($\lambda$﻿): The rate at which jobs or requests arrive in the system (requests per second).
- Service Rate ($\mu$﻿): The rate at which jobs are processed by servers.
- Utilization ($\rho_m$﻿) considering multiple servers:
    - $\rho_m = \frac{\lambda}{m.\mu}$﻿
    - Where m is the number of servers (or cloud instances)

### Value of $\rho$﻿

A utilization of 100% (i.e., $\rho$﻿ = 1) means the system is full utilized, but it leaves no room for handling bursts in traffic or unexpected demand spikes.

A too-low utilization (e.g., $\rho$﻿ < 0.5) means the system is underused, which can result in wasted resources and unnecessary costs.

For most practical systems, an ideal utilization falls in the range of 70% to 85%.

### What if the arrival rate is greater than the service rate?

- Growing Queue: Requests will start to queue indefinitely.
- High Latency: Users experience significant delays, as their requests take longer to be processed.
- Unstable system: Potential system failures due to overload or run into performance bottlenecks.

## Client-Server Architectures

In a client-server system within a distributed system, clients request services or resources from servers over a network.

Clients initiate communication, send requests, and handle user interfaces, while servers

==*** ***==

### Client-Server Architectures

Most common style: client-server architecture

- User-Interface level
- Processing level
- Data level

![[image 1 14.png|image 1 14.png]]

### Multitiered Approach

The simplest client-server architecture

==*** ***==
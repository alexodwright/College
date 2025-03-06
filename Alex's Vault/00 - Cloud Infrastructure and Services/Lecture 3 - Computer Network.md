## What is a network?

A system of “links” that interconnect “nodes” in order to move “information” between nodes is known as a network.

There are _many_ different types of networks:

- Internet
- Telephone network
- Cellular networks
- Optical networks
- Sensor networks

## Nodes and Links

Channels = Links

Peer Entities = Nodes

### Properties of Links (Channels)

- Bandwidth (capacity): “width” of the links
    - Number of bits sent (or received) per unit time (bits/sec or bps)
- Link Latency: “length” of the link
    - Propagation time for data to travel along the link (seconds)
    - Also known as propagation delay
    - Propagation delay = $\frac{Distance}{LightSpeed}$﻿

### Packet Delay

Sending a 100B packet from A to B?

@ 1Mbps, 1ms

The time to transmit one bit is $\frac{1}{10^6}$﻿s.

The time when that bit reaches B is $\frac{1}{10^6}$﻿s + $\frac{1}{10^3}$﻿s.

The time to transmit n bits is ($\frac{1}{10^6}$﻿s x n) + $\frac{1}{10^3}$﻿s.

We can say that:

**Packet Delay = Transmission Delay = Propagation Delay.**

**Packet Delay =** $\frac{PacketSize}{LinkCapacity}$﻿ **+ Link Latency**

## What about connecting multiple nodes?

Solution: A switched network - A network device (node) in between.

![[image 15.png|image 15.png]]

Nodes that share network link resources.

## Circuit Switching (Old Way)

Establishes a dedicated communication path.

Allocated channel remains reserved.

![[image 1 12.png|image 1 12.png]]

It benefits from high quality resource sharing.

## Packet Switching

No dedicated communication path

Data is broken down into small packets, each of which can take different routes.

- Data is sent as chunks of formatted bits (Packets)
- Packets consist of a header and payload
    - Payload is the data being carried
    - Header holds instructions to the network for how to handle the packet.
    - Headers may include
        - Destination address.
        - How this traffic should be handled?
        - Do I acknowledge this? Who signed for it?
        - Were the contents ok?

## Networks are complex, with many “pieces”.

- Hosts
- Routers
- Links of various media
- Applications
- Protocols
- Hardware/software

==Question is:== How do we organize the end-to-end communication?

## Layered Internet Protocol Stack

- Application: supporting network applications
    - HTTP, IMAP, SMTP, DNS
- Transport: end-end data transfer
    - TCP, UDP
- Network: routing of datagrams from source to destination
    - IP, routing protocols
- Link: data transfer between neighbouring network elements.
    - Ethernet, 802.11 (Wi-Fi)
- Physical
    - Bits on the “wire”

## Services, Layering and Encapsulation

![[image 2 11.png|image 2 11.png]]

## Network Devices

- Hubs
    - Hub is a physical layer device i.e. layer 1
    - Broadcast: All frames are sent out all physical ports.
- Switches
    - Switch is a data link layer device i.e. layer 2
    - Only send frames to selected physical port based on destination MAC address
- Routers
    
    - Router is a network layer device i.e. layer 3
    - Only send packet to selected physical port based on destination IP address
    
    ![[image 3 7.png|image 3 7.png]]
    

## Packet Loss in Communication Network

When accessing the internet, ethernet, LAN, or any other network data packets are sent and received.

If one of these packets fails to reach its intended destination, what’s known as “packet loss” occurs.

What causes packet loss?

- Network Congestion
- Issues with the network hardware.
- Loss in the communication channel (especially in wireless channel)

![[image 4 6.png|image 4 6.png]]
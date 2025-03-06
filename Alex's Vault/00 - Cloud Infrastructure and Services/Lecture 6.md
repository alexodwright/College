## Peer-to-Peer Architectures

In peer-to-peer (P2P) systems, interconnected nodes directly communicate and collaborate without centralized control.

- Removes distinction between a client and a server.

Each node can act as both a client and a server ,sharing resources and services with other nodes.

![[image 18.png|image 18.png]]

## Client/Server vs P2P

- Client requests data or functionality from server
    - Disadvantages
        - Single point of failure - if server fails, the entire service is unusable
        - Bandwidth bottlenecks at server
    - Advantages
        - Easy to control access to resources and functionality (including providing security)
        - Simple and efficient algorithms
        - No distinction between clients and servers
        - Individual peers can cooperate with each other.
    - Advantages
        - No longer depend on a single server (no single point of failure)
        - Addition of new users, leads to new server and clients.
    - Disadvantages:
        - Complex algorithms needed
        - Hard to control access and provide security.

## P2P System: Use-Cases

BitTorrent: File-sharing P2P network

Cryptocurrency network: Blockchain-based P2P network.

Amazon DynamoDB is used in Amazon’s internal systems that uses concepts from Chord and consistent hashing for distributed data storage and lookup.

## Resource Location in P2P Systems

Resource location is a fundamental problem of P2P systems.

- How do you locate a resource in a P2P network?
- (In a centralized network, you go direct to the server)

The problem

- Given a network of peers, each peer p has an address, and stores some resources, r, and each resource is identified by a key, k:
- If you have a key, k, for resource r, find the peer p that stores the resource r

## P2P Implementation Choices

Unstructured versus Structured

- Unstructured: Peers connect randomly, with no predefined structure, making search and data retrieval less efficient
- Structured: Peers and resources are organized in a specific topology.

Flat versus Hierarchical

- Flat: All nodes are equivalent (play same role)
- Hierarchical: some nodes have special functionality (only some nodes can search)

## Structured P2P System: Chord

Chord utilizes a Distributed Hash Table (DHT), which distributes both the hash values and the keys across different nodes to store and retrieve key-value pairs efficiently.

N nodes in network

- Aim to distribute files amongst the nodes, and locate the files.

Hashing is used to assign ID’s to nodes and resources (e.g. files)

- SHA-1 hash of node properties (e.g., IP address) produces 160-bit ID
- SHA-1 hash of file properties (e.g., name, type) produces 160-bit key, k

Visualise nodes as circle ordered by ID

Resource with key k is stored at node with ID = k

- If node with ID = k does not exist, resource is stored at node with next highest ID
- Consistent hashing

Node n joins network:

- Need to reassign keys from successor node.

Node n leaves the network:

- Need to reassign keys to successor node.

To insert data, insert(data)

- Node calculates hash of data (e.g. the file) to get k.
- Routing is used to find the node that is responsible for the key k (e.g., node k or >k).
- Data is stored on the node.

To search for data, search(k)

- Node calculates hash of the data to get k.
- Routing is used to find the node that stores k.
- Any access method (e.g. HTTP) is used to retrieve data from the node k.

## Chord: Example

The chord network can have a number of $2^n$﻿ nodes.

Nodes store key values from predecessor node to own node.

![[image 1 15.png|image 1 15.png]]
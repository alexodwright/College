Summer Exam - 80%
Lab Assessments - 20%

Short online quiz at the end of each lab session.

## Textbooks

- J. Kurose & K. Ross "Computer Networking - A Top Down Approach"
	- 8th is the international edition

# The Internet: A 'nuts and bolts' view

Billions of connected computing devices
- Hosts = end systems
- Running network apps at Internet's 'edge'

Packet Switches forward packets (chunks of data)
- Routers, switches

Communication Links
- Fiber, copper, radio, satellite
- Transmission rate: bandwidth

Networks
- Collection of devices, routers, links: made by an organization

An ISP is a generic term that refers to organizations that operate networks (Internet Service Provider) - e.g. Vodafone, Eir

Internet: A network of networks
- Interconnected ISPs

Protocols are everywhere
- Control sending, receiving of messages
- e.g., HTTP, streaming video, Skype, TCP, IP, WiFi, 4G, Ethernet

Internet Standards
- RFC: Request for comments
- IETF: Internet Engineering Task Force

## The Internet: A 'service' view

Infrastructure that provides services to applications:
- Web, streaming video, multimedia teleconferencing, email, games, e-commerce, social media, inter-connected appliances
Provides programming interfaces to distributed applications:
- 'Hooks' allowing sending/receiving apps to 'connect' to, use Internet transport service
- Provides service options, analogous to postal service

## Protocol

- All communication activity in the Internet is governed by protocols
- They are distributed algorithms

Protocols define format, order or messages sent and received among network entities, and actions taken on message transmission, receipt.

### A request-response protocol

Most network protocols are called request-response
- The client sends a message to a server requesting some information
- The server responds by sending back a message to the client

## Specifying Protocols

Protocols are specified as follows:
- The set of message types (e.g., request, response, reject, error)
- The format of each message
- The action to be taken when a message is received, including what response to send.

## Implementing Protocols

- Network protocols are usually implemented in software
- The software must faithfully implement the protocol specification
	- The choice of programming language and operating system does not matter
- The software must be installed at the client and server computers
	- As long as the specification was adhered to, independent implementations should work together

## Types of Protocols

- Each protocol is designed for a specific purpose
- The most crucial protocols allow messages to be routed to the right destination and reliably delivered
	- Their operation is largely invisible to end-users
	- Other protocols are more familiar, such as:
		- HTTP which allows web browsers to send requests to web servers
		- IMAP which is used to read email messages.

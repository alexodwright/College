
## Sample Paper Questions
``
![[Sample Questions.pdf]]

#### Notes:

- Bring a calculator
- Equations will not be given in the exam
- Nothing from the labs will be on it (i.e. Kubernetes, Dockers, Virtual Machines)

# Answers

## Introduction to Cloud Computing, Computer Systems and Computer Networks

1. Cloud computing provides access to various computing services such as servers, storage and software over the internet.
2. Multiplexing gains: multiple VM's can share system resources
   No/Low overhead maintenance: hardware/software maintained by the providers
   Flexibility: VM's can move to another machine if one fails.
   Pay per usage: No need to invest in servers.
3. If you run services on the cloud you may experience a delay or high latency to access servers via the internet. You also may incur a higher cost if heavily used.
4. A computer system is composed of three parts. The hardware, the operating system (the program that manages the system hardware), and application programs.
5. The function of the operating system is to manage and control the system hardware. The bootstrap program is the first program that runs when a computer is powered on or reboot/restarted. It's purpose is to load the operating system.
6. The idea of memory hierarchy is to have multiple levels of storage and ensure that most of the data needed by the CPU is kept in the fast(er) level(s).   ![[Memory-Hierarchy-Design-768.png]]
7. The capacity or bandwidth is the 'width' of the links and it is the number of bits sent/received per unit time and is measured in bits/sec or bps. The propagation delay is also known as the latency or 'length' of the links. It is the time for data to travel across the link and can be calculated by the distance across the link divided by the speed of light.
8. Circuit switching involves establishing a dedicated communication path with the allocated channel for data remaining reserved during the transfer.
	Packet Switching is an implementation of a switch network in which there is no dedicated communication path. The data is broken down into small packets, each of which can take separate routes. The packet contains two fields, the 'header' and the 'payload'. The payload is the actual data being sent and the header contains instructions for the network on how to handle the packet. It contains information such as signatures, destination address and if the contents are OK.
9. The layered internet protocol stack involves 5 layers:
	1. Application layer: Supports network applications and handles formatting, compression and encryption.
	2. Transport layer: end to end data transfer and handles segmentation, flow control and error control.
	3. Network layer: routing of datagrams from source to destination and handles routing and addressing.
	4. Link layer: data transfer between neighbouring network elements and handles channel sharing.
	5. Physical layer: bits 'on the wire' and handles bit/signal transmission.
10. Packet loss is when a packet fails to reach its intended destination and can be caused by a multitude of reasons:
	1. Network congestion
	2. Network hardware issues
	3. Loss in communication (especially wireless) channel.

## Distributed Computer Systems

1. Merits:
	1. Better reliability: even if one node fails, the system keeps functioning as a whole.
	2. Better performance: get the data you need from a nearby node rather than a node halfway around the world.
	3. Solve bigger problems: Huge amounts of data can't fit on one machine.
	Demerits:
	1. Communication may fail without us knowing, the same can be said for processes.
	2. Fault tolerance: it is hard to have a system work with some faulty parts.
	3. Writing a program to work on a single computer is comparatively easy.
2. Cluster computing involves a group of interconnected computers working together as a single system, often with a single data center. They are generally connected through fast LANs. They can be used as part of the underlying infrastructure for cloud computing environments, especially for high performance tasks. e.g. scientific simulations.
   Grid computing is a distributed architecture that combines computer resources from different locations to achieve a common goal. They can be utilised in cloud computing to allocate resources from multiple locations for large-scale computations.
3. The most common computing model is the farm model, where a central controller distributes tasks or computations to a set of workers ensuring the load is evenly balanced across them. Alternatively the program can manage its own components, where different parts of the process run on different PCs. The operation of the PC's is constantly monitored for failures and if one is detected it is automatically replaced by another available PC selected from a free pool of resources.
4. Amdahl's law provides a limit or upper bound on the achievable speedup in a parallel computing system. It is the ratio of the original execution time to the parallelized execution time. it is given by $S = \frac{1}{(1-p)+\frac{p}{n}}$ where is the speedup factor, p is the portion that can be parallelized and n is the number of PCs.
5. ![[486c1333-ff16-44c2-b6bd-9a30594bacef.png]]![[ecb6e602-b146-47f1-bc00-2c978c6babc3.png]]
6. The law recognises that most programs have parts that cannot be parallelized and these become the bottleneck in execution. No matter how many processors are added, the parts that cannot be parallelized will always take the same amount of time, limiting the overall speedup. Additionally, as the number of processors increases the law shows that the speedup gets progressively smaller as the parallelizable portion is divided among more processors but the sequential portion remains constant. Even with infinite processors the speedup is limited by the sequential portion (1-p).
7. Design goals for a distributed system include:
	1. Resource sharing: make it easy for applications to share remote resources.
	2. Transparency: hide the fact that its processes and resources are distributed across multiple computers, possibly separated over large distances.
	3. Openness: A system that offers components that can be easily used by or integrated into other systems. I.e. one that is:
		1. Interoperable: common standard
		2. Portable: Can be executed on DS A and DS B without changes.
		3. Extensible: Can add or remove components without affecting the static components.
	4. Dependable: required to be available, reliable, fault tolerant and maintainable.
	5. Secure: data confidential, authentication and authorization, secure communication, intrusion detection.
	6. Scalable: size, geographical and administratively.
8. Transparency means making distribution of processes and applications invisible to end users and applications.
	1. Access: hide differences in data representation and how an object is accessed.
	2. Location: hide where an object is located
	3. Relocation: hide than an object may be moved while in use.
	4. Migration: hide than an object may move to another location.
	5. Replication: Hide that an object is replicated.
	6. Concurrency: Hide that an object may be shared by many independent users.
	7. Failure: hide the failure and recovery of an object.
9.  In a client-server architecture DS, clients request services or resources from servers over a network. Clients initiate communication, send requests and handle UI, while servers listen for requests, perform tasks and manage resources.
   ![[Pasted image 20241212133205.png]]
10. ![[Pasted image 20241212133330.png]]
11. In peer to peer systems, interconnected nodes directly communicate and elaborate without centralized control. It removes the distinction between a client and a server as each node can act both as a client and a server, sharing resources and services with other nodes.
    Advantages: No single point of failure by depending on a single server. Addition of new users leads to new servers and clients.
    Disadvantages: Complex algorithms, hard to control access and provide security.
12. Unstructured: Peers connecting randomly with no predefined structure making search and data retrieval less efficient.
    Structured: Peers and resources are organised in a specific topology.
    Flat: All nodes play the same role (are equivalent).
    Hierarchical: Some nodes have special functionality.
13. Chord is a structured P2P system that utilizes a distributed hash table which distributes both the hash values and the keys across different nodes to store and retrieval key-value pairs efficiently.
    With n nodes in a network it aims to distribute files amongst the nodes and locate the files.
    Hashing assigns ID's to nodes and resources.
    Resources with key k is stored at node with ID = k or if that doesn't exist, resource is stored at node with next highest ID.
14. Insertion: node calculates hash of data to get k. Routing is used to find the node that's responsible for key k (e.g. node k or > k). Data is stored on the node.
    Searching: Node calculates the hash of data to get k. Routing is used to find the node that stores k. Any access method (e.g. HTTP) is used to retrieve data from node k.
15. A finger table contains up to m entries considering the size of the keyspace is $2^m$. The $i^{th}$ entry in the finger table of a node with ID n points to the first node that succeeds $n + 2^{i-1}$ in the identifier space. Worst case max hops to locate key is $log_2N$ where N = total nodes in a system.

## Virtualisation

1. Virtualisation is the process of making a virtual version of something, such as a computer, server or storage device, by using software to divide the physical resources into multiple virtual environments.
   Hardware: Virtualises the physical hardware into multiple VM's.
   OS: Virtualises the OS kernel to allow multiple isolated user-space instances (containers) to run.
   Network: Abstracts physical network resources into virtual networks.
2. A hypervisor is a software layer that enables virtualisation, allowing multiple VM's to run on a single physical machine. It acts as an intermediary between the hardware resources and the VM's. It manages the computing resources.
	1. Type 1: Runs on bare metal, acts as a lightweight OS and runs on hardware, optimal for large production environments.
	2. Type 2: Runs on a host OS as an additional software layer, guest OS runs inside the hypervisor, latency is higher.
3. Types of Virtualisation:
	1. Full Virtualisation: hypervisor provides a virtual hardware environment to the guest OS making it believe its running on real physical hardware. The hypervisor handles all the hardware calls and translates them onto the physical machine.
	2. Para-Virtualisation: The guest OS is modified to be aware that it's running on a hypervisor. Instead of making hardware calls as if it were running on bare metal, the guest OS directly interacts with the hypervisor using special APIs.
	3. Emulation: The hypervisor emulates different hardware than what is physically present, allowing an OS designed for a different hardware architecture to run. The hardware and architecture don't need to match between the host and the guest.
4. Benefits of virtualisation:
	1. Resource sharing: Increased use of resources by reducing the idle time which reduces hardware costs and saves power.
	2. Flexibility and Scaling: Multiple software running on the same computing platform.
	3. Isolation: protection from other tenants.
	4. Simple management: easy distribution, deployment, testing and automation.
	Uses:
	1. Data centers: server consolidation by packing multiple servers onto a smaller number of physical servers, saving costs.
	2. Cloud computing: Rent virtual servers. Cloud provider handles all physical machines and mapping of VM to physical hosts. User gains root access to the virtual server.
	3. Desk computing.
5. Memory virtualisation allows a computer to run multiple OSs or VM's on the same physical memory. Each VM thinks it has its own memory but its actually the physical memory being shared. Hypervisor maps the virtual memory to the real physical memory.
	I/O virtualisation is when the hypervisor provides virtual I/O devices to VMs. The VM thinks its using real hardware but the hypervisor is translating those requests to the actual physical hardware on the host machine. It does this by intercepting VM requests to the virtual devices and returning the result.
6. VM migration is when a VM is moved from a machine A to a machine B. It is needed to distribute VM load efficiently across servers in a cloud, and in case of system maintenance.
7. Types of VM migration:
	1. Pure stop-and-copy: VM is stopped, all info is sent to the new location, then the VM restarts there.
	2. Pre-copy: most of the VM info is sent to the new location while it's still running, then there's a short stop and copy phase to send any remaining data.
	3. Post-copy: VM is stopped, only essential info to get it running is sent to the new location. The rest of the data is brought over as needed while the VM runs in the new location.
	4. Hybrid: Combines both pre and post copy. Some info is sent while VM is running then stops to send more data, then finally, any remaining data is pulled as needed.
8. Steps of Pre-Copy VM migration:
	1. Enable dirty page tracking
	2. Copy all memory pages to destination
	3. Copy memory pages dirtied during the previous copy agin
	4. Repeat step 3 until specified number of iterations is reached or num of dirty pages falls below a certain threshold.
	5. Stop VM.
	6. Copy rest of memory pages
	7. Resume VM at destination
9. Steps of Post-copy VM migration:
	1. Prepare target
	2. Stop VM
	3. Copy CPU context and minimum memory to the target
	4. Start VM at the target
	5. Pull memory from source via demand paging
		1. Memory access at target causes page fault, page fetched from source.
10. Containers virtualise the OS and do not require dedicated pieces of hardware because they share the same kernel of the hosting system. They give the impression of a separate OS, but since they're sharing the kernel, they're much lighter than a VM.
11. Motivation:
	1. System that can set up required dependencies
	2. Is light
	3. Is isolated
	4. Uses less resources
	5. Starts up quickly
	VM's are heavy because they need to boot up an entire operating system.
	This makes them slow to start and requires a lot of system resources like CPU and memory.
	Virtual environments only solve isolating dependencies, but not system-level issues like OS differences. They also may not work across different OSs.
12. Benefits:
	1. Fast provisioning, fast performance, lightweight and extremely portable.
	2. Fully packaged software with all dependencies included.
	3. Instantiate in seconds
	4. Can run many containers in a laptop
	5. Multiple containers can be started from the same image
	6. Orchestration and scaling of multiple containers can be easily managed
	7. Containers are best suited to deliver microservices.
13. Namespaces:
	1. Containers leverage Linux namespaces to isolate system resources like processes, file systems and networking
	2. They restrict what a container can see
	3. Each container gets it's own isolated environment but runs on the same OS instance, allowing a faster spin-up.
	Control Groups:
	1. Manage resources for each container
	2. What and how much a container can use
	3. Can efficiently share system resources without the need to allocate fixed amounts like in VMs.
14. A docker image is a template to create a running docker container. Docker uses the information available in the image to create a container. Image registries are where images are stored. Can be either locally, on the docker hub registry or a private registry.
15. ![[Pasted image 20241212142935.png]]
16. Each image has many read only layers. The image is built layer by layer and each layer is an image that can be inspected by docker commands. Each layer has its own 256-bit hash. This is adopted because layers can be shared among many images.
17. Volumes:
	1. They are the preferred mechanism for persisting data generated by and used by docker containers as dockers are disposable by design.
	Compose:
	1. Is a tool that helps define and manage multi-container docker applications. It lets you use a single YAML file to configure all the containers, networks and volumes.
18. Limitations:
	1. Single host issue
	2. No auto healing
	3. No auto scaling
	4. Limited load balancing
	5. No enterprise level support.
19. Kubernetes is an open source orchestration platform that manages applications and services deployed and scaled up/down in containers.
20. A pod is the smallest deployable unit in Kubernetes. It can have one or more containers. One container can be the main application, and the other containers can provide services like sync, monitoring and logging. Containers in a pod share the same resources. They can be replaced as needed.
    Kubectl is the CLI tool to interact with a Kubernetes cluster. It allows you to create, manage, and monitor Kubernetes resources. It interacts with the Kubernetes API server to perform actions.
21. ![[Pasted image 20241212150257.png]]
22. A YAML manifest is used for defining configurations for various Kubernetes objects. Kubernetes reads this file and uses it to create, update or manage resources in the cluster.
	Fields:
	1. apiVersion
	2. Kind: Type of resource; pod, deployment, service
	3. metadata: name, labels
	4. spec
23. A replicaset is a Kubernetes object used to maintain a stable set of replicated pods running within a cluster at any tiven time.

## Data Centers & Sustainable Computing

1. A data center is a facility that houses many servers and massive storage systems to store, process, and manage vast amounts of data. They are designed to handle many terabytes or petabytes of data. They are used for data processing, websites and business applications.
2. Rack standards: arranged into racks
	1. Width: 19 inches
	2. Height: measured in U where 1U = 1.75 inches. Common heights include 42, 45, and 48U.
	3. Depth: No strict standard but depths between 600mm to 1200mm are common.
3. Spine/Leaf architecture:
	1. Consists of leaf switches and spine switches for efficient data center networking.
	2. Leaf switches are positioned at the top of racks and connect directly to the servers.
	3. Spine switches are centrally located and connect to all leaf switches, forming a backbone network.
	4. Each leaf switch connects to multiple spine switches to ensure redundancy and fault tolerance.
	5. The architecture supports high volumes of east-west traffic between servers.
	6. Max of two hops for any east-west packet flow, so ultra-low latency comes as standard.
4. TOR:
	1. Switches located at top of each server rack.
	2. Easier maintenance: access to network equipment is within the rack.
	3. Supports leaf-spine architecture optimising east-west traffic

	1. More switches required overall
	2. Higher power consumption due to more switches.
	EOR:
	1. A single switch (or pair for redundancy) at end of each row of racks.
	2. Fewer switches needed. Centralized switching for multiple racks.
	3. Reduced management complexity with fewer devices to monitor.
	Disadvantages:
	1. Longer cabling between server and switches.
	2. More complex cabling layout (higher cabling management costs).
	3. Less optimal for modern data centers with high east-west traffic.
5. Oversubscription is the ratio of all active incoming bandwidth to maximum outgoing bandwidth in a network. It shows how much traffic is being shared or aggregated across the network.
   Switch oversubscription refers to the ratio of the maximum incoming traffic (from connected devices) to the switch's internal capacity to handle and forward that traffic.
6. Mice: Short messages (query, coordination) -> Low Latency
	Elephants: Large flows (data update, backup) -> High Throughput
7. Head of line blocking is queue build up. It can be mitigated with priority flow control and congestion control algorithms. Data centre TCP are specifically designed for data center environments to reduce congestion. If queue build up persists, mitigation strategies may not work and a network redesign will be required.
8. PUE is a metric that describes how efficiently a data center uses energy. It is the ratio of total facility energy to the energy used by the IT department.
9. Sustainable computing is serving computing's demand in a sustainable manner which means in the least carbon intensive way.
10. Embodied: Carbon emissions from manufacturing/building.
	Operational: Emissions from energy use for compute and cooling.
11. The carbon footprint of a data centre refers to the total amount of greenhouse gases, primarily C02, that are emitted as a result of the energy consumption and operations of the data center. It is measured in C02 equivalents (C02e).
    Carbon intensity (kg C02e/kWh): The amount of CO2 emissions produced per kilowatt-hour of energy consumed, which depends on the energy source (renewables, coal, gas, etc.).

## Cloud Computing Services

1. Elasticity and Scalability and Differences:
	1. Elasticity: the ability to automatically adjust cloud resources in real-time to match fluctuating demand.
	2. Scalability: the ability to handle increasing workloads over time by adding more resources or upgrading existing ones.
	3. Differences: Elasticity handles short-term, dynamic changes in demand, while scalability focuses on long-term gradual growth. Scalability doesn't typically account for reducing resources when demand decreases. That's more aligned with elasticity which refers to dynamically adjusting resources both up and down in response to short term fluctuations.
2. Services models:
	1. IaaS: Model that provides VM's over the internet, allowing businesses to rent IT infrastructure rather than owning the physical hardware.
		1. On demand: provision on the fly, pay by the minute, keep until terminated
		2. Reserved: long term commitment; 1yr, 3yr. Discount over on-demand pricing.
		3. Spot: excess capacity sold by cloud platform at high discount, can be revoked with a warning time, take back server if regular customers need it, cheap method to run large computations in off peak periods.
	2. PaaS: Model that provides a platform allowing devs to build, deploy and manage applications without dealing with the underlying infrastructure.
		1. App devs provide code
		2. Platform provisions resources and can scale the application
		3. Users to not need to provision or manage server resources.
	3. SaaS: Model that delivers software applications over the internet as a subscription basis, eliminating the need for installation and maintenance.
		1. Features include web based access, automatic updates, multi-tenancy, subscription pricing.
3. Serverless computing means that the user is neither responsible for handling nor for managing the servers or runtime software. The cloud provider runs the server and manages the allocation of computing resources making PaaS more accessible.
4. Cloud deployment models:
	1. Public: owned and operated by third-party providers
	2. Private: exclusively used by a single org
		1. Use cloud computing concepts in a private data center
		2. Private VM management and deployment
		3. Provides same convenience as public cloud
		4. May have a higher cost.
	3. Hybrid: Combines public and private clouds, allowing data and applications to move between them.
5. SLA: A formal contract between a service provider and a service consumer that outlines the expected level of service, detailing specific metrics, responsibilities and expectations. They contain SLO's (Service Level Objectives).
	1. Service Description: overview of the services
	2. Performance metrics: Criteria used to measure service quality.
	3. Responsibilities: Obligations of both provider and customer
	4. Penalties: Consequences or compensation for not meeting agreed metrics.
	They are specific measurable goals that define the desired level of service performance within a SLA. They serve as benchmarks that orgs use to assess whether they are meeting their service commitments.
6. Common performance metrics:
	1. Response time
	2. Availability
	3. Durability
	4. Elasticity
	5. Customer service response times
	6. Service-level violation rate
	7. Resolution time.
7. Monoliths: A software design approach where the entire application is built as a single, unified unit.
	Microservice: A software design approach where the application is built as a collection of small, independent units, each responsible for a specific service/function.
8. Issues with monolithic software design approach:
	1. Scaling
	2. Releases, troubleshooting.
9. Definitions:
	1. RPC (Remote Procedure Calls): Make distributed computing look like centralized computing. Allow remote services to be called as procedures. Transparency with regard to location, implementation and language.
	2. Client stub: Prepares and sends requests from the client to the server.
	3. Server stub: Receives the request, unpacks it, processes it on the server side, and sends back the response.
10. Steps in an RPC:
	1. Client function call: calls remote function via client stub which acts as a local proxy.
	2. Marshalling/Serialisation: the client stub marshals (prepares) the function arguments by serializing them into a transmittable format like JSON, XML
	3. Network transmission: Serialized data is sent over the network to the server.
	4. Unmarshalling/Deserialisation: The server unpacks the data by deserializing it back into the original arguments using the format schema.
	5. Server function execution: server executes the requested function with the unpacked arguments.
	6. Response serialisation: Function response is serialised by the server stub and sent back to the client.
	7. Client deserialisation and return: Client stub deserializes the response, and the result is returned to the client app as if it were a local call.
11. Issues with microservice software design approach:
	1. Communication: different language between os and hardware.
	2. Hotspot spreading
	3. Cascading failure
	4. Retry storm
	5. Integration: defining service boundaries can be hard
	6. Can have significant communication overheads
	7. Complexity

## Fault Tolerance

1. Requirements for a dependable computing system:
	1. Availability: available for use at any given time
	2. Reliability: Run continuously without failure
	3. Safety: temporary failures should not result in catastrophic event
	4. Maintainability: A failed system should be easy to repair.
2. Types of fault:
	1. Transient faults: temporary faults that occur once and disappear, often caused by brief environmental disturbances.
	2. Intermittent Faults: Faults that appear sporadically and unpredictably, often due to unstable components or connections.
	3. Permanent faults: persistent faults that continue until the faulty component is repaired or replaced, typically due to hardware failure.
3. Failure models:
	1. Crash failure: a server halts but is working correctly until it halts.
	2. Omission failure: A server fails to respond to incoming requests.
	3. Timing failure: A server's response lies outside the specified time interval.
	4. Response failure: The server's response is incorrect
	5. Arbitrary failure: A server may produce arbitrary responses at arbitrary times.
4. ![[Pasted image 20241212162925.png]]
5. A Byzantine fault refers to a situation in a distributed computing system where a component fails and can provide incorrect or inconsistent information to other components, making it challenging to reach a consensus or agreement among the remaining components.
6. Lamport's recursive algorithm is a method for defining recursive functions in formal specifications. It addresses the challenge of defining a function's domain when that definition may be extremely complicated or circular.
7. With m faulty processes/nodes, agreement is possible only if $2^m + 1$ processes/nodes function correctly out of $3^m+1$ total processes/nodes.
8. The CAP theorem states that in a distributed system it is impossible to simultaneously achieve consistency, availability and partition tolerance. Systems can guarantee at most two of these three properties at any time.
## Big Data

1. Big data technology is a set of specialized tools and frameworks for storing, managing and analyzing datasets that exceed single-machine capacity. It enables efficient retrieval of individual data pieces within large datasets and it provides compatibility across diverse technologies, ensuring seamless integration.
2. Three V's in big data:
	1. Volume: The scale or amount of data generated, stored and processed
	2. Variety: The diversity of data types, sources and formats. Text, images, video, geolocation data, logs.
	3. Velocity: The speed at which data is generated, collected and analyzed.
3. Parallel processings in big data:
	1. Batch: Collects and processes data in large 'batches' at scheduled intervals. Suitable for non time-sensitive tasks. e.g. Apache Hadoop, Apache Spark.
	2. Stream: Processes data in real-time as it arrives, without delay. Ideal for tasks that require immediate responses. e.g. Apache Kafka, Apache Flink.
	3. Parallel: Divides large tasks into smaller parts, processed simultaneously across multiple machines or processors. It increases speed and efficiency of data processing. E.g. Apache Spark, Apache Hadoop.
4. Data storage and access approaches:
	1. Traditional DB: Import data first. Extract, transform, load.
	2. Data lake: Read directly from file system.
5. Storage types:
	1. Block: Divides data into fixed-size blocks, each with a unique ID. Allows direct access and modification of individual blocks. Limited scalability and more complex to distribute. Low latency ideal for fast access.
	2. Object: Stores data as objects in flat address space. Each object contains data, metadata and a unique ID. It treats each object as a complete unit. Highly scalable, can easily handle petabytes. Designed for distributed storage access across multiple nodes or regions. Higher latency but potentially higher throughput.
6. High-Level steps to set up an HDFS Cluster:
	1. Procure Hardware: Set up servers with sufficient hardware.
	2. Install OS: Install linux based OS with SSH enabled
	3. Install hadoop
	4. Configure Nodes/servers: configure hadoop files in the servers
	5. Start HDFS
7. ![[Pasted image 20241212170954.png]]
8. ![[Pasted image 20241212170920.png]]
9. ![[Pasted image 20241212170759.png]]
10. Process to read file from HDFS system:
	1. Ask for file
	2. Get block locations, multiple datanodes for each block, sorted by distance.
	3. Read input stream
11. Process to write file to HDFS system:
	1. Create
	2. ID and Datanodes for first block
	3. Organise pipeline
	4. Sends and acknowledges data
	5. Repeat steps 2 - 5 for nth block.
	6. Close/release block.
	7. Check for minimal replication
	8. Acknowledge
	9. Replicates further asynchronously to target replication.
12. S3 is not a filesystem, but an object storage service with filesystem like characteristics. Differences include:
	1. S3 stores data as objects.
	2. Any modification of files requires rewriting entire object
	3. Unlimited storage
	4. Unique access method
	5. Scalable and durable

## Edge Computing and Computing Applications

1. Delay issue is determined by four factors:
	1. Local processing delays at the two endpoints
	2. Queueing delays
	3. Transmission delay due to bit rate
	4. Propagation delay due to physical distances.
2. Edge computing refers to storing and processing data closer to where users and devices reside, reducing latency and bandwidth use.
3. Internet of Things (IoT) refers to a network of interconnected physical devices that can collect, exchange and act on data using embedded sensors, software and network connectivity.
4. Offloading is the process of moving tasks from a mobile device to an edge server to reduce resource use on the device and improve performance.
	1. Vertical offloading: offloads tasks to a higher-level, more powerful resource. e.g. mobile device records voice input but offloads recognition to edge server with specialised algorithms.
	2. Horizontal offloading: offloads tasks to multiple nearby devices or edge servers that are on the same 'layer' as the original device. e.g. smart traffic edge node processes traffic data at busy intersection offloads parts, like video feed analysis, to a neighbouring node with spare computational capacity.
5. Mobile Edge Computing is specifically focused on edge computing within mobile networks, and future cellular technologies. It places computing resources close to mobile users, typically at or near the base stations in the cellular network.
6. A cloudlet is a small data center that provides cloud-like services closer to users. It can be viewed as a data center in a box whose goal is to bring the cloud closer.
7. Web caching involves storing frequently accessed web content in servers that are geographically close to end users.
	1. Benefits include reduced latency, decreased bandwidth demand, and a better user experience.
8. Push vs Pull:
	1. Push: tracks all proxies that have requested objects. If a web page is modified, notify each proxy. Notification types include indicating an object has changed (invalidate) or sending a new version of an object (update). Send updates for more frequent objects, invalidate for rest.
		Advantages include: minimal stale data and that the proxies can be passive.
		Disadvantages include: needing to maintain state at the server, needing mechanisms beyond HTTP and that the state may need to be maintained indefinitely.
	2. Pull: proxy is entirely responsible for maintaining consistency. It periodically polls the server to see if an object has changed. One approach to when a proxy should poll is time-to-live values.
		Advantages: implementation using HTTP, minimal responsibility of server.
		Disadvantages: weaker consistency guarantees (objects can change between two polls so proxy will contain stale data until next poll). Strong consistency only if poll before every HTTP response which is more complex.
9. Building, Transportation and Agriculture with Cloud computing:
	1. Building:
		1. Sense monitory energy, temp, occupancy
		2. Analyze data using computational tools
		3. Control lights, HVAC, doors to reduce energy usage.
	2. Transportation:
		1. Sense: traffic systems, vehicle sensors
		2. Analyze: optimize routes, predict maintenance, predict congestion.
		3. Control: Remote control traffic signals, public transport systems and fleet management.
	3. Agriculture:
		1. Sense: Soil moisture, temp, crop health and weather
		2. Analyze: Crop health, optimal planting, harvesting times, crop yields, weather impacts
		3. Control: Irrigation systems, automated farm equipment, resource distribution
10. Cloud computing in smart cities:
	1. Roads condition and traffic management
	2. Environment sensing and public information
	3. Utility service management and planning
	4. Public order
	5. Leisure and entertainment.
11. Crowd sensing is the capability of mobile devices belonging to a crowd to sense the surroundings and use the data towards a specific goal. e.g. locating events, or road works.
	1. Participatory sensing: requires active involvement. e.g. in city traffic monitoring users actively report accidents or road conditions
	2. Opportunistic: Collects data automatically without requiring active input. Fitness app might use Gps or accelerometer to track movement patterns and contribute this data to study trends.
12. Requirements and challenges for crowd sensing:
	1. Requirements:
		1. Data must be filtered to reduce unnecessary communication:
		2. Users and data must be trusted
		3. Privacy of user must be ensured
		4. Minimize network traffic
		5. Efficient long/short term data storage in cloud depending on app requirement.
	2. Challenges:
		1. Battery lifetime and computation capacity is limited in mobile devices.
		2. Trustworthiness: Smart city apps depend on user involvement, and user trust levels
		3. Data origin: tracking origin of data is useful when data errors occur or when data is analyzed. Tracing origin without affecting privacy is challenging.
		4. Data storage: data is usually offloaded to cloud which is costly, timely and bandwidth intensive.
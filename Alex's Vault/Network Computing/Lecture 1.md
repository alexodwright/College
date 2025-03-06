## Network Edge

- Hosts:
	- Clients and servers
- Servers often in data centres

- Access networks, physical media:
	- Wired, wireless communication links
- Network core:
	- Interconnected routers
	- Network of networks

## Nature of Signals & Encoding Bits

- Messages are encoded as a series of bits (1s and 0s)
- Physical media propagate signals from the transmitter to the receiver.
- Signal changes are used to communicate bit values
	- Physical media made of copper convey bits as voltage changes
	- Those made of optical fibre use pulses of light.

### Concept of Data Rate

Data rate is the amount of data that can be transmitted per time unit over a link.
- Example: 10 mega bits per second (mb/s or Mbps) or 100 Kilo bits per second (Kb/s).

- Notation:
	- Distinguish between bits (b) and bytes (B).
	- One byte = 8 bits; bytes sometimes called octets
	- Kb/s = $10^3$ bits per second; Mb/s $10^6$ bits per second
	- Also okay to use bps instead of the more scientifically correct b/s
- The term bandwidth (measured in Hertz) refers, more formally, to the amount of frequency spectrum available on an communication link, which is related to data rate.
- But bandwidth is commonly used when referring to data rate in bits/second (also sometimes simply speed).

## Host: Send packets of data

Host sending function:

- Takes application message (series of bits).
- Breaks into smaller chunks, known as packets, of length L bits.
- Transmits packet into access network at transmission rate R.
	- Link transmission rate, aka link capacity, data rate, link bandwidth.

Packet transmission delay = time needed to transmit L-bit packet into link = L/R

## Dial-up modem

- First technology for residential Internet access
	- Used existing telephone lines and switches
	- Home is connected to central office of telephone network
- Data conveyed using sounds
	- Up to 50-60 Kb/s
- Cannot use Internet and phone at same time: not 'always on'.
![[Pasted image 20250120122019.png]]

## Access Networks: Digital Subscriber Line (DSL)

- Use existing telephone line to central office DSLALM
	- Data over DSL phone line goes to internet.
	- Voice over DSL phone line goes to telephone network
	- 24-52 Mbps dedicated downstream transmission rate
	- 3.5-16 Mbps dedicated upstream transmission rate.

ADSL - Asymmetric Digital Subscriber Line:
- Asymmetric: download rate is greater than the upload rate

![[Pasted image 20250120122143.png]]

### Fibre to the Home

- Optical links from central office to the home
- Extremely high capacity and scalable technology.
	- Much higher Internet rates (currently multiple Gb/s)
	- Fibre can also carry television and phone services.
- In Ireland, the National Broadband Plan is rolling out fibre to homes across the country.
	- Focused on rural areas which are costly to reach with fibre cables.
	- Fibre cables carried either in underground ducts or along existing roadside poles.

![[Pasted image 20250120122318.png]]

### Home Networks

![[Pasted image 20250120122334.png]]

Modem: Modulator - Demodulator

Dark fibre: Fibre implanted into the ground, but not being used yet.

## Wireless Access Networks

Shared wireless access network connects the end system to the router
- Via base station aka 'access point'.

- Wireless Local Area Networks (WLANs)
	- Typically within or around building (~30m)
	- 802.11b/g/n (WiFi): 11, 54, 450 Mbs Transmission rate.
- Wide-area Cellular Access Networks
	- Provided by mobile, cellular network operator (10's km).
	- 4G 150 MB/s
	- 5G 10 Gb/s
### Enterprise Networks

- Companies, universities, etc.
- Mix of wired, wireless link technologies, connecting a mix of switches and routers.
	- Ethernet: Wired access at 100Mbps, 1Gbps, 10Gbps
	- WiFi: Wireless access points at 11, 54, 450 Mbps and most recently over 1Gbps (WiFi 6).

![[Pasted image 20250120124515.png]]

## Links: Physical Media

- Bit: Propagates between transmitter/ receiver pairs.
- Physical link: What lies between transmitter & receiver
- Guided media: Signals propagate in solid media: copper, flux, coax
- Unguided media: Signals propagate freely, e.g., radio

Twisted Pair (TP)
- Two insulated copper wires.
	- Category 5: 100 Mbps, 1Gbps Ethernet
	- Category 6: 10Gbps Ethernet

Coaxial cable:
- Two concentric copper conductors
- Bidirectional
- Broadband
	- Multiple frequency channels on cable
	- 100's Mbps per channel

Fibre Optic cable:
- Glass fibre carrying light pulses, each pulse a bit
- High-speed operation:
	- High-speed point-to-point transmission (10's-100's Gbps)
- Low error rate:
	- Repeaters spaced far apart
	- Immune to electromagnetic noise

Wireless Radio
- Signal carried in electromagnetic spectrum
- No physical 'wire'
- Broadcast and 'half-duplex' (sender to receiver)
- Propagation environment effects:
	- Reflection
	- Obstruction by objects
	- Interference

Radio Link types:
- Terrestrial Microwave: up to 45 Mbps channels
- Wireless LAN (WiFi): up to 100's Mbps
- Wide-area (e.g. cellular): 4G cellular: ~10's Mbps
- Satellite:
	- Up to 45 Mbps per channel
	- 270 msec end-end delay
	- Geosynchronous versus low-earth-orbit.
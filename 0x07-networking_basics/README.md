# NETWORKING BASICS 0

In this project, I learned about basic networking concepts such as OSI model, the Internet, types of networks, IP and MAC addresses just to name a few.

## OSI Model
OSI (Open Systems Interconnection) is an abstract model to describe layered communication and computer network design. The idea is to segregate the different parts of what make communication possible.

It is organized from the lowest level to the highest level:

    1. The lowest level: layer 1 which is for transmission on physical layers with electrical impulse, light or radio signal
    2. The highest level: layer 7 which is for application specific communication like SNMP for emails, HTTP for your web browser, etc

Note that the OSI model is a concept, it’s not even tangible. The OSI model doesn’t perform any functions in the networking process. It is a conceptual framework so we can better understand complex interactions that are happening. Most of the functionality in the OSI model exists in all communications systems.

## Types of Network
Different types of computer networks are categorized by the scope or scale of the network.
They include:
	1. **LAN** - Local Area Network
	2. **WAN** - Wide Area Network
	3. **WLAN** - Wireless Local Area Network
	4. **MAN** - Metropolitan Area Network and many more.
Specifically, I learned more about LAN and WAN. LAN connect local devices together, WAN connects LANs together, and WANs are operating over the Internet.

## Internet
The Internet (or internet) is the global system of interconnected computer networks that uses the Internet protocol suite (TCP/IP) to communicate between networks and devices. It is a network of networks that consists of private, public, academic, business, and government networks of local to global scope, linked by a broad array of electronic, wireless, and optical networking technologies. The Internet carries a vast range of information resources and services, such as the inter-linked hypertext documents and applications of the World Wide Web (WWW), electronic mail, telephony, and file sharing.

### Internet Protocol(IP)
IP (short for Internet Protocol) specifies the technical format of packets and the addressing scheme for computers to communicate over a network. Most networks combine IP with a higher-level protocol called Transmission Control Protocol (TCP), which establishes a virtual connection between a destination and a source.

There are two versions of Internet Protocol i.e.
	1. **IPv4** - IPv4 is the most widely deployed Internet protocol used to connect devices to the Internet. IPv4 uses a 32-bit address scheme allowing for a total of 2^32 addresses (just over 4 billion addresses).
	2. **IPv6** -  IPv6 is the successor to Internet Protocol Version 4 (IPv4). It was designed as an evolutionary upgrade to the Internet Protocol and will, in fact, coexist with the older IPv4 for some time. IPv6 is designed to allow the Internet to grow steadily, both in terms of the number of hosts connected and the total amount of data traffic transmitted. IPv6 was born out of concern that the demand for IP addresses would exceed the available supply.

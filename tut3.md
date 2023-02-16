1. possible, if we employ rdt 3.0 and pipeline protocols, within the application layer

to be more specific, relying on timeouts(non receivement of ack from opp) - ensuring reliability , and methods such as selective repeat, which keeps track of the sequence numbers pf the packets sent in a given window and sends the entire batch(go back n from the ack onwards), or the files individually within the window) - (to maintain out of order delivery and loss)

2.

assume a pkt 0 times out before rcv and is retransmitted
then, the packet remains in a network and is received after the a new pkt1 is sent and received. this will the pkt0(old) to be received, with the new pkt0 being sent detected as a duplicate.

3.

{  --ans key
    Firstly, TCP use large sequence number field (32-bit) to lower the chance a sequence number is to be reused.

Secondly, a packet cannot “live” in the network forever. For example, IP protocol specifies TTL (Time To Live) in packet header to ensure that datagrams do not circulate infinitely in the network. 
This field is decreased by one each time the datagram arrives at a router along the end-to-end path. If TTL field reaches 0, router will discard this datagram. In practice, a maximum packet lifetime of approximately three minutes is assumed in the TCP extensions for high-speed networks.

}
keep a buffer of packets large enough and indiv packets long enough till it can be deemed that the packet is no longer in the network or keep a ujnique tag for the packets to detect for duplicates even if it is received separately

4.
Go back N (GBN) -
sent segments -
5 + 4 = 9
5 - 1 2 3 4 5  |  4 - 2 3 4 5

ack - 
successfully rcv = 4+4 = 8

Selective repeat(SR) -
sent segments -
5 + 1 = 6
5 - 1 2 3 4 5  |  1 - 2


ack - 
successfully rcv = 4+1 = 5

5.
  92 - 65 = 27 bytes
  ack 65 {cumulative, bytes}

6.

{
    TCP sequence number doesn’t increase by one with each TCP segment. Rather, it increases by the number of bytes of data sent. Therefore the size of the MSS is irrelevant here.

}
    1.

    512 = 2^9
    sequence no max = 2^32
    max bytes = 2^32

    2.
    64 = 2^6
    no of packets = 2^(32-9) = 2^23
    total bytes = 2^32 + 2^23 * 2^6 = 4831838208
    time = 4831838208 * 8 / 155 / 10^6  = 249s
    
    {Mbps = megabits per second / MBPS = MegaBytes per second}

7.
    1.

    src = 128.119.245.12
    gaia = 172.30.1.5





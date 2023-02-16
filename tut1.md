R -> transmission rate
L -> packets to transmit
m -> distance
s -> propagation speed
dnodal = dtrans + dprop + dqueue + dproc
transmission -> push out to link from node
propagation -> time taken to travel from node to node through link
1a) dprop = 2 m / s
1b) dtrans = L/R
1c) dendtoend = 2m/s + L/R
1d) last bit in the transmission line
1e) dprop > dtrans -> first bit packet in the transmission line being propagated
1f) dprop < dtrans -> queueing in input link or being processed in next node


2a) 1500/2*10^6 = 0.75ms -> packet delay
for the packet = 3.375ms ( 4.5 packets )
2b) ((n+1)-x)L/R

3a) 4s
3b) 12s
3c) first packet from source host to the first switch -> 0.005s
    second packet be fully received at the first switch -> 0.01s
3d)  How long does it take to move the file from source host
     to destination host when message segmentation is used
     -> 2 * 0.005 + 800 *0.005 = 4.01s

     much shorter
3e) reduced risk of loss of packet. Increased security from segmentation
3f) increased complexity in the switches given that different routes can be taken for each packets, and in the organisation in the packets sent as the packets will be arriving async and not in order

4a) N-1
4b) N(N-1)/2 -> comlete graph
4c) a) packet will take long time to go over to destination, even if the actual destination is close
    b) cost extremely expensive to build all the links

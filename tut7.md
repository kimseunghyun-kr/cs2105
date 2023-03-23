1. no, TCP still owuld not be redundant as the links being reliable do not remove the issue of the receiving end being non-responsive / not listening

correction
Reliable delivery service does not cover

1. Out of order data delivery
2. Routing loops
3. Equipment failures (router crash)


2.
        110111
1001 11000111010
     1001
     ____________
      1010
      1001
     ____________
        1111
        1001
     ____________
         1101
         1001
     ____________
          1000
          1001
     ____________
             110

R = 110

1001 01101010101
      1101
      1001
       1000
       1001
          1101
          1001
           1000
           1001
             011

R = 011

1001 11111010101
     1001
      1101
      1001
       1000
       1001
          1101
          1001
           1000
           1001
              11


R = 011



1001  10001100001
      1001
         1110
         1001
          1110
          1001
           1110
           1001
            1110
            1001
             1111
             1001
              110

R = 110


3.

𝟎𝟎 𝟏𝟏 𝟎𝟎 𝟏𝟏 | 𝟎𝟎
𝟏𝟏 𝟎𝟎 𝟏𝟏 𝟎𝟎 | 𝟎𝟎
𝟎𝟎 𝟏𝟏 𝟎𝟎 𝟏𝟏 | 𝟎𝟎
𝟏𝟏 𝟎𝟎 𝟏𝟏 𝟎𝟎 | 𝟎𝟎
_________________
𝟎𝟎 𝟎𝟎 𝟎𝟎 𝟎𝟎 | 𝟎𝟎

a.

𝟏𝟏 𝟏𝟏 𝟎𝟎 𝟏𝟏 | 𝟎𝟎
𝟏𝟏 𝟎𝟎 𝟏𝟏 𝟎𝟎 | 𝟎𝟎
𝟎𝟎 𝟏𝟏 𝟎𝟎 𝟏𝟏 | 𝟎𝟎
𝟏𝟏 𝟎𝟎 𝟏𝟏 𝟎𝟎 | 𝟎𝟎
_________________
𝟎𝟎 𝟎𝟎 𝟎𝟎 𝟎𝟎 | 𝟎𝟎

b.

𝟏𝟏 𝟏𝟏 𝟎𝟎 𝟏𝟏 | 𝟎𝟎
𝟏𝟏 𝟏𝟏 𝟏𝟏 𝟎𝟎 | 𝟎𝟎
𝟎𝟎 𝟏𝟏 𝟎𝟎 𝟏𝟏 | 𝟎𝟎
𝟏𝟏 𝟎𝟎 𝟏𝟏 𝟎𝟎 | 𝟎𝟎
_________________
𝟎𝟎 𝟎𝟎 𝟎𝟎 𝟎𝟎 | 𝟎𝟎

c.

𝟏𝟏 𝟏𝟏 𝟏𝟏 𝟏𝟏 | 𝟎𝟎
𝟏𝟏 𝟎𝟎 𝟏𝟏 𝟎𝟎 | 𝟎𝟎
𝟏𝟏 𝟏𝟏 𝟏𝟏 𝟏𝟏 | 𝟎𝟎
𝟏𝟏 𝟎𝟎 𝟏𝟏 𝟎𝟎 | 𝟎𝟎
_________________
𝟎𝟎 𝟎𝟎 𝟎𝟎 𝟎𝟎 | 𝟎𝟎


4.
In a shared medium network with many nodes which transmit frequently, TDMA (Time Division Multiple Access) would be the most suitable multiple access scheme.

TDMA divides the shared medium into time slots and allocates specific time slots to each node, which eliminates the possibility of collisions between nodes. Since each node has an exclusive time slot, it can transmit its data without interference from other nodes, even if many nodes are transmitting frequently. Additionally, TDMA provides a fair allocation of the shared medium by allocating equal time slots to each node.

CSMA (Carrier Sense Multiple Access) is another multiple access scheme where each node listens to the medium to determine if it is idle before transmitting its data. However, collisions can still occur even with CSMA, particularly in a network with many nodes which transmit frequently,
 which will result in low efficiency.

Token passing is a scheme where a token is passed between nodes to determine which node has access to the medium. While it can prevent collisions, it may not be suitable for networks with many nodes, particularly if nodes are transmitting frequently, as the token may have to travel through many nodes before reaching the node that needs to transmit data.


4.
a)
244 bit time before A data can be sensed in medium

b)
yes it is possible
B's data will reach A at latest 489(244 + 245) bit time, which is less than 512 bits (64 bytes), which is the minimum frame size.

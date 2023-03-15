import os
import sys
import time
from _socket import SHUT_RDWR
from socket import socket, AF_INET, SOCK_STREAM

from IceHelperRelease import IceHelper


class ServerClient:
    ice_helper          = IceHelper()
    packet_size_server  = ice_helper.sever_packet_size
    packet_size_client  = ice_helper.client_packet_size

    debug_level = 1

    def ice_debug(self, level, *arg):
        if level <= self.debug_level:
            for a in arg:
                print(a, end=' ')
            print()

    def ice_print(self, *arg):
        # ANSI colors
        _c = (
            "\033[0m",  # End of color
            "\033[36m",  # Cyan
            "\033[91m",  # Red
            "\033[35m",  # Magenta
        )

        if self.is_server:
            print(_c[1] + self.secret_student_id + ' Server:' + _c[0], end=' ')
        else:
            print(_c[2] + self.secret_student_id + ' Client:' + _c[0], end=' ')
        for a in arg:
            print(a, end=' ')
        print()

    def __init__(self, argv, is_server):
        if len(argv) < 6:
            print("missing command line parameter: ip_address port_number out_filename mode Student_id")
            self.ice_helper.print_unreliability_mode_info()
            exit(-1)

        i = 1
        self.ip_address          = str(sys.argv[i])
        i += 1
        self.port_number         = int(sys.argv[i])
        i += 1
        self.filename            = str(sys.argv[i])
        i += 1
        mode                     = int(sys.argv[i])
        i += 1
        self.secret_student_id   = str(sys.argv[i])

        self.is_server = is_server

        # open connection
        self.clientSocket = socket(AF_INET, SOCK_STREAM)
        self.clientSocket.connect((self.ip_address, self.port_number))

        # perform handshake
        self.handshake()

        # we can start transmitting the file now
        self.mode_error          = False
        self.mode_reorder        = False
        self.mode_reliable       = False
        if mode == 0:
            self.mode_reliable      = True
        elif mode == 1:
            self.mode_error         = True
        elif mode == 2:
            self.mode_reorder       = True
        else:
            print("ServerClient init: invalid mode")
            exit(-1)

    '''
    This is a complete code, no need to change the function!
    '''
    def handshake(self):
        # initial handshake is to pass the secret key
        # to which the server response with an ok
        # 'C' implies client
        message = 'STID_'
        if self.is_server:
            message += self.secret_student_id + '_' + 'S'
        else:
            message += self.secret_student_id + '_' + 'C'
        self.ice_print('sending: ' + message)
        self.clientSocket.sendall(message.encode())
        # wait to get a response '0_'
        self.ice_print("waiting for server response")
        while True:
            waiting_list_num = self.ice_helper.get_integer_from_socket(self.clientSocket)
            if waiting_list_num is None:
                exit(-1)
            self.ice_print("waiting_list_num: ", waiting_list_num)

            if waiting_list_num == 0:
                # we can start transmitting the file now
                break

    '''
    This is a complete code, no need to change the function!
    '''
    def send_file(self):
        if not self.is_server:
            self.ice_print("Client cannot send file")
            return

        if self.mode_reliable:
            self.send_file_reliable_channel()
        elif self.mode_reorder:
            self.send_file_reorder_channel()
        elif self.mode_error:
            self.send_file_error_channel()
        else:
            print("ServerClient send_file: invalid_mode")
            exit(-1)

    '''
    This is a complete code, no need to change the function!
    '''
    def recv_file(self):
        if self.is_server:
            self.ice_print("Server cannot receive file")
            return

        # time taken estimated
        tic = time.time()

        if self.mode_reliable:
            self.recv_file_reliable_channel()
        elif self.mode_reorder:
            self.recv_file_reorder_channel()
        elif self.mode_error:
            self.recv_file_error_channel()
        else:
            print("ServerClient recv_file: invalid_mode")
            exit(-1)

        elapsed_time = time.time() - tic
        print("\n\n Elapsed time: ", elapsed_time, " Sec\n\n")

    '''
    File reception over Channel with packet errors
    '''
    def recv_file_error_channel(self):
        
        ACK = b'ACKT' * (self.packet_size_client // 4) + b'0' * (self.packet_size_client % 4)
        NAK = b'ACKF' * (self.packet_size_client // 4) + b'0' * (self.packet_size_client % 4)
        # TODO
        CHKSUM = 8;
        SEQNUM = 8
        DATALEN = 4
        buffer = {};
        seqToRcv = 0;
        with open(self.filename, "wb") as f_out:
            while(True): 
                packet = self.get_one_packet();
                if(len(packet) == 0 ):
                    break;
                pktChkSum = packet[:CHKSUM].decode();
                remainder = packet[CHKSUM:]
                calculatedChckSum = self.checkSum(remainder);
                
                if(pktChkSum != calculatedChckSum):
                    self.clientSocket.sendall(NAK);
                    continue;
                else:
                    self.clientSocket.sendall(ACK);
                
                pktSeqNo = packet[CHKSUM:SEQNUM].decode();
                buffer[pktSeqNo] = packet;
                
                if(int(pktSeqNo) != seqToRcv):
                    continue;
                
                while(buffer):
                    openpkt = buffer.pop(seqToRcv);
                    dataLen = openpkt[SEQNUM:SEQNUM + DATALEN].decode()
                    data = openpkt[SEQNUM+DATALEN : SEQNUM+DATALEN + dataLen];
                    f_out.write(data);

    '''
    File transmission over Channel with packet errors
    '''
    def send_file_error_channel(self):
        ACK = b'ACKT' * (self.packet_size_client // 4) + b'0' * (self.packet_size_client % 4)
        # <8 byte checksum> < 8 byte seq > < 4 byte len > <msg>
        CHKSUM = 8;
        SEQNUM = 8
        DATALEN = 4
        dataPcktSize = 0;
        if(self.is_server):
            dataPcktSize += self.packet_size_server - DATALEN - SEQNUM - CHKSUM;
        else:
            dataPcktSize += self.packet_size_client - DATALEN - SEQNUM - CHKSUM;
            
        # TODO
        file_size = os.path.getsize(self.filename)
        with open(self.filename, "rb") as f_in:
            while(True):
                data = f_in.read(dataPcktSize);
                if(len(data) == 0):
                    break;
                
                dataLen = str(len(data)).encode();
                
                if(len(dataLen) < DATALEN):
                    dataLen = b'0' * (DATALEN - len(dataLen)) + dataLen

                if(len(data) < dataPcktSize):
                    data += b'\x00' * (dataPcktSize - len(data))
                
                currSEQ = str(seqNo).encode();
                if(len(currSEQ) < SEQNUM):
                    currSEQ = b'0' * (SEQNUM - len(currSEQ)) + currSEQ;
                
                data = currSEQ + dataLen + data;
                
                currCheckSum = self.checkSum(data)
                if(len(currCheckSum)<CHKSUM):
                    currCheckSum = b'0' * (CHKSUM - len(currCheckSum)) + currCheckSum
                
                data = currCheckSum + data;
                self.clientSocket.sendall(data)

                rcv = self.get_one_packet();
                while(rcv != ACK) :
                    if(len(rcv == 0)):
                        break;
                    self.clientSocket.sendall(data);
                    rcv = self.get_one_packet();
                
                seqNo = seqNo + dataPcktSize;
                    

    '''
    File reception over Channel which Reorders packets
    '''
    def recv_file_reorder_channel(self):
        # TODO
        SEQNUM = 8
        DATALEN = 4
        buffer = {};
        seqToRcv = 0;
        with open(self.filename, "wb") as f_out:
            while(True): 
                packet = self.get_one_packet();
                if(len(packet) == 0 ):
                    break;
                pktSeqNo = packet[:SEQNUM].decode();
                buffer[pktSeqNo] = packet;
                if(int(pktSeqNo) != seqToRcv):
                    continue;
                while(buffer):
                    openpkt = buffer.pop(seqToRcv);
                    dataLen = openpkt[SEQNUM:SEQNUM + DATALEN].decode()
                    data = openpkt[SEQNUM+DATALEN : SEQNUM+DATALEN + dataLen];
                    f_out.write(data);
                    

    '''
    File transmission over Channel which Reorders packets
    '''
    def send_file_reorder_channel(self):
        # TODO
        SEQNUM = 8
        DATALEN = 4
        dataPcktSize = 0;
        if(self.is_server):
            dataPcktSize += self.packet_size_server - DATALEN - SEQNUM;
        else:
            dataPcktSize += self.packet_size_client - DATALEN - SEQNUM;

        file_size = os.path.getsize(self.filename)
        with open(self.filename, "rb") as f_in:
            seqNo = 0;
            while(True):
                data = f_in.read(dataPcktSize);

                if(len(data) == 0):
                    break;
                
                dataLen = str(len(data)).encode();
                
                if(len(dataLen) < DATALEN):
                    dataLen = b'0' * (DATALEN - len(dataLen)) + dataLen

                if(len(data) < dataPcktSize):
                    data += b'\x00' * (dataPcktSize - len(data))
                
                currSEQ = str(seqNo).encode();
                if(len(currSEQ) < SEQNUM):
                    currSEQ = b'0' * (SEQNUM - len(currSEQ)) + currSEQ;
                
                
                data = currSEQ + dataLen + data;
                self.clientSocket.sendall(data)
                seqNo = seqNo + dataPcktSize;
        

    '''
    File reception over Reliable Channel
    '''
    def recv_file_reliable_channel(self):
        # TODO
        DATALEN = 4
        dataPcktSize = 0;
        if(self.is_server):
            dataPcktSize += self.packet_size_server - DATALEN;
        else:
            dataPcktSize += self.packet_size_client - DATALEN;
            
        with open(self.filename, "wb") as f_out:
            while(True): 
                packet = self.get_one_packet();
                if(len(packet) == 0 ):
                    break;
                dataLen = packet[:DATALEN].decode();
                data = packet[DATALEN:DATALEN + dataLen];
                
                f_out.write(data);
            pass

    '''
    File transmission over Reliable Channel
    '''
    def send_file_reliable_channel(self):
        # TODO
        file_size = os.path.getsize(self.filename)
        # <4 byte len > <data> <padding>
        DATALEN = 4
        dataPcktSize = 0;
        if(self.is_server):
            dataPcktSize += self.packet_size_server - DATALEN;
        else:
            dataPcktSize += self.packet_size_client - DATALEN;
            
        with open(self.filename, "rb") as f_in:
            while(True):
                data = f_in.read(dataPcktSize);

                if(len(data) == 0):
                    break;
                
                dataLen = str(len(data)).encode();
                
                if(len(dataLen) < DATALEN):
                    dataLen = b'0' * (DATALEN - len(dataLen)) + dataLen

                if(len(data) < dataPcktSize):
                    data += b'\x00' * (dataPcktSize - len(data))
                    
                data = dataLen + data;
                self.clientSocket.sendall(data)
            pass

    # ######## Helper #############
    # This is a complete code, no need to change the function!
    def get_one_packet(self):
        # server receives packet from client and vice versa
        if self.is_server:
            packet = self.ice_helper.get_n_bytes_raw(self.clientSocket, self.packet_size_client)
        else:
            packet = self.ice_helper.get_n_bytes_raw(self.clientSocket, self.packet_size_server)

        return packet

    @staticmethod
    # This is a complete code, no need to change the function!
    def _print_data_hex(data, delay=0.0):
        print('-----', len(data), '-------')
        print(data.hex())
        time.sleep(delay)

    # This is a complete code, no need to change the function!
    def terminate(self):
        try:
            self.clientSocket.shutdown(SHUT_RDWR)
            self.clientSocket.close()
        except OSError:
            # the socket may be already closed
            pass
    
    def checkSum(self, data : bytes) -> bytes:
        checksum = 0
        for byte in data:
            checksum += byte
        checksum &= 0xFFFFFFFFFFFFFFFF
        return bytes(checksum)
    
import time
import json
import pingparsing
import math
import logging
from datetime import datetime

def ping():
    ping_parser = pingparsing.PingParsing()
    transmitter = pingparsing.PingTransmitter()
    transmitter.destination_host = "google.com"
    transmitter.count = 1
    result = transmitter.ping()
    json.dumps(ping_parser.parse(result).as_dict(), indent=4)
    global tripTime
    global packetLoss
    tripTime = ping_parser.rtt_avg
    packetLoss= ping_parser.packet_loss
    print(tripTime)
    print(packetLoss)

now = datetime.now()


for x in range(1):
    time.sleep(1)
    ping()
    r1 = tripTime
    p1 = packetLoss
    time.sleep(1)
    ping()
    r2 = tripTime
    p2 = packetLoss
    time.sleep(1)
    ping()
    r3 = tripTime
    p3 = packetLoss
    time.sleep(1)
    ping()
    r4 = tripTime
    p4 = packetLoss
    time.sleep(1)
    ping()
    r5 = tripTime
    p5 = packetLoss
    time.sleep(1)
    ping()
    r6 = tripTime
    p6 = packetLoss
    time.sleep(1)
    ping()
    r7 = tripTime
    p7 = packetLoss
    time.sleep(1)
    ping()
    r8 = tripTime
    p8 = packetLoss
    time.sleep(1)
    ping()
    r9 = tripTime
    p9 = packetLoss
    time.sleep(1)
    ping()
    r10 = tripTime
    p10 = packetLoss
    sum = str((r1 + r2 + r3 + r4 + r5 + r6 + r7 + r8 + r9 + r10)/10)
    sum2 = str((p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10)/10)
    import logging
    logging.basicConfig(filename=r"D:\Users\Tyler\Desktop\log_filename.txt", level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.debug(sum + " 10s RTT avg")
    logging.debug(sum2 + " 10s Packet Loss avg")
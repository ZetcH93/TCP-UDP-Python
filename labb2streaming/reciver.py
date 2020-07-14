from socket import *

recieverPort = 12000
expectedPacket = 10000


recieverSocket = socket(AF_INET, SOCK_DGRAM)
recieverSocket.bind(('', recieverPort))

print ("The UDP reciever is ready to recieve")

while True:
    strValue = ""
    packetNr = ""
    data = ""
    expectedPacket += 1


    message, senderAddress = recieverSocket.recvfrom(2048)
    strValue = str(message.decode())

    for x in range(1410):
     if (x != ";" and x > 6):
       data += strValue[x]
     elif(x != ";" and x < 5):
       packetNr += strValue[x]

    if(expectedPacket < int(packetNr)):
     print("Expected packetNr: "+str(expectedPacket)+ " got instead packet: "+ packetNr)
    if(expectedPacket > int(packetNr)):
     print("Expected packetNr: "+str(expectedPacket)+ " got instead packet: "+ packetNr)
       

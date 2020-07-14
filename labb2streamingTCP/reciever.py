from socket import *


recieverPort = 12000
recieverName = '192.168.1.114'

recieverSocket = socket(AF_INET, SOCK_STREAM)
recieverSocket.bind((recieverName, recieverPort))
recieverSocket.listen(1)

expectedPacket = 10000

print ('The TCP reciever is ready to receive')


connectionSocket, addr = recieverSocket.accept()
   
while True:
        message = connectionSocket.recv(2048).decode()

        strValue = ""
        packetNr = ""
        data = ""
        expectedPacket += 1

        strValue = str(message)
        if(len(strValue) != 0):
          packetNr = strValue[:5]
          data = strValue[6:1410] ## the rest of the data
        print(packetNr)
        print(data)

        if(expectedPacket < int(packetNr)):
          print("Expected packetNr: "+str(expectedPacket)+ " got instead packet: "+ packetNr)
        if(expectedPacket > int(packetNr)):
          print("Expected packetNr: "+str(expectedPacket)+ " got instead packet: "+ packetNr)
        else: break
       

connectionSocket.close()
recieverSocket.close()
print("File received")
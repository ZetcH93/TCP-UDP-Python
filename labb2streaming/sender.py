


from socket import *
import time

recieverName = '192.168.1.159'
recieverPort = 12000

payload = ""
paketNr = 10000
x = 0


for A in range(1400):
 payload = (str(payload) + "A")

payload += "####"
  
senderSocket = socket(AF_INET, SOCK_DGRAM)

print("Sending file...")
while (x < 1000):  #100 paket ska skickas över dvs en fil som består av 140000 bokstäver
    paketNr += 1
    fullPayload = (str(paketNr)+";" + payload)

    senderSocket.sendto(fullPayload.encode(),(recieverName, recieverPort))
    x += 1
    time.sleep(0.02)
    
    
    #0.02 = hög last 1000 paket
    #0.05 = låg last 400 paket
    #1 = 100 paket
   

 

senderSocket.close()
print("the whole file has been sent...")


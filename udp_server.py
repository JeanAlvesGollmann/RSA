import socket
localIP     = "192.168.0.233"
localPort   = 20001
bufferSize  = 250000
chavePublica=''
listaVariaveis=[]
textoCriptografia=''
msg= "The information security is of significant importance to ensure the privacy of communications"
msgFromServer=''
def criptografa(numero,e,N):
    letraCriptografia=pow(numero,e,N)
    return letraCriptografia
#bytesToSend         = str.encode(msgFromServer)
# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")
# Listen for incoming datagrams
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    if(chavePublica==''):
        chavePublica=message
    listaVariaveis=str(chavePublica).split('-')
    e,N=listaVariaveis
    e=e.replace("b'","")
    N=N.replace("'","")
    eInt=int(e)
    NInt=int(N)
    #Realiza a criptografia de letra por letra da palavra e envia para o cliente
    for i in msg:
        numero=ord(i)
        criptografia=criptografa(numero,eInt,NInt)
        bytesToSend         = str.encode(str(criptografia))
        UDPServerSocket.sendto(bytesToSend, address)
        
    msgFromServer=textoCriptografia

    clientMsg = str(message,"utf-8")
    clientIP  = "Client IP Address:{}".format(address)
    
    #Envia a palara fim, para definir que a frase foi enviada completamente
    bytesToSend = str.encode("Fim")
    UDPServerSocket.sendto(bytesToSend, address)

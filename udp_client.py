import socket
import random
from Crypto.Util import number
from sympy import mod_inverse

def geraNumeroPrimo():
    p = number.getPrime(4096)
    return p

def decriptografa(letraDescriptografia,d,N):
    letraDescriptografia=pow(letraDescriptografia,d,N)
    return letraDescriptografia

#Valores para RSA
q=geraNumeroPrimo()
p=geraNumeroPrimo()
N=p*q
totienteN=p*q-p-q+1
e=geraNumeroPrimo()
while e>totienteN:
    e=geraNumeroPrimo()
while totienteN%e==0:
    while e>totienteN:
        e=geraNumeroPrimo()
d = pow(e, -1, totienteN)


PublicKey = ""
msgFromClient       = str(e)+'-'+str(N)
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("192.168.0.233", 20001)
bufferSize          = 250000
encerraConexao=False
# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Send to server using created UDP socket
UDPClientSocket.sendto(bytesToSend, serverAddressPort)

letras=[]
msgFromServer=''

#Recebe cada letra do Servidor e adiciona em uma lista
while msgFromServer!='Fim':
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    msgFromServer = str(msgFromServer[0],"utf-8")
    if(msgFromServer!='Fim'):
        letras.append(msgFromServer)

#Realiza a descriptografia de cada letra recebida do Servidor e une para formar a frase no final do processo
textoDescriptografado=''
for i in letras:
    iInt=int(i)
    numeroOriginal=decriptografa(iInt,d,N)
    letraOriginal=chr(numeroOriginal)
    textoDescriptografado=textoDescriptografado+str(letraOriginal)

#Exibe a frase que foi recebida do Servidor
print('Server:'+textoDescriptografado)


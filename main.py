# Client to request data to server, a randomly generated number, and will receive it from server

from socket import *

clientSocket = socket(AF_INET, SOCK_STREAM)

host = "127.0.0.1"
port = 7676


clientSocket.connect((host, port))
print("CLIENT: connected to " + host + " on port " + str(port))

while True:
    clientMsg = ""

    while clientMsg != "1" and clientMsg != "quit":
        print("Waiting to generate random number")
        with open ('treat.txt', 'r') as f:
            clientMsg = f.readline()

    if "quit" in clientMsg:
        clientSocket.send(clientMsg.encode())
        break

    clientSocket.send(clientMsg.encode())

    print("CLIENT: now waiting for message from server...")
    replyFromServer = clientSocket.recv(1024)

    print("CLIENT, received message from HOST: '" + replyFromServer.decode() + "'")
    print("CLIENT, Random special item #" + replyFromServer.decode() + " will be added to your shopping list.")

clientSocket.close()
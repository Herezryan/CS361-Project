# Server to receive request from client, generate random number, and send that back to client

from socket import *
import random

host = "127.0.0.1"
port = 7676

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

serverSocket.bind((host, port))

serverSocket.listen()

connSocket, connAddr = serverSocket.accept()

print("HOST: connected by a client on " + str(connAddr))

while True:
    print("HOST: waiting for message from client...")
    clientMsg = connSocket.recv(1024)

    if "quit" in clientMsg.decode():
        print("HOST, CLIENT sent 'quit' as a message, now stopping connection. Have a good one!")
        break

    print("HOST, received message from CLIENT: '" + clientMsg.decode() + "'")

    # part of this program to generate random number to correspond
    # to special item to be added to this week's shopping list
    randomSpecialItem = random.randint(0, 10)
    print("randomly generated number: " + str(randomSpecialItem))
    print("The randomly chosen special item that'll be added to your shopping list is special item #" + str(
            randomSpecialItem) + "\n")

    serverResponse = str(randomSpecialItem)

    connSocket.send(serverResponse.encode())


connSocket.close()
serverSocket.close()
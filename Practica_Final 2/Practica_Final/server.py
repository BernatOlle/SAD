import socket
from _thread import *
from player import Player
import pickle

server = "192.168.1.33"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))  # connectes el socket amb el servidor i el port

except socket.error as e:
    str(e)

s.listen(2)  # escolta fins que es connecten dos clients
print("Waiting for a connection, Server Started")

players = [Player(10, 10, 50, 50, (255, 0, 0)),
           Player(10, 10+100*6, 50, 50, (0, 0, 255))]
# Player (posicio x inici, posicio y inici , weigth , length , color )


def threaded_client(conn, player):

    # envia una copia serialitzada del player
    conn.send(pickle.dumps(players[player]))
    reply = " "
    while True:
        try:
            # recibe datos del cliente cuando se mueve
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]
                # imprimeix la posicio nova que has rebuts i envia la teva posicio
                print("Recieved: ", data)
                print("Sending: ", reply)

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()


currentPlayer = 0

while True:
    conn, addr = s.accept()
    # escolta 2 connexions i crea dos threads per agafar la dada rebuda, actualitzarla i envia la seva actual
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1

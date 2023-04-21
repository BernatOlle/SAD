import socket
from _thread import *
import pickle
from game import Game

server = "10.192.152.219"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))  # connectes el socket amb el servidor i el port
except socket.error as e:
    str(e)


s.listen()  # escolta fins que es connecten dos clients
print("Waiting for a connection, Server Started")

connected = set()
games = {}
idCount = 0


def threaded_client(conn, p, gameId):
    global idCount
    conn.send(str.encode(str(p)))
    
    reply = ""
    
    while True:
        try:
            data = conn.recv(4096).decode()
            if gameId in games:
                game = games[gameId]
                
                if not data:
                    break
                else:
                    if data == "reset":
                        game.resetWent()
                        
                    elif data != "get":
                        print(data)
                        game.play(p,data)
                        
                    reply = game
                    conn.sendall(pickle.dumps(reply))
            else:
                break
        except:
            break
        
    print("Lost connectiom")
    
    try:
        del games[gameId]
        print("Closing game", gameId)
    
    except:
        pass

    idCount -= 1
    conn.close()
    


while True:
    conn, addr = s.accept()
    # escolta 2 connexions i crea dos threads per agafar la dada rebuda, actualitzarla i envia la seva actual
    print("Connected to: ", addr)

    idCount += 1
    p = 0
    gameId = (idCount-1)//2
    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        print("Creating a new game...")
    else:
        games[gameId].ready = True
        p = 1

    start_new_thread(threaded_client, (conn,p, gameId))

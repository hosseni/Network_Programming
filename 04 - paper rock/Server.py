from socket import *
from threading import *


host = '127.0.0.1'
port = 7000

def handle_client(conn, players, player_choices):
    while True:
        try:
            data = conn.recv(1024)
            choice = data.decode()
            player_choices.append(choice)
            if len(player_choices) == 2:
                evaluate_game(players, player_choices)
                break
        except:
            return

def evaluate_game(players, player_choices):
    p1_choice = player_choices[0]
    p2_choice = player_choices[1]
    if p1_choice == "rock" and p2_choice == "paper":
        players[0].send("You lose!".encode())
        players[1].send("You win!".encode())
    elif p1_choice == "rock" and p2_choice == "scissors":
        players[0].send("You win!".encode())
        players[1].send("You lose!".encode())
    elif p1_choice == "paper" and p2_choice == "rock":
        players[0].send("You win!".encode())
        players[1].send("You lose!".encode())
    elif p1_choice == "paper" and p2_choice == "scissors":
        players[0].send("You lose!".encode())
        players[1].send("You win!".encode())
    elif p1_choice == "scissors" and p2_choice == "rock":
        players[0].send("You lose!".encode())
        players[1].send("You win!".encode())
    elif p1_choice == "scissors" and p2_choice == "paper":
        players[0].send("You win!".encode())
        players[1].send("You lose!".encode())
    else:
        players[0].send("It's a tie!".encode())
        players[1].send("It's a tie!".encode())

def start_server():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(2)
    players = []
    player_choices = []
    print("Server started listening on {}:{}".format(host, port))
    while True:
        conn, addr = server_socket.accept()
        print("Connected to: ", addr)
        players.append(conn)
        Thread(target=handle_client, args=(conn, players, player_choices)).start()

if __name__ == '__main__':
    start_server()

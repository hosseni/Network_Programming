from socket import *
from threading import *
from tkinter import *

host = gethostname()
port = 9999

def send_choice(choice):
    server_socket.send(choice.encode())
    disable_buttons()
    Thread(target=receive_result).start()

def receive_result():
    data = server_socket.recv(1024)
    result = data.decode()
    result_label.config(text=result)
    enable_buttons()

def disable_buttons():
    rock_button.config(state=DISABLED)
    paper_button.config(state=DISABLED)
    scissors_button.config(state=DISABLED)

def enable_buttons():
    rock_button.config(state=NORMAL)
    paper_button.config(state=NORMAL)
    scissors_button.config(state=NORMAL)

if __name__ == '__main__':
    
    server_socket = socket((AF_INET), SOCK_STREAM)
    server_socket.connect(('127.0.0.1', 7000))

    root = Tk()
    root.title("Paper Rock Game")
    root.geometry("300x300")
    root.resizable(False, False)

    label = Label(root, text="Choose your move:")
    label.pack()

    rock_button = Button(root, text="Rock", command=lambda: send_choice("rock"))
    rock_button.pack()

    paper_button = Button(root, text="Paper", command=lambda: send_choice("paper"))
    paper_button.pack()

    scissors_button = Button(root, text="Scissors", command=lambda: send_choice("scissors"))
    scissors_button.pack()

    result_label = Label(root, text="")
    result_label.pack()

    root.mainloop()
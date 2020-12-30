import time
import socket
import sys
import json
import os
import shutil

os.chdir(__file__.replace(os.path.basename(__file__), ""))
with open("config.json", "r") as f:
    data = json.load(f)

    DEFAULTPORT = data["defaultport"]
    
class Client:
    def __init__(self):
        self.s = socket.socket()

    def connect(self):
        self.IPADDR = input("Please type the IP and PORT (optional, default is {}) of the device you want to connect to. (eg. 192.168.0.11:50234): ".format(DEFAULTPORT))

        if self.IPADDR == "":
            return

        if ":" in self.IPADDR:
            self.IPADDR = self.IPADDR.split(":", 1)
            self.HOST = str(self.IPADDR[0])
            self.PORT = int(self.IPADDR[1])
        else:
            self.HOST = str(self.IPADDR)
            self.PORT = DEFAULTPORT

        self.s.connect((self.HOST, self.PORT))
        print("Connected to the Server.")

    def run_command(self):
        self.command = self.s.recv(1024)
        self.command = self.command.decode()

        try:
            print("Command: {}".format(self.command))
            self.s.send("Received command.".encode())
            os.system(self.command)

        except:
            self.s.send("Oops! Something went wrong. Try again.".encode())
            return

def run():
    client = Client()

    client.connect()
    while True:
        client.run_command()

if __name__ == "__main__":
    run()

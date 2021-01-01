import time
import socket
import sys
import json
import os
import shutil

os.chdir(os.path.dirname(sys.argv[0]))
with open("config.json", "r") as f:
    data = json.load(f)

    DEFAULTPORT = data["defaultport"]
    VERSION = data["client"]["version"]
    
class Client:
    def __init__(self):
        self.s = socket.socket()
        
        print("PySH Client")
        print("Version: {}".format(VERSION))
        print("-"*25)

    def connect(self):
        while True:
            self.IPADDR = input("Please type the IP and PORT (optional, default is {}) of the device you want to connect to. (eg. 192.168.0.11:50234): ".format(DEFAULTPORT))

            if self.IPADDR != "":
                break

        if self.IPADDR.lower() == "localhost":
            self.HOST = "127.0.0.1"
        
        if ":" in self.IPADDR:
            self.IPADDR = self.IPADDR.split(":", 1)
            if self.IPADDR[0] == "localhost":
                self.HOST = "127.0.0.1"

            self.HOST = str(self.IPADDR[0])
            self.PORT = int(self.IPADDR[1])
        else:
            self.HOST = str(self.IPADDR)
            self.PORT = DEFAULTPORT

        self.s.settimeout(5)
        
        try:
            self.s.connect((self.HOST, self.PORT))
        except socket.error:
            print("\nFailed to connect. Check if you've typed the connection address correctly.\n")
            self.connect()
        
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

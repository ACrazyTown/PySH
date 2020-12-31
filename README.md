# PySH
A poorly written SSH alternative in Python

## About
**PySH** is a Python script that allows a user to create a "Server" and connect to it using a "Client". The "Server" can send commands to the "Client". It's basically SSH but in Python.

## How to run
Running the program is fairly simple.
* **OPTIONAL** Edit the config.json to your will.
* Launch **Server.py** on a computer that will send commands to the client.
* Launch **Client.py** on the computer that will receive and execute those commands.
* Using the **Server.py**'s "**Connection Address**", connect to the Server using the Client.
***(NOTE: On macOS the connection address will always be localhost (127.0.0.1), this is due to an issue with socket.gethostbyname() on macOS. If you want to use the Client on a computer running macOS; you are going to have to get the local/public IP manually.***
* You're done

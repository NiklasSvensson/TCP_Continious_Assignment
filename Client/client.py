#!/usr/bin/env python3

from tkinter import filedialog
from tkinter import *

import os

# Import socket module 
import socket

# Defining client functions



def LoginMenu():
    while True:
        print("Select action!")
        print("----------------------")
        print("1 - Login existing user")
        print("2 - Register new user")
        print("3 - Exit the client")
        print("-----------------------")

        menuSelect = input("Select your action: ")
        menuSelect = int(menuSelect)
        
        if type (menuSelect is int):
                
            if(menuSelect == 1):
                return "loggin"

            elif (menuSelect == 2):
                return "register"

            elif (menuSelect == 3):
                return "exit"
            else:
                print("Not a valid input!")

def TakeUserdataInput():
    username = input("Write your username: ")
    password = input("Write your password) ")

    return username, password

def CreateUserData(username, password):
    
    userData = username + ":" + password
    return userData

def CreateNewUserData(newUsername, newPassword):
    print ("Registering new user!")
    print ("---------------------")

    newUser = newUsername + ":" + newPassword + "\n"
    return newUser

def CloseAllConnections ():
    s1.shutdown(1)
    s2.shutdown(1)
    s3.shutdown(1)
    s1.close()
    s2.close()
    s3.close()

def ActionMenu():

    while True:
        print("Welcome to the server!")
        print("----------------------")
        print("Please select what you would like to do")
        print("")
        print("1 - Send file to the server (.jpg, .txt)")
        print("2 - Exit and close the client")
        print("-----------------------")

        menuSelect = input("Select your action: ")
        menuSelect = int(menuSelect)

        if type (menuSelect is int):
            if(menuSelect == 1):
                return "sendFile"

            elif(menuSelect == 2):
                return "exit"
        
            else:
                print("Not a valid input!")

def SendPicture(filename):
    print("Write name of the file on the server: ")

    serverFileName = input ("Save the file as: ")

    s3.send(serverFileName.encode())

    fileToSend = open(filename, "r+b")
    data = fileToSend.read(4096)

    while data:
        print("Sending data...")
        s3.send(data)
        data = fileToSend.read(4096)
    fileToSend.close()
    s3.send(b"DONE")
    print("Done sending data!")

def SendTextFile(filename):
    print("Write name of the file on the server: ")
    
    serverFileName = input ("Save the file as: ")

    s3.send(serverFileName.encode())

    fileToSend = open(filename, "r")

    data = fileToSend.read(1024)
    while data:
        print("Sending data...")
        s3.send(data.encode())
        data = fileToSend.read(1024)
    fileToSend.close()
    s3.send(b"DONE")
    print("Done sending data!")
    
def main():    

    # Create sockets for communication

    s1 = socket.socket() # socket for server <-> client communication
    s2 = socket.socket() # socket for server actions
    s3 = socket.socket() # socket for file transfer

    # Define the port on which you want to connect
    port1 = 81
    port2 = 82
    port3 = 83

    # Connect to the server
    s1.connect(('127.0.0.1', port1))
    s2.connect(('127.0.0.1', port2))
    s3.connect(('127.0.0.1', port3))

    #Creating client

    while True:
        menuSelect = LoginMenu()
        login = False

        if (menuSelect == "loggin"):
            while True:
                username, password = TakeUserdataInput()
                userData = CreateUserData(username, password)

                #SEND TO SERVER
                s2.send(b'LOGGIN')
                s1.send(userData.encode())

                #HANDLE SERVER RESPONSE
                serverResponse = s1.recv(1024)

                if (serverResponse == b'success'):
                    print("Loggin was successful!")
                    login = True
                    break
                elif (serverResponse == b'userNotFound'):
                    print("Username or password were not correct!")
                    break
        
        elif (menuSelect == "register"):
            while True:
            
                #DO SOMEthING
                username, password = TakeUserdataInput()
                newUserData = CreateNewUserData(username, password)

                #SEND TO SERVER
                s2.send(b'REGISTER')
                s1.send(newUserData.encode())

                #HANDEL SERVER RESPONSE
                serverResponse = s1.recv(1024)

                if (serverResponse == b'existing'):
                    print ("Username already exist!")
                elif (serverResponse == b'newUserCreated'):
                    print ("New user was succesfully created!")
                    break

        elif (menuSelect == "exit"):
            # REQUEST CLOSING OF CONNECTIONS
            s2.send(b'exit')
            print("Exiting program, closing all connectioins!")
            CloseAllConnections()
            print("Good bye!")
            exit()
            break
        
#        else:
#           print("DEBUGG: THIS SHOULD NOT HAPPEN (MENNUSELECT)")

        if (login):
            break

#       print("Debugg: end of menuselect loop")

    while True:
        actionSelect = ActionMenu()

        if(actionSelect == "sendFile"):

            filename = input ("Please write the name of the file you would like to send\n(must be in same directory), or provide full path to file:  ")
    
#           root = Tk()
#           root.filename =  filedialog.askopenfilename(initialdir = "/",
#                                                    title = "Select file",
#                                                    filetypes = (("jpeg files","*.jpg"),("txt file", "*.txt")))
#           path, extension = os.path.splitext(root.filename)

            path, extension = os.path.splitext(filename)

            if extension == ".jpg":
                s2.send(b'PICTURE')

                SendPicture(filename)
#               SendPicture(root.filename)
            
            elif extension == ".txt":
                s2.send(b'TEXTFILE')
                SendTextFile(filename)
#                SendTextFile(root.filename)
           
            else:
                print("Not a valid file type or missing file extension")

        elif(actionSelect == "exit"):
            s2.send(b'exit')
            CloseAllConnections()
            print("Good bye!")
            break

if __name__ == "__main__":
    main()
    

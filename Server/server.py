#!/usr/bin/env python3

# Import the socket library 
import socket
import sys


def ParseNewUsername (newUserInfo):
    temp = newUserInfo.rstrip('\n')
    newUsername = temp.split(":")

    return newUsername[0]

def GetAllUsersnames(users):
    userNames = []
    temp = []

    for split in users:
        temp = split.split(":")
        userNames.append(temp[0])

    return userNames
    
def CloseAllConnections(c1, c2, c3):
    c1.shutdown(1)
    c2.shutdown(1)
    c3.shutdown(1)
    c1.close()
    c2.close()
    c3.close()

def reciveUserData(c1):
    userInfo = c1.recv(1024)
    userInfo = userInfo.decode()
    userInfo = userInfo.rstrip("\n")

    return userInfo
    

def LoginFromClient(userInfo):
    f = open('logins.txt', 'r+')

    users = []
    lines = f.readlines()

    for line in lines:
        users.append(line.rstrip('\n'))

    f.close()

    #Check if userInfo exist if true return successful
    #else return that the user was not found
    if userInfo in users:
        return b'success'
    else:
        return b'userNotFound'

def reciveNewUser(c1):
    newUserInfo = c1.recv(1024)
    newUserInfo = newUserInfo.decode()

    return newUserInfo

def WriteToLogin(newUserInfo):
        file = open('logins.txt', 'a+')
        file.write(newUserInfo)
        file.close()
    
    
def RegisterNewUser(newUserInfo):
    f = open('logins.txt', 'r+')

    users = []
    lines = f.readlines()

    for line in lines:
        users.append(line.rstrip('\n'))

    f.close()

    #Check if username already exist
    newUsername = ParseNewUsername(newUserInfo)
    allUsernames = GetAllUsersnames(users)
    if newUsername in allUsernames:
        return b'existing'
    else:
        return b'newUserCreated'

def RecivePicture (c3):
    filename = c3.recv(1024)
    filename = filename.decode()
    filename = filename + ".jpg"
         
    filetodown = open(filename,"w+b")
    
    while True:
        data = c3.recv(4096)
        if data == b"DONE":
            print("Done reciving")
            break
        filetodown.write(data)
    filetodown.close()
    print ("DEBUGG: END IF PICTURE SEND")
        
def ReciveTextFile (c3):
    filename = c3.recv(1024)
    filename = filename.decode()
    filename = filename + ".txt"

    filetodown = open (filename, "w")
    while True:
        data = c3.recv(1024)
        data = data.decode()
        if data == "DONE":
            print ("Done reciving")
            break
        filetodown.write(data)
    filetodown.close()
    print ("DEBUGG: TEXT FILE END")

def main():
    
    print("Server is starting!")

    # next create a socket object 
    s1 = socket.socket()
    s2 = socket.socket()
    s3 = socket.socket()
    print ("Socket successfully created")

    # reserve a port on your computer
    port1 = 81
    port2 = 82
    port3 = 83

    # Next bind to the port 
    # we have not typed any ip in the ip field 
    # instead we have inputted an empty string 
    # this makes the server listen to requests 
    # coming from other computers on the network 
    s1.bind(('127.0.0.1', port1))
    s2.bind(('127.0.0.1', port2))
    s3.bind(('127.0.0.1',port3))
    print ("socket binded to %s" %(port1) )
    print ("socket binded to %s" %(port2) )
    print ("socket binded to %s" %(port3) )

    # put the socket into listening mode 
    s1.listen(5)
    s2.listen(5)
    s3.listen(5)
    print ("socket is listening")		

    # a forever loop until we interrupt it or 
    # an error occurs
    while True:
        
        # Establish connection with client. 
        c1, addr1 = s1.accept() #socket for server <-> client comunication
        c2, addr2 = s2.accept() #socket for server actions
        c3, addr3 = s3.accept() #Socket for file transfer
        print ('Got connection from', addr1)
        print ('Got connection from', addr2)
        print ('Got connection from', addr3)
        while True:
            serverAction = c2.recv(1024)

            print("DEBUGG: server action recived!")
            print(serverAction.decode())
        
            if serverAction == b'LOGGIN':
                while True:
                    userData = reciveUserData(c1)
                    response = LoginFromClient(userData)
                    
                    if response == b'success':
                        c1.send(response)
                        break

                    elif response != b'success':
                        c1.send(response)
                        break

            elif serverAction == b'REGISTER':
                while True:
                    newUserData = reciveNewUser(c1)
                    response = RegisterNewUser(newUserData)
               
                    if response == b'newUserCreated':
                        WriteToLogin(newUserData)
                        c1.send(response)
                        break

                    elif response != b'newUserCreated':
                        c1.send(response)
                        break

            elif serverAction == b'PICTURE':
                RecivePicture(c3)

            elif serverAction == b'TEXTFILE':
                ReciveTextFile(c3)

            elif serverAction == b'exit':
                CloseAllConnections(c1, c2, c3)
                print ("Connection closed!")
                break
            elif serverAction == b'SHUTDOWN':
                s1.close()
                s2.close()
                s3.close()
                exit()
        
if __name__ == '__main__':
    main()

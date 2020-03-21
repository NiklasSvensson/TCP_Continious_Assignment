#!/usr/bin/env python3 -u



# first of all import the socket library 
import socket
import sys


def ParseNewUsername(newUserInfo):
    temp = newUserInfo.rstrip("\n")
    newUsername = temp.split(":")

    return newUsername[0]

def GetAllUsersnames(users):
    userNames = []
    temp = []

    for split in users:
        temp = split.split(":")
        userNames.append(temp[0])

    return userNames
    
def CloseAllConnections ():
    c1.shutdown(1)
    c2.shutdown(1)
    c3.shutdown(1)
    c1.close()
    c2.close()
    c3.close()

#def LoginFromClient(action):
def LoginFromClient():
    f = open('logins.txt', 'r+')

    users = []
    lines = f.readlines()

    for line in lines:
        users.append(line.rstrip('\n'))

    f.close()
    
    userInfo = c1.recv(1024)
    userInfo = userInfo.decode()
    userInfo = userInfo.rstrip("\n")

    #Check if userInfo exist if true return successful
    #else return that the user was not found
    if userInfo in users:
        return b'success'
    else:
        return b'userNotFound'
    
def RegisterNewUser():
    f = open('logins.txt', 'r+')

    users = []
    lines = f.readlines()

    for line in lines:
        users.append(line.rstrip('\n'))

    f.close()

    newUserInfo = c1.recv(1024)
    newUserInfo = newUserInfo.decode()

    #Check if username already exist
    newUsername = ParseNewUsername(newUserInfo)
    allUsernames = GetAllUsersnames(users)
    if newUsername in allUsernames:
        return b'existing'
    else:
        file = open('logins.txt', 'a+')
        file.write(newUserInfo)
        file.close()
        return b'newUserCreated'

    

def RecivePicture ():
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
        
def ReciveTextFile ():
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
#        print("DEBUGG: START OF SERVER")
        serverAction = c2.recv(1024)
#        print("DEBUGG: SERVERACTION RECIVED ")
#        print(serverAction.decode())
    

        if serverAction == b'LOGGIN':
            while True:
                response = LoginFromClient()
            
                if response == b'exit':
                    CloseAllConnections()
                    break
                
                elif response == b'success':
                    c1.send(response)
#                    print("DEBUGG: LOGGIN SUCCESFUL")
                    break

                elif response != b'success':
#                    print("DEUGG: LOGIN FAILED SENDING DATA TO CLIENT FOR HANDLING")
                    c1.send(response)

        elif serverAction == b'REGISTER':
        

            while True:

                response = RegisterNewUser()
           
                if response == b'newUserCreated':
                    c1.send(response)
#                   print("DEBUGG: CREAION OF USER SUCCESS")
                    break

                elif response != b'newUserCreated':
                    print("DEBUGG: CREATION FAILED SENDING DATA TO CLIENT FOR HANDLING")
                    c1.send(response)
                    break

        elif serverAction == b'PICTURE':
            RecivePicture()

        elif serverAction == b'TEXTFILE':
            ReciveTextFile()

        elif serverAction == b'exit':
            CloseAllConnections()
            print ("Connection closed!")
            break

#        else:
#            print("DEBUGG: THIS SHOULD NOT HAPPEN!")
#
#       print("DEBUGG END OF SERVER")
    

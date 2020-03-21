#!/usr/bin/env python3

import unittest
import sys
import socket, time
import random
import string

sys.path.insert(1, '../Client')
import client

sys.path.insert(1, '../Server')
import server


class MyTCPtest(unittest.TestCase):


#Client function tests
    def testLogInExistingUser(self):
        username = "temp"
        password = "admin"
        userData = client.CreateUserData(username, password)

        self.assertEqual(userData, "temp:admin")

    def testRegisterNewUser(self):
        username = "new1"
        password = "new1"
        newUserData = client.CreateNewUserData(username, password)

        self.assertEqual (newUserData, "new1:new1\n")

#Server function tests
    def testParseNewUsername(self):

        newUserData = "test1:test1\n"
        result = server.ParseNewUsername(newUserData)

        self.assertEqual(result, "test1")

    def testgetAllUserNames(self):
        userNames = ["Karl%6:pass1\n", "olof!3:pass2\n", "Bertil&2:pass3\n"]
        allUserNames = server.GetAllUsersnames(userNames)

        expected = ["Karl%6", "olof!3", "Bertil&2"]

        self.assertEqual (allUserNames, expected)

    def testLoginFromClientSuccess(self):

        userData = "test1:admin"
        returnValue = server.LoginFromClient(userData)

        self.assertEqual(returnValue, b'success')

    def testLoginFromClientNotFound(self):

        userData = "should:notExist"
        returnValue = server.LoginFromClient(userData)

        self.assertEqual (returnValue, b'userNotFound')

    def testRegisterNewUserExisting(self):

        userData = "test1:testPassword"
        returnValue = server.RegisterNewUser(userData)

        self.assertEqual (returnValue, b'existing')

    def testRegisterNewUserSucess(self):

        userData = "newUser:newPassword\n"
        returnValue = server.RegisterNewUser(userData)

        self.assertEqual (returnValue, b'newUserCreated')


if(__name__== '__main__'):
    
    unittest.main()






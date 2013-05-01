from persist import shelveWrapper
from key import User
from key import AesEncryption

import unittest
import os

TEST_DB = 'UnitTest.db'

class persistTest(unittest.TestCase):
    
    def setUp(self):
        self.db = shelveWrapper(TEST_DB)
    
    def tearDown(self):
        os.remove(TEST_DB+'.db')
        
        
    def testUserPersistAndRetrie(self):
        
        self.db.writeUser('user1', 'password1', 'firstUser')
        userObj = self.db.retriveUser('user1', 'password1')
        userCheck = User('user1', 'password1', 'firstUser')
        self.assertEquals(userObj.username, 'user1', 'check UserName')
        self.assertEquals(userObj.phrase, 'firstUser', 'check phrase')
        self.assertEquals(userObj.key, userCheck.key, "Check Password")
        
    def testRetriveInvalidUser(self):
        
        self.db.writeUser('user1', 'password1', 'firstUser')
        userObj_WrongUserName = self.db.retriveUser('User12', 'Password1')
        self.assertEquals(userObj_WrongUserName, 'User Data not found', 'check error message')
        userObj_WrongPassword = self.db.retriveUser('User1', 'Password2')
        self.assertEquals(userObj_WrongPassword, 'User Data not found', 'check error message')        
        
    def testPersistExistingUser(self):
        
        SucessMsg =  self.db.writeUser('user1', 'password1', 'firstUser')
        self.assertTrue(SucessMsg.find('User Created Successfully')!=-1, 'Check successMessgae')
        ErrorMsg = self.db.writeUser('user1', 'password1', 'firstUser')
        self.assertEquals(ErrorMsg[0], 'username', 'check ErrorMessgae')
        self.assertEquals(ErrorMsg[1], 'Key Already Exists', 'check ErrorMessgae')
        
    def testPersistAndRetrivePassowordInfo(self):
        
        self.db.writeUser('user1', 'password1', 'firstUser')
        userObj = self.db.retriveUser('user1', 'password1')
        self.db.writeEncrytptionData('user1', 'password1', 'data','passwordData', 'PasswordInfo1')
        aesDataObj = self.db.retriePasswdInfo('user1', 'password1', 'data')
        self.assertEquals(aesDataObj.name, 'data', 'check Name')
        self.assertEquals(aesDataObj.phrase, 'PasswordInfo1', 'check phrase')
        self.assertEquals(aesDataObj.AESDecryptionWrapper(userObj.key,aesDataObj.chiperText), 'passwordData', 'check password')
        
    def testPersistandRetriveDupePasswordInfo(self):
        self.db.writeUser('user1', 'password1', 'firstUser')
        SuccessMsg = self.db.writeEncrytptionData('user1', 'password1', 'data','passwordData', 'PasswordInfo1')
        self.assertEquals(SuccessMsg, 'Password Info created successfully', 'check success msg')
        ErrorMsg =  self.db.writeEncrytptionData('user1', 'password1', 'data','passwordData', 'PasswordInfo1')
        self.assertEquals(ErrorMsg[0], 'Name', 'check ErrorMessgae')
        self.assertEquals(ErrorMsg[1], 'Key Already Exists', 'check ErrorMessgae')
        
    def testPasswordRetriveWithInvalidData(self):
        self.db.writeUser('user1', 'password1', 'firstUser')
        self.db.writeEncrytptionData('user1', 'password1', 'data','passwordData', 'PasswordInfo1')
        WrongUserName = self.db.retriePasswdInfo('user112', 'password1', 'data')
        self.assertEquals(WrongUserName, 'No data Found', 'Check Message')
        WrongPassword = self.db.retriePasswdInfo('user1', 'password12', 'data')
        self.assertEquals(WrongPassword, 'No data Found', 'Check Message')
        WrongName = self.db.retriePasswdInfo('user12', 'password1', 'data123')
        self.assertEquals(WrongName, 'No data Found', 'Check Message')

        
        


    
    
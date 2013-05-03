from persist import shelveWrapper
from key import User
from key import AESDecryptionWrapper

import unittest
import os

TEST_DB = 'UnitTest.db'

class persistTest(unittest.TestCase):
    
    def setUp(self):
        self.db = shelveWrapper(TEST_DB)
    
    def tearDown(self):
        os.remove(TEST_DB+'.db')
        
        
    def testUserPersistAndRetrie(self):
        
        self.db.writeUser('user1', 'Password1', 'firstUser')
        userObj = self.db.retriveUser('user1', 'Password1')
        userCheck = User('user1', 'Password1', 'firstUser')
        self.assertEquals(userObj.username, 'user1', 'check UserName')
        self.assertEquals(userObj.phrase, 'firstUser', 'check phrase')
        self.assertEquals(userObj.key, userCheck.key, "Check Password")
        
    def testRetriveInvalidUser(self):
        
        self.db.writeUser('user1', 'Password1', 'firstUser')
        userObj_WrongUserName = self.db.retriveUser('User12', 'Password1')
        self.assertEquals(userObj_WrongUserName, 'User Data not found', 'check error message')
        userObj_WrongPassword = self.db.retriveUser('user1', 'password1')
        self.assertEquals(userObj_WrongPassword, 'User Data not found', 'check error message')        
        
    def testPersistExistingUser(self):
        
        SucessMsg =  self.db.writeUser('user1', 'Password1', 'firstUser')
        self.assertTrue(SucessMsg.find('User Created Successfully')!=-1, 'Check successMessgae')
        ErrorMsg = self.db.writeUser('user1', 'Password1', 'firstUser')
        self.assertEquals(ErrorMsg, "{'username': Key Already Exists}", 'check ErrorMessgae')
        
    def testPersistAndRetrivePassowordInfo(self):
        
        self.db.writeUser('user1', 'Password1', 'firstUser')
        userObj = self.db.retriveUser('user1', 'Password1')
        self.db.writeEncrytptionData('user1', 'Password1', 'data','passwordData', 'PasswordInfo1')
        aesDataObj = self.db.retriePasswdInfo('user1', 'Password1', 'data')
        self.assertEquals(aesDataObj.name, 'data', 'check Name')
        self.assertEquals(aesDataObj.phrase, 'PasswordInfo1', 'check phrase')
        self.assertEquals(AESDecryptionWrapper(userObj.key,aesDataObj.chiperText), 'passwordData', 'check password')
        
    def testPersistandRetriveDupePasswordInfo(self):
        self.db.writeUser('user1', 'Password1', 'firstUser')
        SuccessMsg = self.db.writeEncrytptionData('user1', 'Password1', 'data','passwordData', 'PasswordInfo1')
        self.assertEquals(SuccessMsg, 'Password Info created successfully', 'check success msg')
        ErrorMsg =  self.db.writeEncrytptionData('user1', 'Password1', 'data','passwordData', 'PasswordInfo1')
        self.assertEquals(ErrorMsg, "{'Name': Key Already Exists}", 'check ErrorMessgae')
      
    def testPasswordRetriveWithInvalidData(self):
        self.db.writeUser('user1', 'Password1', 'firstUser')
        self.db.writeEncrytptionData('user1', 'Password1', 'data','passwordData', 'PasswordInfo1')
        WrongUserName = self.db.retriePasswdInfo('user112', 'Password1', 'data')
        self.assertEquals(WrongUserName, 'No data Found', 'Check Message')
        WrongPassword = self.db.retriePasswdInfo('user1', 'Password12', 'data')
        self.assertEquals(WrongPassword, 'No data Found', 'Check Message')
        WrongName = self.db.retriePasswdInfo('user12', 'Password1', 'data123')
        self.assertEquals(WrongName, 'No data Found', 'Check Message')
          
    def testUserValidationUserName(self):
        msg1 = self.db.writeUser('use', 'Password1', 'None')
        self.assertEqual(msg1, "{'username': ' must be between 4 an 50 chars'}")
        msg2 = self.db.writeUser('userauserauserauserauserauserauserauserauserausera12', 'Password1', 'None')
        self.assertEqual(msg2, "{'username': ' must be between 4 an 50 chars'}")
        msg3 = self.db.writeUser('User 1', 'Password1', 'None')
        self.assertEqual(msg3, "{'username': ' can only contain alphabets and digits'}")
        msg4= self.db.writeUser('User@13R', 'Password1', 'None')
        self.assertEqual(msg4, "{'username': ' can only contain alphabets and digits'}")
        msg5= self.db.writeUser('Valid12User43', 'Password1', 'None')
        self.assertEqual(msg5, "User Created Successfully")
        
    def testUserValidationPhrase(self):
        msg1 = self.db.writeUser('user', 'Password1', 'Noe')
        self.assertEqual(msg1, "{'phrase': ' must be between 4 and 100 chars'}")
        msg2 = self.db.writeUser('user', 'Password1', 'NoneNone  NoneNone  NoneNone  NoneNone  NoneNone  NoneNone  NoneNone  NoneNone  NoneNone  NoneNone  NoneNone  NoneNone  ')
        self.assertEqual(msg2, "{'phrase': ' must be between 4 and 100 chars'}")
        msg3 = self.db.writeUser('User1', 'Password1', 'None !')
        self.assertEqual(msg3, "{'phrase': ' can only contain alphabets and digits(white space allowed'}")
        msg4= self.db.writeUser('Valid12User43', 'Password1', 'This is a valid phrase')
        self.assertEqual(msg4, "User Created Successfully")

    #TODO - userValidation- password
    # PasswordChecker
    #PasswordInfo validation
        
        


    
    
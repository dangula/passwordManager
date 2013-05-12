from persist import shelveWrapper
from search import doSearch

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
        self.db.writeEncrytptionData('user1', 'Password1', 'nameone', 'thisisaTest', 'none')
        self.db.writeEncrytptionData('user1', 'Password1', 'nametwo', 'thisisaTest', 'aaaa')
        self.db.writeEncrytptionData('user1', 'Password1', 'namethree', 'thisisaTest', 'aaabbaaa')
        self.db.writeEncrytptionData('user1', 'Password1', 'onename', 'thisisaTest', 'none')
        self.db.writeEncrytptionData('user1', 'Password1', 'twoname', 'thisisaTest', 'abcabc')
        self.db.writeEncrytptionData('user1', 'Password1', 'threeName', 'thisisaTest', 'hhhhh')
        self.db.writeEncrytptionData('user1', 'Password1', 'nameo1ne', 'thisisaTest', 'abcabc')
        self.db.writeEncrytptionData('user1', 'Password1', 'nameoneone', 'thisisaTest', 'none')
        self.db.writeEncrytptionData('user1', 'Password1', 'mame2two', 'thisisaTest', 'none')
        self.db.writeEncrytptionData('user1', 'Password1', 'namet3ee', 'thisisaTest', 'none')

        resultList1 = doSearch(TEST_DB, 'user1', 'Password1','name', 'one')
        self.assertEquals(len(resultList1), 3)
        resultList2 = doSearch(TEST_DB, 'user1', 'Password1','name', 'two')
        self.assertEquals(len(resultList2), 3)   
        resultList3 = doSearch(TEST_DB, 'user1', 'Password1','name', 'three')
        self.assertEquals(len(resultList3), 2)
        resultList4 = doSearch(TEST_DB, 'user1', 'Password1','name', 'fake')
        self.assertEquals(len(resultList4), 0) 
        resultList5 = doSearch(TEST_DB, 'user1', 'Password1','phrase', 'none')
        self.assertEquals(len(resultList5), 5)
        resultList6 = doSearch(TEST_DB, 'user1', 'Password1','phrase', 'aaa')
        self.assertEquals(len(resultList6), 2)   
        resultList7 = doSearch(TEST_DB, 'user1', 'Password1','phrase', 'hhh')
        self.assertEquals(len(resultList7), 1)        
        resultList8 = doSearch(TEST_DB, 'user1', 'Password1','phrase', 'fake')
        self.assertEquals(len(resultList8), 0)
        
        
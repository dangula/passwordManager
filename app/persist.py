import shelve

from key import User
from key import AesEncryption
from Crypto.Hash import SHA256




shelf_db = 'test_db.db'

class shelveWrapper(object):
    def __init__(self,shelveDB):
        #self.shelveDB = open(shelveDB,'w')
        self.shelveDB = shelveDB

    def checkhashPasswd(self,password):  
            iterations = 154769
            salt = "A1CD3r5FtG8K0980"
            key = ''
           
            for i in xrange(iterations):
                shash = SHA256.new()
                shash.update(key+password+salt)
                key=shash.digest()
                i
            
            return key
    
    
    def writeUser(self,userName,Password,Phrase):
        s = shelve.open(self.shelveDB)
        try:
            kList = s.keys()
            if userName in kList :
                raise ValueExistsError
            else :
                s[userName] = User(userName,Password,Phrase)
                return 'User Created Successfully'
        
        except ValueExistsError,e :
            return 'username',e.value
        finally:
            s.close()
            
    
    def retriveUser(self,userName,password):
        s = shelve.open(self.shelveDB, 'r')
        try:
            data = s[userName]
            if data.key == self.checkhashPasswd(str(password)):
                return data
            else :
                raise KeyError
            
        except KeyError:
            return "User Data not found"
        finally:
            s.close()
        
    
    def writeEncrytptionData(self,userName,password,Name,PlainText,Phrase):
        s = shelve.open(self.shelveDB)
        try:
            user  = self.retriveUser(userName, password)
            kList = s.keys()
            if Name in kList :
                raise ValueExistsError
        
            else :
                data = AesEncryption(user.username,user.key,Name,PlainText,Phrase)
                s[Name] = data
                return 'Password Info created successfully'
            
        except KeyError:
            return " No user found for username password combination"
        except ValueExistsError,e :
            return 'Name',e.value
        
        s.close()
        
    def retriePasswdInfo(self,UserName,Passwd,Name):
        s = shelve.open(self.shelveDB, 'r')
        try:
            data = s[UserName]
            
            if data.key == self.checkhashPasswd(str(Passwd)):
                passInfo = s[Name]
                return passInfo
            else :
                raise KeyError
            
        except KeyError:
            return "No data Found"
        
        s.close()
        
class ValueExistsError(Exception):
    def __init__(self):
        self.value = 'Key Already Exists'
    def __str__(self):
        return repr(self.value)
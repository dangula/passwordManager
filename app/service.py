from flask import Flask
from flask import request
from key import User
from key import AesEncryption
from key import AESDecryptionWrapper
from persist import shelveWrapper

import json

app = Flask(__name__)
STORE_DB = 'passwordStore.db'


@app.route('/',methods = ['GET'])
def test():
    data = { 'a':'A', 'b':(2, 4), 'c':3.0 } 
    print request.data
    data_string = json.dumps(data)
    return data_string

@app.route('/addUser' ,methods = ['POST'])
def addNewUser():
    try :
        data = json.dumps(request.data) 
        data_str = json.loads(data)
        UserDict = eval(data_str)
        if len(UserDict)==2 or len(UserDict)==3:
            db =  shelveWrapper(STORE_DB)
            reqKeys = UserDict.keys()
            if len(reqKeys) == 2:
                if 'password' in reqKeys and 'username' in reqKeys :
                    msg = db.writeUser(UserDict['username'], UserDict['password'], 'None')
                else :
                    raise Exception
            if len(reqKeys)==3:
                if 'password' in reqKeys and 'username' in reqKeys  and 'phrase' in reqKeys:
                    msg = db.writeUser(UserDict['username'], UserDict['password'], UserDict['phrase'])
                else:
                    raise Exception
            if msg == 'User Created Successfully':
                ret_data = {'msg' : msg}
                return json.dumps(ret_data),200
            else :
                ret_data = {'error' : msg }
                return json.dumps(ret_data),400
        else:
            raise Exception
        
    except Exception,e:
        print e
        data_string = {'Error':'Invalid data'}
        return json.dumps(data_string),400

@app.route('/getUser/<user_name>/<password>',methods = ['GET'])
def getUser(user_name,password):
    db =  shelveWrapper(STORE_DB)
    user = db.retriveUser(user_name, password)
    if isinstance(user, User):
        return_data = {'result': 'found','phrase':user.phrase}
        return json.dumps(return_data),200
    else :
        return_data = {'result' : 'Not Found','msg' : user}
        return json.dumps(return_data),404
    
@app.route('/addpassword/<user_name>/<password>',methods = ['POST'])
def addPasswordInfo(user_name,password):
    try :
        db =  shelveWrapper(STORE_DB)
        user = db.retriveUser(user_name, password)
        if isinstance(user, User):
            data = json.dumps(request.data) 
            data_str = json.loads(data)
            UserDict = eval(data_str)
            if len(UserDict)==2 or len(UserDict)==3:
                db =  shelveWrapper(STORE_DB)
                reqKeys = UserDict.keys()
                if len(reqKeys) == 2:
                    if 'name' in reqKeys and 'password' in reqKeys :
                        print UserDict
                        print user_name
                        print user.key
                        msg = db.writeEncrytptionData(user_name, password, UserDict['name'], UserDict['password'], 'None')
                    else :
                        raise Exception
                if len(reqKeys)==3:
                    if 'name' in reqKeys and 'password' in reqKeys  and 'phrase' in reqKeys:
                        msg = db.writeEncrytptionData(user_name, password, UserDict['name'], UserDict['password'], UserDict['phrase'])
                    else:
                        raise Exception
                if msg == 'Password Info created successfully':
                    ret_data = {'msg' : msg}
                    return json.dumps(ret_data),200
                else :
                    ret_data = {'error' : msg }
                    return json.dumps(ret_data),400
            else:
                raise Exception
        else :
            return_data = {'Error' : {'msg' : 'Invalid User info passed'}}
            return json.dumps(return_data),404
            
    except Exception,e:
            print e
            data_string = {'Error':'Invalid data'}
            return json.dumps(data_string),400

@app.route('/getPasswordInfo/<user_name>/<password>/<name>',methods = {'GET'})
def getPasswordInfo(user_name,password,name):
    db =  shelveWrapper(STORE_DB)
    user = db.retriveUser(user_name, password)
    if isinstance(user, User):
        passwordInfo = db.retriePasswdInfo(user_name, password, name)
        if isinstance(passwordInfo, AesEncryption):
            return_data = {'result': 'found','phrase':passwordInfo.phrase,'name':passwordInfo.name,'password':AESDecryptionWrapper(user.key,passwordInfo.chiperText)}
            return json.dumps(return_data),200
        else :
            return_data = {'result' : 'Not Found','msg' : 'No password found with key'+name}
            return json.dumps(return_data),404
    else :
        return_data = {'Error' : {'msg' : 'Invalid User info passed'}}
        return json.dumps(return_data),404
    
    

if __name__ == '__main__':
    app.run(debug=True)
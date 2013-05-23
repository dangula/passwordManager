Password Manager
===============

Project for Python cert class

### Description
    passwordManager is a web service uses to manager passwords. You can create users, with is a username/password combination
    with optionl phrase.Userames are unique. Once user is created,you can add passwords associated with the user. the password contain a unique name
    password and optional phrase. passwrords are encrypted and stored.
    
## prerequisites
* pycrypto
* flask

## How to run
  Password Manager is a REST API running as a Flask app. To run Check out the code, make sure prerequisites are installed.
Then start the service.py file as flask app or deploy service.py(with supporting files) to a service like apache or nginix

## REST API
###### Following REST calls can be made to password Manager app
##### 1. Check service Up - GET /
 
 Example             | http://localhost:5000/  |
 --- | --- |
 Exected result      | '200 OK if service up   |
 Expected Result JSON|```{'status': 'Service Up'}```|
 

##### 2. Add new User - POST /addUser
 Expected JSON of following format in the body of request
 ```json
  {'username' : 'someUserName',
   'password' : 'Some_Password',
   'phrase'   : 'some optional phrase'
   }
 
 ```
 Example        | http://localhost:5000/addUser (with User json in body)  |
 --- | --- |
 Exected result | 200 OK if user is created successfully   |
 |400 Bad Request with matching Error message if user is not created successfully |

  Following are the rules for new user to be added/created.
  
  1. UserName must be unique, if a userName already exists then 400 Bad Request is returned
       with Error message ``` {'username' : 'Key already exists'}```      
  2. The json send in the requst must be valid and must pass user validation
     * user josn must have atlest username and password, if not 400 Bad Requst is returned
       with error message ``` {'error': 'Invalid Data'}```
  3. Following are user validation rules
    1. userName validation
       * userName length must be between 4 and 50 chars
       * userName must be alpha numberic only
       * If username validation fails, 400 Bad Request is retruned with appropriate error
         eg : ```{'error': {'username': ' can only contain alphabets and digits'}} ```
    2. password validation
       * password length must be between 8 and 50 chars
       * password must be alpha numeric with special chars _ ,@ , #, $ and * allowed
       * for a password to be valid it must have 3 for the following 4
         * a uppercase letter
         * a lowercase letter
         * a number
         * atlest one of the allowed special char
       * If password validation fails, 400 Bad Request is returned with appropriate error
         eg : ```{'error': {'password': ' must be between 8 an 50 chars'}}```
    3. phrase validation
       * phrase length must be between 4 and 100 chars
       * phrase  must be alpha numberic only
       * If phrase validation fails, 400 Bad Request is retruned with appropriate error
         eg : ```{'error': {'phrase': ' must be between 4 an 100 chars'}} ```

##### 3. Retrive user - GET /getUser/\<user_name\>/\<password\>


Example        | http://localhost:5000/getUser/user1/Password1  |
 --- | --- |
 Exected result | 200 OK - if user exists name and password from URL |
 |404 Not Found - if user doesnt exist|
 1. For a 200 OK response the user JSON is retrned in body of resposne
    the user json contains the Phrase stored on user, username and password is not returned.
    eg : ``` JSON
            {'result': 'found',
              'phrase' : 'User1 info'}```
 2. 404 Not found is returned if there is no user with the Username in the URL, or 
    The user exists but password is incorrect. appropritae message is retrned too.
    eg.```{'result': 'Not found','msg' : 'User data not found'} ```


##### 4. Add passwordInfo - POST /addPassword/\<user_name\>/\<password\>
Expected JSON of following format in the body of request
 ```json
  {'name' : 'passwordName1',
   'password' : 'some password',
   'phrase'   : 'shome phrase 1'
   }
 
 ```
 Example        | http://localhost:5000/addPassword/User1/Password1 (with password json in body)  |
 --- | --- |
 Exected result | 200 OK if password is created successfully   |
 |400 Bad Request with matching Error message if password is not created successfully |
 
 Following are the rules for new password to be added/created.
  
  1. password name name must be unique, if a name  already exists then 400 Bad Request is returned
       with Error message ``` {'name ' : 'Key already exists'}```  
  2. There must be an existing user with matchign userName and password from URL. If there is no user
     with username or password in URL is incorrect then 400 Bad Request is returned with Error 
     messgae ```{'error' : 'No user found for usernamepassword combination'} ```
  3. The json send in the requst must be valid and must pass password validation
     * passwordInfo josn must have atlest name  and password, if not 400 Bad Requst is returned
       with error message ``` {'error': 'Invalid Data'}```


##### 5. Retrive passwordInfo - GET /getPasswordInfo/\<user_name\>/\<password\>/\<name\>

Example        | TODO  |
 --- | --- |
 Exected result | TODO   |
TODO - Additional Info

##### 6. searh passwrodInfo - GET /searchPasswordInfo/\<user_name\>/\<password\>/\<name\>/\<search\>

Example        | TODO  |
 --- | --- |
 Exected result | TODO   |
TODO - Additional Info

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
 Expected JSON for following format
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

 For a user to be created/added successfully if following rules are qualified
    1. UserName must be unique, if a userName already exists then 400 Bad Request is returned
       with Error message ``` {'username' : 'Key already exists'}```
    2. The json send in the requst must be valid and must pass user validation
        * user josn must have atlest username and password, if not 400 Bad Requst is returned
          with error message ``` {'error': 'Invalid Data'}```
    TODO - add more

##### 3. Retrive user - GET /getUser/\<user_name\>/\<password\>


Example        | TODO  |
 --- | --- |
 Exected result | TODO   |
TODO - Additional Info

##### 4. Add passwordInfo - POST /addpassword/\<user_name\>/\<password\>


|Example        | TODO  |
 --- | --- |
 Exected result | TODO   |
TODO - Additional Info

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

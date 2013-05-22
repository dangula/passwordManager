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
 Expected Result JSON|{'status': 'Service Up'}'|
 

##### 2. Add new User - POST /addUser

 Example        | TODO  |
 --- | --- |
 Exected result | TODO   |
TODO - Additional Info

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

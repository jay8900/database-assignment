##Prerequisits/SetUp:

####1.Download the mysql as per your OS requirements.
####2.create user "root" and set password "root@123456".
####3.login using given credentials using command prompt/terminal create database "family_details" 
create database family_details;
####4.for sql connector, required credentials: host,user,password,database
####3.pip install mysql-connector-python (for python 3 above)

##Run:
####1.First run,for creating the family_details table and insert the deatils
python mysql_database.py 
####2.After that run,following for desired output.
python script.py


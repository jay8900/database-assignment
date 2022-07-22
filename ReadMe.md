##Prerequisits/SetUp:


Take amazon linux server2 


yum update -y 


yum install python* -y 


####1.Download the mysql as per your OS requirements.
     
     
     a. Install mysql8 https://techviewleo.com/how-to-install-mysql-8-on-amazon-linux-2/
      
      
      b. Setup root password and verify 



####2.create user "root" and set password "Jay@123456".



####3.login using given credentials using command prompt/terminal create database "family_details" 
       a. create database family_details;



####4.for sql connector, required credentials: host,user,password,database



####3.pip install mysql-connector-python (for python 3 above)

##Run:


####1.First run,for creating the family_details table and insert the deatils
   
   
   a. python mysql_database.py 


####2.After that run,following for desired output.
     
     b. python script.py
     
     
     
     
     <img width="1792" alt="image" src="https://user-images.githubusercontent.com/90141704/180395430-b86a2c77-cc5e-4eff-b194-c34c7522e85c.png">



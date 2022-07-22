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
     
     
     




==========================================================================
************************DESIRED OUTPUT************************************
==========================================================================
final desired output [('Mathew', 'Neale', 18), ('Jackson', 'Owen', 18), ('Victor', 'Castle', 19), ('Benjamin', 'Hurst', 19), ('Leigh', 'Nicholson', 19), ('Tobias', 'Stott', 19), ('Aidan', 'Tomlinson', 19), ('Mohamed', 'Dodd', 20), ('George', 'Peel', 20), ('Joseph', 'Adams', 21), ('Bradley', 'Davenport', 21), ('Reggie', 'Eaton', 21), ('Bruce', 'Hickman', 21), ('Rory', 'Houghton', 21), ('Muhammad', 'Metcalfe', 21), ('Neil', 'Pritchard', 22), ('Abdul', 'Cotton', 23), ('Joey', 'Jeffery', 23), ('Gordon', 'Burrows', 24), ('Geoffrey', 'Pollard', 24), ('Jack', 'Watkins', 24), ('Paul', 'Bainbridge', 25), ('Brian', 'Callaghan', 25), ('Sam', 'Hanson', 25), ('Raymond', 'King', 25), ('Sebastian', 'McGowan', 25), ('Gordon', 'Thomas', 25), ('Jeffrey', 'Cairns', 26), ('Christopher', 'Coe', 26), ('Kieron', 'Johnson', 26), ('Rowan', 'Ryder', 26), ('Jordan', 'Craig', 27), ('Archibald', 'Daniel', 27), ('Hector', 'Frost', 27), ('Alexander', 'Gibson', 27), ('Frankie', 'Wall', 27), ('Evan', 'Booth', 28), ('Ross', 'Humphries', 28), ('Frank', 'Meredith', 28), ('Tyler', 'Parry', 28), ('Roman', 'Ritchie', 28), ('Theodore', 'Barratt', 29), ('Louis', 'Barratt', 29), ('Harvey', 'Leigh', 29), ('Harry', 'Morris', 29), ('Sidney', 'Clay', 30), ('Alfie', 'Hubbard', 30), ('Frederick', 'Rowe', 30), ('Martin', 'Bateman', 31), ('Dominic', 'Beard', 31), ('Nicholas', 'Franklin', 31), ('Ralph', 'Hancock', 31), ('Adrian', 'Hogan', 31), ('Julian', 'Newman', 31), ('Louis', 'Park', 31), ('Thomas', 'Roberts', 31), ('Jayden', 'Carey', 32), ('John', 'Allen', 33), ('Harold', 'Moran', 33), ('Andrew', 'Norris', 33), ('Finn', 'Nuttall', 33), ('Ollie', 'Bayliss', 34), ('Sydney', 'Blackburn', 34), ('Bryan', 'Clay', 34), ('Blake', 'Craig', 34), ('Colin', 'King', 34), ('Mathew', 'Goldsmith', 35), ('Oakley', 'Hyde', 35), ('Mohammed', 'Peacock', 35), ('Gareth', 'Pritchard', 35), ('Grayson', 'Newell', 36), ('William', 'Castle', 37), ('Ben', 'Rushton', 37), ('Francis', 'Ellis', 38), ('Ross', 'Guest', 38), ('Leon', 'Knowles', 38), ('Michael', 'Marshall', 38), ('Barrie', 'Rutter', 38), ('Ian', 'Bush', 40), ('Taylor', 'McKenna', 40), ('Bruce', 'McMillan', 40), ('James', 'ONeill', 40), ('Mathew', 'Snell', 40), ('Ronald', 'Batchelor', 41), ('Duncan', 'Butler', 41), ('Luca', 'Cairns', 41), ('Noel', 'Fletcher', 41), ('Ollie', 'Greaves', 41), ('Glen', 'Gibson', 42), ('Lawrence', 'Hancock', 42), ('Declan', 'Islam', 42), ('Hubert', 'Stanley', 42), ('Ashley', 'Whittle', 42), ('Jenson', 'Batchelor', 43), ('Toby', 'Bradford', 43), ('Hudson', 'Sharpe', 43), ('Maurice', 'Spence', 43), ('Macauley', 'Cassidy', 44), ('Adrian', 'Holloway', 44)]
MySQL connection is closed

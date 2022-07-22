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
     
     
     






Total number of rows in table:  100

Printing each row
FIRST_NAME =  Mathew
LAST_NAME =  Snell
AGE  =  40
FIRST_NAME =  William
LAST_NAME =  Castle
AGE  =  37
FIRST_NAME =  Hudson
LAST_NAME =  Sharpe
AGE  =  43
FIRST_NAME =  George
LAST_NAME =  Peel
AGE  =  20
FIRST_NAME =  Bryan
LAST_NAME =  Clay
AGE  =  34
FIRST_NAME =  Oakley
LAST_NAME =  Hyde
AGE  =  35
FIRST_NAME =  Jackson
LAST_NAME =  Owen
AGE  =  18
FIRST_NAME =  Kieron
LAST_NAME =  Johnson
AGE  =  26
FIRST_NAME =  Alfie
LAST_NAME =  Hubbard
AGE  =  30
FIRST_NAME =  Andrew
LAST_NAME =  Norris
AGE  =  33
FIRST_NAME =  Brian
LAST_NAME =  Callaghan
AGE  =  25
FIRST_NAME =  Roman
LAST_NAME =  Ritchie
AGE  =  28
FIRST_NAME =  Jenson
LAST_NAME =  Batchelor
AGE  =  43
FIRST_NAME =  Maurice
LAST_NAME =  Spence
AGE  =  43
FIRST_NAME =  Harry
LAST_NAME =  Morris
AGE  =  29
FIRST_NAME =  Gordon
LAST_NAME =  Thomas
AGE  =  25
FIRST_NAME =  Sebastian
LAST_NAME =  McGowan
AGE  =  25
FIRST_NAME =  Benjamin
LAST_NAME =  Hurst
AGE  =  19
FIRST_NAME =  Duncan
LAST_NAME =  Butler
AGE  =  41
FIRST_NAME =  Louis
LAST_NAME =  Park
AGE  =  31
FIRST_NAME =  Lawrence
LAST_NAME =  Hancock
AGE  =  42
FIRST_NAME =  Archibald
LAST_NAME =  Daniel
AGE  =  27
FIRST_NAME =  Joey
LAST_NAME =  Jeffery
AGE  =  23
FIRST_NAME =  Luca
LAST_NAME =  Cairns
AGE  =  41
FIRST_NAME =  Glen
LAST_NAME =  Gibson
AGE  =  42
FIRST_NAME =  Bradley
LAST_NAME =  Davenport
AGE  =  21
FIRST_NAME =  Francis
LAST_NAME =  Ellis
AGE  =  38
FIRST_NAME =  Mathew
LAST_NAME =  Goldsmith
AGE  =  35
FIRST_NAME =  Harold
LAST_NAME =  Moran
AGE  =  33
FIRST_NAME =  Alexander
LAST_NAME =  Gibson
AGE  =  27
FIRST_NAME =  Ross
LAST_NAME =  Humphries
AGE  =  28
FIRST_NAME =  Mathew
LAST_NAME =  Neale
AGE  =  18
FIRST_NAME =  Abdul
LAST_NAME =  Cotton
AGE  =  23
FIRST_NAME =  Bruce
LAST_NAME =  McMillan
AGE  =  40
FIRST_NAME =  Blake
LAST_NAME =  Craig
AGE  =  34
FIRST_NAME =  Joseph
LAST_NAME =  Adams
AGE  =  21
FIRST_NAME =  Bruce
LAST_NAME =  Hickman
AGE  =  21
FIRST_NAME =  Rowan
LAST_NAME =  Ryder
AGE  =  26
FIRST_NAME =  Nicholas
LAST_NAME =  Franklin
AGE  =  31
FIRST_NAME =  Frankie
LAST_NAME =  Wall
AGE  =  27
FIRST_NAME =  Muhammad
LAST_NAME =  Metcalfe
AGE  =  21
FIRST_NAME =  Victor
LAST_NAME =  Castle
AGE  =  19
FIRST_NAME =  Finn
LAST_NAME =  Nuttall
AGE  =  33
FIRST_NAME =  Ollie
LAST_NAME =  Greaves
AGE  =  41
FIRST_NAME =  Hubert
LAST_NAME =  Stanley
AGE  =  42
FIRST_NAME =  Leon
LAST_NAME =  Knowles
AGE  =  38
FIRST_NAME =  Sidney
LAST_NAME =  Clay
AGE  =  30
FIRST_NAME =  Hector
LAST_NAME =  Frost
AGE  =  27
FIRST_NAME =  Leigh
LAST_NAME =  Nicholson
AGE  =  19
FIRST_NAME =  Adrian
LAST_NAME =  Holloway
AGE  =  44
FIRST_NAME =  Aidan
LAST_NAME =  Tomlinson
AGE  =  19
FIRST_NAME =  Paul
LAST_NAME =  Bainbridge
AGE  =  25
FIRST_NAME =  Sam
LAST_NAME =  Hanson
AGE  =  25
FIRST_NAME =  Thomas
LAST_NAME =  Roberts
AGE  =  31
FIRST_NAME =  Taylor
LAST_NAME =  McKenna
AGE  =  40
FIRST_NAME =  Ben
LAST_NAME =  Rushton
AGE  =  37
FIRST_NAME =  Julian
LAST_NAME =  Newman
AGE  =  31
FIRST_NAME =  Evan
LAST_NAME =  Booth
AGE  =  28
FIRST_NAME =  Ian
LAST_NAME =  Bush
AGE  =  40
FIRST_NAME =  Jayden
LAST_NAME =  Carey
AGE  =  32
FIRST_NAME =  Ronald
LAST_NAME =  Batchelor
AGE  =  41
FIRST_NAME =  Mohamed
LAST_NAME =  Dodd
AGE  =  20
FIRST_NAME =  Dominic
LAST_NAME =  Beard
AGE  =  31
FIRST_NAME =  Ralph
LAST_NAME =  Hancock
AGE  =  31
FIRST_NAME =  Frank
LAST_NAME =  Meredith
AGE  =  28
FIRST_NAME =  Theodore
LAST_NAME =  Barratt
AGE  =  29
FIRST_NAME =  Tyler
LAST_NAME =  Parry
AGE  =  28
FIRST_NAME =  James
LAST_NAME =  ONeill
AGE  =  40
FIRST_NAME =  Harvey
LAST_NAME =  Leigh
AGE  =  29
FIRST_NAME =  Adrian
LAST_NAME =  Hogan
AGE  =  31
FIRST_NAME =  Frederick
LAST_NAME =  Rowe
AGE  =  30
FIRST_NAME =  Tobias
LAST_NAME =  Stott
AGE  =  19
FIRST_NAME =  Geoffrey
LAST_NAME =  Pollard
AGE  =  24
FIRST_NAME =  Michael
LAST_NAME =  Marshall
AGE  =  38
FIRST_NAME =  Ollie
LAST_NAME =  Bayliss
AGE  =  34
FIRST_NAME =  Martin
LAST_NAME =  Bateman
AGE  =  31
FIRST_NAME =  Rory
LAST_NAME =  Houghton
AGE  =  21
FIRST_NAME =  Christopher
LAST_NAME =  Coe
AGE  =  26
FIRST_NAME =  Ross
LAST_NAME =  Guest
AGE  =  38
FIRST_NAME =  John
LAST_NAME =  Allen
AGE  =  33
FIRST_NAME =  Gareth
LAST_NAME =  Pritchard
AGE  =  35
FIRST_NAME =  Reggie
LAST_NAME =  Eaton
AGE  =  21
FIRST_NAME =  Ashley
LAST_NAME =  Whittle
AGE  =  42
FIRST_NAME =  Louis
LAST_NAME =  Barratt
AGE  =  29
FIRST_NAME =  Raymond
LAST_NAME =  King
AGE  =  25
FIRST_NAME =  Jordan
LAST_NAME =  Craig
AGE  =  27
FIRST_NAME =  Noel
LAST_NAME =  Fletcher
AGE  =  41
FIRST_NAME =  Colin
LAST_NAME =  King
AGE  =  34
FIRST_NAME =  Mohammed
LAST_NAME =  Peacock
AGE  =  35
FIRST_NAME =  Toby
LAST_NAME =  Bradford
AGE  =  43
FIRST_NAME =  Sydney
LAST_NAME =  Blackburn
AGE  =  34
FIRST_NAME =  Declan
LAST_NAME =  Islam
AGE  =  42
FIRST_NAME =  Jack
LAST_NAME =  Watkins
AGE  =  24
FIRST_NAME =  Macauley
LAST_NAME =  Cassidy
AGE  =  44
FIRST_NAME =  Grayson
LAST_NAME =  Newell
AGE  =  36
FIRST_NAME =  Jeffrey
LAST_NAME =  Cairns
AGE  =  26
FIRST_NAME =  Barrie
LAST_NAME =  Rutter
AGE  =  38
FIRST_NAME =  Gordon
LAST_NAME =  Burrows
AGE  =  24
FIRST_NAME =  Neil
LAST_NAME =  Pritchard
AGE  =  22
FIRST_NAME =  Ivor
LAST_NAME =  Forrest
AGE  =  None

















==========================================================================
************************DESIRED OUTPUT************************************
==========================================================================
final desired output [('Mathew', 'Neale', 18), ('Jackson', 'Owen', 18), ('Victor', 'Castle', 19), ('Benjamin', 'Hurst', 19), ('Leigh', 'Nicholson', 19), ('Tobias', 'Stott', 19), ('Aidan', 'Tomlinson', 19), ('Mohamed', 'Dodd', 20), ('George', 'Peel', 20), ('Joseph', 'Adams', 21), ('Bradley', 'Davenport', 21), ('Reggie', 'Eaton', 21), ('Bruce', 'Hickman', 21), ('Rory', 'Houghton', 21), ('Muhammad', 'Metcalfe', 21), ('Neil', 'Pritchard', 22), ('Abdul', 'Cotton', 23), ('Joey', 'Jeffery', 23), ('Gordon', 'Burrows', 24), ('Geoffrey', 'Pollard', 24), ('Jack', 'Watkins', 24), ('Paul', 'Bainbridge', 25), ('Brian', 'Callaghan', 25), ('Sam', 'Hanson', 25), ('Raymond', 'King', 25), ('Sebastian', 'McGowan', 25), ('Gordon', 'Thomas', 25), ('Jeffrey', 'Cairns', 26), ('Christopher', 'Coe', 26), ('Kieron', 'Johnson', 26), ('Rowan', 'Ryder', 26), ('Jordan', 'Craig', 27), ('Archibald', 'Daniel', 27), ('Hector', 'Frost', 27), ('Alexander', 'Gibson', 27), ('Frankie', 'Wall', 27), ('Evan', 'Booth', 28), ('Ross', 'Humphries', 28), ('Frank', 'Meredith', 28), ('Tyler', 'Parry', 28), ('Roman', 'Ritchie', 28), ('Theodore', 'Barratt', 29), ('Louis', 'Barratt', 29), ('Harvey', 'Leigh', 29), ('Harry', 'Morris', 29), ('Sidney', 'Clay', 30), ('Alfie', 'Hubbard', 30), ('Frederick', 'Rowe', 30), ('Martin', 'Bateman', 31), ('Dominic', 'Beard', 31), ('Nicholas', 'Franklin', 31), ('Ralph', 'Hancock', 31), ('Adrian', 'Hogan', 31), ('Julian', 'Newman', 31), ('Louis', 'Park', 31), ('Thomas', 'Roberts', 31), ('Jayden', 'Carey', 32), ('John', 'Allen', 33), ('Harold', 'Moran', 33), ('Andrew', 'Norris', 33), ('Finn', 'Nuttall', 33), ('Ollie', 'Bayliss', 34), ('Sydney', 'Blackburn', 34), ('Bryan', 'Clay', 34), ('Blake', 'Craig', 34), ('Colin', 'King', 34), ('Mathew', 'Goldsmith', 35), ('Oakley', 'Hyde', 35), ('Mohammed', 'Peacock', 35), ('Gareth', 'Pritchard', 35), ('Grayson', 'Newell', 36), ('William', 'Castle', 37), ('Ben', 'Rushton', 37), ('Francis', 'Ellis', 38), ('Ross', 'Guest', 38), ('Leon', 'Knowles', 38), ('Michael', 'Marshall', 38), ('Barrie', 'Rutter', 38), ('Ian', 'Bush', 40), ('Taylor', 'McKenna', 40), ('Bruce', 'McMillan', 40), ('James', 'ONeill', 40), ('Mathew', 'Snell', 40), ('Ronald', 'Batchelor', 41), ('Duncan', 'Butler', 41), ('Luca', 'Cairns', 41), ('Noel', 'Fletcher', 41), ('Ollie', 'Greaves', 41), ('Glen', 'Gibson', 42), ('Lawrence', 'Hancock', 42), ('Declan', 'Islam', 42), ('Hubert', 'Stanley', 42), ('Ashley', 'Whittle', 42), ('Jenson', 'Batchelor', 43), ('Toby', 'Bradford', 43), ('Hudson', 'Sharpe', 43), ('Maurice', 'Spence', 43), ('Macauley', 'Cassidy', 44), ('Adrian', 'Holloway', 44)]
MySQL connection is closed

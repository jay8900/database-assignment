import mysql.connector

try:
    # establishing the connection
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='Jay@123456',
                                         database='family_details',
                                         auth_plugin='mysql_native_password')

    # Creating a cursor object using the cursor() method
    cursor = connection.cursor()

    # Dropping FAMILY_DETAILS table if already exists.
    cursor.execute("DROP TABLE IF EXISTS FAMILY_DETAILS")

    # Creating table as per requirement
    sql = '''CREATE TABLE FAMILY_DETAILS(
       FIRST_NAME CHAR(20) NOT NULL,
       LAST_NAME CHAR(20),
       AGE INT NULL
    )'''
    cursor.execute(sql)
    print( "FAMILY_DETAILS table created successfully!!")
    # for inserting the values in family_details table
    mySql_insert_query = """INSERT INTO FAMILY_DETAILS(FIRST_NAME, LAST_NAME, AGE) 
                               VALUES 
                               ("Mathew","Snell",40),
    ("William","Castle",37),
    ("Hudson","Sharpe",43),
    ("George","Peel",20),
    ("Bryan","Clay",34),
    ("Oakley","Hyde",35),
    ("Jackson","Owen",18),
    ("Kieron","Johnson",26),
    ("Alfie","Hubbard",30),
    ("Andrew","Norris",33),
    ("Brian","Callaghan",25),
    ("Roman","Ritchie",28),
    ("Jenson","Batchelor",43),
    ("Maurice","Spence",43),
    ("Harry","Morris",29),
    ("Gordon","Thomas",25),
    ("Sebastian","McGowan",25),
    ("Benjamin","Hurst",19),
    ("Duncan","Butler",41),
    ("Louis","Park",31),
    ("Lawrence","Hancock",42),
    ("Archibald","Daniel",27),
    ("Joey","Jeffery",23),
    ("Luca","Cairns",41),
    ("Glen","Gibson",42),
    ("Bradley","Davenport",21),
    ("Francis","Ellis",38),
    ("Mathew","Goldsmith",35),
    ("Harold","Moran",33),
    ("Alexander","Gibson",27),
    ("Ross","Humphries",28),
    ("Mathew","Neale",18),
    ("Abdul","Cotton",23),
    ("Bruce","McMillan",40),
    ("Blake","Craig",34),
    ("Joseph","Adams",21),
    ("Bruce","Hickman",21),
    ("Rowan","Ryder",26),
    ("Nicholas","Franklin",31),
    ("Frankie","Wall",27),
    ("Muhammad","Metcalfe",21),
    ("Victor","Castle",19),
    ("Finn","Nuttall",33),
    ("Ollie","Greaves",41),
    ("Hubert","Stanley",42),
    ("Leon","Knowles",38),
    ("Sidney","Clay",30),
    ("Hector","Frost",27),
    ("Leigh","Nicholson",19),
    ("Adrian","Holloway",44),
    ("Aidan","Tomlinson",19),
    ("Paul","Bainbridge",25),
    ("Sam","Hanson",25),
    ("Thomas","Roberts",31),
    ("Taylor","McKenna",40),
    ("Ben","Rushton",37),
    ("Julian","Newman",31),
    ("Evan","Booth",28),
    ("Ian","Bush",40),
    ("Jayden","Carey",32),
    ("Ronald","Batchelor",41),
    ("Mohamed","Dodd",20),
    ("Dominic","Beard",31),
    ("Ralph","Hancock",31),
    ("Frank","Meredith",28),
    ("Theodore","Barratt",29),
    ("Tyler","Parry",28),
    ("James","ONeill",40),
    ("Harvey","Leigh",29),
    ("Adrian","Hogan",31),
    ("Frederick","Rowe",30),
    ("Tobias","Stott",19),
    ("Geoffrey","Pollard",24),
    ("Michael","Marshall",38),
    ("Ollie","Bayliss",34),
    ("Martin","Bateman",31),
    ("Rory","Houghton",21),
    ("Christopher","Coe",26),
    ("Ross","Guest",38),
    ("John","Allen",33),
    ("Gareth","Pritchard",35),
    ("Reggie","Eaton",21),
    ("Ashley","Whittle",42),
    ("Louis","Barratt",29),
    ("Raymond","King",25),
    ("Jordan","Craig",27),
    ("Noel","Fletcher",41),
    ("Colin","King",34),
    ("Mohammed","Peacock",35),
    ("Toby","Bradford",43),
    ("Sydney","Blackburn",34),
    ("Declan","Islam",42),
    ("Jack","Watkins",24),
    ("Macauley","Cassidy",44),
    ("Grayson","Newell",36),
    ("Jeffrey","Cairns",26),
    ("Barrie","Rutter",38),
    ("Gordon","Burrows",24),
    ("Neil","Pritchard",22),
    ("Ivor","Forrest",null) """

    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into FAMILY_DETAILS table")
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into FAMILY_DETAILS table {}".format(error))

finally:
    if connection.is_connected():
        # Closing the connection
        connection.close()
        print("MySQL connection is closed")

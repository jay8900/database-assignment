import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='Jay@123456',
                                         database='family_details',
                                         auth_plugin='mysql_native_password')

    sql_select_Query = "select * from FAMILY_DETAILS;"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    print("Total number of rows in table: ", cursor.rowcount)

    print("\nPrinting each row")
    for row in records:
        print("FIRST_NAME = ", row[0], )
        print("LAST_NAME = ", row[1])
        print("AGE  = ", row[2])
        # If the age is missing then do not insert that record
        if row[2] is not None:
            continue
        records.remove(row)
    # if the age is the same, please sort by the last name of the matched people.
    records.sort(key=lambda x: x[1])
    # sort by Age
    records.sort(key=lambda x: x[2])
    print("==========================================================================")
    print("************************DESIRED OUTPUT************************************")
    print("==========================================================================")
    print("final desired output", records)
except mysql.connector.Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if connection.is_connected():
        connection.close()
        cursor.close()
        print("MySQL connection is closed")


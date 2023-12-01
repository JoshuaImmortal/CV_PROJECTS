import mysql.connector
import requests
import json

try:
    # http://universities.hipolabs.com/search?country=United+States (end point for get request)
    apidata = requests.get("http://universities.hipolabs.com/search?country=United+States")
    data = apidata.json()
    if(data):
        country = ""
        domain = ""
        alpha = ""
        state = ""
        web = ""
        name =""
        for darts in data:
            country = darts["country"]    
            domain = darts["domains"]
            alpha = darts["alpha_two_code"]
            state = darts["state-province"]
            web = darts["web_pages"]
            name = darts["name"]

    # Creating a sql database to store digested api

    Data = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
    )
    Database = Data.cursor()
    if(Database):
        Database.execute("CREATE DATABASE IF NOT EXISTS `university_db`")
        print("Database created.")
    else:
        print("not connected.")

    # Creating Table in sql database to store digested api

    Tab = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'university_db',
        )
    Table = Tab.cursor()
    if(Table):
        Cable = Table.execute("""
                        CREATE TABLE IF NOT EXISTS `api_data`(
                        `Country` VARCHAR(50),
                        `Domains` VARCHAR(50),
                        `Alpha_two_code` VARCHAR(50),
                        `State_province` VARCHAR(50),
                        `Web_pages` VARCHAR(50),
                        `Name` VARCHAR(50)
                        );
        """)
        print("Table created.")
    else: 
        print("Table not created.")

    # Inserting digested api into the table

    for darts in data:
        insert_query = f"""INSERT INTO `api_data` VALUES(%s, %s, %s, %s, %s, %s);"""
        values = (darts["country"], "".join(darts["domains"]), darts["alpha_two_code"], darts["state-province"], "".join(darts["web_pages"]), darts["name"])    
        Table.execute(insert_query, values)
        Tab.commit()
    print(f"Number of API'S digested is {len(data)}")
except Exception as Error:
    print(Error)
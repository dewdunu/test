from bs4 import BeautifulSoup
import requests
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="sanctions"
)

mycursor = mydb.cursor()
mycursor.execute("DROP TABLE IF EXISTS details")
mycursor.execute("CREATE TABLE details(Name text,Address text,`Sanction Type` text,`Other Name/Logo` text,Nationality text,`Effect Date | Lapse Date` text,Grounds text)")

def list_all_sanctions(source):
    response = requests.get(source)
    soup = BeautifulSoup(response.text, "html.parser")
    container = soup.find(id = "viewcontainer")
    if container is not None:
        table = container.find('table')
        if table is not None:
            all_rows = table.find_all('tr')
            count = 0
            for row in all_rows:
                all_data = row.find_all('td')
                index  = 0
                record = list()
                for td in all_data:
                    index += 1
                    if index == 1:
                        continue
                    record.append(td.text)
                    count += 1
                insert_to_database(record)
                record.clear()
            print(f"{count} records has been scraped")
        else:
            raise Exception("Missing id:viewcontainer in the given source")
            
def insert_to_database(record): 
    try:
        sql = "INSERT INTO details VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = tuple(record)
        mycursor.execute(sql, val)
        mydb.commit()

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))
        
list_all_sanctions('http://lnadbg4.adb.org/oga0009p.nsf/sancALL1P?OpenView&count=999')            
            

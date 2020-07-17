import mysql.connector as mysql

def main(): 
    db = mysql.connect(
    host = "localhost",
    user = "varsha",
    passwd = "var1234",
    database ="testdb"
    )
    
    cursor = db.cursor()
    while (True):
        print("1. Create a record");
        print("2. Read last 10 Records:");
        print("3. Delete a Record by name");
        print("4. Exit the program");
        print("Please Select a option:");
        option= input()
        
        if option=="1":
            create_Record(db, cursor)
            
        elif option =="2":
            read_Record(cursor)
            
        elif option =="3":
            delete_Record(db, cursor)
            
        elif option == "4":
            print("exit the program")
            break
           
        else:
            print("chose correct option")
    
def create_Record(db, cursor):
    print("enter name:")
    new_name= input()
    print("enter value:")
    new_value = input()
    query = "INSERT INTO cars (name, price) VALUES (%s, %s)"
    values = (new_name, new_value)
    cursor.execute(query, values)
    db.commit()
    print("one row inserted")
    
def read_Record(cursor):
    print("Last five record")
    query = "SELECT * FROM cars ORDER BY id DESC LIMIT 5"
    cursor.execute(query)
    records = cursor.fetchall()
    for record in records:
        print(record)
    print("Last five record")
    
def delete_Record(db, cursor):
    print("Delete a record by name")
    print("enter name:")
    new_name= input()
    query = "DELETE FROM cars WHERE name = '%s' " %new_name
    cursor.execute(query)
    db.commit()
    print("record deleted")

if __name__=='__main__':
    main()
    


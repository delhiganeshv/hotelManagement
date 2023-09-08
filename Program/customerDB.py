#import mysql.connector
import sqlite3

class customerDatabase:
    def __init__(self,db):
       # self.con=mysql.connector.connect(host="localhost",user='root',password="Ramana30@")
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS Customer(
            ref text Primary Key,
            name text,
            gender text,
            mobile text,
            email text,
            postcode text,
            nationality text,
            id text,
            idNumber text,
            address text)
        """
        self.cur.execute(sql)
        self.con.commit()

        
    def insert(self,ref,name,gender,mobile,email,postcode,nationality,id,idNumber,address):
        sql = "insert into Customer values (?,?,?,?,?,?,?,?,?,?)"
        self.cur.execute(
            sql, (ref,name,gender,mobile,email,postcode,nationality,id,idNumber,address))
        self.con.commit()

    # fetch all data form db
    def fetch(self):
        self.cur.execute("SELECT * from Customer")
        rows = self.cur.fetchall()
      #  print(rows)
        return rows

    # delete a record
    def remove(self, ref):
        # for tupple if single element put comma after element
        self.cur.execute("delete from Customer where ref=?", (ref,))

    # update a record
    def update(self,ref,name,gender,mobile,email,postcode,nationality,id,idNumber,address):
        sql = "update Customer set name=?, gender=?,mobile=?, email=?, postcode=?, nationality=?,id=?,idNumber=?, address=? where ref=?"
        self.cur.execute(
            sql, (name,gender,mobile,email,postcode,nationality,id,idNumber,address,ref))
        self.con.commit()
        
    # search a record
    
    def search(self, searchVal,searchText):
        sql = "select * from Customer where "+str(searchVal)+" LIKE '%"+str(searchText)+"%'"
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        return rows
    
        
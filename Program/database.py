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
        self.con.commit()

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
    
    def fetchData(self,contact):
        self.cur.execute("SELECT name,gender,email,nationality,address,mobile from Customer where mobile=?",(contact,))
        rows = self.cur.fetchone()
        return rows
    

class roomDatabase:
    def __init__(self,db):
       # self.con=mysql.connector.connect(host="localhost",user='root',password="Ramana30@")
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS Room(
            contact text Primary Key,
            checkIn text,
            checkOut text,
            roomType text,
            RoomAvailable text,
            meal text,
            noOfDays text
            )

        """
        self.cur.execute(sql)
        self.con.commit()
        
        
    def insert(self,contact,checkIn,checkOut,roomType,RoomAvailable,meal,noOfDays,):
        sql = "insert into Room values (?,?,?,?,?,?,?)"
        self.cur.execute(
            sql, (contact,checkIn,checkOut,roomType,RoomAvailable,meal,noOfDays))
        self.con.commit()

    # fetch all data form db
    def fetch(self):
        self.cur.execute("SELECT * from Room")
        rows = self.cur.fetchall()
      #  print(rows)
        return rows

    # delete a record
    def remove(self, contact):
        # for tupple if single element put comma after element
        self.cur.execute("delete from Room where contact=?", (contact,))
        self.con.commit()

    # update a record
    def update(self,contact,checkIn,checkOut,roomType,RoomAvailable,meal,noOfDays):
        sql = "update Room set checkIn=?,checkOut=?,roomType=?, RoomAvailable=?,meal=?, noOfDays=? where contact=?"
        self.cur.execute(
            sql, (checkIn,checkOut,roomType,RoomAvailable,meal,noOfDays,contact))
        self.con.commit()
        
        
    # search a record
    
    def search(self, searchVal,searchText):
        sql = "select * from Room where "+str(searchVal)+" LIKE '%"+str(searchText)+"%'"
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        return rows

    
        
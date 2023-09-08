from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import random
from tkinter import ttk


class RoomBooking:
   
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management system")
        self.root.geometry("970x540+0+0")
      #  self.root.overrideredirect(True)
        
        #variables
        self.contact=StringVar()
        self.check_in=StringVar()
        self.check_out=StringVar()
        self.roomType=StringVar()
        self.availableRoom=StringVar()
        self.meal=StringVar()
        self.NoOfDays=StringVar()
        self.paidTax=StringVar()
        self.subTotal=StringVar()
        self.totalCost=StringVar()
        
        
        
        #Title
        titleLabel=Label(self.root,text="ROOM BOOKING DETAILS",pady=7,font=("times new roman",18,"bold"),bg="black",fg='gold',bd=4,relief=RIDGE)
        titleLabel.place(x=0,y=0,width=970,height=40)
        #titleLabel.grid(row=0,column=1)

        #LOGO
        img1=Image.open("F:\Projects\hotelManagement\Images\logohotel.png")
        img1=img1.resize((100,30),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img1)
        
        img_label=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        img_label.place(x=5,y=2,height=29,width=100)
        
        
        
        
        #labelFrame
        labelFrameLeft=LabelFrame(self.root,bd=2,relief=RIDGE,text='Room Booking Details',font=('arial',12,"bold"),padx=2)
        labelFrameLeft.place(x=5,y=40,width=365,height=465)
        
        #labels and entries
        #customer contact number
        cust_contact_label=Label(labelFrameLeft,text="Customer contact:",font=('times new roman',12,"bold"),padx=2,pady=6)
        cust_contact_label.grid(row=0,column=0,sticky='w')
        
        cust_contact_entry=Entry(labelFrameLeft,state='readonly',textvariable=self.contact,width=25,font=('times new roman',13,"bold"))
        cust_contact_entry.grid(row=0,column=1)
        
        #check in date
        check_inLabel=Label(labelFrameLeft,text="check_in Date:",font=('times new roman',12,"bold"),padx=2,pady=6)
        check_inLabel.grid(row=1,column=0,sticky='w')
        
        check_inEntry=Entry(labelFrameLeft,textvariable=self.check_in,width=25,font=('times new roman',13,"bold"))
        check_inEntry.grid(row=1,column=1)
        
        #check out date
        check_outLabel=Label(labelFrameLeft,text="check_out Date:",font=('times new roman',12,"bold"),padx=2,pady=6)
        check_outLabel.grid(row=2,column=0,sticky='w')
        
        check_outEntry=Entry(labelFrameLeft,textvariable=self.check_out,width=25,font=('times new roman',13,"bold"))
        check_outEntry.grid(row=2,column=1)
        
        
        roomTypelabel=Label(labelFrameLeft,text="Room Type:",font=('times new roman',12,"bold"),padx=2,pady=6)
        roomTypelabel.grid(row=3,column=0,sticky='w')
        
        roomTypeEntry=ttk.Combobox(labelFrameLeft,textvariable=self.roomType,width=23,state="readonly",font=('times new roman',13,"bold"))
        roomTypeEntry["value"]=["Single","Double","Luxury"]
        roomTypeEntry.current(0)  #to set default value
        roomTypeEntry.grid(row=3,column=1)
        
        
        #Available room
        availableRoomLabel=Label(labelFrameLeft,text='Mobile No:',font=('times new roman',12,"bold"),padx=2,pady=6)
        availableRoomLabel.grid(row=4,column=0,sticky='w')
        
        availableRoomEntry=Entry(labelFrameLeft,textvariable=self.availableRoom,width=25,font=('times new roman',13,"bold"))
        availableRoomEntry.grid(row=4,column=1)
        
        #Meal
        meallabel=Label(labelFrameLeft,text="Email Id:",font=('times new roman',12,"bold"),padx=2,pady=6)
        meallabel.grid(row=5,column=0,sticky='w')
    
        mealentry=Entry(labelFrameLeft,textvariable=self.meal,width=25,font=('times new roman',13,"bold"))
        mealentry.grid(row=5,column=1)
        
        #No of days
        NoOfDaysLabel=Label(labelFrameLeft,text="No of Days:",font=('times new roman',12,"bold"),padx=2,pady=6)
        NoOfDaysLabel.grid(row=6,column=0,sticky='w')
        
        NoOfDaysEntry=Entry(labelFrameLeft,textvariable=self.NoOfDays,width=25,font=('times new roman',13,"bold"))
        NoOfDaysEntry.grid(row=6,column=1)
        
        

        #paid tax        
     
        paidTaxLabel=Label(labelFrameLeft,text="Paid Tax:",font=('times new roman',12,"bold"),padx=2,pady=6)
        paidTaxLabel.grid(row=7,column=0,sticky='w')
        
        paidTaxEntry=Entry(labelFrameLeft,textvariable=self.paidTax,width=25,font=('times new roman',13,"bold"))
        paidTaxEntry.grid(row=7,column=1)
        
        #sub Total       
     
        subTotalLabel=Label(labelFrameLeft,text="Paid Tax:",font=('times new roman',12,"bold"),padx=2,pady=6)
        subTotalLabel.grid(row=8,column=0,sticky='w')
        
        subTotalEntry=Entry(labelFrameLeft,textvariable=self.subTotal,width=25,font=('times new roman',13,"bold"))
        subTotalEntry.grid(row=8,column=1)
        
        #Total Cost
        totalCostLabel=Label(labelFrameLeft,text="Total Cost:",font=('times new roman',12,"bold"),padx=2,pady=6)
        totalCostLabel.grid(row=9,column=0,sticky='w')
        
        totalCostEntry=Entry(labelFrameLeft,textvariable=self.totalCost,width=25,font=('times new roman',13,"bold"))
        totalCostEntry.grid(row=9,column=1)
        
if __name__=="__main__":
    root=Tk()
    obj=RoomBooking(root)
    root.mainloop()

    
    
    
    

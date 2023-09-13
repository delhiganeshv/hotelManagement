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
        self.searchVal=StringVar()
        self.searchText=StringVar()
         
        
        
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
        
        cust_contact_entry=Entry(labelFrameLeft,textvariable=self.contact,width=14,font=('times new roman',13,"bold"))
        cust_contact_entry.grid(row=0,column=1,sticky='w')
        
        #fetch data button
        fetch_button=Button(labelFrameLeft,cursor='hand2',text="Fetch Data",width=8,font=('times new roman',12,"bold"),bg='black',fg='gold')
        fetch_button.place(x=272,y=5)
        
        #check in date
        check_inLabel=Label(labelFrameLeft,text="check_in Date:",font=('times new roman',12,"bold"),padx=2,pady=6)
        check_inLabel.grid(row=1,column=0,sticky='w')
        
        check_inEntry=Entry(labelFrameLeft,textvariable=self.check_in,width=23,font=('times new roman',13,"bold"))
        check_inEntry.grid(row=1,column=1,sticky='w')
        
        #check out date
        check_outLabel=Label(labelFrameLeft,text="check_out Date:",font=('times new roman',12,"bold"),padx=2,pady=6)
        check_outLabel.grid(row=2,column=0,sticky='w')
        
        check_outEntry=Entry(labelFrameLeft,textvariable=self.check_out,width=23,font=('times new roman',13,"bold"))
        check_outEntry.grid(row=2,column=1,sticky='w')
        
        
        roomTypelabel=Label(labelFrameLeft,text="Room Type:",font=('times new roman',12,"bold"),padx=2,pady=6)
        roomTypelabel.grid(row=3,column=0,sticky='w')
        
        roomTypeEntry=ttk.Combobox(labelFrameLeft,textvariable=self.roomType,width=21,state="readonly",font=('times new roman',13,"bold"))
        roomTypeEntry["value"]=["Single","Double","Luxury"]
        roomTypeEntry.current(0)  #to set default value
        roomTypeEntry.grid(row=3,column=1,sticky='w')
        
        
        #Available room
        availableRoomLabel=Label(labelFrameLeft,text='Mobile No:',font=('times new roman',12,"bold"),padx=2,pady=6)
        availableRoomLabel.grid(row=4,column=0,sticky='w')
        
        availableRoomEntry=Entry(labelFrameLeft,textvariable=self.availableRoom,width=23,font=('times new roman',13,"bold"))
        availableRoomEntry.grid(row=4,column=1,sticky='w')
        
        #Meal
        meallabel=Label(labelFrameLeft,text="Email Id:",font=('times new roman',12,"bold"),padx=2,pady=6)
        meallabel.grid(row=5,column=0,sticky='w')
    
        mealentry=Entry(labelFrameLeft,textvariable=self.meal,width=23,font=('times new roman',13,"bold"))
        mealentry.grid(row=5,column=1,sticky='w')
        
        #No of days
        NoOfDaysLabel=Label(labelFrameLeft,text="No of Days:",font=('times new roman',12,"bold"),padx=2,pady=6)
        NoOfDaysLabel.grid(row=6,column=0,sticky='w')
        
        NoOfDaysEntry=Entry(labelFrameLeft,textvariable=self.NoOfDays,width=23,font=('times new roman',13,"bold"))
        NoOfDaysEntry.grid(row=6,column=1,sticky='w')
        
        

        #paid tax        
     
        paidTaxLabel=Label(labelFrameLeft,text="Paid Tax:",font=('times new roman',12,"bold"),padx=2,pady=6)
        paidTaxLabel.grid(row=7,column=0,sticky='w')
        
        paidTaxEntry=Entry(labelFrameLeft,textvariable=self.paidTax,width=23,font=('times new roman',13,"bold"))
        paidTaxEntry.grid(row=7,column=1,sticky='w')
        
        #sub Total       
     
        subTotalLabel=Label(labelFrameLeft,text="Paid Tax:",font=('times new roman',12,"bold"),padx=2,pady=6)
        subTotalLabel.grid(row=8,column=0,sticky='w')
        
        subTotalEntry=Entry(labelFrameLeft,textvariable=self.subTotal,width=23,font=('times new roman',13,"bold"))
        subTotalEntry.grid(row=8,column=1,sticky='w')
        
        #Total Cost
        totalCostLabel=Label(labelFrameLeft,text="Total Cost:",font=('times new roman',12,"bold"),padx=2,pady=6)
        totalCostLabel.grid(row=9,column=0,sticky='w')
        
        totalCostEntry=Entry(labelFrameLeft,textvariable=self.totalCost,width=23,font=('times new roman',13,"bold"))
        totalCostEntry.grid(row=9,column=1,sticky='w')
        
        #bill button
        bill_button=Button(labelFrameLeft,cursor='hand2',text="Bill",width=37,font=('times new roman',12,"bold"),bg='black',fg='gold')
        bill_button.grid(row=10,column=0,pady=10,columnspan=2,sticky='w')
        
        #Add,delete,update and reset buttons in a single row
        btn_frame = Frame(labelFrameLeft)
        btn_frame.place(x=0,y=400,width=355,height=40)
       # btn_frame.grid(row=11,columnspan=2)
        
        add_button=Button(btn_frame,cursor='hand2',text="Add",width=8,font=('times new roman',12,"bold"),bg='black',fg='gold')
        add_button.grid(row=0,column=0,padx=2)
        
        update_button=Button(btn_frame,cursor='hand2',text="Update",width=8,font=('times new roman',12,"bold"),bg='black',fg='gold')
        update_button.grid(row=0,column=1,padx=2)
        
        delete_button=Button(btn_frame,cursor='hand2',text="Delete",width=8,font=('times new roman',12,"bold"),bg='black',fg='gold')
        delete_button.grid(row=0,column=2,padx=2)
        
        reset_button=Button(btn_frame,cursor='hand2',text="Reset",width=8,font=('times new roman',12,"bold"),bg='black',fg='gold')
        reset_button.grid(row=0,column=3,padx=2)
      
        #Right side image
        img2=Image.open(r"F:\Projects\hotelManagement\Images\bed.jpg")
        img2=img2.resize((200,200),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        img_label2=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        img_label2.place(x=760,y=45,width=200,height=200)
        
      
      
        #table frame
        
        tableFrame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=('arial',12,'bold'),padx=2)
        tableFrame.place(x=370,y=250,width=597,height=255)
        
        searchLabel=Label(tableFrame,font=('arial',11,'bold'),bg='red',fg='white',text='Search by:')
        searchLabel.grid(row=0,column=0,sticky='w',padx=2)
        
        comboSearch=ttk.Combobox(tableFrame,textvariable=self.searchVal,font=('arial',12,'bold'),width=14,state='readonly')
        comboSearch['value']=('select option','Contact','Room')
        comboSearch.current(0)
        comboSearch.grid(row=0,column=1,padx=2)
        
        textSearch=ttk.Entry(tableFrame,textvariable=self.searchText,font=('arial',12,'bold'),width=20)
        textSearch.grid(row=0,column=2,padx=2)
        
        btnSearch=Button(tableFrame,cursor='hand2',text='Search',font=('arial',11,'bold'),bg='black',fg='gold',width=7)
        btnSearch.grid(row=0,column=4,padx=2)
        
        btnShowAll=Button(tableFrame,cursor='hand2',text='Show All',font=('arial',11,'bold'),bg='black',fg='gold',width=7)
        btnShowAll.grid(row=0,column=5,padx=1)
        
        
        #show data table
        
        detailTable=Frame(tableFrame,bd=2,relief=RIDGE)
        detailTable.place(x=0,y=50,width=595,height=180)
        
        scrollX=ttk.Scrollbar(detailTable,orient=HORIZONTAL)
        scrollY=ttk.Scrollbar(detailTable,orient=VERTICAL)
        
        self.roomDetail=ttk.Treeview(detailTable,column=('contact','roomNumber','checkin','checkout','roomType','roomAvailable','meal','NoOfDays'),xscrollcommand=scrollX.set,yscrollcommand=scrollY.set)       #infor 
        
        scrollX.pack(side=BOTTOM,fill=X)
        scrollY.pack(side=RIGHT,fill=Y)
        
        scrollX.config(command=self.roomDetail.xview)        
        scrollY.config(command=self.roomDetail.yview)
         
         
        self.roomDetail.heading('contact',text='Contact')
        self.roomDetail.heading('roomNumber',text='Room No')
        self.roomDetail.heading('checkin',text='Check In')
        self.roomDetail.heading('checkout',text='Check Out')
        self.roomDetail.heading('roomType',text='Room Type')
        self.roomDetail.heading('roomAvailable',text='Room Available')
        self.roomDetail.heading('meal',text='Meal')
        self.roomDetail.heading('NoOfDays',text='Nationality')
        
        self.roomDetail['show']='headings'
        #self.roomDetail.bind("<ButtonRelease-1>", self.getData)
        self.roomDetail.pack(fill=BOTH,expand=1)
              

        
if __name__=="__main__":
    root=Tk()
    obj=RoomBooking(root)
    root.mainloop()

    
    
    
    

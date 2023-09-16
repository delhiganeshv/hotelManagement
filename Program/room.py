from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import random
from tkinter import ttk
from database import *
from tkcalendar import DateEntry
from datetime import datetime


customerDB=customerDatabase("Customer.db") 
roomDB=roomDatabase("Room.db")


class RoomBooking:
   
  def __init__(self,root):
    self.root=root
    #self.root.title("Hotel Management system")
    self.root.geometry("970x540+0+0")
    self.root.overrideredirect(True)
    
    #variables
    self.contact=StringVar()
    self.check_in=StringVar()
    self.check_out=StringVar()
    self.roomType=StringVar()
    self.availableRoom=StringVar()
    self.availableRoom.set(str(random.randint(1,50)))
    
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
    #titleLabel.grid(row=0,column=1
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
    fetch_button=Button(labelFrameLeft,command=self.fetchContact,cursor='hand2',text="Fetch Data",width=8,font=('times new roman',12,"bold"),bg='black',fg='gold')
    fetch_button.place(x=272,y=5)
    
    #check in date
    check_inLabel=Label(labelFrameLeft,text="check_in Date:",font=('times new roman',12,"bold"),padx=2,pady=6)
    check_inLabel.grid(row=1,column=0,sticky='w')
    
    check_inEntry=DateEntry(labelFrameLeft,selectmode='day',date_pattern='dd/mm/yyyy',state='readonly',textvariable=self.check_in,width=23,font=('times new roman',13,"bold"))
    check_inEntry.grid(row=1,column=1,sticky='w')
    
    #check out date
    check_outLabel=Label(labelFrameLeft,text="check_out Date:",font=('times new roman',12,"bold"),padx=2,pady=6)
    check_outLabel.grid(row=2,column=0,sticky='w')
    
    check_outEntry=DateEntry(labelFrameLeft,selectmode='day',date_pattern='dd/mm/yyyy',state='readonly',textvariable=self.check_out,width=23,font=('times new roman',13,"bold"))
    check_outEntry.grid(row=2,column=1,sticky='w')
    
    
    roomTypelabel=Label(labelFrameLeft,text="Room Type:",font=('times new roman',12,"bold"),padx=2,pady=6)
    roomTypelabel.grid(row=3,column=0,sticky='w')
    
    roomTypeEntry=ttk.Combobox(labelFrameLeft,textvariable=self.roomType,width=21,state="readonly",font=('times new roman',13,"bold"))
    roomTypeEntry["value"]=["Single","Double","Luxury"]
    roomTypeEntry.current(0)  #to set default value
    roomTypeEntry.grid(row=3,column=1,sticky='w')
    
    
    #Available room
    availableRoomLabel=Label(labelFrameLeft,text='Available Room:',font=('times new roman',12,"bold"),padx=2,pady=6)
    availableRoomLabel.grid(row=4,column=0,sticky='w')
    
    availableRoomEntry=Entry(labelFrameLeft,textvariable=self.availableRoom,width=23,font=('times new roman',13,"bold"))
    availableRoomEntry.grid(row=4,column=1,sticky='w')
    
    #Meal
    meallabel=Label(labelFrameLeft,text="Meal:",font=('times new roman',12,"bold"),padx=2,pady=6)
    meallabel.grid(row=5,column=0,sticky='w')
    
    mealEntry=ttk.Combobox(labelFrameLeft,textvariable=self.meal,width=21,state="readonly",font=('times new roman',13,"bold"))
    mealEntry["value"]=["None","Breakfast","Lunch","Dinner"]
    mealEntry.current(0)  #to set default value
    mealEntry.grid(row=5,column=1,sticky='w')

    # mealentry=Entry(labelFrameLeft,textvariable=self.meal,width=23,font=('times new roman',13,"bold"))
    # mealentry.grid(row=5,column=1,sticky='w')
    
    #No of days
    NoOfDaysLabel=Label(labelFrameLeft,text="No of Days:",font=('times new roman',12,"bold"),padx=2,pady=6)
    NoOfDaysLabel.grid(row=6,column=0,sticky='w')
    
    NoOfDaysEntry=Entry(labelFrameLeft,textvariable=self.NoOfDays,width=23,font=('times new roman',13,"bold"))
    NoOfDaysEntry.grid(row=6,column=1,sticky='w')
    
    
    #paid tax        
  
    paidTaxLabel=Label(labelFrameLeft,text="Paid Tax:",font=('times new roman',12,"bold"),padx=2,pady=6)
    paidTaxLabel.grid(row=7,column=0,sticky='w')
    
    paidTaxEntry=Entry(labelFrameLeft,state='readonly',textvariable=self.paidTax,width=23,font=('times new roman',13,"bold"))
    paidTaxEntry.grid(row=7,column=1,sticky='w')
    
    #sub Total       
  
    subTotalLabel=Label(labelFrameLeft,text="Actual Total:",font=('times new roman',12,"bold"),padx=2,pady=6)
    subTotalLabel.grid(row=8,column=0,sticky='w')
    
    subTotalEntry=Entry(labelFrameLeft,state='readonly',textvariable=self.subTotal,width=23,font=('times new roman',13,"bold"))
    subTotalEntry.grid(row=8,column=1,sticky='w')
    
    #Total Cost
    totalCostLabel=Label(labelFrameLeft,text="Total Cost:",font=('times new roman',12,"bold"),padx=2,pady=6)
    totalCostLabel.grid(row=9,column=0,sticky='w')
    
    totalCostEntry=Entry(labelFrameLeft,state='readonly',textvariable=self.totalCost,width=23,font=('times new roman',13,"bold"))
    totalCostEntry.grid(row=9,column=1,sticky='w')
    
    #bill button
    bill_button=Button(labelFrameLeft,command=self.totalBill,cursor='hand2',text="Bill",width=37,font=('times new roman',12,"bold"),bg='black',fg='gold')
    bill_button.grid(row=10,column=0,pady=10,columnspan=2,sticky='w')
    
    #Add,delete,update and reset buttons in a single row
    btn_frame = Frame(labelFrameLeft)
    btn_frame.place(x=0,y=400,width=355,height=40)
    # btn_frame.grid(row=11,columnspan=2)
    
    add_button=Button(btn_frame,command=self.addData,cursor='hand2',text="Add",width=8,font=('times new roman',12,"bold"),bg='black',fg='gold')
    add_button.grid(row=0,column=0,padx=2)
    
    update_button=Button(btn_frame,command=self.updateData,cursor='hand2',text="Update",width=8,font=('times new roman',12,"bold"),bg='black',fg='gold')
    update_button.grid(row=0,column=1,padx=2)
    
    delete_button=Button(btn_frame,command=self.deleteData,cursor='hand2',text="Delete",width=8,font=('times new roman',12,"bold"),bg='black',fg='gold')
    delete_button.grid(row=0,column=2,padx=2)
    
    reset_button=Button(btn_frame,command=self.resetData,cursor='hand2',text="Reset",width=8,font=('times new roman',12,"bold"),bg='black',fg='gold')
    reset_button.grid(row=0,column=3,padx=2)
  
    #Right side image
    img2=Image.open(r"F:\Projects\hotelManagement\Images\bed.jpg")
    img2=img2.resize((300,200),Image.LANCZOS)
    self.photoimg2=ImageTk.PhotoImage(img2)
    
    img_label2=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
    img_label2.place(x=700,y=45,width=265,height=200)
    
  
  
    #table frame
    
    tableFrame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=('arial',12,'bold'),padx=2)
    tableFrame.place(x=370,y=250,width=597,height=255)
    
    searchLabel=Label(tableFrame,font=('arial',11,'bold'),bg='red',fg='white',text='Search by:')
    searchLabel.grid(row=0,column=0,sticky='w',padx=2)
    
    comboSearch=ttk.Combobox(tableFrame,textvariable=self.searchVal,font=('arial',12,'bold'),width=14,state='readonly')
    comboSearch['value']=('select option','contact','RoomAvailable')
    comboSearch.current(0)
    comboSearch.grid(row=0,column=1,padx=2)
    
    textSearch=ttk.Entry(tableFrame,textvariable=self.searchText,font=('arial',12,'bold'),width=20)
    textSearch.grid(row=0,column=2,padx=2)
    
    btnSearch=Button(tableFrame,command=self.SearchRoom,cursor='hand2',text='Search',font=('arial',11,'bold'),bg='black',fg='gold',width=7)
    btnSearch.grid(row=0,column=4,padx=2)
    
    btnShowAll=Button(tableFrame,command=self.displayAll,cursor='hand2',text='Show All',font=('arial',11,'bold'),bg='black',fg='gold',width=7)
    btnShowAll.grid(row=0,column=5,padx=1)
    
    
    #show data table
    
    detailTable=Frame(tableFrame,bd=2,relief=RIDGE)
    detailTable.place(x=0,y=50,width=595,height=180)
    
    scrollX=ttk.Scrollbar(detailTable,orient=HORIZONTAL)
    scrollY=ttk.Scrollbar(detailTable,orient=VERTICAL)
    
    self.roomDetail=ttk.Treeview(detailTable,column=('contact','checkin','checkout','roomType','roomAvailable','meal','NoOfDays'),xscrollcommand=scrollX.set,yscrollcommand=scrollY.set)       #infor 
    
    scrollX.pack(side=BOTTOM,fill=X)
    scrollY.pack(side=RIGHT,fill=Y)
    
    scrollX.config(command=self.roomDetail.xview)        
    scrollY.config(command=self.roomDetail.yview)
     
     
    self.roomDetail.heading('contact',text='Contact')
    self.roomDetail.heading('checkin',text='Check In')
    self.roomDetail.heading('checkout',text='Check Out')
    self.roomDetail.heading('roomType',text='Room Type')
    self.roomDetail.heading('roomAvailable',text='Room Available')
    self.roomDetail.heading('meal',text='Meal')
    self.roomDetail.heading('NoOfDays',text='No Of Days')
    
    self.roomDetail['show']='headings'
    self.roomDetail.bind("<ButtonRelease-1>", self.getData)
    self.roomDetail.pack(fill=BOTH,expand=1)
          
  def fetchContact(self):
    if self.contact.get()=="":
      messagebox.showerror("Error","Please enter the Contact Number",parent=self.root)
    else:
      row=customerDB.fetchData(self.contact.get())

      if row==None:
        messagebox.showerror("Error","This contact number is not found",parent=self.root)
      else:
       # print(row)
        showDataFrame=Frame(self.root,bd=4,relief=RIDGE,padx=2)
        showDataFrame.place(x=375,y=45,width=320,height=200)
        
        lblName=Label(showDataFrame,text="Name          :",font=('arial',12,'bold'),padx=2,pady=4)
        lblName.grid(row=0,column=0,sticky='w')
        
        name=Label(showDataFrame,text=row[0],font=('arial',12,'bold'),padx=2,pady=4)
        name.grid(row=0,column=1,sticky='w')
        
        lblGender=Label(showDataFrame,text="Gender       :",font=('arial',12,'bold'),padx=2,pady=4)
        lblGender.grid(row=1,column=0,sticky='w')
        
        gender=Label(showDataFrame,text=row[1],font=('arial',12,'bold'),padx=2,pady=4)
        gender.grid(row=1,column=1,sticky='w')
        
        lblemail=Label(showDataFrame,text="Email           :",font=('arial',12,'bold'),padx=2,pady=4)
        lblemail.grid(row=2,column=0,sticky='w')
        
        email=Label(showDataFrame,text=row[2],font=('arial',12,'bold'),padx=2,pady=4)
        email.grid(row=2,column=1)
        
        lblNationality=Label(showDataFrame,text="Nationality :",font=('arial',12,'bold'),padx=2,pady=4)
        lblNationality.grid(row=3,column=0,sticky='w')
        
        nationality=Label(showDataFrame,text=row[3],font=('arial',12,'bold'),padx=2,pady=4)
        nationality.grid(row=3,column=1,sticky='w')
        
        lblAddress=Label(showDataFrame,text="Address     :",font=('arial',12,'bold'),padx=2,pady=4)
        lblAddress.grid(row=4,column=0,sticky='w')
        
        address=Label(showDataFrame,text=row[4],font=('arial',12,'bold'),padx=2,pady=4)
        address.grid(row=4,column=1,sticky='w')
        
        lblcontact=Label(showDataFrame,text="Contact     :",font=('arial',12,'bold'),padx=2,pady=4)
        lblcontact.grid(row=5,column=0,sticky='w')
        
        contact=Label(showDataFrame,text=row[5],font=('arial',12,'bold'),padx=2,pady=4)
        contact.grid(row=5,column=1,sticky='w')
        
        
  def addData(self):
     
    if self.contact.get()=="" or self.check_in.get()=="" or self.check_out.get()=="" or self.roomType.get()=="" or self.availableRoom.get()=="" or self.meal.get()=="" or self.NoOfDays.get()=="":
        messagebox.showerror("Error","All fields are required",parent=self.root)
    else:
        #mydb=mysql.connector.connect(host="localhost",username='root',password="Ramana30@")
        try:
            roomDB.insert(self.contact.get(),self.check_in.get(),self.check_out.get(),self.roomType.get(),self.availableRoom.get(),self.meal.get(),self.NoOfDays.get())
            messagebox.showinfo("Success","Room Details has been added",parent=self.root)
            self.displayAll()
            self.resetData()
            
        except Exception as es:
            messagebox.showerror("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)                
  
  def getData(self,event=''):
    selected_row = self.roomDetail.focus()
    data = self.roomDetail.item(selected_row)
    global row
    row = data["values"]
    self.contact.set(row[0])
    self.check_in.set(row[1])
    self.check_out.set(row[2])
    self.roomType.set(row[3])
    self.availableRoom.set(row[4])
    self.meal.set(row[5])
    self.NoOfDays.set(row[6])
    # self.paidTax.set(row[7])
    # self.subTotal.set(row[8])
    # self.totalCost.set(row[9])
       


  def displayAll(self):
    """if i call the display function multiple times it will shows the same datas
    multiple times to aviod these the below line is used which clear the displaying
    data if displayall is called again"""
    rows=roomDB.fetch()
    if len(rows)!=0:
        self.roomDetail.delete(*self.roomDetail.get_children())
        for row in rows:
            self.roomDetail.insert("", END, values=row)

  def updateData(self):
    
    if self.contact.get()=="" or self.check_in.get()=="" or self.check_out.get()=="" or self.roomType.get()=="" or self.availableRoom.get()=="" or self.meal.get()=="" or self.NoOfDays.get()=="":
        messagebox.showerror("Error","All fields are required",parent=self.root)
    else:
        #mydb=mysql.connector.connect(host="localhost",username='root',password="Ramana30@")
        try:
            roomDB.update(self.contact.get(),self.check_in.get(),self.check_out.get(),self.roomType.get(),self.availableRoom.get(),self.meal.get(),self.NoOfDays.get())
            messagebox.showinfo("Success","Room Details has been updated",parent=self.root)
            self.displayAll()
            self.resetData()
        except Exception as es:
            messagebox.showerror("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)
    
  def deleteData(self):
    if self.contact.get()=="":
        messagebox.showerror("Error","Customer contact is required",parent=self.root)
    else:
        try:
            ask=messagebox.askyesno("Confirm","Do you want to delete this customer?",parent=self.root)
            if ask>0:
                roomDB.remove(self.contact.get())
                messagebox.showinfo("Success","Room Detail has been deleted",parent=self.root)
                self.displayAll()
        except Exception as es:
            messagebox.showerror("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)
    
  def resetData(self):
    self.contact.set("")
    self.check_in.set("")
    self.check_out.set("")
    self.availableRoom.set(str(random.randint(1,50)))
   # self.meal.set("")
    self.NoOfDays.set("")
    self.paidTax.set("")
    self.subTotal.set("")
    self.totalCost.set("")
    self.searchVal.set("")
    self.searchText.set("")
    self.displayAll()
    
    
    
  def SearchRoom(self):
    if self.searchVal.get()=="" or self.searchText.get()=="":
        messagebox.showerror("Error","All fields are required",parent=self.root)
    else:
        try:
          rows=roomDB.search(self.searchVal.get(),self.searchText.get())
          if len(rows)!=0:
              self.roomDetail.delete(*self.roomDetail.get_children())
              for row in rows:
                  self.roomDetail.insert("", END, values=row)
          else:
              messagebox.showerror("Error","No such data found",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"Some thing went wrong:{str(es)}",parent=self.root)
  
  def totalBill(self):
    inDate=self.check_in.get()
    outDate=self.check_out.get()
    inDate=datetime.strptime(inDate,"%d/%m/%Y")
    outDate=datetime.strptime(outDate,"%d/%m/%Y")
    self.NoOfDays.set(str(abs(outDate-inDate).days))
    if self.roomType.get()=="Single":
        self.subTotal.set(str('%.2f'%(float(self.NoOfDays.get())*1000)))
        self.paidTax.set(str('%.2f'%(float(self.subTotal.get())*0.1)))
    elif self.roomType.get()=="Double":
        self.subTotal.set(str('%.2f'%(float(self.NoOfDays.get())*2000)))
        self.paidTax.set(str('%.2f'%(float(self.subTotal.get())*0.1)))
    elif self.roomType.get()=="Luxury":
        self.subTotal.set(str('%.2f'%(float(self.NoOfDays.get())*3000)))
        self.paidTax.set(str('%.2f'%(float(self.subTotal.get())*0.1)))
    if self.meal.get()=="Breakfast":
        self.subTotal.set(str('%.2f'%(float(self.subTotal.get())+float(self.NoOfDays.get())*100)))
        self.paidTax.set(str('%.2f'%(float(self.paidTax.get())+(float(self.subTotal.get())*0.05))))
    elif self.meal.get()=="Lunch":
        self.subTotal.set(str('%.2f'%(float(self.subTotal.get())+float(self.NoOfDays.get())*200)))
        self.paidTax.set(str('%.2f'%(float(self.paidTax.get())+(float(self.subTotal.get())*0.05))))
    elif self.meal.get()=="Dinner":
        self.subTotal.set(str('%.2f'%(float(self.subTotal.get())+float(self.NoOfDays.get())*200)))
        self.paidTax.set(str('%.2f'%(float(self.paidTax.get())+(float(self.subTotal.get())*0.05))))
    
    self.totalCost.set(str('%.2f'%(float(self.subTotal.get())+float(self.paidTax.get()))))
          
    
    
    

        
# if __name__=="__main__":
#     root=Tk()
#     obj=RoomBooking(root)
#     obj.displayAll()
#     root.mainloop()

    
    
    
    


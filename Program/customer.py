from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk   #for  combobox
from random import *
from tkinter import messagebox
from customerDB import Database

db=Database("Customer.db") 




class CustomerWindow:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management system")
        self.root.geometry("970x510+0+0")
        
        #variables
        self.ref=StringVar()
        self.ref.set(str(randint(1000,9999)))
        
        self.name=StringVar()
        self.gender=StringVar()
        self.mobileNumber=StringVar()
        self.email=StringVar()
        self.postcode=StringVar()
        self.nationality=StringVar()
        self.id=StringVar()
        self.idNumber=StringVar()
        self.address=StringVar()
        
        
        
        
        #Title
        titleLabel=Label(self.root,text="ADD CUSTOMER DETAILS",pady=7,font=("times new roman",18,"bold"),bg="black",fg='gold',bd=4,relief=RIDGE)
        titleLabel.place(x=0,y=0,width=970,height=40)
        #titleLabel.grid(row=0,column=1)

        #LOGO
        img1=Image.open("F:\Projects\hotelManagement\Images\logohotel.png")
        img1=img1.resize((100,30),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img1)
        
        img_label=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        img_label.place(x=5,y=2,height=29,width=100)
        #img_label.grid(row=0,column=0) 
        
        #labelFrame
        labelFrameLeft=LabelFrame(self.root,bd=2,relief=RIDGE,text='Customer Details',font=('arial',12,"bold"),padx=2)
        labelFrameLeft.place(x=5,y=40,width=365,height=465)
        
        #labels and entries
        #customer Reference number
        cust_ref_label=Label(labelFrameLeft,text="Customer Ref:",font=('times new roman',12,"bold"),padx=2,pady=6)
        cust_ref_label.grid(row=0,column=0,sticky='w')
        
        cust_ref_entry=Entry(labelFrameLeft,state='readonly',textvariable=self.ref,width=25,font=('times new roman',13,"bold"))
        cust_ref_entry.grid(row=0,column=1)
        
        #customer Name
        customerNameLabel=Label(labelFrameLeft,text="Customer Name:",font=('times new roman',12,"bold"),padx=2,pady=6)
        customerNameLabel.grid(row=1,column=0,sticky='w')
        
        customerNameEntry=Entry(labelFrameLeft,textvariable=self.name,width=25,font=('times new roman',13,"bold"))
        customerNameEntry.grid(row=1,column=1)
        
        #Gender
        genderlabel=Label(labelFrameLeft,text="Gender:",font=('times new roman',12,"bold"),padx=2,pady=6)
        genderlabel.grid(row=2,column=0,sticky='w')
        
        genderEntry=ttk.Combobox(labelFrameLeft,textvariable=self.gender,width=23,state="readonly",font=('times new roman',13,"bold"))
        genderEntry["value"]=["Male","Female","Other"]
        #genderEntry.current(0)  to set default value
        genderEntry.grid(row=2,column=1)
        
        
        #customer mobile number
        phoneNumberLabel=Label(labelFrameLeft,text='Mobile No:',font=('times new roman',12,"bold"),padx=2,pady=6)
        phoneNumberLabel.grid(row=3,column=0,sticky='w')
        
        phoneNumberEntry=Entry(labelFrameLeft,textvariable=self.mobileNumber,width=25,font=('times new roman',13,"bold"))
        phoneNumberEntry.grid(row=3,column=1)
        
        #customer Email id
        emailIdlabel=Label(labelFrameLeft,text="Email Id:",font=('times new roman',12,"bold"),padx=2,pady=6)
        emailIdlabel.grid(row=4,column=0,sticky='w')
    
        emailIdentry=Entry(labelFrameLeft,textvariable=self.email,width=25,font=('times new roman',13,"bold"))
        emailIdentry.grid(row=4,column=1)
        
        #customer postcode
        postcodeLabel=Label(labelFrameLeft,text="Postcode:",font=('times new roman',12,"bold"),padx=2,pady=6)
        postcodeLabel.grid(row=5,column=0,sticky='w')
        
        postcodeEntry=Entry(labelFrameLeft,textvariable=self.postcode,width=25,font=('times new roman',13,"bold"))
        postcodeEntry.grid(row=5,column=1)
        
        
        #customer Nationality
        nationalityLabel=Label(labelFrameLeft,text="Nationality:",font=('times new roman',12,"bold"),padx=2,pady=6)
        nationalityLabel.grid(row=6,column=0,sticky='w')
        
        nationalityEntry=ttk.Combobox(labelFrameLeft,textvariable=self.nationality,width=23,state="readonly",font=('times new roman',13,"bold"))
        nationalityEntry['value']=['Indian','American','British','Chinese','Japanese','Korean','Other']
        nationalityEntry.grid(row=6,column=1)
        
        #customer Id Proof
        idLabel=Label(labelFrameLeft,text="Id Proof Type:",font=('times new roman',12,"bold"),padx=2,pady=6)
        idLabel.grid(row=7,column=0,sticky='w')
        
        idEntry=ttk.Combobox(labelFrameLeft,textvariable=self.id,width=23,state="readonly",font=('times new roman',13,"bold"))
        idEntry['value']=['Aadhar','Pan',"Voter Id","Passport","Driving Licence"]
        idEntry.grid(row=7,column=1)
        
        #customer Id proof number
        idNumberLabel=Label(labelFrameLeft,text="Id Number:",font=('times new roman',12,"bold"),padx=2,pady=6)
        idNumberLabel.grid(row=8,column=0,sticky='w')
        
        idNumberEntry=Entry(labelFrameLeft,textvariable=self.idNumber,width=25,font=('times new roman',13,"bold"))
        idNumberEntry.grid(row=8,column=1)
        
        #customer Address
        addressLabel=Label(labelFrameLeft,text="Address:",font=('times new roman',12,"bold"),padx=2,pady=6)
        addressLabel.grid(row=9,column=0,sticky='w')
        
        addressEntry=Entry(labelFrameLeft,textvariable=self.address,width=25,font=('times new roman',13,"bold"))
        addressEntry.grid(row=9,column=1)
        
        #buttons
        
        btnFrame=Frame(labelFrameLeft)
        btnFrame.place(x=5,y=370,width=350,height=40)
    
        btnAdd=Button(btnFrame,text='Add',command=self.addData,font=('arial',11,'bold'),bg='black',fg='gold',width=8)
        btnAdd.grid(row=0,column=0,padx=3)
        
        btnUpdate=Button(btnFrame,text='Update',command=self.update,font=('arial',11,'bold'),bg='black',fg='gold',width=8)
        btnUpdate.grid(row=0,column=1,padx=3)
        
        btnDelete=Button(btnFrame,text='Delete',command=self.delete,font=('arial',11,'bold'),bg='black',fg='gold',width=8)
        btnDelete.grid(row=0,column=2,padx=3)
        
        btnReset=Button(btnFrame,command=self.reset,text='Reset',font=('arial',11,'bold'),bg='black',fg='gold',width=8)
        btnReset.grid(row=0,column=3,padx=3)
        
        #table frame
        
        tableFrame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=('arial',12,'bold'),padx=2)
        tableFrame.place(x=370,y=40,width=597,height=465)
        
        searchLabel=Label(tableFrame,font=('arial',11,'bold'),bg='red',fg='white',text='Search by:')
        searchLabel.grid(row=0,column=0,sticky='w',padx=2)
        
        comboSearch=ttk.Combobox(tableFrame,font=('arial',12,'bold'),width=14,state='readonly')
        comboSearch['value']=('select option','Mobile','Ref')
        comboSearch.current(0)
        comboSearch.grid(row=0,column=1,padx=2)
        
        textSearch=ttk.Entry(tableFrame,font=('arial',12,'bold'),width=20)
        textSearch.grid(row=0,column=2,padx=2)
        
        btnSearch=Button(tableFrame,text='Search',font=('arial',11,'bold'),bg='black',fg='gold',width=7)
        btnSearch.grid(row=0,column=4,padx=2)
        
        btnShowAll=Button(tableFrame,text='Show All',font=('arial',11,'bold'),bg='black',fg='gold',width=7)
        btnShowAll.grid(row=0,column=5,padx=1)
        
        
        #show data table
        
        detailTable=Frame(tableFrame,bd=2,relief=RIDGE)
        detailTable.place(x=0,y=50,width=595,height=370)
        
        scrollX=ttk.Scrollbar(detailTable,orient=HORIZONTAL)
        scrollY=ttk.Scrollbar(detailTable,orient=VERTICAL)
        
        self.customerDetail=ttk.Treeview(detailTable,column=('ref','name','gender','mobileNumber','Email','postcode','nationality','id','idNumber','address'),xscrollcommand=scrollX.set,yscrollcommand=scrollY.set)       #infor 
        
        scrollX.pack(side=BOTTOM,fill=X)
        scrollY.pack(side=RIGHT,fill=Y)
        
        scrollX.config(command=self.customerDetail.xview)        
        scrollY.config(command=self.customerDetail.yview)        
        
        self.customerDetail.heading('ref',text='Refer No')
        self.customerDetail.heading('name',text='Name')
        self.customerDetail.heading('gender',text='Gender')
        self.customerDetail.heading('mobileNumber',text='Mobile')
        self.customerDetail.heading('Email',text='Email')
        self.customerDetail.heading('postcode',text='PostCode')
        self.customerDetail.heading('id',text='Id Proof')
        self.customerDetail.heading('nationality',text='Nationality')
        self.customerDetail.heading('idNumber',text='Id Number')
        self.customerDetail.heading('address',text='Address')
        
        self.customerDetail['show']='headings'
        self.customerDetail.bind("<ButtonRelease-1>", self.getData)
        self.customerDetail.pack(fill=BOTH,expand=1)
        
            
    def addData(self):
            if self.name.get()=='' or self.address.get()=="" or self.mobileNumber.get()=="" or self.email.get()=="" or self.gender.get()=='' or self.nationality.get()=='' or self.id.get()=="" or self.idNumber.get()=="" or self.postcode.get()=="":
                messagebox.showerror("Error","All fields are required")
            else:
                #mydb=mysql.connector.connect(host="localhost",username='root',password="Ramana30@")
                try:
                    db.insert(self.ref.get(),self.name.get(),self.gender.get(),self.mobileNumber.get(),self.email.get(),self.postcode.get(),self.nationality.get(),self.id.get(),self.idNumber.get(),self.address.get())
                    messagebox.showinfo("Success","Customer has been added")
                    self.displayAll()
                except Exception as es:
                    messagebox.showerror("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)
                        
    def getData(self,event=''):
        selected_row = self.customerDetail.focus()
        data = self.customerDetail.item(selected_row)
        global row
        row = data["values"]
        # print(row)
        self.ref.set(row[0])
        self.name.set(row[1])
        self.gender.set(row[2])
        self.mobileNumber.set(row[3])
        self.email.set(row[4])
        self.postcode.set(row[5])
        self.nationality.set(row[6])
        self.id.set(row[7])
        self.idNumber.set(row[8])
        self.address.set(row[9])
        


    def displayAll(self):
        """if i call the display function multiple times it will shows the same datas
        multiple times to aviod these the below line is used which clear the displaying
        data if displayall is called again"""
        rows=db.fetch()
        if len(rows)!=0:
            self.customerDetail.delete(*self.customerDetail.get_children())
            for row in rows:
                self.customerDetail.insert("", END, values=row)

    def update(self):
            if self.name.get()=='' or self.address.get()=="" or self.mobileNumber.get()=="" or self.email.get()=="" or self.gender.get()=='' or self.nationality.get()=='' or self.id.get()=="" or self.idNumber.get()=="" or self.postcode.get()=="":
                messagebox.showerror("Error","All fields are required")
            else:
                #mydb=mysql.connector.connect(host="localhost",username='root',password="Ramana30@")
                try:
                    db.update(self.ref.get(),self.name.get(),self.gender.get(),self.mobileNumber.get(),self.email.get(),self.postcode.get(),self.nationality.get(),self.id.get(),self.idNumber.get(),self.address.get())
                    messagebox.showinfo("Success","Customer Detail has been updated")
                    self.displayAll()
                except Exception as es:
                    messagebox.showerror("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)
                    
    def delete(self):
        delete=messagebox.askyesno("Hotel Management System","Do you want to delete this Customer",parent=self.root)
        if delete>0:
            db.remove(self.ref.get())
        self.displayAll()
        
    def reset(self):
       # self.ref.set("")
        self.name.set("")
        self.gender.set("")
        self.mobileNumber.set("")
        self.email.set("")
        self.postcode.set("")
      #  self.nationality.set("")
      #  self.id.set("")
        self.idNumber.set("")
        self.address.set("")
        self.ref.set(str(randint(1000,9999)))
if __name__=="__main__":
    root=Tk()
    obj=CustomerWindow(root)
    obj.displayAll()
    root.mainloop()
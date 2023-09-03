from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk   #for  combobox
class CustomerWindow:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management system")
        self.root.geometry("970x510+0+0")
        
        
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
        
        cust_ref_entry=Entry(labelFrameLeft,width=25,font=('times new roman',13,"bold"))
        cust_ref_entry.grid(row=0,column=1)
        
        #customer Name
        customerNameLabel=Label(labelFrameLeft,text="Customer Name:",font=('times new roman',12,"bold"),padx=2,pady=6)
        customerNameLabel.grid(row=1,column=0,sticky='w')
        
        customerNameEntry=Entry(labelFrameLeft,width=25,font=('times new roman',13,"bold"))
        customerNameEntry.grid(row=1,column=1)
        
        #Gender
        genderlabel=Label(labelFrameLeft,text="Gender:",font=('times new roman',12,"bold"),padx=2,pady=6)
        genderlabel.grid(row=2,column=0,sticky='w')
        
        genderEntry=ttk.Combobox(labelFrameLeft,width=23,state="readonly",font=('times new roman',13,"bold"))
        genderEntry["value"]=["Male","Female","Other"]
        #genderEntry.current(0)  to set default value
        genderEntry.grid(row=2,column=1)
        
        
        #customer mobile number
        phoneNumberLabel=Label(labelFrameLeft,text='Mobile No:',font=('times new roman',12,"bold"),padx=2,pady=6)
        phoneNumberLabel.grid(row=3,column=0,sticky='w')
        
        phoneNumberEntry=Entry(labelFrameLeft,width=25,font=('times new roman',13,"bold"))
        phoneNumberEntry.grid(row=3,column=1)
        
        #customer Email id
        emailIdlabel=Label(labelFrameLeft,text="Email Id:",font=('times new roman',12,"bold"),padx=2,pady=6)
        emailIdlabel.grid(row=4,column=0,sticky='w')
    
        emailIdentry=Entry(labelFrameLeft,width=25,font=('times new roman',13,"bold"))
        emailIdentry.grid(row=4,column=1)
        
        #customer postcode
        postcodeLabel=Label(labelFrameLeft,text="Postcode:",font=('times new roman',12,"bold"),padx=2,pady=6)
        postcodeLabel.grid(row=5,column=0,sticky='w')
        
        postcodeEntry=Entry(labelFrameLeft,width=25,font=('times new roman',13,"bold"))
        postcodeEntry.grid(row=5,column=1)
        
        
        #customer Nationality
        nationalityLabel=Label(labelFrameLeft,text="Nationality:",font=('times new roman',12,"bold"),padx=2,pady=6)
        nationalityLabel.grid(row=6,column=0,sticky='w')
        
        nationalityEntry=ttk.Combobox(labelFrameLeft,width=23,state="readonly",font=('times new roman',13,"bold"))
        nationalityEntry['value']=['Indian','American','British','Chinese','Japanese','Korean','Other']
        nationalityEntry.grid(row=6,column=1)
        
        #customer Id Proof
        idLabel=Label(labelFrameLeft,text="Id Proof Type:",font=('times new roman',12,"bold"),padx=2,pady=6)
        idLabel.grid(row=7,column=0,sticky='w')
        
        idEntry=ttk.Combobox(labelFrameLeft,width=23,state="readonly",font=('times new roman',13,"bold"))
        idEntry['value']=['Aadhar','Pan',"Voter Id","Passport","Driving Licence"]
        idEntry.grid(row=7,column=1)
        
        #customer Id proof number
        idNumberLabel=Label(labelFrameLeft,text="Id Number:",font=('times new roman',12,"bold"),padx=2,pady=6)
        idNumberLabel.grid(row=8,column=0,sticky='w')
        
        idNumberEntry=Entry(labelFrameLeft,width=25,font=('times new roman',13,"bold"))
        idNumberEntry.grid(row=8,column=1)
        
        #customer Address
        addressLabel=Label(labelFrameLeft,text="Address:",font=('times new roman',12,"bold"),padx=2,pady=6)
        addressLabel.grid(row=9,column=0,sticky='w')
        
        addressEntry=Entry(labelFrameLeft,width=25,font=('times new roman',13,"bold"))
        addressEntry.grid(row=9,column=1)
        
        #buttons
        
        btnFrame=Frame(labelFrameLeft)
        btnFrame.place(x=5,y=370,width=350,height=40)
    
        btnAdd=Button(btnFrame,text='Add',font=('arial',11,'bold'),bg='black',fg='gold',width=8)
        btnAdd.grid(row=0,column=0,padx=3)
        
        btnUpdate=Button(btnFrame,text='Update',font=('arial',11,'bold'),bg='black',fg='gold',width=8)
        btnUpdate.grid(row=0,column=1,padx=3)
        
        btnDelete=Button(btnFrame,text='Delete',font=('arial',11,'bold'),bg='black',fg='gold',width=8)
        btnDelete.grid(row=0,column=2,padx=3)
        
        btnReset=Button(btnFrame,text='Reset',font=('arial',11,'bold'),bg='black',fg='gold',width=8)
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
        self.customerDetail.pack(fill=BOTH,expand=1)
        
        
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=CustomerWindow(root)
    root.mainloop()
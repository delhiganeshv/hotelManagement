from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk   #for  combobox
class CustomerWindow:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management system")
        self.root.geometry("970x510+0+0")
        
        
        #Title
        lblTitle=Label(self.root,text="ADD CUSTOMER DETAILS",pady=7,font=("times new roman",18,"bold"),bg="black",fg='gold',bd=4,relief=RIDGE)
        lblTitle.place(x=0,y=0,width=970,height=40)
        #lblTitle.grid(row=0,column=1)

        #LOGO
        img1=Image.open("F:\Projects\hotelManagement\Images\logohotel.png")
        img1=img1.resize((100,30),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img1)
        
        img_label=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        img_label.place(x=5,y=2,height=29,width=100)
        #img_label.grid(row=0,column=0) 
        
        #labelFrame
        labelFrameLeft=LabelFrame(self.root,bd=2,relief=RIDGE,text='Customer Details',font=('times new roman',12,"bold"),padx=2)
        labelFrameLeft.place(x=5,y=40,width=400,height=465)
        
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
        
if __name__=="__main__":
    root=Tk()
    obj=CustomerWindow(root)
    root.mainloop()
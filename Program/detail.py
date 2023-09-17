from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import ttk
from database import *


roomDb=roomDatabase('room.db')


class DetailWindow:
    def __init__(self,root):
        self.root=root
        #self.root.title("Hotel Management system")
        self.root.geometry("970x540+0+0")
        self.root.overrideredirect(True)
        
        
        #Title
        titleLabel=Label(self.root,text="ROOM ADDING DEPARTMENT",pady=7,font=("times new roman",18,"bold"),bg="black",fg='gold',bd=4,relief=RIDGE)
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
        labelFrameLeft.place(x=5,y=40,width=450,height=465)
        
        #image frame in labelFrame
        imageFrame=Frame(labelFrameLeft,bd=2,relief=RIDGE,bg="white")
       # imageFrame.grid(row=0,column=0)
        imageFrame.pack(fill=X)
        
        #new room add image
        img2=Image.open(r"F:\Projects\hotelManagement\Images\room1.jpg")
        img2=img2.resize((150,100),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img2)
        
        img_label1=Label(imageFrame,image=self.photoimg4,bd=0,relief=RIDGE)
        #img_label1.place(x=5,y=2,height=100,width=170)
        img_label1.grid(row=0,column=0)
        
        img3=Image.open(r"F:\Projects\hotelManagement\Images\room5.jpg")
        img3=img3.resize((150,100),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img3)
        
        img_label2=Label(imageFrame,image=self.photoimg5,bd=0,relief=RIDGE)
        #img_label2.place(x=135,y=2,height=100,width=170)
        img_label2.grid(row=0,column=1)
        
        
        
        img4=Image.open(r"F:\Projects\hotelManagement\Images\room3.jpg")
        img4=img4.resize((150,100),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img4)
        
        img_label3=Label(imageFrame,image=self.photoimg6,bd=0,relief=RIDGE)
        #img_label3.place(x=265,y=2,height=100,width=170)
        img_label3.grid(row=0,column=2)
        
        #variables
        self.floor=StringVar()
        self.roomNo=StringVar()
        self.roomType=StringVar()
        self.searchVal=StringVar()
        
        #entryFrame
        entryFrame=Frame(labelFrameLeft,pady=40)
        #entryFrame.grid(row=1,column=0)
        entryFrame.pack(fill=X)
        
        #floor
        floorLabel=Label(entryFrame,text="Floor No",font=("arial",12,"bold"))
        floorLabel.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        floorEntry=ttk.Entry(entryFrame,textvariable=self.floor,width=20,font=("arial",12,"bold"))
        floorEntry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        #Room No.
        roomNoLabel=Label(entryFrame,text="Room No",font=("arial",12,"bold"))
        roomNoLabel.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        roomNoEntry=ttk.Entry(entryFrame,textvariable=self.roomNo,width=20,font=("arial",12,"bold"))
        roomNoEntry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        #Room Type
        roomTypeLabel=Label(entryFrame,text="Room Type",font=("arial",12,"bold"))
        roomTypeLabel.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        roomTypeEntry=ttk.Combobox(entryFrame,textvariable=self.roomType,width=18,font=("arial",12,"bold"),state="readonly")
        roomTypeEntry["values"]=("Single","Double","Luxury")
        roomTypeEntry.current(0)
        roomTypeEntry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        #Add,delete,update and reset buttons in a single row
        btnFrame=Frame(labelFrameLeft,padx=6)
        #btnFrame.grid(row=2,column=0)
        btnFrame.pack(fill=X)
        
       
        add_button=Button(btnFrame,command=self.addRoom,cursor='hand2',text="Add",width=10,font=('times new roman',12,"bold"),bg='black',fg='gold')
        add_button.grid(row=0,column=0,padx=3)

        update_button=Button(btnFrame,command=self.updateRoom,cursor='hand2',text="Update",width=10,font=('times new roman',12,"bold"),bg='black',fg='gold')
        update_button.grid(row=0,column=1,padx=3)

        delete_button=Button(btnFrame,command=self.deleteRoom,cursor='hand2',text="Delete",width=10,font=('times new roman',12,"bold"),bg='black',fg='gold')
        delete_button.grid(row=0,column=2,padx=3)

        reset_button=Button(btnFrame,command=self.resetRoom,cursor='hand2',text="Reset",width=10,font=('times new roman',12,"bold"),bg='black',fg='gold')
        reset_button.grid(row=0,column=3,padx=3)
    
   
        #labelFrameRight
        labelFrameRight=LabelFrame(self.root,bd=2,relief=RIDGE,text='Show Room Details',font=('arial',12,"bold"),padx=2)
        labelFrameRight.place(x=460,y=40,width=500,height=465)
        
        searchLabel=Label(labelFrameRight,font=('arial',11,'bold'),bg='red',fg='white',text='Search by:')
        searchLabel.grid(row=0,column=0,sticky='w',padx=2)
    
    
        textSearch=ttk.Entry(labelFrameRight,textvariable=self.searchVal,font=('arial',12,'bold'),width=20)
        textSearch.grid(row=0,column=2,padx=2)
    
        btnSearch=Button(labelFrameRight,command=self.searchRoom,cursor='hand2',text='Search',font=('arial',11,'bold'),bg='black',fg='gold',width=7)
        btnSearch.grid(row=0,column=4,padx=2)
    
        btnShowAll=Button(labelFrameRight,command=self.displayAll,cursor='hand2',text='Show All',font=('arial',11,'bold'),bg='black',fg='gold',width=7)
        btnShowAll.grid(row=0,column=5,padx=1)
    
        detailTable=Frame(labelFrameRight,bd=2,relief=RIDGE)
        detailTable.place(x=0,y=50,width=500,height=400)
        
      #  scrollX=ttk.Scrollbar(labelFrameRight,orient=HORIZONTAL)
        scrollY=ttk.Scrollbar(detailTable,orient=VERTICAL)
        
        self.roomDetail=ttk.Treeview(detailTable,column=('floor','roomNo','roomType'),yscrollcommand=scrollY.set)       #infor 
        
       # scrollX.pack(side=BOTTOM,fill=X)
        scrollY.pack(side=RIGHT,fill=Y)
        
        #scrollX.config(command=self.roomDetail.xview)        
        scrollY.config(command=self.roomDetail.yview)
        
        
        self.roomDetail.heading('floor',text='Floor No')
        self.roomDetail.column('floor',width=40)
        
        self.roomDetail.heading('roomNo',text='Room No')
        self.roomDetail.column('roomNo',width=40)   
        self.roomDetail.heading('roomType',text='Room Type')
        self.roomDetail.column('roomType',width=40)
        self.roomDetail['show']='headings'
        self.roomDetail.bind("<ButtonRelease-1>", self.getData)
       
        self.roomDetail.pack(fill=BOTH,expand=1)
            

    def getData(self,event=''):
        cursor_row=self.roomDetail.focus()
        content=self.roomDetail.item(cursor_row)
        row=content['values']
        self.floor.set(row[0])
        self.roomNo.set(row[1])
        self.roomType.set(row[2])
        
    def addRoom(self):
        if self.floor.get()=="" or self.roomNo.get()=="" or self.roomType.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                roomDb.insert(self.floor.get(),self.roomNo.get(),self.roomType.get())
                messagebox.showinfo("Success","Room added successfully",parent=self.root)
                self.displayAll()
            except:
                messagebox.showerror("Error","Room already exists",parent=self.root)
        
        
    
    def deleteRoom(self):
        if self.roomNo.get()=="":
            messagebox.showerror("Error","Room No. is required",parent=self.root)
        else:
            try:
                ask=messagebox.askyesno("Confirm","Do you want to delete this room?",parent=self.root)
                if ask>0:
                    roomDb.remove(self.roomNo.get())
                    messagebox.showinfo("Success","Room deleted successfully",parent=self.root)
                    self.displayAll()
            except:
                messagebox.showerror("Error","Room does not exist",parent=self.root)
        
    
    def updateRoom(self):
        if self.floor.get()=="" or self.roomNo.get()=="" or self.roomType.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                ask=messagebox.askyesno("Confirm","Do you want to update this room?",parent=self.root)
                if ask>0:
                    roomDb.update(self.floor.get(),self.roomNo.get(),self.roomType.get())
                    messagebox.showinfo("Success","Room updated successfully",parent=self.root)
                    self.displayAll()
            except:
                messagebox.showerror("Error","Room does not exist",parent=self.root)
        
    
    def resetRoom(self):
        self.floor.set("")
        self.roomNo.set("")
        
        
    def displayAll(self):
        self.roomDetail.delete(*self.roomDetail.get_children())
        for row in roomDb.fetch():
            self.roomDetail.insert('',END,values=row)
        
    def searchRoom(self):
        if self.searchVal.get()=="":
            messagebox.showerror("Error","Search input required",parent=self.root)
        else:
            try:
                self.roomDetail.delete(*self.roomDetail.get_children())
                for row in roomDb.search(self.searchVal.get()):
                    self.roomDetail.insert('',END,values=row)
            except:
                messagebox.showerror("Error","Room does not exist",parent=self.root)
        
        
       
# if __name__=="__main__":
#     root=Tk()
#     obj=DetailWindow(root)
#     obj.displayAll()
#     root.mainloop()
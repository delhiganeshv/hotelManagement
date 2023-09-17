from tkinter import*
from PIL import Image,ImageTk   #pip install pillow
from customer import CustomerWindow
from room import RoomBooking
from detail import DetailWindow


class hotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1200x700+0+0")
        #self.root.state("zoomed")
        
        # IST IMAGE
        img1=Image.open("F:\Projects\hotelManagement\Images\hotel1.png")
        img1=img1.resize((1200,110),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        img_label=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        img_label.place(x=0,y=0,width=1200,height=110)
        
        #LOGO
        img2=Image.open("F:\Projects\hotelManagement\Images\logohotel.png")
        img2=img2.resize((200,110),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        img_label2=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        img_label2.place(x=0,y=0,width=200,height=110)
        
        #Title
        label_title=Label(self.root,pady=5,text='HOTEL MANAGEMENT SYSTEM',font=("times new roman",30,"bold"),bg='black',fg='gold',bd=4,relief=RIDGE)
        label_title.place(x=0,y=110,width=1200,height=40,)
        
        #main frame
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=150,width=1550,height=560)
        
        #Button Frame
        btn_frame = Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.grid(row=0,column=0)  
             
        #menu
        label_menu=Label(btn_frame,text='MENU',width=12,font=("times new roman",20,"bold"),bg='black',fg='gold',bd=4,relief=RIDGE)
        label_menu.grid(row=0,column=0,pady=2)
        
        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.customer_detail,padx=10,width=16,bd=0,cursor='hand2',font=("times new roman",14,"bold"),bg='black',fg='gold',)
        cust_btn.grid(row=1,column=0,pady=1)
        
        room_btn=Button(btn_frame,text="ROOM",command=self.room_detail,padx=10,width=16,bd=0,cursor='hand2',font=("times new roman",14,"bold"),bg='black',fg='gold',)
        room_btn.grid(row=2,column=0,pady=1)
        
        detail_btn=Button(btn_frame,text="DETAIL",command=self.roominfo,padx=10,width=16,bd=0,cursor='hand2',font=("times new roman",14,"bold"),bg='black',fg='gold',)
        detail_btn.grid(row=3,column=0,pady=1)
        
        report_btn=Button(btn_frame,text="REPORT",padx=10,width=16,bd=0,cursor='hand2',font=("times new roman",14,"bold"),bg='black',fg='gold',)
        report_btn.grid(row=4,column=0,pady=1)
        
        logout_btn=Button(btn_frame,text="LOGOUT",padx=10,width=16,bd=0,cursor='hand2',font=("times new roman",14,"bold"),bg='black',fg='gold',)
        logout_btn.grid(row=5,column=0,pady=1)
        
        img4=Image.open("F:\Projects\hotelManagement\Images\myh.jpg")
        img4=img4.resize((200,145),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        img_label3=Label(btn_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        img_label3.grid(row=6,column=0)
        
        img5=Image.open("F:\Projects\hotelManagement\Images\myh.jpg")
        img5=img5.resize((200,145),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        img_label4=Label(btn_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        img_label4.grid(row=7,column=0)
        
        
        #right side image
        img3=Image.open("F:\Projects\hotelManagement\Images\slide3.jpg")
        img3=img3.resize((971,540),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        img_label2=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        img_label2.grid(row=0,column=1)
        

    def customer_detail(self):
        # x=self.root.winfo_x()
        # y=self.root.winfo_y()
        self.newWindow=Toplevel(self.root)
        self.app=CustomerWindow(self.newWindow)
        self.app.displayAll()
        self.newWindow.geometry("+%d+%d" % (232,188)) 
        #self.newWindow.grab_set()
        
    def room_detail(self):
        self.newWindow=Toplevel(self.root)
        self.app=RoomBooking(self.newWindow)
        self.app.displayAll()
        self.newWindow.geometry("+%d+%d" % (232,188)) 
        #self.newWindow.grab_set()
        
    def roominfo(self):
        self.newWindow=Toplevel(self.root)
        self.app=DetailWindow(self.newWindow)
        self.app.displayAll()
        self.newWindow.geometry("+%d+%d" % (232,188)) 
        #self.newWindow.grab_set()
          
if __name__=="__main__":
    root=Tk()
    obj=hotelManagementSystem(root)
    root.mainloop()
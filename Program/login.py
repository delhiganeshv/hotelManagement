from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from main import hotelManagementSystem


class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1200x700+0+0")

        self.bg = ImageTk.PhotoImage(file=r"F:\Projects\hotelManagement\Images\myh.jpg")
        bgLabel = Label(self.root, image=self.bg)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="black")
        frame.place(x=450, y=120, width=300, height=500)

        img1 = Image.open(
            r"F:\Projects\hotelManagement\Images\LoginIconApp.png"
        )  # type:ignore
        img1 = img1.resize((100, 100), Image.LANCZOS)  # type: ignore
        self.photoimage1 = ImageTk.PhotoImage(img1)
        labeling1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        labeling1.place(x=550, y=125, width=100, height=100)

        get_str = Label(
            frame,
            text="Get Started",
            font=("times new roman", 20, "bold"),
            fg="white",
            bg="black",
        )
        get_str.place(x=80, y=100)

        # label
        # icon image
        img2 = Image.open(
            r"F:\Projects\hotelManagement\Images\LoginIconApp.png"
        )  # type:ignore
        img2 = img2.resize((25, 25), Image.LANCZOS)  # type: ignore
        self.photoimage2 = ImageTk.PhotoImage(img2)
        labeling2 = Label(frame, image=self.photoimage2, bg="black", borderwidth=0)
        labeling2.place(x=20, y=160, width=25, height=25)

        # variables
        self.username = StringVar()
        self.password = StringVar()

        # username label
        usernameLabel = Label(
            frame,
            text="Username",
            font=("times new roman", 15, "bold"),
            fg="white",
            bg="black",
        )
        usernameLabel.place(x=45, y=160)

        usernameEntry = ttk.Entry(
            frame,
            textvariable=self.username,
            font=("times new roman", 15, "bold"),
            width=25,
        )
        usernameEntry.place(x=20, y=190)

        # icon image
        img3 = Image.open(
            r"F:\Projects\hotelManagement\Images\Lock-512.png"
        )  # type:ignore
        img3 = img3.resize((25, 25), Image.LANCZOS)  # type: ignore
        self.photoimage3 = ImageTk.PhotoImage(img3)
        labeling3 = Label(frame, image=self.photoimage3, bg="black", borderwidth=0)
        labeling3.place(x=20, y=230, width=25, height=25)

        # password label
        passwordLabel = Label(
            frame,
            text="Password",
            font=("times new roman", 15, "bold"),
            fg="white",
            bg="black",
        )
        passwordLabel.place(x=45, y=230)

        passwordEntry = ttk.Entry(
            frame,
            textvariable=self.password,
            font=("times new roman", 15, "bold"),
            width=25,
        )
        passwordEntry.place(x=20, y=260)

        # login button
        loginBtn = Button(
            frame,
            command=self.login,
            text="Login",
            font=("times new roman", 15, "bold"),
            bd=3,
            relief=RIDGE,
            cursor="hand2",
            bg="red",
            fg="white",
            activeforeground="white",
            activebackground="green",
        )
        loginBtn.place(x=20, y=320, width=260, height=35)

        # register button
        registerBtn = Button(
            frame,
            text="New User? Register",
            font=("times new roman", 15, "bold"),
            bd=0,
            cursor="hand2",
            bg="black",
            fg="white",
            activeforeground="green",
            activebackground="black",
        )
        registerBtn.place(x=20, y=400, width=260, height=35)

        # forget password button
        forgetBtn = Button(
            frame,
            text="Forget Password ?",
            font=("times new roman", 15, "bold"),
            bd=0,
            cursor="hand2",
            bg="black",
            fg="white",
            activeforeground="green",
            activebackground="black",
        )
        forgetBtn.place(x=20, y=360, width=260, height=35)

    def login(self):
        if self.username.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.username.get() != "Delhi" or self.password.get() != "123456":
            messagebox.showerror("Error", "Invalid Username/Password", parent=self.root)
        else:
            messagebox.showinfo(
                "Welcome",
                f"Welcome {self.username.get()}\nYour Password:{self.password.get()}",
                parent=self.root,
            )
            self.root.destroy()
            self.newWindow = Tk()
            self.app = hotelManagementSystem(self.newWindow)
            self.newWindow.mainloop()


if __name__ == "__main__":
    root = Tk()
    obj = LoginWindow(root)
    root.mainloop()

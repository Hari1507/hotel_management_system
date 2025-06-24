from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector



class Register_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # ==============variable================

        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # ==============bg iamge================

        self.bg = ImageTk.PhotoImage(file=r"C:\Users\HARISH\Downloads\hotel-images\images\0-3450_3d-nature-wallpaper-hd-1080p-free-download-new.jpg")
        bg_label = Label(self.root, image=self.bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # ==============left iamge================
        
        self.bg1 = ImageTk.PhotoImage(file=r"C:\Users\HARISH\Downloads\hotel-images\images\thought-good-morning-messages-LoveSove.jpg")
        left_label = Label(self.root, image=self.bg1)
        left_label.place(x=50, y=100, width=470, height=550)

        # ==============main Frame================
        
        frame=Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="darkgreen", bg="white")
        register_lbl.place(x=20, y=20)

        # ==============labels and entry================

        # name
        fname_label = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
        fname_label.place(x=50, y=100)

        self.fname_entry = ttk.Entry(frame,textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        self.fname_entry.place(x=50, y=130, width=250)

        # last name

        l_name_label = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white",fg="black")
        l_name_label.place(x=370, y=100)

        self.txt_lname= ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman", 15))
        self.txt_lname.place(x=370, y=130, width=250)

        # contact

        contact = Label(frame, text="Contact No.", font=("times new roman", 15, "bold"), bg="white",fg="black")
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman", 15))
        self.txt_contact.place(x=50, y=200, width=250)

        # email

        email = Label(frame, text="Email",font=("times new roman", 15, "bold"), bg="white",fg="black")
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(frame,textvariable=self.var_email, font=("times new roman", 15))
        self.txt_email.place(x=370, y=200, width=250)

        # security question

        security_Q = Label(frame, text="Security Question", font=("times new roman", 15, "bold"), bg="white",fg="black")
        security_Q.place(x=50, y=240)

        self.cmb_security_Q = ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman", 15, "bold"), state="readonly")
        self.cmb_security_Q["values"] = ("Select", "Your Birth Place", "Your Pet Name", "Your Best Friend Name", "Your Mother Name", "Your Father Name")
        self.cmb_security_Q.place(x=50, y=270, width=250)
        self.cmb_security_Q.current(0)

        # answer

        security_A = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white",fg="black")
        security_A.place(x=370, y=240)

        self.txt_security_A = ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman", 15))
        self.txt_security_A.place(x=370, y=270, width=250)

        # password

        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white",fg="black")
        password.place(x=50, y=310)

        self.txt_password = ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman", 15))
        self.txt_password.place(x=50, y=340, width=250)

        # confirm password

        confirm_password = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white",fg="black")
        confirm_password.place(x=370, y=310)

        self.txt_confirm_password = ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman", 15))
        self.txt_confirm_password.place(x=370, y=340, width=250)

        # ================check button================
        
        self.var_check = IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree with terms and conditions",font=("times new roman", 12, "bold"),onvalue=1, offvalue=0)
        checkbtn.place(x=50, y=380)

        # ================buttons================

        img=Image.open(r"C:\Users\HARISH\Downloads\hotel-images\images\register-now-button1.jpg")
        img=img.resize((200,50),Image.Resampling.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman", 15, "bold"))
        b1.place(x=10, y=420, width=200)

        img1=Image.open(r"C:\Users\HARISH\Downloads\hotel-images\images\loginpng.png")
        img1=img1.resize((200,50),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2",font=("times new roman", 15, "bold"))
        b1.place(x=330, y=420, width=200)


    # ===================function declaration================

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="" or self.txt_email.get()=="" or self.cmb_security_Q.get()=="" or self.txt_security_A.get()=="" or self.txt_password.get()=="" or self.txt_confirm_password.get()=="select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and conditions")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Harish@150799",database="hotel_management_system")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist, please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.txt_security_A.get(),
                    self.var_pass.get()
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registration is done successfully")
           
       

       

        



if __name__ == "__main__":
    root = Tk()
    app = Register_Win(root)
    root.mainloop()
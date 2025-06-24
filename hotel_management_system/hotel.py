from tkinter import *
from PIL import Image, ImageTk
from customer import Cust_Win
from room import Room_Win
from details import Details_Win
from report import Report_Win
from register import Register_Win


class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        # ================== 1st Image =================
        img1 = Image.open(r"C:\Users\HARISH\Desktop\hotel_management_system\images\hotel1.png")
        img1 = img1.resize((1550, 140), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1550, height=140)

        # ================== Logo =================
        img2 = Image.open(r"C:\Users\HARISH\Desktop\hotel_management_system\images\logohotel.png")
        img2 = img2.resize((230, 140), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=230, height=140)

        # ================== Title =================
        lbl_title = Label(self.root, text="HOTEL MANAGEMENT SYSTEM", font=("arial", 40, "bold"),
                          bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1550, height=50)

        # ================== Main Frame =================
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=620)

        # ================== Menu =================
        lbl_menu = Label(main_frame, text="MENU", font=("arial", 20, "bold"), bg="black",
                         fg="gold", bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

        # ================== Button Frame =================
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=190)

        # ================== Buttons =================
        cust_btn = Button(btn_frame, text="CUSTOMER", command=self.open_customer_window, width=22,font=("arial", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        cust_btn.grid(row=0, column=0, pady=1)

        room_btn = Button(btn_frame, text="ROOM", command=self.open_room_window, width=22,font=("arial", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand2")
        room_btn.grid(row=1, column=0, pady=1)

        details_btn = Button(btn_frame, text="DETAILS", command=self.open_details_window, width=22,font=("arial", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand2")
        details_btn.grid(row=2, column=0, pady=1)

        report_btn = Button(btn_frame, text="REPORT",command=self.open_report_window,width=22,font=("arial", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand2")
        report_btn.grid(row=3, column=0, pady=1)

        logout_btn = Button(btn_frame, text="LOGOUT",command=self.open_logout_Win,width=22,font=("arial", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand2")
        logout_btn.grid(row=4, column=0, pady=1)

        # ================== Right Side Image =================
        img3 = Image.open(r"C:\Users\HARISH\Desktop\hotel_management_system\images\slide3.jpg")
        img3 = img3.resize((1310, 590), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg1 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg1.place(x=225, y=0, width=1310, height=590)

        # ================== Down Side Images =================
        img4 = Image.open(r"C:\Users\HARISH\Desktop\hotel_management_system\images\myh.jpg")
        img4 = img4.resize((230, 210), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg2 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg2.place(x=0, y=225, width=230, height=210)

        img5 = Image.open(r"C:\Users\HARISH\Desktop\hotel_management_system\images\khana.jpg")
        img5 = img5.resize((230, 190), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lblimg3 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg3.place(x=0, y=420, width=230, height=190)

    # =============== Button Functions =================

    def open_customer_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_Win(self.new_window)

    def open_room_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Room_Win(self.new_window)

    def open_details_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Details_Win(self.new_window)

    def open_register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register_Win(self.new_window)

    def open_report_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Report_Win(self.new_window)

    def open_logout_Win(self):
        self.root.destroy()
        

        


if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()

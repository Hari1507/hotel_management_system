from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class Report_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Report")
        self.root.geometry("900x500+200+100")

        # ====================Variables====================
        self.var_id = StringVar()
        x = random.randint(1000, 9999)
        self.var_id.set(str(x))
        self.var_name = StringVar()
        self.var_mobile = StringVar()
        self.var_room_no = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_total_bill = StringVar()


        # ====================Title====================
        lbl_title = Label(self.root, text="CustomerReport Details", font=("Arial", 20, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # ==================logo=====================
        img2 = Image.open(r"C:\Users\HARISH\Desktop\hotel_management_system\images\logohotel.png")
        img2 = img2.resize((100, 40), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=40)

        # ==================label frame=====================
        LabelFrameleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="CustomerReport Details", font=("arial", 12, "bold"), padx=2)
        LabelFrameleft.place(x=5, y=50, width=425, height=490)
        

        # ==================labels and entry=====================

        # cust id
        lbl_cust_id = Label(LabelFrameleft, text="Cust_id:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_id.grid(row=0, column=0, sticky=W)
        entry_id = ttk.Entry(LabelFrameleft, textvariable=self.var_id, font=("arial", 13, "bold"), width=20)
        entry_id.grid(row=0, column=1, sticky=W, padx=5)

        # name
        name = Label(LabelFrameleft, text="Name:", font=("arial", 12, "bold"), padx=2, pady=6)
        name.grid(row=1, column=0, sticky=W)
        txtname = ttk.Entry(LabelFrameleft, textvariable=self.var_name, font=("arial", 13, "bold"), width=20)
        txtname.grid(row=1, column=1, sticky=W, padx=5)

        # contact
        mobile = Label(LabelFrameleft, text="Mobile:", font=("arial", 12, "bold"), padx=2, pady=6)
        mobile.grid(row=2, column=0, sticky=W)
        mobile = ttk.Entry(LabelFrameleft, textvariable=self.var_mobile, font=("arial", 13, "bold"), width=20)
        mobile.grid(row=2, column=1, sticky=W, padx=5)

        # room no
        lbl_room = Label(LabelFrameleft, text="Room No:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_room.grid(row=3, column=0, sticky=W)
        txtroom_no = ttk.Entry(LabelFrameleft, textvariable=self.var_room_no, font=("arial", 13, "bold"), width=20)
        txtroom_no.grid(row=3, column=1, sticky=W, padx=5)

        # check in
        checkin = Label(LabelFrameleft, text="Check In:", font=("arial", 12, "bold"), padx=2, pady=6)
        checkin.grid(row=4, column=0, sticky=W)
        txtcheckin = ttk.Entry(LabelFrameleft, textvariable=self.var_checkin, font=("arial", 13, "bold"), width=20)
        txtcheckin.grid(row=4, column=1, sticky=W, padx=5)

        # check out
        checkout = Label(LabelFrameleft, text="Check Out:", font=("arial", 12, "bold"), padx=2, pady=6)
        checkout.grid(row=5, column=0, sticky=W)
        txtcheckout = ttk.Entry(LabelFrameleft, textvariable=self.var_checkout, font=("arial", 13, "bold"), width=20)
        txtcheckout.grid(row=5, column=1, sticky=W, padx=5)

        # total bill
        total_bill = Label(LabelFrameleft, text="Total Bill:", font=("arial", 12, "bold"), padx=2, pady=6)
        total_bill.grid(row=6, column=0, sticky=W)
        txttotal_bill = ttk.Entry(LabelFrameleft, textvariable=self.var_total_bill, font=("arial", 13, "bold"), width=20)
        txttotal_bill.grid(row=6, column=1, sticky=W, padx=5)
        
        
        # ==================buttons=====================
        btn_frame = Frame(LabelFrameleft, bd=2, relief=RIDGE, padx=2)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd=Button(btn_frame, text="Add",command=self.add_data,font=("arial", 12, "bold"), bg="black", fg="gold", width=9,)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate=Button(btn_frame, text="Update",command=self.update,font=("arial", 12, "bold"), bg="black", fg="gold", width=9,)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete=Button(btn_frame, text="Delete",command=self.delete,font=("arial", 12, "bold"), bg="black", fg="gold", width=9,)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset=Button(btn_frame, text="Reset",command=self.reset,font=("arial", 12, "bold"), bg="black", fg="gold", width=9,)
        btnReset.grid(row=0, column=3, padx=1)

          # ==================table Frame search system=====================

        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System",font=("arial", 12, "bold"), padx=2)
        Table_Frame.place(x=435, y=50, width=850, height=490)

        lblSearchBy = Label(Table_Frame, font=("arial", 12, "bold"), text="Search By:", bg="red", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=5, pady=5)

        self.search_var = StringVar()
        combo_search = ttk.Combobox(Table_Frame, textvariable=self.search_var,font=("arial", 12, "bold"),width=18, state="readonly")
        combo_search["values"] = ("Mobile", "ID")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=5,pady=5)



        self.search_txt = StringVar()
        txt_search =ttk.Entry(Table_Frame, textvariable=self.search_txt, font=("arial", 13, "bold"), width=24)
        txt_search.grid(row=0, column=2, padx=2)

        btn_search = Button(Table_Frame, text="Search", command=self.search, font=("arial", 12, "bold"), bg="black", fg="gold", width=10)
        btn_search.grid(row=0, column=3, padx=2)

        btnShowAll=Button(Table_Frame, text="Show All",command=self.fetch_data, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnShowAll.grid(row=0, column=4, padx=1)

        
        # ====================Treeview Frame====================

        details_table = Frame(Table_Frame, bd=4, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=350)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Report_Details = ttk.Treeview(details_table,columns=("id", "name", "mobile", "room_no", "checkin", "checkout", "total_bill"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        
        scroll_x.config(command=self.Report_Details.xview)
        scroll_y.config(command=self.Report_Details.yview)

        self.Report_Details.pack(fill=BOTH, expand=1)

        self.Report_Details.heading("id", text="Id")
        self.Report_Details.heading("name", text="Name")
        self.Report_Details.heading("mobile", text="Mobile No")
        self.Report_Details.heading("room_no", text="Room No")
        self.Report_Details.heading("checkin", text="CheckIn")
        self.Report_Details.heading("checkout", text="CheckOut")
        self.Report_Details.heading("total_bill", text="Total Bill")


        self.Report_Details["show"] = "headings"


        self.Report_Details.column("id", width=100)
        self.Report_Details.column("name", width=100)
        self.Report_Details.column("mobile", width=100)
        self.Report_Details.column("room_no", width=100)
        self.Report_Details.column("checkin", width=100)
        self.Report_Details.column("checkout", width=100)
        self.Report_Details.column("total_bill", width=100)

        self.Report_Details.pack(fill=BOTH, expand=1)
        self.Report_Details.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()
        


    def add_data(self):
        if self.var_mobile.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Harish@150799", database="hotel_management_system")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO report VALUES (%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_mobile.get(),
                    self.var_room_no.get(),
                    self.var_checkin.get(),
                    self.var_checkout.get(),
                    self.var_total_bill.get()
                ))
                conn.commit()
                conn.close()
                self.fetch_data()
                messagebox.showinfo("Success", "Report has been added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Harish@150799", database="hotel_management_system")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from report")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Report_Details.delete(*self.Report_Details.get_children())
            for i in rows:
                self.Report_Details.insert("", END, values=i)
            conn.commit()
            conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.Report_Details.focus()
        content = self.Report_Details.item(cursor_row)
        row = content["values"]
        if row:
            self.var_id.set(row[0])
            self.var_name.set(row[1])
            self.var_mobile.set(row[2])
            self.var_room_no.set(row[3])
            self.var_checkin.set(row[4])
            self.var_checkout.set(row[5])
            self.var_total_bill.set(row[6])

    def update(self):
        if self.var_mobile.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "Please enter mobile number", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Harish@150799", database="hotel_management_system")
            my_cursor = conn.cursor()
            my_cursor.execute("update report set name=%s,mobile=%s,room_no=%s,checkin=%s,checkout=%s,total_bill=%s where id=%s", (
               self.var_name.get(),
                self.var_mobile.get(),
                self.var_room_no.get(),
                self.var_checkin.get(),
                self.var_checkout.get(),
                self.var_total_bill.get(),
                self.var_id.get()
            ))
            conn.commit()
            conn.close()
            self.fetch_data()
            messagebox.showinfo("Update","Report details has been updated Successfully", parent=self.root)

    def delete(self):
        if self.var_Cust_id.get() == "":
            messagebox.showerror("Error", "Please enter ID", parent=self.root)
        else:
        
                delete_confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this customer?", parent=self.root)
                if delete_confirm:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Harish@150799", database="hotel_management_system")
                my_cursor = conn.cursor()
                
                query = "DELETE FROM report WHERE cust_id = %s"
                value = (self.var_id.get(),)
                my_cursor.execute(query, value)
                conn.commit()

                if my_cursor.rowcount > 0:
                    self.fetch_data()
                    messagebox.showinfo("Deleted", "record has been deleted", parent=self.root)
                else:
                    messagebox.showwarning("Not Found", "No record found with that Id", parent=self.root)

                conn.close()

    def reset(self):
        self.var_id.set("")
        self.var_name.set("")
        self.var_mobile.set("")
        self.var_room_no.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_total_bill.set("")

    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Harish@150799", database="hotel_management_system")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM report WHERE " + str(self.search_var.get() + " LIKE '%" + str(self.search_txt.get()) + "%'"))
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Report_Details.delete(*self.Report_Details.get_children())
            for i in rows:
                self.Report_Details.insert("", END, values=i)
            conn.commit()
            conn.close()
        
       






        

if __name__ == "__main__":
    root = Tk()
    obj = Report_Win(root)
    root.mainloop()


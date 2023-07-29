from tkinter import *
from tkinter import ttk
import mysql.connector
import random
from PIL import Image,ImageTk 
from tkinter import messagebox
from time import strftime
from datetime import datetime


class Room:
    def __init__(self,root) :
        self.root=root
        self.root.title("Room Details")
        self.root.geometry("1300x560+230+230")

        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_tax=StringVar()
        self.var_totalcost=StringVar()   

        labeltitle=Label(self.root,text="Add Room Details",font=("raleway",20),bg="#00003d",fg="white",bd=4,relief=RIDGE)
        labeltitle.place(x=0,y=0,width=1300,height=50)

        labelFrameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking",font=("Raleway",12,"bold"),padx=2)
        labelFrameleft.place(x=5,y=50,width=425,height=500)

        label_custCon=Label(labelFrameleft,text="Customer Contact",font=("Raleway",12),padx=2,pady=6)
        label_custCon.grid(row=0,column=0,sticky=W)
        entry_contact=ttk.Entry(labelFrameleft,width=20,textvariable=self.var_contact,font=("Raleway",12))
        entry_contact.grid(row=0,column=1,sticky=W)

        btnfetch=Button(labelFrameleft,text="Fetch Data",command=self.fetch_contact,font=("Raleway",10, "bold"),bg="#00003d",fg="white",width=8)
        btnfetch.place(x=330,y=4)

        label_checkIn=Label(labelFrameleft,text="Check In Date",font=("Raleway",12),padx=2,pady=6)
        label_checkIn.grid(row=1,column=0,sticky=W)
        entry_cI=ttk.Entry(labelFrameleft,textvariable=self.var_checkin,width=25,font=("Raleway",12))
        entry_cI.grid(row=1,column=1)

        label_checkOut=Label(labelFrameleft,text="Check Out Date",font=("Raleway",12),padx=2,pady=6)
        label_checkOut.grid(row=2,column=0,sticky=W)
        entry_cO=ttk.Entry(labelFrameleft,textvariable=self.var_checkout,width=25,font=("Raleway",12))
        entry_cO.grid(row=2,column=1)

        label_roomt=Label(labelFrameleft,text="Room Type",font=("Raleway",12),padx=2,pady=6)
        label_roomt.grid(row=3,column=0,sticky=W)
        textroom=ttk.Combobox(labelFrameleft,width=24,textvariable=self.var_roomtype,font=("Raleway",12),state="readonly")
        textroom["value"]=("Single","Double","Suite")
        textroom.current(0)
        textroom.grid(row=3,column=1)

        label_availr=Label(labelFrameleft,text="Available Room",font=("Raleway",12),padx=2,pady=6)
        label_availr.grid(row=4,column=0,sticky=W)
        entry_avail=ttk.Entry(labelFrameleft,textvariable=self.var_roomavailable,width=25,font=("Raleway",12))
        entry_avail.grid(row=4,column=1)

        label_days=Label(labelFrameleft,text="Number of Days",font=("Raleway",12),padx=2,pady=6)
        label_days.grid(row=5,column=0,sticky=W)
        entry_days=ttk.Entry(labelFrameleft,textvariable=self.var_noofdays,width=25,font=("Raleway",12))
        entry_days.grid(row=5,column=1)

        label_meal=Label(labelFrameleft,text="Meal",font=("Raleway",12),padx=2,pady=6)
        label_meal.grid(row=6,column=0,sticky=W)
        entry_meal=ttk.Entry(labelFrameleft,textvariable=self.var_meal,width=25,font=("Raleway",12))
        entry_meal.grid(row=6,column=1)

        label_tax=Label(labelFrameleft,text="Tax",font=("Raleway",12),padx=2,pady=6)
        label_tax.grid(row=7,column=0,sticky=W)
        entry_tax=ttk.Entry(labelFrameleft,textvariable=self.var_tax,width=25,font=("Raleway",12))
        entry_tax.grid(row=7,column=1)

        label_cost=Label(labelFrameleft,text="Total Cost",font=("Raleway",12),padx=2,pady=6)
        label_cost.grid(row=8,column=0,sticky=W)
        entry_cost=ttk.Entry(labelFrameleft,textvariable=self.var_totalcost,width=25,font=("Raleway",12))
        entry_cost.grid(row=8,column=1)
        
        btnbill=Button(labelFrameleft,text="Bill",command=self.total,font=("Raleway",12, "bold"),bg="#00003d",fg="white",width=9)
        btnbill.grid(row=9,column=0,padx=2,pady=6,sticky=W)

        btn_frame=Frame(labelFrameleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0, y=365, width=412, height=40)

        btnadd=Button(btn_frame,text="ADD",command=self.add_data,font=("Raleway",12, "bold"),bg="#00003d",fg="white",width=9)
        btnadd.grid(row=0,column=0,padx=1)

        btnup=Button(btn_frame,text="UPDATE",command=self.update,font=("Raleway",12, "bold"),bg="#00003d",fg="white",width=9)
        btnup.grid(row=0,column=1,padx=1)

        btndelete=Button(btn_frame,text="DELETE",command=self.delete_m,font=("Raleway",12, "bold"),bg="#00003d",fg="white",width=9)
        btndelete.grid(row=0,column=2,padx=1)

        btnreset=Button(btn_frame,text="RESET",command=self.reset,font=("Raleway",12, "bold"),bg="#00003d",fg="white",width=9)
        btnreset.grid(row=0,column=4,padx=1)

        img2=Image.open(r"C:\Users\Riti\Documents\Hotel Management System\images\room.jpg")
        img2=img2.resize((520,300),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        labelimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        labelimg.place(x=770,y=55,width=520,height=300)

        tableFrame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search",font=("Raleway",12,"bold"),padx=2)
        tableFrame.place(x=435,y=280,width=860,height=270)

        lblSearchBy=Label(tableFrame,text="Search By",font=("Raleway",10),padx=2,pady=6, bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        comboSearch=ttk.Combobox(tableFrame,textvariable=self.search_var,width=24,font=("Raleway",12),state="readonly")
        comboSearch["value"]=("Contact","Room")
        comboSearch.current(0)
        comboSearch.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        textSearch=ttk.Entry(tableFrame,textvariable=self.txt_search,width=24,font=("Raleway",12))
        textSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(tableFrame,text="SEARCH",font=("Raleway",10, "bold"),bg="#00003d",fg="white",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShow=Button(tableFrame,text="Show All",font=("Raleway",10, "bold"),bg="#00003d",fg="white",width=10)
        btnShow.grid(row=0,column=4,padx=1)

        detailsFrame=Frame(tableFrame,bd=2,relief=RIDGE)
        detailsFrame.place(x=0,y=50,width=860,height=195)

        scrollx=ttk.Scrollbar(detailsFrame,orient=HORIZONTAL)
        scrolly=ttk.Scrollbar(detailsFrame,orient=VERTICAL)

        self.CustDetails=ttk.Treeview(detailsFrame,column=("contact","checkin","checkout","roomtype","roomavail","meal","noofdays"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.CustDetails.xview)
        scrolly.config(command=self.CustDetails.yview)

        self.CustDetails.heading("contact",text="Contact")
        self.CustDetails.heading("checkin",text="Check In")
        self.CustDetails.heading("checkout",text="Check Out")
        self.CustDetails.heading("roomtype",text="Room Type")
        self.CustDetails.heading("roomavail",text="Room Available")
        self.CustDetails.heading("meal",text="Meal")
        self.CustDetails.heading("noofdays",text="No of Days")        

        self.CustDetails["show"]="headings"
        self.CustDetails.column("contact",width=100)
        self.CustDetails.column("checkin",width=100)
        self.CustDetails.column("checkout",width=100)
        self.CustDetails.column("roomtype",width=100)
        self.CustDetails.column("roomavail",width=100)
        self.CustDetails.column("meal",width=100)
        self.CustDetails.column("noofdays",width=100)
        self.CustDetails.pack(fill=BOTH,expand=1)
        self.CustDetails.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="" :
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="blackberry@1106",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_contact.get(),
                                                                                    self.var_checkin.get(),
                                                                                    self.var_checkout.get(),
                                                                                    self.var_roomtype.get(),
                                                                                    self.var_roomavailable.get(),
                                                                                    self.var_meal.get(),
                                                                                    self.var_noofdays.get(),
                                                                            
                                                                               ))
                conn.commit() 
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room Booked",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="blackberry@1106",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from room")
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                self.CustDetails.delete(*self.CustDetails.get_children())
                for i in rows:
                    self.CustDetails.insert("",END,values=i)
                    conn.commit()
            conn.close()

    def get_cursor(self,event=""):
            cursor_row=self.CustDetails.focus()
            content=self.CustDetails.item(cursor_row)
            row=content["values"]
            self.var_contact.set(row[0]),
            self.var_checkin.set(row[1]),
            self.var_checkout.set(row[2]),
            self.var_roomtype.set(row[3]),
            self.var_roomavailable.set(row[4]),
            self.var_meal.set(row[5]),
            self.var_noofdays.set(row[6])                                                                                   

    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="blackberry@1106",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set Checkin=%s, Checkout=%s, Roomtype=%s, Roomavail=%s, Meal=%s, Noofdays=%s where Contact=%s",(
                                                                                                                                                                                                                                                                                                              
                                                                                                                                    self.var_checkin.get(),
                                                                                                                                    self.var_checkout.get(),
                                                                                                                                    self.var_roomtype.get(),
                                                                                                                                    self.var_roomavailable.get(),
                                                                                                                                    self.var_meal.get(),
                                                                                                                                    self.var_noofdays.get(),
                                                                                                                                    self.var_contact.get(),
                                                                                                                                                        ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room Details have been updated successfully.",parent=self.root)


    def fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter your contact number",parent=self.root)
        else: 
            conn=mysql.connector.connect(host="localhost",username="root",password="blackberry@1106",database="management")
            my_cursor=conn.cursor() 
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","This number is not found",parent=self.root)
            else: 
                conn.commit()
                conn.close()

                showDataFrame=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataFrame.place(x=440,y=58,width=315,height=215)

                lblname=Label(showDataFrame,text="Name:",font=("Raleway",12,"bold"))
                lblname.place(x=0,y=5)

                lbl=Label(showDataFrame,text=row,font=("Raleway",12))
                lbl.place(x=90,y=5)

                conn=mysql.connector.connect(host="localhost",username="root",password="blackberry@1106",database="management")
                my_cursor=conn.cursor() 
                query2=("select Age from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query2,value)
                row=my_cursor.fetchone()

                lblage=Label(showDataFrame,text="Age:",font=("Raleway",12,"bold"))
                lblage.place(x=0,y=35)

                lbl2=Label(showDataFrame,text=row,font=("Raleway",12))
                lbl2.place(x=90,y=35)

                conn=mysql.connector.connect(host="localhost",username="root",password="blackberry@1106",database="management")
                my_cursor=conn.cursor() 
                query=("select Gender from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblname=Label(showDataFrame,text="Gender:",font=("Raleway",12,"bold"))
                lblname.place(x=0,y=65)

                lbl=Label(showDataFrame,text=row,font=("Raleway",12))
                lbl.place(x=90,y=65)

                conn=mysql.connector.connect(host="localhost",username="root",password="blackberry@1106",database="management")
                my_cursor=conn.cursor() 
                query=("select Email from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblemail=Label(showDataFrame,text="Email:",font=("Raleway",12,"bold"))
                lblemail.place(x=0,y=95)

                lbl=Label(showDataFrame,text=row,font=("Raleway",12))
                lbl.place(x=90,y=95)
                

                conn=mysql.connector.connect(host="localhost",username="root",password="blackberry@1106",database="management")
                my_cursor=conn.cursor() 
                query=("select Nationality from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblname=Label(showDataFrame,text="Nationality:",font=("Raleway",12,"bold"))
                lblname.place(x=0,y=125)

                lbl=Label(showDataFrame,text=row,font=("Raleway",12))
                lbl.place(x=90,y=125)

                conn=mysql.connector.connect(host="localhost",username="root",password="blackberry@1106",database="management")
                my_cursor=conn.cursor() 
                query=("select IDnumber from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblname=Label(showDataFrame,text="ID Number:",font=("Raleway",12,"bold"))
                lblname.place(x=0,y=155)

                lbl=Label(showDataFrame,text=row,font=("Raleway",12))
                lbl.place(x=90,y=155)

    def delete_m(self):
        delete_m=messagebox.askyesno("Warning","Are you sure you want to delete this customer",parent=self.root)
        if delete_m>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="blackberry@1106",database="management")
            my_cursor=conn.cursor() 
            my_cursor.execute("delete from room where Contact=%s",(self.var_contact.get(),))
            conn.commit()
            conn.close()
            self.fetch_data()
        else: 
            if not delete_m:
                return


    def reset(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomavailable.set(""),
        self.var_meal.set(""),
        self.var_noofdays.set("")


    def total(self):
        indate=self.var_checkin.get()
        outdate=self.var_checkout.get()
        indate=datetime.strptime(indate,"%d/%m/%Y")
        outdate=datetime.strptime(outdate,"%d/%m/%Y")
        self.var_noofdays.set((outdate-indate).days)

        if(self.var_meal.get=="Breakfast ")

if __name__=="__main__":
    root=Tk()
    obj=Room(root)
    root.mainloop()
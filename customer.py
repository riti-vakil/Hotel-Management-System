from tkinter import *
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox


class Customer:
    def __init__(self,root) :
        self.root=root
        self.root.title("Customer Details")
        self.root.geometry("1300x560+230+230")

        self.var_ref=IntVar()
        x=random.randint(1000,9999)
        self.var_ref.set(x)

        self.var_cust_name=StringVar()
        self.var_age=IntVar()
        self.var_gender=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_nationality=StringVar()
        self.var_IDproof=StringVar()
        self.var_IDnumber=StringVar()        


        labeltitle=Label(self.root,text="Add Customer Details",font=("raleway",20),bg="#00003d",fg="white",bd=4,relief=RIDGE)
        labeltitle.place(x=0,y=0,width=1300,height=50)

        labelFrameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("Raleway",12,"bold"),padx=2)
        labelFrameleft.place(x=5,y=50,width=425,height=500)

        label_custRef=Label(labelFrameleft,text="Customer Reference",font=("Raleway",12),padx=2,pady=6)
        label_custRef.grid(row=0,column=0,sticky=W)
        entry_ref=ttk.Entry(labelFrameleft,textvariable=self.var_ref,width=25,font=("Raleway",12),state="readonly")
        entry_ref.grid(row=0,column=1)

        cName=Label(labelFrameleft,text="Name",font=("Raleway",12),padx=2,pady=6)
        cName.grid(row=1,column=0,sticky=W)
        textcname=ttk.Entry(labelFrameleft,textvariable=self.var_cust_name,width=25,font=("Raleway",12))
        textcname.grid(row=1,column=1)

        age=Label(labelFrameleft,text="Age",font=("Raleway",12),padx=2,pady=6)
        age.grid(row=2,column=0,sticky=W)
        textage=ttk.Entry(labelFrameleft,textvariable=self.var_age,width=25,font=("Raleway",12))
        textage.grid(row=2,column=1)

        gender=Label(labelFrameleft,text="Gender",font=("Raleway",12),padx=2,pady=6)
        gender.grid(row=3,column=0,sticky=W)
        textgender=ttk.Combobox(labelFrameleft,textvariable=self.var_gender,width=24,font=("Raleway",12),state="readonly")
        textgender["value"]=("Male","Female","Other")
        textgender.current(0)
        textgender.grid(row=3,column=1)

        mobile=Label(labelFrameleft,text="Mobile Number",font=("Raleway",12),padx=2,pady=6)
        mobile.grid(row=4,column=0,sticky=W)
        textmobile=ttk.Entry(labelFrameleft,textvariable=self.var_mobile,width=25,font=("Raleway",12))
        textmobile.grid(row=4,column=1)

        email=Label(labelFrameleft,text="Email",font=("Raleway",12),padx=2,pady=6)
        email.grid(row=5,column=0,sticky=W)
        textemail=ttk.Entry(labelFrameleft,textvariable=self.var_email,width=25,font=("Raleway",12))
        textemail.grid(row=5,column=1)

        address=Label(labelFrameleft,text="Address",font=("Raleway",12),padx=2,pady=6)
        address.grid(row=6,column=0,sticky=W)
        textadd=ttk.Entry(labelFrameleft,textvariable=self.var_address,width=25,font=("Raleway",12))
        textadd.grid(row=6,column=1)

        nationality=Label(labelFrameleft,text="Nationalty",font=("Raleway",12),padx=2,pady=6)
        nationality.grid(row=7,column=0,sticky=W)
        textnation=ttk.Combobox(labelFrameleft,textvariable=self.var_nationality,width=24,font=("Raleway",12),state="readonly")
        textnation["value"]=("Indian","American","British","Other")
        textnation.current(0)
        textnation.grid(row=7,column=1)

        nationality=Label(labelFrameleft,text="ID Proof",font=("Raleway",12),padx=2,pady=6)
        nationality.grid(row=8,column=0,sticky=W)
        textnation=ttk.Combobox(labelFrameleft,textvariable=self.var_IDproof,width=24,font=("Raleway",12),state="readonly")
        textnation["value"]=("Aadhar Card","Driving Licence","Passport","")
        textnation.current(0)
        textnation.grid(row=8,column=1)

        id=Label(labelFrameleft,text="ID Number",font=("Raleway",12),padx=2,pady=6)
        id.grid(row=9,column=0,sticky=W)
        textid=ttk.Entry(labelFrameleft,textvariable=self.var_IDnumber,width=25,font=("Raleway",12))
        textid.grid(row=9,column=1)


        btn_frame=Frame(labelFrameleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0, y=375, width=412, height=40)

        btnadd=Button(btn_frame,text="ADD",command=self.add_data,font=("Raleway",12, "bold"),bg="#00003d",fg="white",width=9)
        btnadd.grid(row=0,column=0,padx=1)

        btnup=Button(btn_frame,text="UPDATE",command=self.update,font=("Raleway",12, "bold"),bg="#00003d",fg="white",width=9)
        btnup.grid(row=0,column=1,padx=1)

        btndelete=Button(btn_frame,text="DELETE",command=self.delete_m,font=("Raleway",12, "bold"),bg="#00003d",fg="white",width=9)
        btndelete.grid(row=0,column=2,padx=1)

        btnreset=Button(btn_frame,text="RESET",command=self.reset,font=("Raleway",12, "bold"),bg="#00003d",fg="white",width=9)
        btnreset.grid(row=0,column=4,padx=1)


        tableFrame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search",font=("Raleway",12,"bold"),padx=2)
        tableFrame.place(x=435,y=50,width=860,height=500)

        lblSearchBy=Label(tableFrame,text="Search By",font=("Raleway",10),padx=2,pady=6, bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        comboSearch=ttk.Combobox(tableFrame,textvariable=self.search_var,width=24,font=("Raleway",12),state="readonly")
        comboSearch["value"]=("Name","Mobile")
        comboSearch.current(0)
        comboSearch.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        textSearch=ttk.Entry(tableFrame,textvariable=self.txt_search,width=24,font=("Raleway",12))
        textSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(tableFrame,text="SEARCH",command=self.search,font=("Raleway",10, "bold"),bg="#00003d",fg="white",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShow=Button(tableFrame,text="Show All",command=self.fetch_data,font=("Raleway",10, "bold"),bg="#00003d",fg="white",width=10)
        btnShow.grid(row=0,column=4,padx=1)

        detailsFrame=Frame(tableFrame,bd=2,relief=RIDGE)
        detailsFrame.place(x=0,y=50,width=860,height=360)

        scrollx=ttk.Scrollbar(detailsFrame,orient=HORIZONTAL)
        scrolly=ttk.Scrollbar(detailsFrame,orient=VERTICAL)

        self.CustDetails=ttk.Treeview(detailsFrame,column=("ref","name","age","gender","mobile","email","address","nationality","idproof","idnumber"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.CustDetails.xview)
        scrolly.config(command=self.CustDetails.yview)

        self.CustDetails.heading("ref",text="Ref")
        self.CustDetails.heading("name",text="Name")
        self.CustDetails.heading("age",text="Age")
        self.CustDetails.heading("gender",text="Gender")
        self.CustDetails.heading("mobile",text="Mobile")
        self.CustDetails.heading("email",text="Email")
        self.CustDetails.heading("address",text="Address")
        self.CustDetails.heading("nationality",text="Nationality")
        self.CustDetails.heading("idproof",text="IDproof")
        self.CustDetails.heading("idnumber",text="IDnumber")
        

        self.CustDetails["show"]="headings"
        self.CustDetails.column("ref",width=100)
        self.CustDetails.column("name",width=100)
        self.CustDetails.column("age",width=100)
        self.CustDetails.column("gender",width=100)
        self.CustDetails.column("mobile",width=100)
        self.CustDetails.column("email",width=100)
        self.CustDetails.column("address",width=100)
        self.CustDetails.column("nationality",width=100)
        self.CustDetails.column("idproof",width=100)
        self.CustDetails.column("idnumber",width=100)
        
        self.CustDetails.pack(fill=BOTH,expand=1)
        self.CustDetails.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_mobile.get()=="" or self.var_IDproof.get()=="" or self.var_IDnumber.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="blackberry@1106",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_ref.get(),
                                                                                    self.var_cust_name.get(),
                                                                                    self.var_age.get(),
                                                                                    self.var_gender.get(),
                                                                                    self.var_mobile.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_address.get(),
                                                                                    self.var_nationality.get(),
                                                                                    self.var_IDproof.get(),
                                                                                    self.var_IDnumber.get()
                                                                               ))
                conn.commit() 
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Details added successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="blackberry@1106",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
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

        self.var_ref.set(row[0]),   
        self.var_cust_name.set(row[1]),
        self.var_age.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_mobile.set(row[4]),
        self.var_email.set(row[5]),
        self.var_address.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_IDproof.set(row[8]),
        self.var_IDnumber.set(row[9])

    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="blackberry@1106",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set Name=%s, Age=%s, Gender=%s, Mobile=%s, Email=%s, Address=%s, Nationality=%s, Idproof=%s, IDnumber=%s where Ref=%s",(
                                                                                                                                                        
                                                                                                                                                        self.var_cust_name.get(),
                                                                                                                                                        self.var_age.get(),
                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                        self.var_mobile.get(),
                                                                                                                                                        self.var_email.get(),
                                                                                                                                                        self.var_address.get(),
                                                                                                                                                        self.var_nationality.get(),
                                                                                                                                                        self.var_IDproof.get(),
                                                                                                                                                        self.var_IDnumber.get(),
                                                                                                                                                        self.var_ref.get()
                                                                                                                                                        ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Details have been updated successfully.",parent=self.root)

    def delete_m(self):
        delete_m=messagebox.askyesno("Warning","Are you sure you want to delete this customer",parent=self.root)
        if delete_m>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="blackberry@1106",database="management")
            my_cursor=conn.cursor() 
            my_cursor.execute("delete from customer where Ref=%s",(self.var_ref.get(),))
            conn.commit()
            conn.close()
            self.fetch_data()
        else: 
            if not delete_m:
                return


    def reset(self):
        self.var_cust_name.set(""),
        self.var_age.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        self.var_address.set(""),
        self.var_IDnumber.set("")
        x=random.randint(1000,9999)
        self.var_ref.set(x)  

    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="blackberry@1106",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'") 
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.CustDetails.delete(*self.CustDetails.get_children())
            for i in rows:
                self.CustDetails.insert("",END,values=i)
            conn.commit()
        conn.close() 
        

if __name__=="__main__":
    root=Tk()
    obj=Customer(root)
    root.mainloop()
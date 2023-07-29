from tkinter import*
from PIL import Image,ImageTk 
from customer import Customer
from room import Room

class HotelManagementSystem:
    def __init__(self,root) :
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")


        img1=Image.open(r"C:\Users\Riti\Documents\Hotel Management System\images\hotel1.jpg")
        img1=img1.resize((1550,150),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        labelimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        labelimg.place(x=0,y=0,width=1550,height=150)


        img2=Image.open(r"C:\Users\Riti\Documents\Hotel Management System\images\logo.webp")
        img2=img2.resize((230,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        labelimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        labelimg.place(x=0,y=0,width=230,height=150)


        labeltitle=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("raleway",25),bg="#00003d",fg="white",bd=4,relief=RIDGE)
        labeltitle.place(x=0,y=150,width=1550,height=50)

        mainFrame=Frame(self.root,bd=4,relief=RIDGE)
        mainFrame.place(x=0,y=200,width=1550,height=620)


        labelmenu=Label(mainFrame,text="MENU",font=("raleway",20),bg="#00003d",fg="white",relief=RIDGE)
        labelmenu.place(x=0,y=0,width=230) 

        buttonFrame=Frame(mainFrame,bd=4,relief=RIDGE)
        buttonFrame.place(x=0,y=35,width=228,height=200)       


        custButton=Button(buttonFrame,text="Customer",command=self.cust_details,width=20,font=("raleway",14),bg="#00003d",fg="white")
        custButton.grid(row=0,column=0,pady=1)
        
        roomButton=Button(buttonFrame,text="Rooms",command=self.room_details,width=20,font=("raleway",14),bg="#00003d",fg="white")
        roomButton.grid(row=1,column=0,pady=1)

        detailsButton=Button(buttonFrame,text="Details",width=20,font=("raleway",14),bg="#00003d",fg="white")
        detailsButton.grid(row=2,column=0,pady=1)

        reportButton=Button(buttonFrame,text="Report",width=20,font=("raleway",14),bg="#00003d",fg="white")
        reportButton.grid(row=3,column=0,pady=1)

        logoutButton=Button(buttonFrame,text="Logout",width=20,font=("raleway",14),bg="#00003d",fg="white")
        logoutButton.grid(row=4,column=0,pady=1)



    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Customer(self.new_window)

    def room_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Room(self.new_window)



if __name__=="__main__" :
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()      
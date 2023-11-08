#!/usr/bin/env python
# coding: utf-8

# In[15]:


#Database design
#table:accounts
#acn integer primary key autoincrement
#name text
#pass text
#email text
#mobile text
#bal text
#type text
#opendate text

from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from datetime import datetime
import time

import sqlite3

try:
    conobj=sqlite3.connect(database="Banking.sqlite")
    curobj=conobj.cursor()
    curobj.execute("create table accounts(acn integer primary key autoincrement,name text,pass text,email text,mobile text,bal float,type text,opendate text)")
    conobj.commit()
    print("table created")
    
except:
    print("something went wrong,might be table already exists")

conobj.close()


win=Tk()
win.state("zoomed")
win.configure(bg="powder blue")
win.resizable(width=False,height=False)


title=Label(win,text="Banking Atuomation",font=("arial",60,"bold","underline"),bg="powder blue")
title.pack()


date=Label(win,text=f"{datetime.now().date()}",font=("arial",15,"bold"),bg="powder blue")
date.place(relx=.9,rely=.10)


def mainscreen():
    frm=Frame(win)
    frm.configure(bg="pink")
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)
    
    def new():
        frm.destroy()
        newuserscreen()
    
    def fp():
        frm.destroy()
        fpscreen()
        
    def login():
        acn=e_acn.get()
        pwd=e_pass.get()
        if len(acn)==0 or len(pwd)==0:
            messagebox.showerror("login","Empty fields are not allowed!")
        else:
            conobj=sqlite3.connect(database="banking.sqlite") 
            curobj=conobj.cursor()
            curobj.execute("select * from accounts where acn=? and pass=? ",(acn,pwd))
            tup=curobj.fetchone()
            if tup==None:
                messagebox.showerror("login","Invalid ACN/Pass")
            else:
                global uname,uacn
                uacn=tup[0]
                uname=tup[1]
                frm.destroy()
                homescreen()
                
    def reset():
        e_acn.delete(0,"end")
        e_pass.delete(0,"end")
        e_acn.focus()
    
    lbl_acn=Label(frm,text="Account",font=("arial",20,"bold"),fg="blue",bg="pink")
    lbl_acn.place(relx=.3,rely=.1)
    
    e_acn=Entry(frm,font=("arial",20,"bold"),bd=5)
    e_acn.place(relx=.42,rely=.1)
    e_acn.focus()

    
    lbl_pass=Label(frm,text="Password",font=("arial",20,"bold"),fg="blue",bg="pink")
    lbl_pass.place(relx=.3,rely=.2)
    
    e_pass=Entry(frm,font=("arial",20,"bold"),bd=5,show="*")
    e_pass.place(relx=.42,rely=.2)
    
    Login_btn=Button(frm,text="Login",font=("arial",20,"bold"),bd=5,command=login)
    Login_btn.place(relx=.44,rely=.3)
    
    Reset_btn=Button(frm,text="Reset",font=("arial",20,"bold"),bd=5,command=reset)
    Reset_btn.place(relx=.54,rely=.3)
    
    FP_btn=Button(frm,text="Forgot Password",font=("arial",20,"bold"),bd=5,width=16,command=fp)
    FP_btn.place(relx=.42,rely=.43)
    
    
    New_btn=Button(frm,text="Open New Account",font=("arial",20,"bold"),bd=5,width=19,command=new)
    New_btn.place(relx=.4,rely=.56)
    
    
def newuserscreen():
    frm=Frame(win)
    frm.configure(bg="pink")
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)
    
    def back():
        frm.destroy()
        mainscreen()
        
    def openaccountdb():
        name=e_name.get()
        pwd=e_pass.get()
        email=e_email.get()
        mobile=e_mobile.get()
        actype=cb_acn.get()
        bal=0
        opendate=time.ctime()
        
        
        conobj=sqlite3.connect(database="banking.sqlite") 
        curobj=conobj.cursor()
        curobj.execute("insert into accounts(name,pass,email,mobile,bal,type,opendate)values(?,?,?,?,?,?,?)",(name,pwd,email,mobile,bal,actype,opendate))
        conobj.commit()
        curobj.close()
        
        curobj=conobj.cursor() 
        curobj.execute("select max(acn) from accounts") 
        tup=curobj.fetchone() 
        conobj.close() 
        messagebox.showinfo("open account",f"Account opened with ACN:{tup[0]}")
        
    def reset():
        e_name.delete(0,"end")
        e_pass.delete(0,"end")
        e_email.delete(0,"end")
        e_mobile.delete(0,"end")
        e_name.focus()
        
                       
    back_btn=Button(frm,text="Back",font=("arial",20,"bold"),bd=5,command=back)
    back_btn.place(relx=0,rely=0)
    
    
    lbl_name=Label(frm,text="Name",font=("arial",20,"bold"),fg="blue",bg="pink")
    lbl_name.place(relx=.3,rely=.1)
    
    e_name=Entry(frm,font=("arial",20,"bold"),bd=5)
    e_name.place(relx=.42,rely=.1)
    e_name.focus()
    
    lbl_pass=Label(frm,text="Password",font=("arial",20,"bold"),fg="blue",bg="pink")
    lbl_pass.place(relx=.3,rely=.2)
    
    e_pass=Entry(frm,font=("arial",20,"bold"),bd=5)
    e_pass.place(relx=.42,rely=.2)
    
    lbl_email=Label(frm,text="Email",font=("arial",20,"bold"),fg="blue",bg="pink")
    lbl_email.place(relx=.3,rely=.3)
    
    e_email=Entry(frm,font=("arial",20,"bold"),bd=5)
    e_email.place(relx=.42,rely=.3)
    
    lbl_mobile=Label(frm,text="Mobile",font=("arial",20,"bold"),fg="blue",bg="pink")
    lbl_mobile.place(relx=.3,rely=.4)
    
    e_mobile=Entry(frm,font=("arial",20,"bold"),bd=5)
    e_mobile.place(relx=.42,rely=.4)
    
    lbl_type=Label(frm,text="Type",font=("arial",20,"bold"),fg="blue",bg="pink")
    lbl_type.place(relx=.3,rely=.5)
    
    cb_acn=Combobox(frm,font=("arial",20,"bold"),values=["Savings","Current"])
    cb_acn.current(0)
    cb_acn.place(relx=.42,rely=.5)
    
    open_btn=Button(frm,text="Open",font=("arial",20,"bold"),bd=5,command=openaccountdb)
    open_btn.place(relx=.45,rely=.6)
    
    reset_btn=Button(frm,text="Reset",font=("arial",20,"bold"),bd=5,command=reset)
    reset_btn.place(relx=.55,rely=.6)
    

def fpscreen():
    frm=Frame(win)
    frm.configure(bg="pink")
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)
    
    def back():
        frm.destroy()
        mainscreen()
        
    def getpassdb():
        acn=e_acn.get()
        email=e_email.get()
        mobile=e_mobile.get()
        
        conobj=sqlite3.connect(database="banking.sqlite") 
        curobj=conobj.cursor()
        curobj.execute("select pass from accounts where acn=? and email=? and mobile=?",(acn,email,mobile))
        tup=curobj.fetchone()
        conobj.close()
        if tup==None:
                messagebox.showerror("Forgot Password","Invalid Details!")
        else:
            messagebox.showinfo("Forgot Password",f"Your Password:{tup[0]}")
            
    def reset():
        e_acn.delete(0,"end")
        e_email.delete(0,"end")
        e_mobile.delete(0,"end")
        e_acn.focus()
        
    back_btn=Button(frm,text="Back",font=("arial",20,"bold"),bd=5,command=back)
    back_btn.place(relx=0,rely=0)
    
    lbl_acn=Label(frm,text="Account",font=("arial",20,"bold"),fg="blue",bg="pink")
    lbl_acn.place(relx=.3,rely=.2)
    
    e_acn=Entry(frm,font=("arial",20,"bold"),bd=5)
    e_acn.place(relx=.42,rely=.2)
    e_acn.focus()
    
    lbl_email=Label(frm,text="Email",font=("arial",20,"bold"),fg="blue",bg="pink")
    lbl_email.place(relx=.3,rely=.3)
    
    e_email=Entry(frm,font=("arial",20,"bold"),bd=5)
    e_email.place(relx=.42,rely=.3)
    
    lbl_mobile=Label(frm,text="Mobile",font=("arial",20,"bold"),fg="blue",bg="pink")
    lbl_mobile.place(relx=.3,rely=.4)
    
    e_mobile=Entry(frm,font=("arial",20,"bold"),bd=5)
    e_mobile.place(relx=.42,rely=.4)
    
    recvr_btn=Button(frm,text="Recover",font=("arial",20,"bold"),bd=5,command=getpassdb)
    recvr_btn.place(relx=.43,rely=.5)
    
    reset_btn=Button(frm,text="Reset",font=("arial",20,"bold"),bd=5,command=reset)
    reset_btn.place(relx=.56,rely=.5)
    

def homescreen():
    frm=Frame(win)
    frm.configure(bg="pink")
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)
    
    def logout():
        frm.destroy()
        mainscreen()
        
    def details():
        ifrm=Frame(frm,highlightbackground="black",highlightthickness=2)
        ifrm.configure(bg="white")
        ifrm.place(relx=.22,rely=.16,relwidth=.7,relheight=.69)
        
        lbl=Label(ifrm,text="THIS IS DETAILS SCREEN",font=("arial",18,"bold"),fg="blue",bg="white")
        lbl.pack()
        
        conobj=sqlite3.connect(database="banking.sqlite") 
        curobj=conobj.cursor()
        curobj.execute("select * from accounts where acn=?",(uacn,))
        tup=curobj.fetchone()
        conobj.close()
        
        lbl_acn=Label(ifrm,text=f"Account Number\t{tup[0]}",font=("arial",15,"bold"),bg="white")
        lbl_acn.place(relx=.3,rely=.2)
        
        lbl_bal=Label(ifrm,text=f"Account Balance\t{tup[5]}",font=("arial",15,"bold"),bg="white")
        lbl_bal.place(relx=.3,rely=.34)
        
        lbl_type=Label(ifrm,text=f"Account Type\t{tup[6]}",font=("arial",15,"bold"),bg="white")
        lbl_type.place(relx=.3,rely=.48)
        
        lbl_opendate=Label(ifrm,text=f"Account Date\t{tup[7]}",font=("arial",15,"bold"),bg="white")
        lbl_opendate.place(relx=.3,rely=.64)
        
        
    def profile():
        ifrm=Frame(frm,highlightbackground="black",highlightthickness=2)
        ifrm.configure(bg="white")
        ifrm.place(relx=.22,rely=.16,relwidth=.7,relheight=.69)
        
        def updatedb():
            name=e_name.get()
            pwd=e_pass.get()
            email=e_email.get()
            mobile=e_mobile.get()
            
            conobj=sqlite3.connect(database="banking.sqlite") 
            curobj=conobj.cursor()
            curobj.execute("update accounts set name=?,pass=?,email=?,mobile=? where acn=?",(name,pwd,email,mobile,uacn))
            conobj.commit()
            conobj.close()
            messagebox.showinfo("Update Profile","Record Updated")
            global uname
            uname=name
            ifrm.destroy()
            homescreen()
            
        lbl=Label(ifrm,text="THIS IS UPDATE PROFILE SCREEN",font=("arial",18,"bold"),fg="blue",bg="white")
        lbl.pack()
        
        conobj=sqlite3.connect(database="banking.sqlite") 
        curobj=conobj.cursor()
        curobj.execute("select * from accounts where acn=?",(uacn,))
        tup=curobj.fetchone()
        conobj.close()
        
        lbl_name=Label(ifrm,text="Name",font=("arial",15,"bold"),bg="white")
        lbl_name.place(relx=.15,rely=.2)
        
        e_name=Entry(ifrm,font=("arial",15,"bold"),bd=5)
        e_name.place(relx=.15,rely=.28)
        
        lbl_email=Label(ifrm,text="Email",font=("arial",15,"bold"),bg="white")
        lbl_email.place(relx=.65,rely=.2)
        
        e_email=Entry(ifrm,font=("arial",15,"bold"),bd=5)
        e_email.place(relx=.65,rely=.28)
        
        lbl_pass=Label(ifrm,text="Password",font=("arial",15,"bold"),bg="white")
        lbl_pass.place(relx=.15,rely=.5)
        
        e_pass=Entry(ifrm,font=("arial",15,"bold"),bd=5)
        e_pass.place(relx=.15,rely=.58)
        
        lbl_mobile=Label(ifrm,text="Mobile",font=("arial",15,"bold"),bg="white")
        lbl_mobile.place(relx=.65,rely=.5)
        
        e_mobile=Entry(ifrm,font=("arial",15,"bold"),bd=5)
        e_mobile.place(relx=.65,rely=.58)
        
        update_btn=Button(ifrm,text="Update",font=("arial",20,"bold"),bd=5,command=updatedb)
        update_btn.place(relx=.45,rely=.7)
        
        conobj=sqlite3.connect(database="banking.sqlite") 
        curobj=conobj.cursor()
        curobj.execute("select * from accounts where acn=?",(uacn,))
        tup=curobj.fetchone()
        conobj.close()
        
        e_name.insert(0,tup[1])
        e_pass.insert(0,tup[2])
        e_email.insert(0,tup[3])
        e_mobile.insert(0,tup[4])
        
        
    def deposit():
        ifrm=Frame(frm,highlightbackground="black",highlightthickness=2)
        ifrm.configure(bg="white")
        ifrm.place(relx=.22,rely=.16,relwidth=.7,relheight=.69)
        
        def depositdb():
            amt=float(e_amt.get())
            conobj=sqlite3.connect(database="banking.sqlite")
            curobj=conobj.cursor()
            curobj.execute("select bal from accounts where acn=?",(uacn,))
            tup=curobj.fetchone()
            bal=tup[0]
            curobj.close()
            
            curobj=conobj.cursor()
            curobj.execute("update accounts set bal=bal+? where acn=?",(amt,uacn))
            conobj.commit()
            conobj.close()
            messagebox.showinfo("Deposit",f"Amount {amt} Deposited,Updated Bal:{bal+amt}")
            
        
        lbl=Label(ifrm,text="THIS IS DEPOSIT SCREEN",font=("arial",18,"bold"),fg="blue",bg="white")
        lbl.pack()
        
        lbl_amt=Label(frm,text="Amount",font=("arial",20,"bold"),fg="black",bg="white")
        lbl_amt.place(relx=.35,rely=.3)
    
        e_amt=Entry(frm,font=("arial",20,"bold"),bd=5)
        e_amt.place(relx=.45,rely=.3)
        
        deposit_btn=Button(ifrm,text="Deposit",font=("arial",20,"bold"),bd=5,command=depositdb)
        deposit_btn.place(relx=.42,rely=.35)
        
        
    def withdraw():
        ifrm=Frame(frm,highlightbackground="black",highlightthickness=2)
        ifrm.configure(bg="white")
        ifrm.place(relx=.22,rely=.16,relwidth=.7,relheight=.69)
        
        def withdrawdb():
            amt=float(e_amt.get())
            conobj=sqlite3.connect(database="banking.sqlite") 
            curobj=conobj.cursor()
            curobj.execute("select bal from accounts where acn=?",(uacn,))
            tup=curobj.fetchone()
            bal=tup[0]
            curobj.close()
            if bal>=amt:
                curobj=conobj.cursor()
                curobj.execute("update accounts set bal=bal-? where acn=?",(amt,uacn))
                conobj.commit()
                conobj.close()
                messagebox.showinfo("Withdraw",f"Amount {amt} Withdrawn,Updated Bal:{bal-amt}")
            else:
                messagebox.showwarning("Withdraw",f"Insufficient Bal:{bal}")
                
            
        lbl=Label(ifrm,text="THIS IS WITHDRAW SCREEN",font=("arial",18,"bold"),fg="blue",bg="white")
        lbl.pack()
        
        lbl_amt=Label(frm,text="Amount",font=("arial",20,"bold"),fg="black",bg="white")
        lbl_amt.place(relx=.35,rely=.3)
    
        e_amt=Entry(frm,font=("arial",20,"bold"),bd=5)
        e_amt.place(relx=.45,rely=.3)
        
        withdraw_btn=Button(ifrm,text="Withdraw",font=("arial",20,"bold"),bd=5,command=withdrawdb)
        withdraw_btn.place(relx=.41,rely=.35)
        
        
    def transfer():
        ifrm=Frame(frm,highlightbackground="black",highlightthickness=2)
        ifrm.configure(bg="white")
        ifrm.place(relx=.22,rely=.16,relwidth=.7,relheight=.69)
        
        def transferdb():
            to=e_to.get()
            amt=float(e_amt.get())
            conobj=sqlite3.connect(database="banking.sqlite") 
            curobj=conobj.cursor()
            curobj.execute("select *from accounts where acn=?",(to,))
            tup=curobj.fetchone()
            curobj.close()
            if tup==None:
                messagebox.showerror("Transfer","To Account does not exist!")
            else:
                curobj=conobj.cursor()
                curobj.execute("select bal from accounts where acn=?",(uacn,))
                tup=curobj.fetchone()
                bal=tup[0]
                curobj.close()
                if bal>=amt:
                    curobj=conobj.cursor()
                    curobj.execute("update accounts set bal=bal-? where acn=?",(amt,uacn))
                    curobj.execute("update accounts set bal=bal+? where acn=?",(amt,to))
                    conobj.commit()
                    conobj.close()
                    messagebox.showinfo("Transfer",f"Amount {amt} Transfered to ACN:{to}")
                else:
                    messagebox.showwarning("Transfer",f"Insufficient Bal:{bal}")
                
                
        lbl=Label(ifrm,text="THIS IS TRANSFER SCREEN",font=("arial",18,"bold"),fg="blue",bg="white")
        lbl.pack()
        
        lbl_to=Label(frm,text="To",font=("arial",20,"bold"),fg="black",bg="white")
        lbl_to.place(relx=.35,rely=.3)
    
        e_to=Entry(frm,font=("arial",20,"bold"),bd=5)
        e_to.place(relx=.45,rely=.3)
        
        lbl_amt=Label(frm,text="Amount",font=("arial",20,"bold"),fg="black",bg="white")
        lbl_amt.place(relx=.35,rely=.4)
    
        e_amt=Entry(frm,font=("arial",20,"bold"),bd=5)
        e_amt.place(relx=.45,rely=.4)
        
        transfer_btn=Button(ifrm,text="Transfer",font=("arial",20,"bold"),bd=5,command=transferdb)
        transfer_btn.place(relx=.41,rely=.48)
        
        
    logout_btn=Button(frm,text="Logout",font=("arial",20,"bold"),bd=5,command=logout)
    logout_btn.place(relx=.9,rely=0)
    
    lbl_wel=Label(frm,text=f"WELCOME, {uname}",font=("arial",15,"bold"),fg="blue",bg="pink")
    lbl_wel.place(relx=0,rely=0)
    
    details_btn=Button(frm,text="Details",font=("arial",20,"bold"),bd=5,width=12,command=details)
    details_btn.place(relx=0,rely=.15)
    
    profile_btn=Button(frm,text="Update Profile",font=("arial",20,"bold"),bd=5,width=12,command=profile)
    profile_btn.place(relx=0,rely=.3)
    
    deposit_btn=Button(frm,text="Deposit",font=("arial",20,"bold"),bd=5,width=12,command=deposit)
    deposit_btn.place(relx=0,rely=.45)
    
    withdraw_btn=Button(frm,text="Withdraw",font=("arial",20,"bold"),bd=5,width=12,command=withdraw)
    withdraw_btn.place(relx=0,rely=.6)
    
    transfer_btn=Button(frm,text="Transfer",font=("arial",20,"bold"),bd=5,width=12,command=transfer)
    transfer_btn.place(relx=0,rely=.75)
    

mainscreen()
win.mainloop()


# In[ ]:





# In[ ]:





import tkinter as tk
from tkinter import*
from tkinter import messagebox

#Creating tkinter window

win=tk.Tk()    
win.title("Login")
win.geometry("1166x718")
win.configure(bg="#fff")
win.resizable(TRUE,TRUE)
win.state("zoomed")

#icon image
image_icon=PhotoImage(file="img.png")
win.iconphoto(FALSE,image_icon) 


#signin
def signin():   
    username=user.get()
    password=code.get()

    if username=="admin" and password=="1234":
        screen=Toplevel(win)
        
     


    elif username!="admin" or password!="1234":
        messagebox.showerror("Invalid","Invalid username or password")

   



#Inserting image
img= PhotoImage(file="mobilelogo.png")
Label(win,image=img,bg="white").place(x=450,y=50)

#Sign In button
frame=Frame(win,width=350,height=350,bg="white")
frame.place(x=520,y=290)

heading=Label(frame,text="Sign In",fg="#405DE6",bg="white",font=("Microsoft YaHei UI Light",23,"bold"))
heading.place(x=100,y=5)


#username
def on_enter(e):
    user.delete(0,"end")

def on_leave(e):
    name=user.get()
    if name=="":
        user.insert(0,"Username")

user = Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
user.place(x=30,y=80)
user.insert(0,"username")
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)


#Password
def on_enter(e):
    code.delete(0,"end")

def on_leave(e):
    name=code.get()
    if name=="":
        code.insert(0,"Password")


code = Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
code.place(x=30,y=150)
code.insert(0,"Password")
code.bind("<FocusIn>",on_enter)
code.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)

Button(frame,width=39,pady=7,text="Sign in",bg="#E50914",fg="White",border=0,command=signin).place(x=35,y=204)


win.mainloop()
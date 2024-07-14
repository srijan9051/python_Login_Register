from tkinter import *
from tkinter import messagebox
import mysql.connector

background="#06283D"
framebg="#EDEDED"
framefg="#08263D"


global trial_no
trial_no=0

def trial():
    global trial_no

    trial_no+=1
    if (3-trial_no==1):
        messagebox.showinfo("Error",f"Wrong Password, This is your last attempt")
    elif (3-trial_no==0):
        pass
    else:
        messagebox.showinfo("Error",f"Wrong Username or Password, only {3-trial_no} attempt left..")
    #print(f"You have only {3-trial_no} left")
    if trial_no==3:
        messagebox.showwarning("Warning","You have exceeded the limit to login")
        root.destroy()


def loginuser():
    username=user.get()
    password=code.get()
    
    if (username=="" or username=="UserID") or (password=="" or password=="Password"):
        messagebox.showerror("Entry error","Type username or password!!")

    else:
        try:
            mydb=mysql.connector.connect(host='localhost',user='root',password='Srijan@2000',database="studentregistration")
            mycursor=mydb.cursor()
            print("connected successfully....")
        except:
            messagebox.showerror("Connection","Database not connected")
            return
        command="use studentregistration"
        mycursor.execute(command)

        command="select * from login where Username=%s and Password=%s"
        mycursor.execute(command,(username,password))
        myresult=mycursor.fetchone()

        if myresult==None:
            #messagebox.showinfo("invalid","Invalid userid and password")
            trial()
        else:
            messagebox.showinfo("Login","Successfully loggedin!!!!")
            root.destroy()
            import main

def register():
    root.destroy()
    import register



root=Tk()
root.title("Login System")
root.geometry("1250x700+210+100")
root.config(bg=background)
root.resizable(False,False)


#icon-image
image_icon=PhotoImage(file="Images/icon.png")
root.iconphoto(False,image_icon)

#background image
frame=Frame(root,bg="red")
frame.pack()

backgroundimage=PhotoImage(file="Images/LOGIN.png")
Label(frame,image=backgroundimage).pack()

#user entry
def user_enter(e):
    user.delete(0,'end')

def user_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'UserID')


user=Entry(frame,width=18,fg="#fff",border=0,bg="#375174",font=('Arial Bold',24))
user.insert(0,'UserID')
user.bind("<FocusIn>",user_enter)
user.bind("<FocusOut>",user_leave)
user.place(x=500,y=315)


#password entry
def password_enter(e):
    code.config(show="*")
    code.delete(0,'end')
def password_leave(e):
    if code.get()=='':
        code.insert(0,"Password")


code=Entry(frame,width=18,fg="#fff",border=0,bg="#375174",font=('Arial Bold',24))
code.insert(0,'Password')
code.bind("<FocusIn>",password_enter)
code.bind("<FocusOut>",password_leave)
code.place(x=500,y=410)

######Hide show button####
Button_mode=True
def hide():
    global Button_mode
    if Button_mode:
        eyeButton.config(image=openeye,activebackground="white")
        code.config(show="")
        Button_mode=False
    else:
        eyeButton.config(image=closeeye,activebackground="white")
        code.config(show="*")
        Button_mode=True


openeye=PhotoImage(file="Images/openeye.png")
closeeye=PhotoImage(file="Images/close eye.png")
eyeButton=Button(frame,image=closeeye,bg="#375174",bd=0,cursor="hand2",command=hide)
eyeButton.place(x=780,y=410)

#########################

#####login button########
loginButton=Button(root,text="LOGIN",bg="#1f5675",fg="white",cursor="hand2",width=10,height=1,font=("arial",16,'bold'),bd=0,command=loginuser)
loginButton.place(x=570,y=600)

Label=Label(root,text="Don't have an account",fg="#fff",bg="#00264d",font=('Microsoft YaHei UI Light',9))
Label.place(x=500,y=500)

registerButton=Button(root,width=10,text="add new user",border=0,bg="#00264d",cursor="hand2",fg="#57a1f8",command=register)
registerButton.place(x=650,y=500)

root.mainloop()
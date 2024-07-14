from tkinter import *
from tkinter import messagebox
import mysql.connector


def register():
    username=user.get()
    password=code.get()
    admincode=adminaccess.get()

    #print(username,password,admincode)
    if admincode=="9051":
        if(username=="" or username=="UserId") or (password=="" or password=="Password"):
            messagebox.showerror("Entry Error!!","Please enter username or password")
        else:
            try:
                mydb=mysql.connector.connect(host='localhost',user='root',password='Srijan@2000')
                mycursor=mydb.cursor()
                print("Connected to database")

            except:
                messagebox.showerror("Connection","database not connected!!!")
            
            try:
                command="create database StudentRegistration"
                mycursor.execute(command)

                command="use StudentRegistration"
                mycursor.execute(command)

                command="create table login (user int auto_increment key not null,Username varchar(50),Password varchar(100))"
                mycursor.execute(command)
            except:
                mycursor.execute("use StudentRegistration")
                mydb=mysql.connector.connect(host='localhost',user='root',password='Srijan@2000',database="StudentRegistration")
                mycursor=mydb.cursor()

                command="insert into login(Username,Password) values(%s,%s)"
                mycursor.execute(command,(username,password))
                mydb.commit()
                mydb.close()
                messagebox.showinfo("Register","New user added successfully!!!")
                root.destroy()
                import login
    else:
        messagebox.showerror("Admin Code","Wrong admin code")



def login():
    root.destroy()
    import login


background="#06283D"
framebg="#EDEDED"
framefg="#06283D"

root=Tk()
root.title("User Registration")
root.geometry("1250x700+210+100")
root.config(bg=background)
root.resizable(False,False)

#icon-image
image_icon=PhotoImage(file="Images/icon.png")
root.iconphoto(False,image_icon)

#background-image
frame=Frame(root,bg="red")
frame.pack(fill=Y)

backgroundimage=PhotoImage(file="Images/register.png")
Label(frame,image=backgroundimage).pack()

adminaccess=Entry(frame,width=15,fg="#000",border=0,bg="#e8ecf7",font=("Arial Bold",20),show="*")
adminaccess.focus()
adminaccess.place(x=550,y=280)

###########User Entry###########
def user_enter(e):
    user.delete(0,'end')
def user_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,"UserId")

user=Entry(frame,width=18,fg="#fff",bg="#375174",border=0,font=("Arial Bold",20))
user.insert(0,"UserID")
user.bind("<FocusIn>",user_enter)
user.bind("<FocusOut>",user_leave)
user.place(x=500,y=380)
#####################################
###########Password Entry###########
def Password_enter(e):
    code.config(show="*")
    code.delete(0,'end')
def Password_leave(e):
    if code.get()=='':
        code.insert(0,"Password")

code=Entry(frame,width=18,fg="#fff",bg="#375174",border=0,font=("Arial Bold",20))
code.insert(0,"Password")
code.bind("<FocusIn>",Password_enter)
code.bind("<FocusOut>",Password_leave)
code.place(x=500,y=470)
#####################################################
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

eyeButton=Button(root,image=closeeye,bg="#375174",bd=0,cursor="hand2",command=hide)
eyeButton.place(x=780,y=470)
#####################################################################

regis_button=Button(root,text="Add New User",bg="#455c88",cursor="hand2",fg="white",width=13,height=1,font=("Arial",16,"bold"),bd=0,command=register)
regis_button.place(x=530,y=600)


backbuttonimage=PhotoImage(file="Images/backbutton.png")
Backbutton=Button(root,image=backbuttonimage,fg="#deeefb",cursor="hand2",command=login)
Backbutton.place(x=20,y=10)











root.mainloop()
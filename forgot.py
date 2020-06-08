from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import loginbackend
import login


def update_command():
    check = loginbackend.update(username.get(),security_answer.get(),New_Password.get())
    if check == 'True' :
        messagebox.showinfo(title="success",message="Password Updated Successfully")
        
    else:
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        messagebox.showinfo(title="Error", message="Invalid Creditials")

def log_des():
    login_screen.quit()
    login_screen.destroy()
    import main


def quit_me():
    print('quit')
    login_screen.quit()
    login_screen.destroy()


login_screen = Tk()
login_screen.protocol("WM_DELETE_WINDOW", quit_me)
login_screen.title("Forgot Password")
login_screen.geometry('300x300')

l1 = Label(login_screen, text='Username*',padx=10,pady=10,height=1)
l1.grid(row=1,column=1,padx=20, columnspan=2)
username = StringVar()
e1 = Entry(login_screen,textvariable=username, width=30)
e1.grid(row=2,column=1,padx=20, columnspan=2)

l2 = Label(login_screen, text="Answer of security question*" ,padx=10,pady=10,height=1)
l2.grid(row=3,column=1,padx=20, columnspan=2)
security_answer = StringVar()
e2 = Entry(login_screen,textvariable=security_answer, width=30)
e2.grid(row=4,column=1,padx=20, columnspan=2)

l2 = Label(login_screen, text='New Password*',padx=10,pady=10,height=1)
l2.grid(row=5,column=1,padx=20, columnspan=2)
New_Password = StringVar()
e3 = Entry(login_screen,textvariable=New_Password, width=30)
e3.grid(row=6,column=1,padx=20, columnspan=2)

b1 = Button(login_screen, text='Home',bg="gray",fg='black',height=1,width=15,padx=5,pady=5,command= log_des)
b1.grid(row=7,column=1,padx=5,pady=5)
b2 = Button(login_screen, text='Update',bg="gray",fg='black',height=1,width=15,padx=5,pady=5,command=update_command)
b2.grid(row=7,column=2,padx=5,pady=5)


login_screen.mainloop()

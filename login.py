from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import loginbackend


def log_verify():
    check = loginbackend.login_verify(username.get(),password.get())
    if check == 'True' :
        print("Logged in")
    else:
        print("Invalid Creditials")



def forget_pass():
    login_screen.quit()
    login_screen.destroy()
    import forgot

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
login_screen.title("Login")
login_screen.geometry('300x300')

l1 = Label(login_screen, text='Username*',padx=10,pady=10,height=1)
l1.grid(row=1,column=1,padx=20, columnspan=2)
username = StringVar()
e1 = Entry(login_screen,textvariable=username, width=30)
e1.grid(row=2,column=1,padx=20, columnspan=2)
l2 = Label(login_screen, text='Password*',padx=10,pady=10,height=1)
l2.grid(row=3,column=1,padx=20, columnspan=2)
password = StringVar()
e2 = Entry(login_screen,textvariable=password, width=30)
e2.grid(row=4,column=1,padx=20, columnspan=2)

b1 = Button(login_screen, text='Home',bg="gray",fg='black',height=1,width=15,padx=5,pady=5,command= log_des)
b1.grid(row=5,column=1,padx=5,pady=5)
b2 = Button(login_screen, text='Login',bg="gray",fg='black',height=1,width=15,padx=5,pady=5, command=log_verify)
b2.grid(row=5,column=2,padx=5,pady=5)
b3 = Button(login_screen, text='Forgot Password',bg="gray",fg='black',height=1,width=30,padx=5,pady=5,command=forget_pass)
b3.grid(row=7,column=1,padx=5,pady=5, columnspan=2)


login_screen.mainloop()

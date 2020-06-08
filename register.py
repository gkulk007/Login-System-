from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import loginbackend

def add_command():
    loginbackend.insert(username_entry.get(),password_entry.get(),security_question.get(),security_answer.get())
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    messagebox.showinfo(title="Registration",
    message="""
    Data has been added Successfully,
    Please remember your security question and answer""")
    register_screen.quit()
    register_screen.destroy()
    import login


def reg_des():
    register_screen.quit()
    register_screen.destroy()
    import main


def quit_me():
    print('quit')
    register_screen.quit()
    register_screen.destroy()


register_screen = Tk()
register_screen.protocol("WM_DELETE_WINDOW", quit_me)
register_screen.title("Register")
register_screen.geometry('500x350')

l1 = Label(register_screen, text='Username*',padx=10,pady=10,height=1)
l1.grid(row=1,column=1,padx=20, columnspan=2)
username_entry = StringVar()
e3 = Entry(register_screen,textvariable=username_entry, width=30)
e3.grid(row=2,column=1,padx=20, columnspan=2)
l2 = Label(register_screen, text='Password*',padx=10,pady=10,height=1)
l2.grid(row=3,column=1,padx=20, columnspan=2)
password_entry = StringVar()
e4 = Entry(register_screen,textvariable=password_entry, width=30)
e4.grid(row=4,column=1,padx=20, columnspan=2)

security_question = StringVar()
l5 = Label(register_screen, text='Choose security question',padx=10,pady=10,height=1)
l5.grid(row=5,column=1,padx=20, columnspan=2)
e5 = Combobox(register_screen,width=30,textvariable=security_question)
e5['values'] = ('What is your pet’s name?',
'What is your favorite place ?','Last 4 digits of driving license',
'What is Your mother madien name?','Name of Childhood bestfriend?'
)
e5.grid(row=6,column=1,columnspan=3)
e5.current(0)
security_answer = StringVar()
e6 = Entry(register_screen,textvariable=security_answer, width=30)
e6.grid(row=7,column=1,padx=20,pady=20, columnspan=2)


b1 = Button(register_screen, text='Home',bg="gray",fg='black',height=1,width=15,padx=5,pady=5,command= reg_des)
b1.grid(row=8,column=1,padx=5,pady=5)
b2 = Button(register_screen, text='Register',bg="gray",fg='black',height=1,width=15,padx=5,pady=5,command=add_command)
b2.grid(row=8,column=2,padx=5,pady=5)




register_screen.mainloop()

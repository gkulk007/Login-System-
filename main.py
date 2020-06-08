from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import loginbackend


loginbackend.connect()

def login():
    main_screen.quit()
    main_screen.destroy()
    import login


def register():
    main_screen.quit()
    main_screen.destroy()
    import register


def quit_me():
    # print('quit')
    main_screen.quit()
    main_screen.destroy()


main_screen = Tk()
main_screen.protocol("WM_DELETE_WINDOW", quit_me)
main_screen.geometry("300x250")
main_screen.title("Account Login")
Label(text="Select Your Choice", bg="skyblue", width="300", height="2", font=("Calibri", 13)).pack()
Label(text="").pack()
Button(text="Login", height="2", width="30", command=login, bg="gray",fg="black").pack()
Label(text="").pack()
Button(text="Register", height="2", width="30", command=register, bg="gray",fg="black").pack()

main_screen.mainloop()

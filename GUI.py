from SignUp import sign_up
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Sign Up")
window.geometry("925x480+300+200")
window.config(bg="#fff")
window.resizable(False, False)

img = PhotoImage(file="C:\\Users\\Dell\\Desktop\\uni4012\\AP\\TAMRIN\\LogIn-Form-TKInter\\login.png")
Label(window, image=img, border=0, bg='white').place(x=50, y=90)

frame = Frame(window, width=350, height=390, bg="#fff")
frame.place(x=480, y=50)


heading = Label(window, text="Sign Up", fg="#57a1f8", bg="white", font=("Microsoft Yahei UI Light", 23, "bold"))
heading.place(x=170, y=45)



#===============================================================

def select(arg):
    user.delete(0, 8)
    user_frame.config(bg='blue')
def deselect(arg):
    if user.get() == '':
        user.insert(0, "Username")
        user_frame.config(bg='red')
    else:
        user_frame.config(bg='cyan')

user = Entry(frame, width=25, fg='black', border=0, bg="white", font=("Microsoft Yahei UI Light", 11))
user.place(x=30, y=10)
user.insert(0, "Username")
user.bind("<FocusIn>", select)
user.bind("<FocusOut>", deselect)

user_frame = Frame(frame, width=295, height=2, bg='black')
user_frame.place(x=25, y=37)
#===============================================================

def select(arg):
    email.delete(0, 8)
    email_frame.config(bg='blue')
def deselect(arg):
    if email.get() == '':
        email.insert(0, "Email")
        email_frame.config(bg='red')
    else:
        email_frame.config(bg='cyan')

email = Entry(frame, width=25, fg='black', border=0, bg="white", font=("Microsoft Yahei UI Light", 11))
email.place(x=30, y=80)
email.insert(0, "Email")
email.bind("<FocusIn>", select)
email.bind("<FocusOut>", deselect)

email_frame = Frame(frame, width=295, height=2, bg='black')
email_frame.place(x=25, y=107)


#===============================================================


def select(arg):
    password.delete(0, 8)
    password_frame.config(bg='blue')
def deselect(arg):
    if password.get() == '':
        password.insert(0, "Password")
        password_frame.config(bg='red')
    else:
        password_frame.config(bg='cyan')


password = Entry(frame, width=25, fg='black', border=0, bg="white", font=("Microsoft Yahei UI Light", 11), show='*')
password.place(x=30, y=150)
password.insert(0, "Password")
password.bind("<FocusIn>", select)
password.bind("<FocusOut>", deselect)

password_frame = Frame(frame, width=295, height=2, bg='black')
password_frame.place(x=25, y=177)

#===============================================================


def select(arg):
    reenter_password.delete(0, 21)
    reenter_password_frame.config(bg='blue')

def deselect(arg):
    if reenter_password.get() == '':
        reenter_password.insert(0, "Confirm Your Password")
        reenter_password_frame.config(bg='red')
    else:
        reenter_password_frame.config(bg='cyan')


reenter_password = Entry(frame, width=25, fg='black', border=0, bg="white", font=("Microsoft Yahei UI Light", 11), show='*')
reenter_password.place(x=30, y=220)
reenter_password.insert(0, "Confirm Your Password")
reenter_password.bind("<FocusIn>", select)
reenter_password.bind("<FocusOut>", deselect)

reenter_password_frame = Frame(frame, width=295, height=2, bg='black')
reenter_password_frame.place(x=25, y=247)

#===============================================================


def sign_up_to_app():
    username = user.get()
    e_mail = email.get()
    passcode = password.get()
    pass_confirm = reenter_password.get()
    sign_up(username, e_mail, passcode, pass_confirm)



sign_up_btn = Button(frame, width=39, pady=7, text="Sign Up", bg="#57a1f8", fg="white", border=0, command=sign_up_to_app)
sign_up_btn.place(x=35, y=280)

have_account_lbl = Label(frame, text="I have an account,", fg="black", bg="white", font=("Microsoft YaHei UI Light", 9))
have_account_lbl.place(x=90, y=340)

sign_in = Button(frame, width=6, text="Sign in!", border=0, bg="white", cursor="hand2", fg="#57a1f8", command=lambda: messagebox.showerror(title="ok!", message="That doesn't really matter, create a new account"))
sign_in.place(x=200, y=340)



window.mainloop()
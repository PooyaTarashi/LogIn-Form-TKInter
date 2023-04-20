from tkinter import *
from tkinter import messagebox
import ast

window = Tk()
window.title("Sign Up")
window.geometry("925x500+300+200")
window.config(bg="#fff")
window.resizable(False, False)

img = PhotoImage(file="C:\\Users\\Dell\\Desktop\\uni4012\\AP\\TAMRIN\\LogIn-Form-TKInter\\login.png")
Label(window, image=img, border=0, bg='white').place(x=50, y=90)

frame = Frame(window, width=350, height=390, bg="#fff")
frame.place(x=480, y=50)


heading = Label(frame, text="Sign Up", fg="#57a1f8", bg="white", font=("Microsoft Yahei UI Light", 23, "bold"))
heading.place(x=100, y=5)


user = Entry(frame, width=25, fg='black', border=0, bg="white", font=("Microsoft Yahei UI Light", 11))
user.place(x=30, y=80)
user.insert(0, "Username")




window.mainloop()
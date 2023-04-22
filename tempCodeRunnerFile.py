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
from tkinter import messagebox
import re

def check_username(sign_up):
    from functools import wraps
    @wraps(sign_up)
    def inner(username:str, *args):
        if username.isalnum() == False:
            messagebox.showerror("Invalid username", "your username must be made up of alphanumeric characters!")
            pass
        else:
            sign_up(username, *args)
    return inner


def check_email(sign_up):
    from functools import wraps
    @wraps(sign_up)
    def inner(*args):
        email = args[1]
        email_pattern = r"[^@]+@[^@]+\.[^@]+"
        is_valid = re.match(email_pattern, email)
        if is_valid == None:
            messagebox.showerror("Invalid email", "Email address must have address@mail.com form")
            pass
        else:
            sign_up(*args)
    return inner


def check_pass(sign_up):
    from functools import wraps
    @wraps(sign_up)
    def inner(*args):
        password = args[2]
        pass_pattern = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$'
        is_valid = re.match(pass_pattern, password)
        if is_valid == None:
            messagebox.showerror("Invalid password", "Your email must be made up of Latin characters and must have at least one digitand one special charactrer!")
            pass
        elif len(password) < 8:
            messagebox.showerror("Invalid password", "Your password must contain at least 8 characters!")
            pass
        else:
            sign_up(*args)
    return inner

def check_confirmation(sign_up):
    from functools import wraps
    @wraps(sign_up)
    def inner(*args):
        if args[2] != args[3]:
            messagebox.showerror("Password and Password Confirmation Mismatch!", "Password and password confirmation do not match. Please make sure you enter the same password in both fields.")
            sys.exit()
        else:
            sign_up(*args)
    return inner



@check_username
@check_email
@check_pass
@check_confirmation
def sign_up(username, email, password, password_confirmation):
    messagebox.showinfo("Done!", "You logged in as {0}\nYour email address is {1}\n and your password is {2}".format(username, email, password))




if __name__ == '__main__':
    pass
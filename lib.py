import smtplib
import sqlite3
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("1000x562+200+80")
root.resizable(False, False)
root.title("Library Management System")

# Setup SQLite database connection
def create_database():
    con = sqlite3.connect('amanlib.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS admin_logindata (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL,
                    email TEXT NOT NULL,
                    name TEXT NOT NULL)''')
    con.commit()
    con.close()

create_database()

# Login Button Function
def loginbtnfunc():
    global user, passw, Admin_name, con, cur
    user = username.get()
    passw = password.get()
    if user == "" or passw == "":
        messagebox.showinfo("Notification", "All fields are required", parent=root)
    elif len(passw) < 8:
        messagebox.showerror("Notification", "Password Must be of 8 Characters!!!", parent=root)
    else:
        try:
            con = sqlite3.connect('amanlib.db')
            cur = con.cursor()
            query = 'SELECT * FROM admin_logindata WHERE username=? AND password=?;'
            cur.execute(query, (user, passw))
            result = cur.fetchone()
            if result:
                root.withdraw()
                Admin_name = result[4]
                openTop()
            else:
                messagebox.showerror('Notification', 'Incorrect Username or Password!!!\nPlease try again...', parent=root)
                loginForgetPassbtn.place(x=500, y=455)
            con.close()
        except Exception as e:
            print(e)
            messagebox.showerror('Notification', 'Something is wrong!!!\nPlease try again...', parent=root)
            return

# Login Frame Labels
titleLabel = Label(root, text='LOGIN SYSTEM', font=('Georgia', 20, 'italic bold'), bg="#6D93B1", fg="white", height=2, relief=GROOVE, bd=2)
titleLabel.place(x=1, y=1, relwidth=1)

usernameLabel = Label(root, text="Username :", font=('times', 15, 'italic bold'))
usernameLabel.place(x=300, y=275)

passwordLabel = Label(root, text="Password :", font=('times', 15, 'italic bold'))
passwordLabel.place(x=300, y=355)

# Login Entry Boxes
username = StringVar()
password = StringVar()

usernameEntry = Entry(root, textvariable=username, width=25, font=('times', 15, 'italic'), bd=5, bg='lightblue')
usernameEntry.place(x=420, y=270)
usernameEntry.focus()

passwordEntry = Entry(root, width=25, show='*', textvariable=password, font=('times', 15, 'italic'), bd=5, bg='lightblue')
passwordEntry.place(x=420, y=350)

# Login Submit Button
loginbtn = Button(root, text='Login', font=('times', 13, 'italic bold'), bg='lightgreen', bd=5, activebackground='green',
                  activeforeground='white', command=loginbtnfunc, width=8)
loginbtn.place(x=580, y=410)

def ForGetPass(event):
    root.withdraw()
    Forget = Toplevel()
    Forget.geometry('500x290')
    Forget.resizable(False, False)
    Forget.title('Forget PassWord')

    for_frame = Frame(Forget, bd=4, relief='groove', bg='red')
    for_frame.place(x=0, y=0, relwidth=1, relheight=1)

    ForTitle = Label(for_frame, text='Enter Verified Email ID', font=('serif', 15, 'italic'), bg='#6D93B1', fg='White', bd=3,
                     relief='groove')
    ForTitle.place(x=10, y=5, width=468)

    forcan = Canvas(for_frame)
    forcan.place(x=0, y=0, relwidth=1, relheight=1)

    emailLabel = Label(for_frame, text="Email :", font=('Time', 12, 'bold'))
    emailLabel.place(x=60, y=110)

    Emailval = StringVar()
    ForEmailVal = Entry(for_frame, textvariable=Emailval, font=('Time', 12, 'italic'), bd=3, width=28)
    ForEmailVal.place(x=145, y=110)

    def SendMail():
        if Emailval.get() == '':
            messagebox.showerror('Error', "Email Field Cannot be Empty  !!!", parent=for_frame)
        else:
            try:
                con = sqlite3.connect('amanlib.db')
                cur = con.cursor()
                query = 'SELECT password FROM admin_logindata WHERE email = ?;'
                cur.execute(query, (Emailval.get(),))
                result = cur.fetchone()
                if result:
                    Otp = random.randint(1000, 9999)
                    print(Otp)

                    # Send Mail
                    sender = 'amanmakode993@gmail.com'
                    reciver = Emailval.get()
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(sender, 'yourpassword')
                    server.sendmail(sender, reciver, f'These Is Your XIE Library \n\n \tEmail ID : {Emailval.get()} \n\n \tOTP       : {Otp}')
                    server.quit()

                    def NewPass():
                        if otpval.get() == '':
                            messagebox.showinfo('INFORMATION', "OTP Field cannot be Empty !!!", parent=for_frame)
                        else:
                            if otpval.get() == str(Otp):
                                NewPass_frame = Frame(Forget, bd=4, relief='groove', bg='yellow')
                                NewPass_frame.place(x=0, y=0, relwidth=1, relheight=1)

                                newpassLabel = Label(NewPass_frame, text="New Password :", font=('Time', 12, 'bold'))
                                newpassLabel.place(x=60, y=100)

                                NewPassval = StringVar()
                                NewPassLabval = Entry(NewPass_frame, textvariable=NewPassval, font=('Times', 12, 'italic'), bd=4)
                                NewPassLabval.place(x=220, y=100)

                                confirmPassLabel = Label(NewPass_frame, text="Confirm Password :", font=('Time', 12, 'bold'))
                                confirmPassLabel.place(x=60, y=150)

                                ConNewPassval = StringVar()
                                ConNewPassLabval = Entry(NewPass_frame, show='*', textvariable=ConNewPassval,
                                                         font=('Times', 12, 'italic'), bd=4)
                                ConNewPassLabval.place(x=220, y=150)

                                def ConPass():
                                    if NewPassval.get() != '' and ConNewPassval.get() != '':
                                        if len(NewPassval.get()) >= 8:
                                            if NewPassval.get() == ConNewPassval.get():
                                                query = 'UPDATE admin_logindata SET password = ? WHERE email = ?;'
                                                cur.execute(query, (ConNewPassval.get(), Emailval.get()))
                                                con.commit()
                                                messagebox.showinfo('INFORMATION', "Password Successfully Updated !!!", parent=for_frame)
                                                Forget.destroy()
                                                root.update()
                                                root.deiconify()
                                                username.set('')
                                                password.set('')
                                            else:
                                                messagebox.showwarning('WARNING', "New Password and Confirm Password Must be Same!!!", parent=for_frame)
                                        else:
                                            messagebox.showwarning('WARNING', "Password Must contain Atleast 8 Characters!!!", parent=for_frame)
                                    else:
                                        messagebox.showinfo('INFORMATION', "Any Field cannot be Empty !!!", parent=for_frame)

                                ConfirmNewPassBtn = Button(NewPass_frame, font=('Times', 13, 'bold'), bd=4, width=8,
                                                           text='Confirm', bg="sky blue", command=ConPass)
                                ConfirmNewPassBtn.place(x=300, y=190)
                            else:
                                messagebox.showwarning("WARNING", "Wrong OTP !!!", parent=for_frame)

                    otpLabel = Label(for_frame, text="OTP :", font=('Time', 12, 'bold'))
                    otpLabel.place(x=60, y=190)

                    otpval = StringVar()
                    ForotpVal = Entry(for_frame, textvariable=otpval, font=('Time', 12, 'italic'), bd=4)
                    ForotpVal.place(x=145, y=190)

                    ForotpBtn = Button(for_frame, text='Next', bg="sky blue", bd=4, font=('Times', 13, 'bold'), width=8, command=NewPass)
                    ForotpBtn.place(x=300, y=230)
                else:
                    Emailval.set('')
                    messagebox.showwarning('WARNING', "Such Email Id Is Not There In Record !!!", parent=for_frame)
                con.close()
            except Exception as e:
                print(e)
                messagebox.showerror('Error', "SomeThing Went Wrong Please Try Again Later!!!", parent=for_frame)

    ForBtn = Button(for_frame, text='Submit', font=('Times', 13, 'bold'), bd=4, bg='sky blue', command=SendMail)
    ForBtn.place(x=180, y=160)

    Forget.mainloop()

loginForgetPassbtn = Button(root, text='Forget Password', font=('time', 13, 'italic'), bg='lightgreen', bd=5, command=lambda: ForGetPass(None))
loginForgetPassbtn.place(x=510, y=455)

root.mainloop()

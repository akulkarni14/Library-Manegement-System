import subprocess
import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
from database import add_member, create_table, verify_login

create_table()

top = tk.Tk()
top.title("TechTitan's Library Management System")
top.geometry("995x575+265+120")
top.configure(bg="white")
top.resizable(width=False, height=False)
menubar = tk.Menu(top)

def logout(event=None):
    result = messagebox.askyesno("Logout", "Are you sure you want to exit?")
    if result:
        top.destroy()
    else:
        pass

def show_rules(event=None):
    rules_window = tk.Toplevel(top)
    rules_window.title("Rules and Regulations")
    rules_window.geometry("600x400+300+200")
    rules_window.configure(bg="white")
    rules_window.resizable(width=False, height=False)

    rules_label = tk.Label(rules_window, text="Library Rules and Regulations", font=("Times New Roman", 20, "bold"), bg="white", fg="brown")
    rules_label.pack(pady=20)

    rules_text = Text(rules_window, width=70, height=15, wrap=WORD, bg="white", font=("Times New Roman", 14))
    rules_text.pack(pady=10)

    rules = (
        "1. Maintain silence in the library.\n"
        "2. No eating or drinking inside the library.\n"
        "3. Handle library materials with care.\n"
        "4. Return borrowed books on time.\n"
        "5. Use the library resources responsibly.\n"
    )
    
    rules_text.insert(INSERT, rules)
    rules_text.config(state=DISABLED)

def show_contact(event=None):
    contact_window = tk.Toplevel(top)
    contact_window.title("Contact Us")
    contact_window.geometry("600x400+300+200")
    contact_window.configure(bg="white")
    contact_window.resizable(width=False, height=False)

    contact_label = tk.Label(contact_window, text="Contact Us", font=("Times New Roman", 20, "bold"), bg="white", fg="brown")
    contact_label.pack(pady=20)

    contact_info = (
        "Library Address:\n"
        "TechTitan's Library\n"
        "Ghat Khopar\n"
        "Nagpur, Itwari 11345\n\n"
        "Phone: 121-456-7890\n"
        "Email: library@techtitan.com\n"
    )

    contact_text = Text(contact_window, width=70, height=10, wrap=WORD, bg="white", font=("Times New Roman", 14))
    contact_text.pack(pady=10)
    contact_text.insert(INSERT, contact_info)
    contact_text.config(state=DISABLED)

def show_fees(event=None):
    fees_window = tk.Toplevel(top)
    fees_window.title("Fees Detail")
    fees_window.geometry("600x400+300+200")
    fees_window.configure(bg="white")
    fees_window.resizable(width=False, height=False)

    fees_label = tk.Label(fees_window, text="Library Fees Detail", font=("Times New Roman", 20, "bold"), bg="white", fg="brown")
    fees_label.pack(pady=20)

    fees_info = (
        "Membership Fees:\n"
        "1. Standard Membership: 5000 Rs/year\n"
        "2. Premium Membership: 10000 Rs/year\n\n"
        "Late Return Fees:\n"
        "25 Rs per day after the due date\n\n"
        "Lost Book Fees:\n"
        "Full price of the lost book\n"
    )

    fees_text = Text(fees_window, width=70, height=10, wrap=WORD, bg="white", font=("Times New Roman", 14))
    fees_text.pack(pady=10)
    fees_text.insert(INSERT, fees_info)
    fees_text.config(state=DISABLED)
    
aboutmenu = tk.Menu(menubar)
menubar.add_cascade(label="About Us", menu=aboutmenu)

aboutmenu.add_command(label="Rules and Regulations", command=show_rules)
aboutmenu.add_command(label="Contact Us", command=show_contact)
aboutmenu.add_command(label="Fees Detail", command=show_fees)
aboutmenu.add_separator()
aboutmenu.add_command(label="Exit", command=logout)
top.config(menu=menubar)

title_label = tk.Label(top, text="LIBRARY MANAGEMENT SYSTEM", font=("Times New Roman", 31, "bold"), bg="white", fg="brown")
title_label.place(x=145, y=20)

img = PhotoImage(file="back.png")
Label(top, image=img, bg='white').place(x=0, y=90)

def show_registration_page(event=None):
    register_window = tk.Toplevel(top)
    register_window.title("User Registration")
    register_window.geometry("900x700+260+70")
    register_window.configure(bg="white")
    register_window.resizable(width=False, height=False)
    
    reg_label = tk.Label(register_window, text="User Registration", font=("Times New Roman", 25, "bold"), bg="white", fg="brown")
    reg_label.place(x=300, y=20)
    
    first_name_label = Label(register_window, text="First Name:", font=("Times New Roman", 18, "bold"), bg="white")
    first_name_label.place(x=150, y=65)
    first_name_entry = ttk.Entry(register_window, width=30, font=("Times New Roman", 18, "bold"))
    first_name_entry.place(x=350, y=65)

    last_name_label = tk.Label(register_window, text="Last Name:", font=("Times New Roman", 18, "bold"), bg="white")
    last_name_label.place(x=150, y=110)
    last_name_entry = ttk.Entry(register_window, width=30, font=("Times New Roman", 18, "bold"))
    last_name_entry.place(x=350, y=105)

    password_label = tk.Label(register_window, text="Password:", font=("Times New Roman", 18, "bold"), bg="white")
    password_label.place(x=150, y=150)
    password_entry = ttk.Entry(register_window, width=30, font=("Times New Roman", 18, "bold"))
    password_entry.place(x=350, y=155)

    phone_label = tk.Label(register_window, text="Phone Number:", font=("Times New Roman", 18, "bold"), bg="white")
    phone_label.place(x=150, y=200)
    phone_entry = ttk.Entry(register_window, width=30, font=("Times New Roman", 18, "bold"))
    phone_entry.place(x=350, y=205)

    email_label = tk.Label(register_window, text="Email:", font=("Times New Roman", 18, "bold"), bg="white")
    email_label.place(x=150, y=250)
    email_entry = ttk.Entry(register_window, width=30, font=("Times New Roman", 18, "bold"))
    email_entry.place(x=350, y=255)

    gender_label = tk.Label(register_window, text="Gender:", font=("Times New Roman", 18, "bold"), bg="white")
    gender_label.place(x=150, y=300)
    gender_combo = ttk.Combobox(register_window, values=["Select an Option", "Male", "Female", "Other"], width=30, font=("Times New Roman", 18, "bold"))
    gender_combo.place(x=350, y=305)

    dob_label = tk.Label(register_window, text=" Age:", font=("Times New Roman", 18, "bold"), bg="white")
    dob_label.place(x=150, y=350)
    dob_entry = ttk.Entry(register_window, width=30, font=("Times New Roman", 18, "bold"))
    dob_entry.place(x=350, y=355)

    address_label = tk.Label(register_window, text="Address:", font=("Times New Roman", 18, "bold"), bg="white")
    address_label.place(x=150, y=400)
    address_entry = ttk.Entry(register_window, width=30, font=("Times New Roman", 18, "bold"))
    address_entry.place(x=350, y=405)

    city_label = tk.Label(register_window, text="City:", font=("Times New Roman", 18, "bold"), bg="white")
    city_label.place(x=150, y=450)
    city_entry = ttk.Entry(register_window, width=30, font=("Times New Roman", 18, "bold"))
    city_entry.place(x=350, y=455)

    state_label = tk.Label(register_window, text="State:", font=("Times New Roman", 18, "bold"), bg="white")
    state_label.place(x=150, y=500)
    state_entry = ttk.Entry(register_window, width=30, font=("Times New Roman", 18, "bold"))
    state_entry.place(x=350, y=505)
    
    declaration_var = tk.BooleanVar()
    declaration_checkbox = tk.Checkbutton(register_window, text="I hereby declare all the details written by me are correct", 
                                          variable=declaration_var, onvalue=True, offvalue=False, 
                                          font=("Times New Roman", 14), bg="white")
    declaration_checkbox.place(x=150, y=550)
    
    def add_member_to_db(event=None):
        if (not first_name_entry.get() or not last_name_entry.get() or not password_entry.get() or 
            not phone_entry.get() or not email_entry.get() or not dob_entry.get() or 
            not address_entry.get() or not city_entry.get() or not state_entry.get() or 
            gender_combo.get() == "Select an Option"):
            messagebox.showwarning("Warning", "All fields are required!")
        else:
            member_id = add_member(first_name_entry.get(), last_name_entry.get(), password_entry.get(), phone_entry.get(), email_entry.get(), gender_combo.get(), int(dob_entry.get()), address_entry.get(), city_entry.get(), state_entry.get())
            if member_id:
                messagebox.showinfo("Congratulations!", f"Now you are a member of our Library. Your Member ID is {member_id}")
                register_window.destroy()  # Close the registration window
                top.deiconify()  # Bring the main window back to focus
            else:
                messagebox.showerror("Error", "Failed to add member. Please try again.")

    add_member_button = tk.Button(register_window, text="Add Member", font=("Times New Roman", 18, "bold"), bg="brown", fg="white", command=add_member_to_db)
    add_member_button.place(x=350, y=590)
    
    def back_to_main():
        register_window.destroy()  # Close the registration window
        top.deiconify()  # Bring the main window back to focus
    
    back_button = tk.Button(register_window, text="Back", font=("Times New Roman", 18, "bold"), bg="brown", fg="white", command=back_to_main)
    back_button.grid(row=1, column=1)
      
def registerPage(event=None):
    show_registration_page()
    top.withdraw()
    
frame = Frame(top, width=362, height=360, bg="#8FA0A2")
frame.place(x=630, y=85)  
    
heading = Label(frame, text="Login Here !!", fg="blue", bg="#8FA0A2", font=("Magento", 20, "bold"))
heading.place(x=100, y=7)

def on_enter(e):
    user.delete(0, "end")
def on_leave(e):
    name = user.get()
    if name == "":
        user.insert(0, "Username/Email")
user = Entry(frame, width=25, fg="white", border=0, bg="#8FA0A2", font=("Times new Roman", 11, "bold"))
user.place(x=30, y=80)
user.insert(0, "Username/Email")
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)
def on_enter(e):
    code.delete(0, "end")
def on_leave(e):
    name = code.get()
    if name == "":
        code.insert(0, "Password")
        
code = Entry(frame, width=25, fg="white", border=0, bg="#8FA0A2", font=("Times new Roman", 11, "bold"))
code.place(x=30, y=150)
code.insert(0, "Password")
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

def toggle_password():
    if show_var.get():
        code.config(show=" ")
    else:
        code.config(show="*")

show_var = BooleanVar()
show_var.set(True)
show_password = Checkbutton(frame, text="Show Password", variable=show_var, onvalue=True, offvalue=False, command=toggle_password, bg="#8FA0A2")
show_password.place(x=30, y=180)

def login(event=None):
    if verify_login(user.get(), code.get()):
        messagebox.showinfo("Login Successful", "Welcome to TechTitan's Library Management System")
        top.destroy()  # Close the current window
        subprocess.Popen(["python", "main_page.py"])  # Open the main page script
    else:
        messagebox.showerror("Error", "Invalid Username or Password")

Button(frame, width=35, pady=6, text="Login", font=("Arial", 12), bg="blue", fg="white", border=0, command=login).place(x=20, y=210)

label = Label(frame, text="Not a member of a library?", fg="black", bg="#8FA0A2", font=("Microsoft YaHei UI Light", 9))
label.place(x=75, y=285)

sign_up = Button(frame, width=15, text="Register Here", border=0, bg="#8FA0A2", cursor="hand2", fg="blue", command=registerPage)
sign_up.place(x=230, y=285)

top.mainloop()

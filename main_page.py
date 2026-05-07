import tkinter as tk
from tkinter import *
from tkinter import messagebox
import subprocess
from tkinter import ttk
from database import create_table, add_member, verify_login, add_book, issue_book, return_book, get_statistics,get_member

def clear_main_frame():
    for widget in main_frame.winfo_children():
        widget.destroy()

def outlog():
    top_a.destroy()
    subprocess.Popen(["python", "lms.py"])

def show_success_message():
    messagebox.showinfo("Success", "Book details saved successfully")

def show_removal_message():
    messagebox.showinfo("Success", "Book details removed successfully")

def show_error_message():
    messagebox.showerror("Error", "Please fill all details")

def add_button(frame, text, command):
    button = Button(frame, text=text, font=("Times New Roman", 20), bg="#343a40", fg="white", command=command)
    button.pack(pady=10, fill=X)

def add_book_ui():
    book_window = tk.Toplevel(top_a)
    book_window.title("Add Book")
    book_window.geometry("450x350")
    book_window.configure(bg="white")
   
    def save_book():
        book_id = book_id_entry.get()
        title = title_entry.get()
        author = author_entry.get()
        price = price_entry.get()

        if not all([book_id, title, author, price]):
            show_error_message()
        else:
            add_book(book_id, title, author, price)
            show_success_message()
            book_window.destroy()

    Label(book_window, text="Add Book", font=("Helvetica", 20, "bold"), bg="white", fg="blue").pack(pady=20)

    form_frame = Frame(book_window, bg="white")
    form_frame.pack(pady=20)

    Label(form_frame, text="Book ID", bg="white").grid(row=0, column=0, padx=10, pady=10)
    book_id_entry = Entry(form_frame, width=30)
    book_id_entry.grid(row=0, column=1, padx=10, pady=10)

    Label(form_frame, text="Title", bg="white").grid(row=1, column=0, padx=10, pady=10)
    title_entry = Entry(form_frame, width=30)
    title_entry.grid(row=1, column=1, padx=10, pady=10)

    Label(form_frame, text="Author", bg="white").grid(row=2, column=0, padx=10, pady=10)
    author_entry = Entry(form_frame, width=30)
    author_entry.grid(row=2, column=1, padx=10, pady=10)

    Label(form_frame, text="Price", bg="white").grid(row=3, column=0, padx=10, pady=10)
    price_entry = Entry(form_frame, width=30)
    price_entry.grid(row=3, column=1, padx=10, pady=10)

    Button(book_window, text="Save", bg='#007bff', fg='white', font=('Arial', 12), command=save_book).pack(pady=20)

def remove_book_ui():
    remove_window = tk.Toplevel(top_a)
    remove_window.title("Remove Book")
    remove_window.geometry("400x300")
    remove_window.configure(bg="white")
    remove_window.resizable(width=False, height=False)

    def delete_book():
        book_id = book_id_entry.get()

        if not book_id:
            show_error_message()
        else:
            # Implement the remove book logic here
            show_removal_message()
            remove_window.destroy()

    Label(remove_window, text="Remove Book", font=("Helvetica", 20, "bold"), bg="white", fg="blue").pack(pady=20)

    form_frame = Frame(remove_window, bg="white")
    form_frame.pack(pady=20)

    Label(form_frame, text="Book ID", bg="white").grid(row=0, column=0, padx=10, pady=10)
    book_id_entry = Entry(form_frame, width=30)
    book_id_entry.grid(row=0, column=1, padx=10, pady=10)

    Button(remove_window, text="Delete", bg='#007bff', fg='white', font=('Arial', 12), command=delete_book).pack(pady=20)

def issue_book_ui():
    issue_window = tk.Toplevel(top_a)
    issue_window.title("Issue Book")
    issue_window.geometry("400x400")
    issue_window.configure(bg="white")
    issue_window.resizable(width=False, height=False)

    def save_issue():
        book_id = book_id_entry.get()
        member_id = member_id_entry.get()
        issue_date = issue_date_entry.get()

        if not book_id or not member_id or not issue_date:
            show_error_message()
        else:
            issue_book(book_id, member_id, issue_date)
            show_success_message()
            issue_window.destroy()

    Label(issue_window, text="Issue Book", font=("Helvetica", 20, "bold"), bg="white", fg="blue").pack(pady=20)

    form_frame = Frame(issue_window, bg="white")
    form_frame.pack(pady=20)

    Label(form_frame, text="Book ID", bg="white").grid(row=0, column=0, padx=10, pady=10)
    book_id_entry = Entry(form_frame, width=30)
    book_id_entry.grid(row=0, column=1, padx=10, pady=10)

    Label(form_frame, text="Member ID", bg="white").grid(row=1, column=0, padx=10, pady=10)
    member_id_entry = Entry(form_frame, width=30)
    member_id_entry.grid(row=1, column=1, padx=10, pady=10)

    Label(form_frame, text="Issue Date", bg="white").grid(row=2, column=0, padx=10, pady=10)
    issue_date_entry = Entry(form_frame, width=30)
    issue_date_entry.grid(row=2, column=1, padx=10, pady=10)

    Button(issue_window, text="Save", bg='#007bff', fg='white', font=('Arial', 12), command=save_issue).pack(pady=20)

def return_book_ui():
    return_window = tk.Toplevel(top_a)
    return_window.title("Return Book")
    return_window.geometry("400x400")
    return_window.configure(bg="white")
    return_window.resizable(width=False, height=False)

    def save_return():
        transaction_id = transaction_id_entry.get()
        return_date = return_date_entry.get()

        if not transaction_id or not return_date:
            show_error_message()
        else:
            return_book(transaction_id, return_date)
            show_success_message()
            return_window.destroy()

    Label(return_window, text="Return Book", font=("Helvetica", 20, "bold"), bg="white", fg="blue").pack(pady=20)

    form_frame = Frame(return_window, bg="white")
    form_frame.pack(pady=20)

    Label(form_frame, text="Transaction ID", bg="white").grid(row=0, column=0, padx=10, pady=10)
    transaction_id_entry = Entry(form_frame, width=30)
    transaction_id_entry.grid(row=0, column=1, padx=10, pady=10)

    Label(form_frame, text="Member ID", bg="white").grid(row=1, column=0, padx=10, pady=10)
    member_id_entry = Entry(form_frame, width=30)
    member_id_entry.grid(row=1, column=1, padx=10, pady=10)

    Label(form_frame, text="Return Date", bg="white").grid(row=2, column=0, padx=10, pady=10)
    return_date_entry = Entry(form_frame, width=30)
    return_date_entry.grid(row=2, column=1, padx=10, pady=10)

    Button(return_window, text="Save", bg='#007bff', fg='white', font=('Arial', 12), command=save_return).pack(pady=20)

def show_home():
    clear_main_frame()
    img_label = Label(main_frame, image=img)
    img_label.pack()

    reg_label = tk.Label(img_label, text="WELCOME TO LIBRARY MANAGEMENT SYSTEM", font=("Times New Roman", 25, "bold"), fg="brown", bg="white")
    reg_label.place(x=200, y=20)

    quote_label = tk.Label(img_label, text="“A room without books is like a body without a soul.” - Cicero", 
                           font=("Times New Roman", 16, "italic"), fg="blue", bg="white")
    quote_label.place(x=200, y=70)
    
    stats = get_statistics()

    button_colors = ["#4CAF50", "#2196F3", "#9C27B0"]
    
    button_x_start = 150
    button_y = 150
    button_spacing = 310

    for i, (key, value) in enumerate(stats.items()):
        btn = Button(img_label, text=f"{key.replace('_', ' ').title()}: {value}", font=("Times New Roman", 20, "bold"),
                     bg=button_colors[i], fg="white", padx=20, pady=20)
        btn.place(x=button_x_start + i*button_spacing, y=button_y)

    description_label = Label(img_label, text="Our library offers a wide range of books and resources for all your reading needs. "
                                               "Whether you're looking for fiction, non-fiction, or academic materials, we have it all.",
                              font=("Times New Roman", 16), bg="white", justify=tk.LEFT, wraplength=1000)
    description_label.place(x=150, y=350)

    hours_label = Label(img_label, text="Operating Hours:\nMonday - Friday: 9 AM - 8 PM\nSaturday: 10 AM - 6 PM\nSunday: Closed",
                        font=("Times New Roman", 16), bg="white", justify=tk.LEFT)
    hours_label.place(x=150, y=500)
    
    logout_button = Button(img_label, text="Logout", font=("Times New Roman", 16), bg="red", fg="white", command=outlog)
    logout_button.place(x=1100, y=600)

def show_books():
    clear_main_frame()
    books_label = Label(main_frame, text="Books Section", font=("Times New Roman", 25, "bold"), fg="brown", bg="white")
    books_label.pack(pady=20)

    add_button(main_frame, "Add Book", add_book_ui)
    add_button(main_frame, "Remove Book", remove_book_ui)



def clear_table():
    for row in tree.get_children():
        tree.delete(row)

def show_members():
    clear_main_frame()
    members_label = Label(main_frame, text="Members Section", font=("Times New Roman", 25, "bold"), fg="brown", bg="white")
    members_label.pack(pady=20)

    search_frame = Frame(main_frame, bg="white")
    search_frame.pack(pady=20)

    Label(search_frame, text="Member ID:", bg="white").grid(row=0, column=0, padx=10, pady=10)
    member_id_entry = Entry(search_frame, width=30)
    member_id_entry.grid(row=0, column=1, padx=10, pady=10)
    
    def search_member():
    
        member_id = member_id_entry.get()

        if not member_id:
            show_error_message()
        else:
            member = get_member(member_id)
            if member:
               clear_table()
               tree.insert('', 'end', values=member)
            else:
               messagebox.showerror("Error", f"No member found with Member ID {member_id}")

    search_button = Button(search_frame, text="Search", bg='#007bff', fg='white', font=('Arial', 12), command=search_member)
    search_button.grid(row=0, column=2, padx=10, pady=10)

    global tree
    tree_frame = Frame(main_frame)
    tree_frame.pack(pady=20)

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)

    tree = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11), show="headings", height="5", yscrollcommand=tree_scroll.set)
    tree.pack()

    tree.heading(1, text="Member ID")
    tree.heading(2, text="First Name")
    tree.heading(3, text="Last Name")
    tree.heading(4, text="Password")
    tree.heading(5, text="Phone")
    tree.heading(6, text="Email")
    tree.heading(7, text="Gender")
    tree.heading(8, text="Age")
    tree.heading(9, text="Address")
    tree.heading(10, text="City")
    tree.heading(11, text="State")

    tree_scroll.config(command=tree.yview)

def add_fine():
    fine_window = tk.Toplevel(top_a)
    fine_window.title("Add Fine")
    fine_window.geometry("400x300")
    fine_window.configure(bg="white")
    fine_window.resizable(width=False, height=False)

    def save_fine():
        user_id = user_id_entry.get()
        fine_amount = fine_amount_entry.get()
        fine_date = fine_date_entry.get()

        if not user_id or not fine_amount or not fine_date:
            show_error_message()
        else:
            # Implement the save fine logic here
            show_success_message()
            fine_window.destroy()

    Label(fine_window, text="Add Fine", font=("Helvetica", 20, "bold"), bg="white", fg="blue").pack(pady=20)

    form_frame = Frame(fine_window, bg="white")
    form_frame.pack(pady=20)

    Label(form_frame, text="User ID", bg="white").grid(row=0, column=0, padx=10, pady=10)
    user_id_entry = Entry(form_frame, width=30)
    user_id_entry.grid(row=0, column=1, padx=10, pady=10)

    Label(form_frame, text="Fine Amount", bg="white").grid(row=1, column=0, padx=10, pady=10)
    fine_amount_entry = Entry(form_frame, width=30)
    fine_amount_entry.grid(row=1, column=1, padx=10, pady=10)

    Label(form_frame, text="Fine Date", bg="white").grid(row=2, column=0, padx=10, pady=10)
    fine_date_entry = Entry(form_frame, width=30)
    fine_date_entry.grid(row=2, column=1, padx=10, pady=10)

    Button(fine_window, text="Save", bg='#007bff', fg='white', font=('Arial', 12), command=save_fine).pack(pady=20)

def remove_fine():
    remove_window = tk.Toplevel(top_a)
    remove_window.title("Remove Fine")
    remove_window.geometry("400x300")
    remove_window.configure(bg="white")
    remove_window.resizable(width=False, height=False)

    def delete_fine():
        user_id = user_id_entry.get()
        fine_amount = fine_amount_entry.get()
        fine_date = fine_date_entry.get()

        if not user_id or not fine_amount or not fine_date:
            show_error_message()
        else:
            # Implement the remove fine logic here
            show_removal_message()
            remove_window.destroy()

    Label(remove_window, text="Remove Fine", font=("Helvetica", 20, "bold"), bg="white", fg="blue").pack(pady=20)

    form_frame = Frame(remove_window, bg="white")
    form_frame.pack(pady=20)

    Label(form_frame, text="User ID", bg="white").grid(row=0, column=0, padx=10, pady=10)
    user_id_entry = Entry(form_frame, width=30)
    user_id_entry.grid(row=0, column=1, padx=10, pady=10)

    Label(form_frame, text="Fine Amount", bg="white").grid(row=1, column=0, padx=10, pady=10)
    fine_amount_entry = Entry(form_frame, width=30)
    fine_amount_entry.grid(row=1, column=1, padx=10, pady=10)

    Label(form_frame, text="Fine Date", bg="white").grid(row=2, column=0, padx=10, pady=10)
    fine_date_entry = Entry(form_frame, width=30)
    fine_date_entry.grid(row=2, column=1, padx=10, pady=10)

    Button(remove_window, text="Delete", bg='#007bff', fg='white', font=('Arial', 12), command=delete_fine).pack(pady=20)

def show_borrow_return():
    clear_main_frame()
    borrow_return_label = Label(main_frame, text="Issue/Return Section", font=("Times New Roman", 25, "bold"), fg="brown", bg="white")
    borrow_return_label.pack(pady=20)

    add_button(main_frame, "Issue Book", issue_book_ui)
    add_button(main_frame, "Return Book", return_book_ui)

def show_fine_details():
    clear_main_frame()
    fine_label = Label(main_frame, text="Fine Details Section", font=("Times New Roman", 25, "bold"), fg="brown", bg="white")
    fine_label.pack(pady=20)

    add_button(main_frame, "Add Fine", add_fine)
    add_button(main_frame, "Remove Fine", remove_fine)


top_a = tk.Tk()
top_a.title("TechTitan's Library Management System")
top_a.geometry("1425x698+70+45")
top_a.configure(bg="white")

sidebar_frame = Frame(top_a, width=325, bg="#343a40")
sidebar_frame.pack(side=LEFT, fill=Y)

main_frame = Frame(top_a, bg='white')
main_frame.pack(side=RIGHT, expand=True, fill=BOTH)

img = PhotoImage(file="backti.png")

# Initialize with the home content
show_home()

# Add buttons to the sidebar
home_button = Button(sidebar_frame, text="Home", font=("Times New Roman", 20), bg="#343a40", fg="white", command=show_home)
home_button.pack(pady=10, fill=X)

books_button = Button(sidebar_frame, text="Books", font=("Times New Roman", 20), bg="#343a40", fg="white", command=show_books)
books_button.pack(pady=10, fill=X)

members_button = Button(sidebar_frame, text="Members", font=("Times New Roman", 20), bg="#343a40", fg="white", command=show_members)
members_button.pack(pady=10, fill=X)

borrow_return_button = Button(sidebar_frame, text="Issue/Return", font=("Times New Roman", 20), bg="#343a40", fg="white", command=show_borrow_return)
borrow_return_button.pack(pady=10, fill=X)

fine_button = Button(sidebar_frame, text="Fine Details", font=("Times New Roman", 20), bg="#343a40", fg="white", command=show_fine_details)
fine_button.pack(pady=10, fill=X)

top_a.mainloop()

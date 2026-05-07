import sqlite3
from sqlite3 import Error
import random

def create_connection():
    try:
        conn = sqlite3.connect("library.db")
        return conn
    except Error as e:
        print(e)
    return None

def create_table():
    conn = create_connection()
    if conn:
        try:
            sql_create_members_table = """
            CREATE TABLE IF NOT EXISTS members (
                member_id INTEGER PRIMARY KEY,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                password TEXT NOT NULL,
                phone TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                gender TEXT NOT NULL,
                age INTEGER NOT NULL,
                address TEXT NOT NULL,
                city TEXT NOT NULL,
                state TEXT NOT NULL
            );
            """
            
            sql_create_books_table = """
            CREATE TABLE IF NOT EXISTS books (
                book_id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                price INTEGER NOT NULL
            );
            """
            
            sql_create_issue_return_table = """
            CREATE TABLE IF NOT EXISTS issue_return (
                transaction_id INTEGER PRIMARY KEY,
                book_id INTEGER NOT NULL,
                member_id INTEGER NOT NULL,
                issue_date TEXT NOT NULL,
                return_date TEXT,
                FOREIGN KEY (book_id) REFERENCES books (book_id),
                FOREIGN KEY (member_id) REFERENCES members (member_id)
            );
            """
            sql_create_fine_table ="""
            CREATE TABLE IF NOT EXISTS fine (
            fine_id INTEGER PRIMARY KEY AUTOINCREMENT,
            member_id INTEGER NOT NULL,
            fine_amount REAL,
            fine_date TEXT,
            FOREIGN KEY (member_id) REFERENCES members(member_id)
            );
            """
           
            
            conn.execute(sql_create_members_table)
            conn.execute(sql_create_books_table)
            conn.execute(sql_create_issue_return_table)
            conn.execute(sql_create_fine_table)
        
            conn.commit()
        except Error as e:
            print(e)
        finally:
            conn.close()

def generate_member_id():
    return random.randint(1000, 9999)

def add_member(first_name, last_name, password, phone, email, gender, age, address, city, state):
    conn = create_connection()
    if conn:
        try:
            member_id = generate_member_id()
            sql_insert_member = """
            INSERT INTO members (member_id, first_name, last_name, password, phone, email, gender, age, address, city, state)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
            """
            cur = conn.cursor()
            cur.execute(sql_insert_member, (member_id, first_name, last_name, password, phone, email, gender, age, address, city, state))
            conn.commit()
            return cur.lastrowid
        except Error as e:
            print(e)
        finally:
            conn.close()
    return None

def add_book(book_id, title, author, price):
    conn = create_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("INSERT INTO books (book_id, title, author, price) VALUES (?, ?, ?, ?)",
                        (book_id, title, author, price))
            conn.commit()
            return cur.lastrowid
        except Error as e:
            print(e)
        finally:
            conn.close()
    return None

def issue_book(book_id, member_id, issue_date):
    conn = create_connection()
    if conn:
        try:
            sql_issue_book = """
            INSERT INTO issue_return (book_id, member_id, issue_date)
            VALUES (?, ?, ?);
            """
            cur = conn.cursor()
            cur.execute(sql_issue_book, (book_id, member_id, issue_date))
            conn.commit()
            return cur.lastrowid
        except Error as e:
            print(e)
        finally:
            conn.close()
    return None

def return_book(transaction_id, return_date):
    conn = create_connection()
    if conn:
        try:
            sql_return_book = """
            UPDATE issue_return
            SET return_date = ?
            WHERE transaction_id = ?;
            """
            cur = conn.cursor()
            cur.execute(sql_return_book, (return_date, transaction_id))
            conn.commit()
            return cur.rowcount
        except Error as e:
            print(e)
        finally:
            conn.close()
    return None

def add_fine(member_id, fine_amount, fine_date):
    conn = create_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("INSERT INTO fine (member_id, fine_amount, fine_date) VALUES (?, ?, ?)",
                        (member_id, fine_amount, fine_date))
            conn.commit()
            return cur.lastrowid
        except Error as e:
            print(e)
        finally:
            conn.close()
    return None

def remove_fine(fine_id):
    conn = create_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("DELETE FROM fine WHERE fine_id = ?", (fine_id,))
            conn.commit()
            return cur.rowcount
        except Error as e:
            print(e)
        finally:
            conn.close()
    return None

def get_statistics():
    conn = create_connection()
    stats = {"total_books": 0, "books_issued": 0, "books_returned": 0}
    if conn:
        try:
            cursor = conn.cursor()
            
            # Query to get total number of books
            cursor.execute('SELECT COUNT(*) FROM books')
            total_books = cursor.fetchone()[0]
            
            # Query to get number of books currently issued (where return_date is NULL)
            cursor.execute('SELECT COUNT(*) FROM issue_return WHERE return_date IS NULL')
            books_issued = cursor.fetchone()[0]
            
            # Query to get number of books returned (where return_date is not NULL)
            cursor.execute('SELECT COUNT(*) FROM issue_return WHERE return_date IS NOT NULL')
            books_returned = cursor.fetchone()[0]
            stats['total_books'] = total_books
            stats['books_issued'] = books_issued
            stats['books_returned'] = books_returned
            
        except Error as e:
            print(e)
        finally:
            conn.close()
    return stats

def verify_login(email, password):
    conn = create_connection()
    if conn:
        try:
            sql_select_member = "SELECT * FROM members WHERE email=? AND password=?"
            cur = conn.cursor()
            cur.execute(sql_select_member, (email, password))
            row = cur.fetchone()
            return row is not None
        except Error as e:
            print(e)
        finally:
            conn.close()
    return False

def get_member(member_id):
    conn = create_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM members WHERE member_id=?", (member_id,))
            member = cur.fetchone()
            return member
        except Error as e:
            print(e)
        finally:
            conn.close()
    return None


if __name__ == "__main__":
    create_table()

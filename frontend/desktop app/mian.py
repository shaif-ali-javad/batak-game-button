import tkinter as tk
from tkinter import messagebox
import psycopg2

def connect_to_db():
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="1234",
            host="localhost",
            port="5432",
            database="user_db"
        )
        return connection
    except (Exception, psycopg2.Error) as error:
        messagebox.showerror("Error", f"Failed to connect to PostgreSQL database: {error}")
        return None

def login():
    username = entry_login_username.get()
    password = entry_login_password.get()

    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
            user = cursor.fetchone()
            if user:
                messagebox.showinfo("Login Successful", f"Welcome, {username}!")
            else:
                messagebox.showerror("Login Failed", "Invalid username or password")
        except (Exception, psycopg2.Error) as error:
            messagebox.showerror("Error", f"Failed to login: {error}")
        finally:
            connection.close()

def register(username, password):
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            connection.commit()
            messagebox.showinfo("Registration Successful", f"User {username} registered successfully!")
        except (Exception, psycopg2.Error) as error:
            messagebox.showerror("Error", f"Failed to register user: {error}")
        finally:
            connection.close()

def open_register_window():
    register_window = tk.Toplevel(root)
    register_window.title("Register")
    register_window.geometry("300x150")

    label_reg_username = tk.Label(register_window, text="Username:")
    label_reg_username.grid(row=0, column=0, padx=10, pady=5)
    entry_reg_username = tk.Entry(register_window)
    entry_reg_username.grid(row=0, column=1, padx=10, pady=5)

    label_reg_password = tk.Label(register_window, text="Password:")
    label_reg_password.grid(row=1, column=0, padx=10, pady=5)
    entry_reg_password = tk.Entry(register_window, show="*")
    entry_reg_password.grid(row=1, column=1, padx=10, pady=5)

    button_register = tk.Button(register_window, text="Register", command=lambda: register(entry_reg_username.get(), entry_reg_password.get()))
    button_register.grid(row=2, column=0, columnspan=2, pady=10)

root = tk.Tk()
root.title("Login")
root.geometry("300x150")

label_login_username = tk.Label(root, text="Username:")
label_login_username.grid(row=0, column=0, padx=10, pady=5)
entry_login_username = tk.Entry(root)
entry_login_username.grid(row=0, column=1, padx=10, pady=5)

label_login_password = tk.Label(root, text="Password:")
label_login_password.grid(row=1, column=0, padx=10, pady=5)
entry_login_password = tk.Entry(root, show="*")
entry_login_password.grid(row=1, column=1, padx=10, pady=5)

button_login = tk.Button(root, text="Login", command=lambda: (login(), open_welcome_window()))
button_login.grid(row=2, column=0, columnspan=2, pady=10)

button_register = tk.Button(root, text="Register", command=open_register_window)
button_register.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()



def open_welcome_window():
    register_window = tk.Toplevel(root)
    register_window.title("welcom")
    register_window.geometry("300x150")
    print

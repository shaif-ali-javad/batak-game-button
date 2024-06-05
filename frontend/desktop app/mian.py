# import tkinter as tk
# from tkinter import messagebox
# import psycopg2

# connection = None  # Define connection globally
# logged_in_user_id = None  # To store the logged-in user's ID

# def connect_to_db():
#     global connection  # Access the global connection variable
#     try:
#         connection = psycopg2.connect(
#             user="postgres",
#             password="1234",
#             host="localhost",
#             port="5432",
#             database="user_db"
#         )
#         messagebox.showinfo("Success", "Connected to PostgreSQL database successfully!")
#         return connection
#     except (Exception, psycopg2.Error) as error:
#         messagebox.showerror("Error", f"Failed to connect to PostgreSQL database: {error}")
#         return None

# def login():
#     global logged_in_user_id
#     username = entry_login_username.get()
#     password = entry_login_password.get()

#     connection = connect_to_db()
#     if connection:
#         try:
#             cursor = connection.cursor()
#             cursor.execute("SELECT id FROM users WHERE username=%s AND password=%s", (username, password))
#             user = cursor.fetchone()
#             if user:
#                 logged_in_user_id = user[0]
#                 messagebox.showinfo("Login Successful", f"Welcome, {username}!")
#                 open_welcome_window()
#             else:
#                 messagebox.showerror("Login Failed", "Invalid username or password")
#         except (Exception, psycopg2.Error) as error:
#             messagebox.showerror("Error", f"Failed to login: {error}")
#         finally:
#             connection.close()

# def register(username, password):
#     connection = connect_to_db()
#     if connection:
#         try:
#             cursor = connection.cursor()
#             cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
#             connection.commit()
#             messagebox.showinfo("Registration Successful", f"User {username} registered successfully!")
#         except (Exception, psycopg2.Error) as error:
#             messagebox.showerror("Error", f"Failed to register user: {error}")
#         finally:
#             connection.close()

# def save_timer(seconds):
#     if logged_in_user_id is None:
#         messagebox.showerror("Error", "No user is logged in.")
#         return
    
#     connection = connect_to_db()
#     if connection:
#         try:
#             cursor = connection.cursor()
#             cursor.execute("INSERT INTO timers (user_id, seconds) VALUES (%s, %s)", (logged_in_user_id, seconds))
#             connection.commit()
#             messagebox.showinfo("Success", f"Timer {seconds} saved successfully!")
#         except (Exception, psycopg2.Error) as error:
#             messagebox.showerror("Error", f"Failed to save timer: {error}")
#         finally:
#             connection.close()

# def open_welcome_window():
#     welcome_window = tk.Toplevel(root)
#     welcome_window.title("Welcome")
#     welcome_window.geometry("500x550")

#     timer_label = tk.Label(welcome_window, text="00:00:00", font=("Arial", 24))
#     timer_label.pack()

#     def update_timer(seconds):
#         nonlocal running
#         if running:
#             hours = seconds // 3600
#             minutes = (seconds % 3600) // 60
#             secs = seconds % 60
#             timer_label.config(text=f"{hours:02d}:{minutes:02d}:{secs:02d}")
#             welcome_window.after(1000, update_timer, seconds + 1)
#             return seconds + 1

#     def start_timer():
#         nonlocal running, seconds
#         if not running:
#             running = True
#             seconds = update_timer(0)

#     def stop_timer():
#         nonlocal running
#         running = False

#     def submit_time():
#         nonlocal running, seconds
#         running = False
#         save_timer(seconds)

#     running = False
#     seconds = 0

#     start_button = tk.Button(welcome_window, text="Start Timer", command=start_timer)
#     start_button.pack()

#     stop_button = tk.Button(welcome_window, text="Stop Timer", command=stop_timer)
#     stop_button.pack()

#     submit_button = tk.Button(welcome_window, text="Submit Time", command=submit_time)
#     submit_button.pack()

# def open_register_window():
#     register_window = tk.Toplevel(root)
#     register_window.title("Register")
#     register_window.geometry("300x150")

#     label_reg_username = tk.Label(register_window, text="Username:")
#     label_reg_username.grid(row=0, column=0, padx=10, pady=5)
#     entry_reg_username = tk.Entry(register_window)
#     entry_reg_username.grid(row=0, column=1, padx=10, pady=5)

#     label_reg_password = tk.Label(register_window, text="Password:")
#     label_reg_password.grid(row=1, column=0, padx=10, pady=5)
#     entry_reg_password = tk.Entry(register_window, show="*")
#     entry_reg_password.grid(row=1, column=1, padx=10, pady=5)

#     button_register = tk.Button(register_window, text="Register", command=lambda: register(entry_reg_username.get(), entry_reg_password.get()))
#     button_register.grid(row=2, column=0, columnspan=2, pady=10)

# root = tk.Tk()
# root.title("Login")
# root.geometry("300x150")

# label_login_username = tk.Label(root, text="Username:")
# label_login_username.grid(row=0, column=0, padx=10, pady=5)
# entry_login_username = tk.Entry(root)
# entry_login_username.grid(row=0, column=1, padx=10, pady=5)

# label_login_password = tk.Label(root, text="Password:")
# label_login_password.grid(row=1, column=0, padx=10, pady=5)
# entry_login_password = tk.Entry(root, show="*")
# entry_login_password.grid(row=1, column=1, padx=10, pady=5)

# button_login = tk.Button(root, text="Login", command=login)
# button_login.grid(row=2, column=0, columnspan=2, pady=10)

# button_register = tk.Button(root, text="Register", command=open_register_window)
# button_register.grid(row=3, column=0, columnspan=2, pady=10)

# root.mainloop()



#0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000#0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000#0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000#0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000#00000



# import tkinter as tk
# from tkinter import messagebox
# import psycopg2

# connection = None  # Define connection globally
# logged_in_user_id = None  # To store the logged-in user's ID

# def connect_to_db():
#     global connection  # Access the global connection variable
#     try:
#         connection = psycopg2.connect(
#             user="postgres",
#             password="1234",
#             host="localhost",
#             port="5432",
#             database="user_db"
#         )
#         messagebox.showinfo("Success", "Connected to PostgreSQL database successfully!")
#         return connection
#     except (Exception, psycopg2.Error) as error:
#         messagebox.showerror("Error", f"Failed to connect to PostgreSQL database: {error}")
#         return None

# def create_tables():
#     connection = connect_to_db()
#     if connection:
#         try:
#             cursor = connection.cursor()
#             cursor.execute("""
#                 CREATE TABLE IF NOT EXISTS users (
#                     id SERIAL PRIMARY KEY,
#                     username VARCHAR(255) NOT NULL UNIQUE,
#                     password VARCHAR(255) NOT NULL
#                 );
#             """)
#             cursor.execute("""
#                 CREATE TABLE IF NOT EXISTS timers (
#                     id SERIAL PRIMARY KEY,
#                     user_id INTEGER NOT NULL,
#                     seconds INTEGER NOT NULL,
#                     FOREIGN KEY (user_id) REFERENCES users(id)
#                 );
#             """)
#             connection.commit()
#             cursor.close()
#         except (Exception, psycopg2.Error) as error:
#             messagebox.showerror("Error", f"Failed to create tables: {error}")
#         finally:
#             connection.close()

# def login():
#     global logged_in_user_id
#     username = entry_login_username.get()
#     password = entry_login_password.get()

#     connection = connect_to_db()
#     if connection:
#         try:
#             cursor = connection.cursor()
#             cursor.execute("SELECT id FROM users WHERE username=%s AND password=%s", (username, password))
#             user = cursor.fetchone()
#             if user:
#                 logged_in_user_id = user[0]
#                 messagebox.showinfo("Login Successful", f"Welcome, {username}!")
#                 open_welcome_window()
#             else:
#                 messagebox.showerror("Login Failed", "Invalid username or password")
#         except (Exception, psycopg2.Error) as error:
#             messagebox.showerror("Error", f"Failed to login: {error}")
#         finally:
#             connection.close()

# def register(username, password):
#     connection = connect_to_db()
#     if connection:
#         try:
#             cursor = connection.cursor()
#             cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
#             connection.commit()
#             messagebox.showinfo("Registration Successful", f"User {username} registered successfully!")
#         except (Exception, psycopg2.Error) as error:
#             messagebox.showerror("Error", f"Failed to register user: {error}")
#         finally:
#             connection.close()

# def save_timer(seconds):
#     if logged_in_user_id is None:
#         messagebox.showerror("Error", "No user is logged in.")
#         return
    
#     connection = connect_to_db()
#     if connection:
#         try:
#             cursor = connection.cursor()
#             cursor.execute("INSERT INTO timers (user_id, seconds) VALUES (%s, %s)", (logged_in_user_id, seconds))
#             connection.commit()
#             messagebox.showinfo("Success", f"Timer {seconds} saved successfully!")
#         except (Exception, psycopg2.Error) as error:
#             messagebox.showerror("Error", f"Failed to save timer: {error}")
#         finally:
#             connection.close()

# def open_welcome_window():
#     welcome_window = tk.Toplevel(root)
#     welcome_window.title("Welcome")
#     welcome_window.geometry("500x550")

#     timer_label = tk.Label(welcome_window, text="00:00:00", font=("Arial", 24))
#     timer_label.pack()

#     def update_timer(seconds):
#         nonlocal running
#         if running:
#             hours = seconds // 3600
#             minutes = (seconds % 3600) // 60
#             secs = seconds % 60
#             timer_label.config(text=f"{hours:02d}:{minutes:02d}:{secs:02d}")
#             welcome_window.after(1000, update_timer, seconds + 1)
#             return seconds + 1

#     def start_timer():
#         nonlocal running, seconds
#         if not running:
#             running = True
#             seconds = update_timer(0)

#     def stop_timer():
#         nonlocal running
#         running = False

#     def submit_time():
#         nonlocal running, seconds
#         running = False
#         save_timer(seconds)
#         open_scoreboard_window()

#     running = False
#     seconds = 0

#     start_button = tk.Button(welcome_window, text="Start Timer", command=start_timer)
#     start_button.pack()

#     stop_button = tk.Button(welcome_window, text="Stop Timer", command=stop_timer)
#     stop_button.pack()

#     submit_button = tk.Button(welcome_window, text="Submit Time", command=submit_time)
#     submit_button.pack()

# def open_scoreboard_window():
#     scoreboard_window = tk.Toplevel(root)
#     scoreboard_window.title("top users")
#     scoreboard_window.geometry("500x550")

#     timer_label = tk.Label(scoreboard_window, text="00:00:00", font=("Arial", 24))
#     timer_label.pack()

# def open_register_window():
#     register_window = tk.Toplevel(root)
#     register_window.title("Register")
#     register_window.geometry("300x150")

#     label_reg_username = tk.Label(register_window, text="Username:")
#     label_reg_username.grid(row=0, column=0, padx=10, pady=5)
#     entry_reg_username = tk.Entry(register_window)
#     entry_reg_username.grid(row=0, column=1, padx=10, pady=5)

#     label_reg_password = tk.Label(register_window, text="Password:")
#     label_reg_password.grid(row=1, column=0, padx=10, pady=5)
#     entry_reg_password = tk.Entry(register_window, show="*")
#     entry_reg_password.grid(row=1, column=1, padx=10, pady=5)

#     button_register = tk.Button(register_window, text="Register", command=lambda: register(entry_reg_username.get(), entry_reg_password.get()))
#     button_register.grid(row=2, column=0, columnspan=2, pady=10)

# root = tk.Tk()
# root.title("Login")
# root.geometry("300x150")

# label_login_username = tk.Label(root, text="Username:")
# label_login_username.grid(row=0, column=0, padx=10, pady=5)
# entry_login_username = tk.Entry(root)
# entry_login_username.grid(row=0, column=1, padx=10, pady=5)

# label_login_password = tk.Label(root, text="Password:")
# label_login_password.grid(row=1, column=0, padx=10, pady=5)
# entry_login_password = tk.Entry(root, show="*")
# entry_login_password.grid(row=1, column=1, padx=10, pady=5)

# button_login = tk.Button(root, text="Login", command=login)
# button_login.grid(row=2, column=0, columnspan=2, pady=10)

# button_register = tk.Button(root, text="Register", command=open_register_window)
# button_register.grid(row=3, column=0, columnspan=2, pady=10)


# create_tables()  # Create tables if they do not exist
# root.mainloop()



#1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111#1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111#1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111#1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111#111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111




import tkinter as tk
from tkinter import messagebox
import psycopg2

connection = None  # Define connection globally
logged_in_user_id = None  # To store the logged-in user's ID

def connect_to_db():
    global connection  # Access the global connection variable
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="1234",
            host="localhost",
            port="5432",
            database="user_db"
        )
        messagebox.showinfo("Success", "Connected to PostgreSQL database successfully!")
        return connection
    except (Exception, psycopg2.Error) as error:
        messagebox.showerror("Error", f"Failed to connect to PostgreSQL database: {error}")
        return None

def create_tables():
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    username VARCHAR(255) NOT NULL UNIQUE,
                    password VARCHAR(255) NOT NULL
                );
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS timers (
                    id SERIAL PRIMARY KEY,
                    user_id INTEGER NOT NULL,
                    seconds INTEGER NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users(id)
                );
            """)
            connection.commit()
            cursor.close()
        except (Exception, psycopg2.Error) as error:
            messagebox.showerror("Error", f"Failed to create tables: {error}")
        finally:
            connection.close()

def login():
    global logged_in_user_id
    username = entry_login_username.get()
    password = entry_login_password.get()

    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT id FROM users WHERE username=%s AND password=%s", (username, password))
            user = cursor.fetchone()
            if user:
                logged_in_user_id = user[0]
                messagebox.showinfo("Login Successful", f"Welcome, {username}!")
                open_welcome_window()
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

def save_timer(seconds):
    if logged_in_user_id is None:
        messagebox.showerror("Error", "No user is logged in.")
        return
    
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO timers (user_id, seconds) VALUES (%s, %s)", (logged_in_user_id, seconds))
            connection.commit()
            messagebox.showinfo("Success", f"Timer {seconds} saved successfully!")
        except (Exception, psycopg2.Error) as error:
            messagebox.showerror("Error", f"Failed to save timer: {error}")
        finally:
            connection.close()

def open_welcome_window():
    welcome_window = tk.Toplevel(root)
    welcome_window.title("Welcome")
    welcome_window.geometry("500x550")

    timer_label = tk.Label(welcome_window, text="00:00:00", font=("Arial", 24))
    timer_label.pack()

    def update_timer(seconds):
        nonlocal running
        if running:
            hours = seconds // 3600
            minutes = (seconds % 3600) // 60
            secs = seconds % 60
            timer_label.config(text=f"{hours:02d}:{minutes:02d}:{secs:02d}")
            welcome_window.after(1000, update_timer, seconds + 1)
            return seconds + 1

    def start_timer():
        nonlocal running, seconds
        if not running:
            running = True
            seconds = update_timer(0)

    def stop_timer():
        nonlocal running
        running = False

    def submit_time():
        nonlocal running, seconds
        running = False
        save_timer(seconds)

    running = False
    seconds = 0

    start_button = tk.Button(welcome_window, text="Start Timer", command=start_timer)
    start_button.pack()

    stop_button = tk.Button(welcome_window, text="Stop Timer", command=stop_timer)
    stop_button.pack()

    submit_button = tk.Button(welcome_window, text="Submit Time", command=submit_time)
    submit_button.pack()

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

def open_scoreboard_window():
    scoreboard_window = tk.Toplevel(root)
    scoreboard_window.title("Top Users")
    scoreboard_window.geometry("500x550")

    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT users.username, SUM(timers.seconds) AS total_time
                FROM timers
                JOIN users ON timers.user_id = users.id
                GROUP BY users.username
                ORDER BY total_time DESC
                LIMIT 10
            """)
            top_users = cursor.fetchall()
            cursor.close()
            
            if top_users:
                for idx, user in enumerate(top_users):
                    user_label = tk.Label(scoreboard_window, text=f"{idx + 1}. {user[0]} - {user[1]} seconds")
                    user_label.pack()
            else:
                no_data_label = tk.Label(scoreboard_window, text="No data available")
                no_data_label.pack()
        except (Exception, psycopg2.Error) as error:
            messagebox.showerror("Error", f"Failed to retrieve scoreboard data: {error}")
        finally:
            connection.close()

root = tk.Tk()
root.title("Login")
root.geometry("300x250")

label_login_username = tk.Label(root, text="Username:")
label_login_username.grid(row=0, column=0, padx=10, pady=5)
entry_login_username = tk.Entry(root)
entry_login_username.grid(row=0, column=1, padx=10, pady=5)

label_login_password = tk.Label(root, text="Password:")
label_login_password.grid(row=1, column=0, padx=10, pady=5)
entry_login_password = tk.Entry(root, show="*")
entry_login_password.grid(row=1, column=1, padx=10, pady=5)

button_login = tk.Button(root, text="Login", command=login)
button_login.grid(row=2, column=0, columnspan=2, pady=10)

button_register = tk.Button(root, text="Register", command=open_register_window)
button_register.grid(row=3, column=0, columnspan=2, pady=10)

button_scoreboard = tk.Button(root, text="Scoreboard", command=open_scoreboard_window)
button_scoreboard.grid(row=4, column=0, columnspan=2, pady=10)

create_tables()  # Create tables if they do not exist
root.mainloop()

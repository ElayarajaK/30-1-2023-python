import tkinter as tk
import mysql.connector


# Connect to MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="raja_db"
)


# Create cursor
mycursor = mydb.cursor()


# Create GUI window
root = tk.Tk()
root.title("CRUD App")


# Define functions for CRUD operations
def create():
    # Get input values from user
    name = name_entry.get()
    email = email_entry.get()
    
    # Execute MySQL query to insert data
    sql = "INSERT INTO customers (name, email) VALUES (%s, %s)"
    val = (name, email)
    mycursor.execute(sql, val)
    mydb.commit()
    
    # Clear input fields
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)


def read():
    # Execute MySQL query to select all data
    mycursor.execute("SELECT * FROM customers")
    result = mycursor.fetchall()
    
    # Display data in a new window
    top = tk.Toplevel()
    top.title("Read Data")
    for row in result:
        tk.Label(top, text=row).pack()


def update():
    # Get input values from user
    name = name_entry.get()
    email = email_entry.get()
    
    # Execute MySQL query to update data
    sql = "UPDATE customers SET email = %s WHERE name = %s"
    val = (email, name)
    mycursor.execute(sql, val)
    mydb.commit()
    
    # Clear input fields
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)


def delete():
    # Get input values from user
    name = name_entry.get()
    
    # Execute MySQL query to delete data
    sql = "DELETE FROM customers WHERE name = %s"
    val = (name,)
    mycursor.execute(sql, val)
    mydb.commit()
    
    # Clear input fields
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)


# Create input fields and buttons
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)


email_label = tk.Label(root, text="Email:")
email_label.grid(row=1, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1)


create_button = tk.Button(root, text="Create", command=create)
create_button.grid(row=2, column=0)


read_button = tk.Button(root, text="Read", command=read)
read_button.grid(row=2, column=1)


update_button = tk.Button(root, text="Update", command=update)
update_button.grid(row=2, column=2)


delete_button = tk.Button(root, text="Delete", command=delete)
delete_button.grid(row=2, column=3)


# Run GUI loop
root.mainloop()

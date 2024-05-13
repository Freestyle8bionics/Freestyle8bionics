import random
from cryptography.fernet import Fernet
import Password_Management
import Password_management_generator
import Password_Management_GUI
import password_security
import string
import customtkinter
import sqlite3
import hashlib
import os
import sys

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")


def login():
    print("Sign In")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login System", font=("Roboto", 24))
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)
entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)

root.mainloop()

conn = sqlite3.connect("userdata.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS userdata (
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL

)
""")

username1, password1 = "connor942", hashlib.sha256("connorpassword392".encode("utf-8")).hexdigest()
username2, password2 = "myaccount123", hashlib.sha256("myP4s5w0rd".encode("utf-8")).hexdigest()
username3, password3 = "otheraccount", hashlib.sha256("0tHerP4s5W()rd".encode("utf-8")).hexdigest()
username4, password4 = "oldman", hashlib.sha256("oldhackers".encode("utf-8")).hexdigest()
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username1, password1))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username2, password2))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username3, password3))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username4, password4))

conn.commit()

def PasswordGenerator():
    uppercase_letters = Password_management_generator.uppercase_letters
    lowercase_letters = Password_management_generator.lowercase_letters
    digits = Password_management_generator.digits
    symbols = Password_management_generator.symbols

    upper, lower, nums, syms = True, True, True, True

    all = ""

    if upper:
        all += uppercase_letters
    if lower:
        all += lowercase_letters
    if nums:
        all += digits
    if syms:
        all += symbols

    length = 20
    amount = 10

    seed = "FreestyleBionics"

    random.seed(seed)

    for x in range(amount):
        password = "".join(random.sample(all, length))
        new_password = str(password)

    return new_password

print(PasswordGenerator)

password = "helloworld"

upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
special = any([1 if c in string.punctuation else 0 for c in password])
digits = any([1 if c in string.digits else 0 for c in password])

characters = [upper_case, lower_case, special, digits]

length = len(password)

score = 0

with open('common.txt', 'r') as f:
    common = f.read().splitlines()

if password in common:
    print("Password was found in a common list. Score: 0 / 7")
    exit()

if length > 8:
    score += 1
if length > 12:
    score += 1
if length > 17:
    score += 1
if length > 20:
    score += 1

class PasswordManager:
    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dict = {}

    def create_key(self, path):
        self.key = Fernet.generate_key()
        with open(path, 'wb') as f:
            f.write(self.key)

    def load_key(self, path):
        with open(path, 'rb') as f:
            self.key = f.read()

    def create_password_file(self, path, initual_values=None):
        self.password_file = path

        if initual_values is not None:
            for key, value in initual_values.items():
                self.add_password(key, value)

    def load_password_file(self, path):
        self.password_file = path

        with open(path, 'r') as f:
            for line in f:
                site, encrypted = line.split(":")
                self.password_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode()

    def add_password(self, site, password):
        self.password_dict[site] = password

        if self.password_file is not None:
            with open(self.password_file, 'a+') as f:
                encrypted = Fernet(self.key).encrypt(password.encode())
                f.write(site + ":" + encrypted.decode() + "\n")

    def get_password(self, site):
        return self.password_dict[site]

def mAin():
    password = {
    "email": "1234567",
    "facebook": "fbp/^\_/^\>-<ssword",
    "youtube": "rU5u85(r!b3d",
    "another thing": "1241wd3"
    }

    pm = PasswordManager()

    print("""What do you want to do?
        (1) Create a new key
        (2) Load an existing key
        (3) Create new password file
        (4) Load and existing password file
        (5) Add a new password
        (6) Get a password
        (q) Quit
        """)

    done = False

    while not done:
        choice = input("Enter your choice: ")
        if choice == "1":
            path = input("Enter path: ")
            pm.create_key(path)
        elif choice == "2":
            path = input("Enter path: ")
            pm.load_key(path)
        elif choice == "3":
            path = input("Enter path: ")
            pm.create_password_file(path, password)
        elif choice == "4":
            path = input("Enter path: ")
            pm.load_password_file(path)
        elif choice == "5":
            site = input("Enter the site: ")
            password = input("Enter the password: ")
            pm.add_password(site, password)
        elif choice == "6":
            site = input("What site do you want: ")
            print(f"Password for {site} is {pm.get_password(site)}")
        elif choice == "q":
            done = True
            print("Bye")
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    mAin()
    PasswordGenerator()

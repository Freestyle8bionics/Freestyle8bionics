import customtkinter
from streamlit import switch_page
import Password_management_generator
from Password_manager.Main import PasswordGenerator
import password_storage
import Password_strength_checker

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Do you want to save or reset?", font=("Roboto", 24))
label.pack(pady=12, padx=10)

button1 = customtkinter.CTkButton(master=frame, text="Save", root='/Users/freestylebionicsyt/Documents/Freestyle bionics Official/Artificial intelligence/Password_manager/password_storage.py')
button1.pack(pady=12, padx=10)

button2 = customtkinter.CTkButton(master=frame, text="Reset", root='/Users/freestylebionicsyt/Documents/Freestyle bionics Official/Artificial intelligence/Password_manager/password_generator_UI.py')
button2.pack(pady=12, padx=10)

password_generator = Password_management_generator
manager = password_storage.manager

def Password_generator_tool(self, password_generator):
    self.password_generator = Password_management_generator
    password_generator = PasswordGenerator

def generator_sign_up():
    """
    Prompts the user to enter their username and password for manual sign up.
    """
    username = input("Enter your preferred Email: ")
    password = print(Password_management_generator.password)

    if password != Password_strength_checker.score:
        print("Passwords do not match. Please try again.")
        generator_sign_up()
    else:
        manager.add_password(username, password)
        print("Sign up successful!")

root.mainloop()


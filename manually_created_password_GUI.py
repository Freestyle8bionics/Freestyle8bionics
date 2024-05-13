from click import password_option
import customtkinter
from django.forms import EmailInput, PasswordInput
import password_storage
import manually_created_password_GUI
import password_generator_UI
import create_new_password
import Password_strength_checker

manager = password_storage.manager

def manual_sign_up():
    """
    Prompts the user to enter their username and password for manual sign up.
    """
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    confirm_password = input("Confirm your password: ")

    if password != (confirm_password and Password_strength_checker):
        print("Passwords do not match. Please try again.")
        manual_sign_up()
    else:
        manager.add_password(username, password)
        print("Sign up successful!")

from streamlit import switch_page
import password_generator_UI
import manually_created_password_GUI

def sign_up_op1(self):
    self.manual_sign_up = manually_created_password_GUI
    switch_page(page='/Users/freestylebionicsyt/Documents/Freestyle bionics Official/Artificial intelligence/Password_manager/manually_created_password_GUI.py')

def sign_up_op2(self):
    self.password_generator_tool = password_generator_UI
    switch_page(page='/Users/freestylebionicsyt/Documents/Freestyle bionics Official/Artificial intelligence/Password_manager/password_generator_UI.py')

def sign_up_options():
    """
    Provides two sign up options: manual and automatic tool.
    """
    print("Welcome to the sign up process!")
    print("Choose one of the following options:")
    print("1. Manual sign up")
    print("2. Automatic sign up tool")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        sign_up_op1(self=manually_created_password_GUI)
    elif choice == "2":
        sign_up_op2(self=password_generator_UI)
    else:
        print("Invalid choice. Please try again.")


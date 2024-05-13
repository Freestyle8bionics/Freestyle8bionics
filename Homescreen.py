import customtkinter
import Password_Management_GUI
import create_new_password

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")


def HomePage():
    print("Password Manager")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="HomePage", font=("Roboto", 24))
label.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", root=Password_Management_GUI)
button.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Sign Up", root=create_new_password)
button.pack(pady=12, padx=10)


root.mainloop()


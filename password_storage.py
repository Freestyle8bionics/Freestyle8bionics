import Password_Management
import Password_management_generator
import Password_strength_checker
import Password_Management_GUI
import manually_created_password_GUI
import password_generator_UI
import server
import client
import API_keys
import password_security
import create_new_password

class PasswordStorageManager:
    def __init__(self):
        self.passwords = {}

    def add_password(self, username, password):
        self.passwords[username] = password

    def get_password(self, username):
        try:
            return self.passwords[username]
        except KeyError:
            return None

    def delete_password(self, username):
        try:
            del self.passwords[username]
        except KeyError:
            pass

    def change_password(self, username, new_password):
        try:
            self.passwords[username] = new_password
        except KeyError:
            pass
    
# Example usage:
manager = PasswordStorageManager()
manager.add_password("admin", "password")
print(manager.get_password("admin"))  # Output: password
manager.delete_password("admin")
print(manager.get_password("admin"))  # Output: None
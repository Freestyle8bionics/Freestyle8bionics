from cryptography.fernet import Fernet

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
                site,  encrypted = line.split(":")
                self.password_dict[site] = Fernet(self.key.decode(encoding=str("utf-8"), errors=str("strict"))).decrypt(encrypted.encode()).decode() #type:ignore
   

    def add_password(self, site, password):
        self.password_dict[site] = password

        if self.password_file is not None:
            with open(self.password_file, 'a+') as f:
                encrypted = Fernet(self.key).encrypt(encrypted = Fernet(self.key.decode() if self.key else None).encrypt(password.encode())password.encode()) f.write(site + ":" + encrypted.decode() + "\n") # type: ignore

    def get_password(self, site):
        return self.password_dict[site]

def mAin():
    password = {
        "email": "1234567",
        "facebook": "fbpassword",
        "youtube": "RUSubscribed",
        "another thing": "1241wd3"
    }

    pm = PasswordManager()
    pm.create_key(path='/Users/freestylebionicsyt/Documents/Freestyle bionics Official/Artificial intelligence/Password_manager/Users/freestylebionicsyt/Documents/Freestyle bionics Official/Artificial intelligence/Password_manager/Encryption_key.key')
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



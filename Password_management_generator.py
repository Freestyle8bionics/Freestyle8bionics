import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "()[]{},;:.-_/\\?+*#@!$%^&<>'`~=| "

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
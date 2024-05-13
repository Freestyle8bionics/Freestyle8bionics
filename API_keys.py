import secrets
import string

def generate_api_key(length=32):
    alphabet = string.ascii_letters + string.digits
    api_key = ''.join(secrets.choice(alphabet) for _ in range(length))
    return api_key

# Generate a 32-character API key
api_key = generate_api_key()
print("Generated API Key:", api_key)

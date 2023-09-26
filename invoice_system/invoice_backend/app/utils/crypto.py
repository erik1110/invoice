from Crypto.Cipher import AES
import base64
import hashlib
import os
from dotenv import load_dotenv
from rich.console import Console

console = Console()
load_dotenv("/usr/src/app/.env")
secret = os.getenv("SECRET_KEY")

def encrypt_with_salt(data):
    salt = hashlib.sha256(secret.encode()).digest()
    key = hashlib.pbkdf2_hmac('sha256', secret.encode(), salt, 100000)
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(data.encode())
    return base64.b64encode(salt + cipher.nonce + tag + ciphertext).decode('utf-8')

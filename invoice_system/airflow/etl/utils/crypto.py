from Crypto.Cipher import AES
from dotenv import load_dotenv
import base64
import logging
import hashlib
import os

load_dotenv("/opt/airflow/.env")
secret_key = os.getenv("SECRET_KEY")

def decrypt_with_salt(encrypted_data):
    encrypted_data = base64.b64decode(encrypted_data)
    salt = encrypted_data[:32]
    nonce = encrypted_data[32:32+16]
    tag = encrypted_data[32+16:32+32]
    ciphertext = encrypted_data[32+32:]

    key = hashlib.pbkdf2_hmac('sha256', secret_key.encode(), salt, 100000)
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)

    try:
        decrypted_data = cipher.decrypt_and_verify(ciphertext, tag)
        return decrypted_data.decode('utf-8')
    except Exception as e:
        logging.info(e)
        raise e
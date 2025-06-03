import re
import bcrypt
import os
from dotenv import load_dotenv


load_dotenv()

# Load password from env
def load_hashed_password():
    hashed_password = os.getenv("HASHED_PASSWORD")
    if hashed_password is None:
        hashed_password = False
    return hashed_password

def check_password(password):
    hashed_password = load_hashed_password()
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))


def escape_filename(filename):
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    filename = filename.replace(' ', '-')
    return filename
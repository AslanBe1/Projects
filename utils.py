import time
import bcrypt


def generate_id():
    return time.time_ns()


def hash_password(raw_password: str):
    raw_password = raw_password.encode('utf-8')
    return bcrypt.hashpw(raw_password, salt=bcrypt.gensalt())

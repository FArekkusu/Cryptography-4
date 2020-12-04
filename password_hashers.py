import bcrypt
import hashlib
import secrets

def hash_md5(password):
    password_bytes = bytes(password, encoding="ascii")
    hash = hashlib.md5(password_bytes).hexdigest()
    return {"hash": hash}

def hash_sha1_salt(password):
    salt = secrets.token_hex(8)
    salt_bytes = bytes.fromhex(salt)
    password_bytes = bytes(password, encoding="ascii")
    hash = hashlib.sha1(password_bytes + salt_bytes).hexdigest()
    return {"hash": hash, "salt": salt}

def hash_bcrypt(password):
    salt = bcrypt.gensalt(6)
    password_bytes = bytes(password, encoding="ascii")
    hash = bcrypt.hashpw(password_bytes, salt).decode()
    return {"hash": hash}
import hashlib


def hash_data(data: dict) -> str:
    return hashlib.sha256(str(data).encode()).hexdigest()

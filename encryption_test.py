import hashlib
print(hashlib.md5(b"hello").hexdigest())  # Insecure
print(hashlib.sha1(b"hello").hexdigest())  # Deprecated
from Crypto.Cipher import AES  # Good

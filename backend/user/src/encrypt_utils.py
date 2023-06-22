from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import base64,environ

class EncryptUtils:

    env = environ.Env()
    key = env('KEY')
    BS = 16
    def __init__(self):
        self.cipher = AES.new(pad(self.key.encode(), self.BS), AES.MODE_ECB)

    def encrypt(self, raw: str):
        encrypted =self.cipher.encrypt(pad(raw.encode(), self.BS))
        return base64.b64encode(encrypted).decode()

    def decrypt(self, base64decode):
        decrypted=base64.b64decode(base64decode)
        return unpad(self.cipher.decrypt(decrypted),self.BS).decode()


# from Crypto.Cipher import AES
# from Crypto import Random
# from Crypto.Protocol.KDF import PBKDF2
#
# import base64
#
#
#
# BLOCK_SIZE = 16
# s= "23"
# pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
# unpad = lambda s: s[:-ord(s[len(s) -1:])]
#
# #
# # def get_private_key(random):
# #     # salt = my_settings.SECRET.get('salt')
# #     salt = "testsalt"
# #     kdf = PBKDF2(random,salt,64,1000)
# #     key = kdf[:32]
# random="randomkey" #py_settings.SECRET.get('random')0
# raw = "test"
# raw = pad(raw).encode('utf-8')
# print("raw 값이다")
# print(raw)
#
# iv = Random.new().read(AES.block_size)
# print(iv)
# salt = "testsalt"
# kdf = PBKDF2(random, salt, 64, 1000)
# key = kdf[:32]
# cipher = AES.new(key,AES.MODE_CBC, iv)
# print(cipher.encrypt(raw))

# # key = get_random_bytes(16)  # 16바이트(128비트)의 임의의 키 생성
# key = "test"  # 16바이트(128비트)의 임의의 키 생성
# print(key)
# # 키를 생성합니다.
#
# def encrypt_data(data, key):
#     cipher = AES.new(key, AES.MODE_EAX)
#     nonce = cipher.nonce
#     ciphertext, tag = cipher.encrypt_and_digest(data.encode())
#
#     return nonce + ciphertext + tag
#
# plaintext = "Hello, World!"
# print(plaintext)
# encrypted_data = encrypt_data(plaintext, key)
# print(encrypted_data)
#
# def decrypt_data(encrypted_data, key):
#     nonce = encrypted_data[:16]
#     ciphertext = encrypted_data[16:-16]
#     tag = encrypted_data[-16:]
#
#     cipher = AES.new(key, AES.MODE_EAX, nonce)
#     decrypted_data = cipher.decrypt_and_verify(ciphertext, tag)
#
#     return decrypted_data.decode()
#
# decrypted_text = decrypt_data(encrypted_data, key)
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import base64

#padding 설정
BS = 16

#변수 설정
key = 'testkey'
ori = 'test@doru.com'
print('ori',ori)

#암호화
cipher = AES.new(pad(key.encode(), BS), AES.MODE_ECB)
msg = cipher.encrypt(pad(ori.encode(), BS))
print('msg',msg)
m2 = base64.b64encode(msg)
print('base64',m2)

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

# ¡¡¡IMPORTANTE!!!
# Primero ejecutar en terminal "pip install pycryptodome"

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = b'SeguridadInforma'
iv = key
# la b es para poner la cadena en formato de array de bytes, para que pueda ser utilizada como clave AES
# Vector de inicialización pseudoaleatorio de 16 bytes, mismo tamaño que la clave

def aes_decrypt(ciphertext):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_ciphertext = cipher.decrypt(ciphertext)
    unpadded_plaintext = unpad(decrypted_ciphertext, AES.block_size)
    # el unpad elimina los bytes de relleno del mensaje que se habían agregado anteriormente al cifrar el mensaje
    return unpadded_plaintext.decode('utf-8')

def aes_encrypt(plaintext):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_plaintext = pad(plaintext.encode('latin-1'), AES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext.hex()

print("Presione 1 para desencriptar, 2 para encriptar")

decision = int(input().strip())

if decision == 1:
    print("introduzca string hexadecimal a desencriptar: ")
    print("String desencriptado:", aes_decrypt(bytes.fromhex(input().strip())))
else:
    print("introduzca string a encriptar: ")
    print("String encriptado:", aes_encrypt(input().strip()))

# ¡¡¡IMPORTANTE!!!
# Primero ejecutar en terminal "pip install pycryptodome"

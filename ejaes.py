
# ¡¡IMPORTANTE!!
# Primero ejecutar en terminal "pip install pycryptodome"

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

key = b'SeguridadInforma'
iv = key
# la b es para poner la cadena en formato de array de bytes, para que pueda ser utilizada como clave AES
# Vector de inicialización pseudoaleatorio de 16 bytes, mismo tamaño que la clave

def aes_encrypt(plaintext):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_plaintext = pad(plaintext.encode('utf-8'), AES.block_size)
    # el "padding" consiste en agregar bytes de relleno al mensaje para que este tenga un nº de bytes que sea múltiplo de 16
    # sino, no se podría aplicar el algoritmo de cifrado en bloques de 128 bits (16 bytes)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

def aes_decrypt(ciphertext):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_ciphertext = cipher.decrypt(ciphertext)
    unpadded_plaintext = unpad(decrypted_ciphertext, AES.block_size)
    # el unpad elimina los bytes de relleno del mensaje que se habían agregado anteriormente al cifrar el mensaje
    return unpadded_plaintext.decode('utf-8')


ciphertext = input().strip()

ciphertext_as_array_of_bites = bytes.fromhex(ciphertext)

decrypted_plaintext = aes_decrypt(ciphertext_as_array_of_bites)
print("Mensaje desencriptado:", decrypted_plaintext)

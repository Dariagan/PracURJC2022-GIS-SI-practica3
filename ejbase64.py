import base64

def base64_encode(string):
    encoded_bytes = base64.b64encode(string.encode('utf-8'))
    return encoded_bytes.decode('utf-8')

def base64_decode(string):
    decoded_bytes = base64.b64decode(string.encode('utf-8'))
    return decoded_bytes.decode('utf-8')


print("quieres codificar o descodificar en base64?")

if input().strip() == "codificar":
    print("escribe tu string a codificar")
    print("codificado base 64:", base64_encode(input().strip()))
else:
    print("escribe tu string a descodificar")
    print("descodificado base 64:", base64_decode(input().strip()))


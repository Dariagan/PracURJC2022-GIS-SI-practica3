def xor_encode_decode(message, key):

    message_bytes = message.encode('iso-8859-1')
    key_bytes = key.encode('iso-8859-1')

    encoded_bytes = bytearray(len(message_bytes))

    for i in range(len(message_bytes)):
        # Por cada byte i del mensaje, se le realizan internamente 8 operaciones XORs (hay 8 bits por byte)...
        # respectivamente con cada bit del byte (i mod tamaño_clave) de la clave
        encoded_bytes[i] = message_bytes[i] ^ key_bytes[i % len(key_bytes)]
        # El módulo, como siempre, es para "dar la vuelta" dentro de la llave si el mensaje sobrepasa la longitud de esta
    encoded_message = encoded_bytes.decode('iso-8859-1')

    return encoded_message

text, key = input().strip().split()

print(xor_encode_decode(text, key))
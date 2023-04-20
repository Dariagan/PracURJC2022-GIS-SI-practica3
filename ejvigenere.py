ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def vigenere_cipher(plaintext, key):
    ciphertext = ""
    key_index = 0
    for char in plaintext:
        if char in ALPHABET:
            # Se consigue el índice horizontal numérico del carácter del texto en claro dentro de la tabla de Vigenère
            msgchar_table_index = ALPHABET.index(char)

            # Se consigue el carácter de clave correspondiente a la posición en la que estamos
            key_char = key[key_index]
            key_index += 1

            # Si nos sobrepasamos el tamaño de la clave, el índice vuelve a apuntar a la primera posición de esta
            key_index %= len(key)

            # Se consigue el índice vertical numérico del carácter de la clave dentro de la tabla de Vigenère
            key_char_table_index = ALPHABET.index(key_char)

            # Porque la tabla se basa en rotar 1 hacia arriba por cada columna atravesada,
            # se puede aplicar la fórmula de cifrado de Vigenere.
            # El módulo es para "dar la vuelta" en el alfabeto y no sobrepasarlo.
            cipher_index = (msgchar_table_index + key_char_table_index) % len(ALPHABET)

            # Se añade la letra cifrada
            ciphertext += ALPHABET[cipher_index]
        else:
            ciphertext += char
    return ciphertext


def vigenere_decipher(ciphertext, key):
    plaintext = ""
    key_index = 0
    for char in ciphertext:
        if char in ALPHABET:
            msgchar_table_index = ALPHABET.index(char)
            key_char = key[key_index]
            key_index += 1
            key_index %= len(key)
            key_char_table_index = ALPHABET.index(key_char)

            # En este caso hay que "deshacer" la suma que había aplicado la letra de la llave (su índice en la tabla)
            plain_index = (msgchar_table_index - key_char_table_index) % len(ALPHABET)
            plaintext += ALPHABET[plain_index]
        else:
            plaintext += char

    return plaintext


print("quieres cifrar o descifrar en Vigenère?")

if input().strip() == "cifrar":
    print("escribe tu string a cifrar, y la clave")
    ciphertext, key = input().strip().split()
    print("cifrado en Vigénere:", vigenere_cipher(ciphertext, key))
else:
    print("escribe tu string a descifrar, y la clave")
    ciphertext, key = input().strip().split()
    print("descifrado en Vigénere:", vigenere_decipher(ciphertext, key))




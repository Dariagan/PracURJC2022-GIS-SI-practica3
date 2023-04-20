def rotate_char(char, n):
    if not char.isalpha():
        return char
    if char.isupper():
        return chr((ord(char) - 65 + n) % 26 + 65)
    else:
        return chr((ord(char) - 97 + n) % 26 + 97)

# Esta función sirve tanto para cifrar como para descifrar
def rotate_n(string, n):
    rotated = ""
    for char in string:
        rotated += rotate_char(char, n)
    return rotated

def brute_force(string):
    for i in range(1, 26):
        print(rotate_n(string, i))

# Si queremos cifrar en ROT-N descomentamos estas dos líneas y comentamos la otra
# string, n = input().strip().split()
# print(rotate_n(string, n))

brute_force(input().strip())


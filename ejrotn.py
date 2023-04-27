def rotate_char(char, n):
    if not char.isalpha():
        return char
    if char.isupper():
        return chr((ord(char) - 65 + n) % 26 + 65)
    else:
        return chr((ord(char) - 97 + n) % 26 + 97)

# Esta función sirve tanto para codificar como para descodificar
def rotate_n(string, n):
    rotated = ""
    for char in string:
        rotated += rotate_char(char, n)
    return rotated

def brute_force(string):
    for i in range(1, 26):
        print("rotado", i, rotate_n(string, i))

print("Presione 1 para rotar N, 2 para realizar fuerza bruta")

if (int(input().strip()) == 1):
    print("String, y N a rotar:")
    string, n = input().strip().split()
    print((rotate_n(string, int(n))))
else:
    print("String a rotar 25 veces:")
    brute_force(input().strip())



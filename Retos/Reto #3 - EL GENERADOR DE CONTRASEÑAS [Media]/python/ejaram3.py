import string
import random

CARACTERES = (
    string.digits
    + string.punctuation
    + string.ascii_lowercase
    + string.ascii_uppercase
)


def generador_contrasenas(longitud: int) -> str:
    if 8 <= longitud <= 16:
        return ''.join(random.choices(CARACTERES, k=longitud))
    return 'La longitud de tu contraseña debe ser entre 8 y 16 caracteres'


if __name__ == "__main__":
    print(generador_contrasenas(8))
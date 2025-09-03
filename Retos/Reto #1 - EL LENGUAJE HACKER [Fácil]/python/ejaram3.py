# Mapa de conversión a LEET
leet_map = [
    ('a', '4'),  ('b', '8'),   ('c', '<'),   ('d', '[)'),  ('e', '3'),
    ('f', 'ph'), ('g', '6'),   ('h', '#'),   ('i', '1'),   ('j', '_|'),
    ('k', '|<'), ('l', '|_'),  ('m', '/\\/\\'), ('n', '|\\|'), ('o', '0'),
    ('p', '|>'), ('q', '0_'),  ('r', '|2'),  ('s', '5'),   ('t', '7'),
    ('u', '(_)'), ('v', '\\/'), ('w', '\\/\\/'), ('x', '><'), ('y', '`/'),
    ('z', '2'),
    (' ', ' '),
    ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'),
    ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9')
]

# Convertimos la lista de tuplas en diccionario para búsqueda O(1)
LEET = dict(leet_map)


def translate(text: str) -> str:
    """
    Traduce un texto a LEET.

    Parámetros:
        text (str): cadena de entrada

    Retorna:
        str: cadena traducida a estilo LEET
    """
    return ''.join(LEET.get(char.lower(), char) for char in text)


message = input('¿Qué quieres traducir?\n')
print(translate(message))

def menu() -> str:
    texto_menu = (
        "Bienvenido al juego de 🗿 Piedra, 📄 Papel, ✂️ Tijera, 🦎 Lagarto o 🖖 Spock\n\n"
        "Elige una de las siguientes opciones:\n"
        "1. 🗿 Piedra\n"
        "2. 📄 Papel\n"
        "3. ✂️ Tijera\n"
        "4. 🦎 Lagarto\n"
        "5. 🖖 Spock\n"
        "6. Salir\n"
    )
    return texto_menu


def seleccion_juego(seleccion):
    match seleccion:
        case 1: return '🗿 Piedra'
        case 2: return '📄 Papel'
        case 3: return '✂️ Tijera'
        case 4: return '🦎 Lagarto'
        case 5: return '🖖 Spock'
        case _: return None


condiciones = {
    ('✂️ Tijera', '📄 Papel'): '✂️ Tijera',
    ('✂️ Tijera', '🦎 Lagarto'): '✂️ Tijera',
    ('📄 Papel', '🗿 Piedra'): '📄 Papel',
    ('📄 Papel', '🖖 Spock'): '📄 Papel',
    ('🗿 Piedra', '✂️ Tijera'): '🗿 Piedra',
    ('🗿 Piedra', '🦎 Lagarto'): '🗿 Piedra',
    ('🦎 Lagarto', '🖖 Spock'): '🦎 Lagarto',
    ('🦎 Lagarto', '📄 Papel'): '🦎 Lagarto',
    ('🖖 Spock', '✂️ Tijera'): '🖖 Spock',
    ('🖖 Spock', '🗿 Piedra'): '🖖 Spock'
}

opciones = {x for k in condiciones.keys() for x in k}


def main():
    salir = False
    while not salir:
        print(menu())

        partidas = 3
        puntos_j1 = 0
        puntos_j2 = 0

        while partidas > 0:
            seleccion = int(input('Elige Jugador 1 (1-6): '))
            if seleccion == 6:
                print("Hasta Luego!!")
                salir = True
                break
            j1 = seleccion_juego(seleccion)

            seleccion = int(input('Elige Jugador 2 (1-6): '))
            if seleccion == 6:
                print("Hasta Luego!!")
                salir = True
                break
            j2 = seleccion_juego(seleccion)

            print(f"Jugador 1 eligió {j1}, Jugador 2 eligió {j2}")

            if j1 not in opciones or j2 not in opciones:
                print('Opción inválida')
                continue

            if j1 == j2:
                print("Empate")
                partidas -= 1
                continue

            for par, gana in condiciones.items():
                if (j1, j2) == par:
                    puntos_j1 += 1
                    print("Punto para Jugador 1")
                    print(f'Gana {gana}\n')
                    break
                if (j2, j1) == par:
                    puntos_j2 += 1
                    print("Punto para Jugador 2")
                    print(f'Gana {gana}\n')
                    break

            print(f'Puntos Jugador 1 {puntos_j1}')
            print(f'Puntos Jugador 2 {puntos_j2}')
            partidas -= 1

        if salir:
            break

        if puntos_j1 > puntos_j2:
            print("Felicitaciones 🎉 gana Jugador 1\n\n")
        elif puntos_j2 > puntos_j1:
            print("Felicitaciones 🎉 gana Jugador 2\n\n")
        else:
            print("La serie terminó en empate 🤝\n\n")


if __name__ == "__main__":
    main()
import random

PUNTOS_TENIS = {0: "Love", 1: "15", 2: "30", 3: "40"}


def juego(partidas: int) -> list[str]:
    secuencia = []
    while partidas > 0:
        secuencia.append('P1' if random.randint(0, 1) == 1 else 'P2')
        partidas -= 1
    return secuencia


def mostrar_marcador(secuencia: list[str]) -> str | None:
    p1 = p2 = 0

    for ganador in secuencia:
        if ganador == 'P1':
            p1 += 1
        else:
            p2 += 1

        # ¿Juego ganado?
        if (p1 >= 4 or p2 >= 4) and abs(p1 - p2) >= 2:
            ganador_juego = 'P1' if p1 > p2 else 'P2'
            print(f"Ha ganado {ganador_juego}")
            return ganador_juego

        # Zona deuce/ventaja
        if p1 >= 3 and p2 >= 3:
            if p1 == p2:
                print("Deuce")
            elif p1 > p2:
                print("Ventaja P1")
            else:
                print("Ventaja P2")
            continue

        # Marcador normal
        s1 = PUNTOS_TENIS.get(p1, "40")
        s2 = PUNTOS_TENIS.get(p2, "40")
        print(f"{s1} - {s2}")

    return None


def jugar_partido(jugador1: str, jugador2: str):
    seguir = "si"
    while seguir == "si":
        print("\nWimbledon")
        print(f"{jugador1} VS {jugador2}")

        sorteo_saque = random.choice([jugador1, jugador2])
        print(f"Inicia con el saque: {sorteo_saque.split()[0]}")

        secuencia_juego = juego(12)
        print(f"Secuencia: {secuencia_juego}")

        ganador_id = mostrar_marcador(secuencia_juego)
        if ganador_id == 'P1':
            print(f"Ganador del juego: {jugador1}")
        elif ganador_id == 'P2':
            print(f"Ganador del juego: {jugador2}")
        else:
            print("El juego no terminó correctamente.")

        seguir = input("¿Quieres seguir jugando? (si/no): ").lower()


if __name__ == "__main__":
    j1 = input('Ingresa el nombre del segundo jugador: ')
    j2 = input('Ingresa el nombre del segundo jugador: ')
    jugar_partido(j1, j2)

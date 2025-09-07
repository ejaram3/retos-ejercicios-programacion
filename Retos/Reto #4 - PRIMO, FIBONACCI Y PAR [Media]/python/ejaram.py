
def es_primo(n: int) -> bool:
    """Determina si un número es primo.

    Args:
        n (int): Número entero a evaluar.

    Returns:
        bool: True si el número es primo, False en caso contrario.
    """
    if n <= 1:
        return False
    divisores = [d for d in range(1, n+1) if n % d == 0]
    return len(divisores) == 2


def fib(n: int) -> int:
    """Determina la secuencia fibonacci para un numero.

    Args:
        n (int): numero entero mayor a cero

    Returns:
        int: el resultado fibonacci de la de la sumatoria de su secuencia fib
    """
    if n < 0:
        raise ValueError("n debe ser >= 0")
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)



def es_fibonacci(x: int) -> bool:
    """Determina si un numero es fibonacci.

    Args:
        x (int): numero entero a evaluar.

    Returns:
        bool: True si el numero es fibonacci, de lo contrario retorna False
    """

    if x == 0 or x == 1:
        return True

    i = 2
    while True:
        f = fib(i)
        if f == x:
            return True
        if f > x:
            return False
        i += 1


def es_par(n: int) -> bool:
    """Determina si un numero es par.

    Args:
        n (int): numero entero a evaluar.

    Returns:
        bool: True si es par, de lo contrarios False
    """
    if n % 2 == 0:
        return True
    return False


def evaluar_condicion(n: int) -> str:
    """Evalúa un número y determina si es primo, de Fibonacci y/o par.

    Args:
        n (int): Número entero a evaluar.

    Returns:
        str: Cadena descriptiva con la combinación de propiedades del número:
             - Primo o no primo
             - Fibonacci o no Fibonacci
             - Par o impar
    """
    fibonacci = es_fibonacci(n)
    primo = es_primo(n)
    par = es_par(n)

    combinaciones = {
        (True, True, True): f"{n} es primo, es fibonacci y es par",
        (True, True, False): f"{n} es primo, es fibonacci y es impar",
        (True, False, True): f"{n} es primo, no es fibonacci y es par",
        (True, False, False): f"{n} es primo, no es fibonacci y es impar",
        (False, True, True): f"{n} no es primo, es fibonacci y es par",
        (False, True, False): f"{n} no es primo, es fibonacci y es impar",
        (False, False, True): f"{n} no es primo, no es fibonacci y es par",
        (False, False, False): f"{n} no es primo, no es fibonacci y es impar",
    }

    return combinaciones[(primo, fibonacci, par)]


if __name__ == "__main__":
    print(evaluar_condicion(2))
    print(evaluar_condicion(3))
    print(evaluar_condicion(4))
    print(evaluar_condicion(22))
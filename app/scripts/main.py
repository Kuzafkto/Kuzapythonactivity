"""
main.py
Archivo principal para interactuar con el usuario.
Última Modificación: 1/12/2024
Autor: Marco Valente
"""

from app.scripts.charfun import esPalindromo

def main():
    """
    Función principal que interactúa con el usuario para determinar si las frases son palíndromas.
    """
    print("Bienvenido al Verificador de Palíndromos.")
    print("Escribe una frase para verificar si es un palíndromo.")
    print("Escribe 'salir' para terminar el programa.\n")

    while True:
        # Solicitar entrada del usuario
        frase = input("Introduce una frase: ")
        
        if frase.lower() == "salir":
            print("Programa finalizado. ¡Hasta luego!")
            break
        
        # Evaluar si la frase es un palíndromo
        if esPalindromo(frase):
            print("La frase es palíndroma.\n")
        else:
            print("La frase no es palíndroma.\n")

if __name__ == "__main__":
    main()

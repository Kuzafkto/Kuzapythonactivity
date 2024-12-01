"""
charfun.py
Módulo que contiene la función para determinar si una cadena es palíndroma.
Última Modificación: 21/11/2024
Autor: Gregorio Coronado Morón
Dependencias: Unicodedata
"""

import unicodedata

def esPalindromo(cadena):
    """
    Función que verifica si una cadena es palíndroma.
    Ignora espacios, mayúsculas, tildes y caracteres no alfabéticos.

    Parámetros:
    - cadena (str): La cadena de texto a evaluar.

    Retorna:
    - bool: True si la cadena es palíndroma, False en caso contrario.
    """
    # Normalizar la cadena: eliminar tildes y convertir a ASCII
    cadena_normalizada = unicodedata.normalize('NFD', cadena).encode('ascii', 'ignore').decode('utf-8')
    
    # Eliminar caracteres no alfanuméricos y convertir a minúsculas
    cadena_limpia = ''.join(char.lower() for char in cadena_normalizada if char.isalnum())
    
    # Si la cadena limpia está vacía, se considera palíndroma
    if not cadena_limpia:
        return True

    # Comparar la cadena limpia con su reverso
    return cadena_limpia == cadena_limpia[::-1]

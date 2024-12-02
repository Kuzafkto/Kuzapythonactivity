"""
test_charfun.py
Archivo de pruebas unitarias para la función esPalindromo.
Última Modificación: 1/12/2024
Autor: Marco Valente
Dependencias: unittest, parameterized
"""

import unittest
from parameterized import parameterized
from app.scripts.charfun import esPalindromo
import random
import string

class TestCharfun(unittest.TestCase):
    """
    Clase de pruebas para la función esPalindromo.
    Contiene casos de prueba para diversos escenarios, incluyendo palíndromos generados aleatoriamente.
    """

    @parameterized.expand([
        ("palindromo_simple", "Anita lava la tina", True),
        ("con_espacios", "A man a plan a canal Panama", True),
        ("sin_palabras", "No lemon no melon", True)
    ])
    def test_palindromos_simples(self, name, cadena, esperado):
        """Tests de casos positivos simples"""
        self.assertEqual(esPalindromo(cadena), esperado)

    @parameterized.expand([
        ("no_palindromo_1", "Esto no es un palíndromo", False),
        ("no_palindromo_2", "Ensamblador me encanta", False),
        ("no_palindromo_3", "Gregorio me dará un diez", False)
    ])
    def test_no_palindromos(self, name, cadena, esperado):
        """Tests de casos negativos"""
        self.assertEqual(esPalindromo(cadena), esperado)

    @parameterized.expand([
        ("cadena_vacia", "", True),
        ("solo_espacios", "    ", True),
        ("un_caracter", "   a", True)
    ])
    def test_vacios_y_espacios(self, name, cadena, esperado):
        """Tests de cadenas vacías o con espacios"""
        self.assertEqual(esPalindromo(cadena), esperado)

    @parameterized.expand([
        ("solo_especiales", "!!!", True),
        ("especiales_y_espacios", "...   ", True),
        ("especiales_y_letra", "...a.", True)
    ])
    def test_caracteres_especiales(self, name, cadena, esperado):
        """Test de cadenas con caracteres especiales"""
        self.assertEqual(esPalindromo(cadena), esperado)

    @parameterized.expand([
        ("unicode_con_tildes", "Ánita láva la tíná", True)
    ])
    def test_combinaciones_unicode(self, name, cadena, esperado):
        """Test de cadenas con caracteres Unicode"""
        self.assertEqual(esPalindromo(cadena), esperado)

    def generar_palindromo_aleatorio(self, longitud=10):
        """
        Genera un palíndromo aleatorio.
        Toma una cadena de texto aleatoria y la convierte en palíndromo.
        
        :param longitud: longitud de la cadena aleatoria.
        :return: un palíndromo generado aleatoriamente.
        """
        # Generar una cadena aleatoria
        letras = string.ascii_lowercase
        cadena = ''.join(random.choice(letras) for _ in range(longitud))
        
        # Crear un palíndromo añadiendo la cadena invertida a la original
        palindromo = cadena + cadena[::-1]
        return palindromo

    def test_palindromos_aleatorios(self):
        """
        Genera varios palíndromos aleatorios y los prueba para asegurar que la función esPalindromo los detecte correctamente.
        """
        for _ in range(22):  # Genera y prueba 10 palíndromos aleatorios
            palindromo = self.generar_palindromo_aleatorio()
            self.assertTrue(esPalindromo(palindromo), f"El palíndromo generado {palindromo} no fue reconocido correctamente.")

if __name__ == "__main__":
    unittest.main()

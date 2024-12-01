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

class TestCharfun(unittest.TestCase):
    """
    Clase de pruebas para la función esPalindromo.
    Contiene casos de prueba para diversos escenarios.
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

if __name__ == "__main__":
    unittest.main()

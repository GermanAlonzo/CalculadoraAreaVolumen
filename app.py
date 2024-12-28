import math
import unittest

def area_circulo(radio: float) -> float:
    """
    Calcula el área de un círculo dado su radio.

    Parámetros:
        radio (float): El radio del círculo. Debe ser un número no negativo.

    Retorna:
        float: El área del círculo.

    Lanza:
        ValueError: Si el radio es negativo.
    """
    if radio < 0:
        raise ValueError("El radio no puede ser negativo.")
    return math.pi * (radio ** 2)

def area_triangulo(base: float, altura: float) -> float:
    """
    Calcula el área de un triángulo dado su base y altura.

    Parámetros:
        base (float): La base del triángulo. Debe ser un número no negativo.
        altura (float): La altura del triángulo. Debe ser un número no negativo.

    Retorna:
        float: El área del triángulo.

    Lanza:
        ValueError: Si la base o la altura son negativas.
    """
    if base < 0 or altura < 0:
        raise ValueError("La base y la altura no pueden ser negativas.")
    return (base * altura) / 2

def area_cuadrado(lado: float) -> float:
    """
    Calcula el área de un cuadrado dado su lado.

    Parámetros:
        lado (float): La longitud de un lado del cuadrado. Debe ser un número no negativo.

    Retorna:
        float: El área del cuadrado.

    Lanza:
        ValueError: Si el lado es negativo.
    """
    if lado < 0:
        raise ValueError("El lado no puede ser negativo.")
    return lado ** 2

def volumen_cubo(lado: float) -> float:
    """
    Calcula el volumen de un cubo dado su lado.

    Parámetros:
        lado (float): La longitud de un lado del cubo. Debe ser un número no negativo.

    Retorna:
        float: El volumen del cubo.

    Lanza:
        ValueError: Si el lado es negativo.
    """
    if lado < 0:
        raise ValueError("El lado no puede ser negativo.")
    return lado ** 3

def mostrar_menu():
    """
    Muestra el menú interactivo al usuario con las opciones de cálculo disponibles.
    """
    print("\n¿Qué desea calcular?")
    print("1. Área de un círculo")
    print("2. Área de un triángulo")
    print("3. Área de un cuadrado")
    print("4. Volumen de un cubo")
    print("5. Salir")

def main():
    """
    Función principal que ejecuta el programa interactivo para cálculos geométricos.
    Permite al usuario seleccionar opciones, ingresar datos y visualizar resultados.
    """
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción (1-5): "))
            if opcion == 1:
                radio = float(input("Ingrese el radio del círculo: "))
                print(f"El área del círculo es: {area_circulo(radio):.2f}")
            elif opcion == 2:
                base = float(input("Ingrese la base del triángulo: "))
                altura = float(input("Ingrese la altura del triángulo: "))
                print(f"El área del triángulo es: {area_triangulo(base, altura):.2f}")
            elif opcion == 3:
                lado = float(input("Ingrese el lado del cuadrado: "))
                print(f"El área del cuadrado es: {area_cuadrado(lado):.2f}")
            elif opcion == 4:
                lado = float(input("Ingrese el lado del cubo: "))
                print(f"El volumen del cubo es: {volumen_cubo(lado):.2f}")
            elif opcion == 5:
                print("Gracias por usar el programa. ¡Adiós!")
                break
            else:
                print("Opción inválida. Por favor, seleccione un número del 1 al 5.")
        except ValueError as e:
            print(f"Error: {e}. Por favor, ingrese un número válido.")

# Pruebas unitarias
class TestGeometria(unittest.TestCase):
    """
    Clase de pruebas unitarias para las funciones geométricas.

    Métodos:
        test_area_circulo: Prueba el cálculo del área de un círculo.
        test_area_triangulo: Prueba el cálculo del área de un triángulo.
        test_area_cuadrado: Prueba el cálculo del área de un cuadrado.
        test_volumen_cubo: Prueba el cálculo del volumen de un cubo.
    """
    def test_area_circulo(self):
        self.assertAlmostEqual(area_circulo(5), 78.53981633974483)
        with self.assertRaises(ValueError):
            area_circulo(-1)

    def test_area_triangulo(self):
        self.assertEqual(area_triangulo(4, 3), 6)
        with self.assertRaises(ValueError):
            area_triangulo(-1, 2)

    def test_area_cuadrado(self):
        self.assertEqual(area_cuadrado(4), 16)
        with self.assertRaises(ValueError):
            area_cuadrado(-1)

    def test_volumen_cubo(self):
        self.assertEqual(volumen_cubo(3), 27)
        with self.assertRaises(ValueError):
            volumen_cubo(-1)

if __name__ == "__main__":
    with open("resultados_pruebas.txt", "w") as f:
        # Crear un TextTestRunner y redirigir la salida al archivo
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        unittest.main(testRunner=runner, exit=False)

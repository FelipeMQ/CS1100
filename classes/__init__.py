class mathtools:
    """Clase para funciones matemáticas complementarias"""
    def fib(p1):
        """La función de fibbonaci imprime todos los numeros de la serie"""
        pass

print(mathtools.__doc__)
print(mathtools.fib.__doc__)

class World:
    def gravity(self, peso, const=9.8):
        return peso * const

tierra = World()
print(tierra.gravity(10))
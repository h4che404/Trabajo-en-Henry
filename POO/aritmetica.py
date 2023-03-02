class Aritmetica:
    def __init__ (self, A, B):
        self.A = A
        self.B = B
    def suma(self):
        return self.A + self.B
    def restar(self):
        return self.A - self.B
    def multiplicar(self):
        return self.A * self.B

resultado = Aritmetica(10, 5)
print (resultado.suma())
print(resultado.restar())
print(resultado.multiplicar())

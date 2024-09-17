class Potencia:
   def __init__(self,val):
      self.val=val
   def getVal(self):
       print(f"El numero al cuadrado es:{self.val*self.val}") 
 
 
class Opeacion:
   def suma(self, a, b):
      print(f"la suma de los numeros es: {a + b}")
   def resta(self, a, b):
      print(f"la resta de los numeros es: {a - b}")
   def multiplicacion(self, a, b):
      print(f"la Multiplicación de los numeros es: {a * b}")
   def division(self, a, b):
      print(f"la divisió de los numeros es: {a / b}")

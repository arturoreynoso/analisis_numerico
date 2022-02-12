from typing import Callable

def regla_falsa(f:Callable[[float], float], a:float, b:float, tolerancia:float) -> float:
  """
  Regresa una raíz de la función (si es que existe) contenido en [a, b] por el 
  método de la regla falsa o lanza un error.

  Argumentos:
  f -- la función a obtener el cero. 
  a -- el primer punto inicial.
  b -- el segundo punto inicial.
  tolerancia -- la tolerancia de la función.

  Regresa:
  La raíz de la función, o error si no la encuentra.
  
  """
  iteracion = 1
  if (f(a)*f(b)> 0):
    print("Error: Puntos iniciales incorrectos. Las imágenes debe  tener signos diferentes.")
    return 
  condicion = True

  while (condicion):
    c = (a*f(b) - b*f(a))/(f(b) - f(a)) 
    print('Iteración %d, x2 = %0.6f and f(c) = %0.6f' % (iteracion, c, f(c)))
    if (f(a)*f(c) < 0):
      b = c
    else:
      a = c
    iteracion +=1
    condicion = abs(f(c)) > tolerancia
  return c

def f(x):
  return x**2 - 2
  
regla_falsa(f, -1, 3, 0.0001)
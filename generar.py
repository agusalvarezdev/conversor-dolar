import random
import string
longitud=int(input("introduzca una contraseña:"))
caracteres= string.ascii_letters + string.digits + string.punctuation
contrasena= "".join(random.choices(caracteres, k=longitud))
print (contrasena)

texto='''
hola
hola
'''
print(texto)

'''
también podemos
hacer varias lineas de
comentario
'''

valor=True
print(type(valor))

s=input("Dime tu nombre:")
print(f" Hola, {s}")

try:
    num=int(input("Dime tu numero:"))
except:
    print("fallo")
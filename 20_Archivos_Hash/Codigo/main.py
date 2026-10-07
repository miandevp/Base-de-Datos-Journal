from Hash import *

hash = Hash(10, 3)

hash.crear_archivo_hash("data.csv")

print("Estado inicial")
hash.print()

print("\nBúsqueda de 39")
print(hash.search(39))

print("\nBúsqueda de 100")
print(hash.search(100))

print("\nEliminación de 39")
print(hash.delete(39))

print("\nEstado después de eliminar 39")
hash.print()

print("\nActualización de 12")
print(hash.update((12, "Luis", 26)))

print("\nEstado después de actualizar 12")
hash.print()

print("\nInserción de un nuevo registro")
hash.insert((29, "Carlos", 30))

print("\nEstado después de insertar 29")
hash.print()
estudiantes = []

def pedir_numero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except:
            print("Error: debes ingresar un número válido")


def pedir_texto(mensaje):
    while True:
        texto = input(mensaje)
        if texto.strip() == "":
            print("Error: no puedes dejar esto vacío")
        else:
            return texto


def agregar_estudiante():
    cantidad = pedir_numero("¿Cuántos estudiantes deseas agregar?: ")

    for i in range(cantidad):
        print(f"\nEstudiante {i+1}")

        nombre = pedir_texto("Nombre: ")
        edad = pedir_numero("Edad: ")
        curso = pedir_texto("Curso: ")

        id_estudiante = len(estudiantes) + 1

        estudiante = {
            "id": id_estudiante,
            "nombre": nombre,
            "edad": edad,
            "curso": curso
        }

        estudiantes.append(estudiante)
        print("Estudiante agregado correctamente")


def mostrar_estudiantes():
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados")
    else:
        print("\nLista de estudiantes:")
        for estudiante in estudiantes:
            print("----------------------")
            print("ID:", estudiante["id"])
            print("Nombre:", estudiante["nombre"])
            print("Edad:", estudiante["edad"])
            print("Curso:", estudiante["curso"])


def buscar_estudiante():
    if len(estudiantes) == 0:
        print("No hay estudiantes para buscar")
        return

    id_buscar = pedir_numero("Ingresa el ID del estudiante: ")

    encontrado = False

    for est in estudiantes:
        if est["id"] == id_buscar:
            print("\nEstudiante encontrado:")
            print("Nombre:", est["nombre"])
            print("Edad:", est["edad"])
            print("Curso:", est["curso"])
            encontrado = True
            break

    if not encontrado:
        print("No se encontró el estudiante")


def eliminar_estudiante():
    if len(estudiantes) == 0:
        print("No hay estudiantes para eliminar")
        return

    id_eliminar = pedir_numero("Ingresa el ID a eliminar: ")

    encontrado = False

    for est in estudiantes:
        if est["id"] == id_eliminar:
            estudiantes.remove(est)
            print("Estudiante eliminado correctamente")
            encontrado = True
            break

    if not encontrado:
        print("No se encontró el estudiante")


while True:
    print("""
======== MENÚ ========
1.Agregar estudiante
2. Mostrar estudiantes
3. Buscar estudiante
4. Eliminar estudiante
5. Salir
=====================
""")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        agregar_estudiante()
    elif opcion == "2":
        mostrar_estudiantes()
    elif opcion == "3":
        buscar_estudiante()
    elif opcion == "4":
        eliminar_estudiante()
    elif opcion == "5":
        print("Programa terminado")
        break
    else:
        print("Opción inválida")
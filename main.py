from modulos.Pelicula import Pelicula
from modulos.PeliculaAnimada import PeliculaAnimada
from modulos.Cine import Cine
from baseDeDatos.conexion import Conexion
import os


def agregar_pelicula():
  es_animada = input("¿Es una película animada? (Si/No): ").lower()
  if es_animada == 'si':
    pelicula = PeliculaAnimada(input("Ingresar el título de la película: "),
                               input("Ingresar la duración de la película: "),
                               input("Ingresar el género de la película: "),
                               input("Ingresar estudio de animación: "))
    conexion.agregarPelicula(pelicula)
  elif es_animada == 'no':
    pelicula = Pelicula(input("Ingresar el título de la película: "),
                        input("Ingresar la duración de la película: "),
                        input("Ingresar el género de la película: "))
    conexion.agregarPelicula(pelicula)
  else:
    print("Opción inválida.")


def modificar_pelicula():
  peliculas = conexion.getPeliculas()
  if not peliculas:
    print("No hay películas en la base de datos.")
  else:
    while True:
      id = input("Ingresar el ID de la película a modificar: ")
      peliculaAnterior = conexion.getPelicula(id)
      if peliculaAnterior:
        if isinstance(peliculaAnterior, PeliculaAnimada):
          pelicula = PeliculaAnimada(
              input("Ingresar el nuevo título de la película: "),
              input("Ingresar la nueva duración de la película: "),
              input("Ingresar el nuevo género de la película: "),
              input("Ingresar el nuevo estudio de animación: "))
          conexion.modificarPelicula(id, pelicula)
        elif isinstance(peliculaAnterior, Pelicula):
          pelicula = Pelicula(
              input("Ingresar el nuevo título de la película: "),
              input("Ingresar la nueva duración de la película: "),
              input("Ingresar el nuevo género de la película: "))
          conexion.modificarPelicula(id, pelicula)
        break
      else:
        print(
            "La película con el ID especificado no existe. Intente nuevamente."
        )


def eliminar_pelicula():
  peliculas = conexion.getPeliculas()
  if not peliculas:
    print("No hay películas en la base de datos.")
  else:
    while True:
      id = input("Ingresar el ID de la película a eliminar: ")
      pelicula_existente = False

      for pelicula in peliculas:
        if pelicula[0] == int(id):
          pelicula_existente = True
          conexion.eliminarPelicula(id)
          print("Película eliminada exitosamente.")
          break

      if pelicula_existente:
        break
      else:
        print(
            "La película con el ID especificado no existe. Intente nuevamente."
        )


def listar_peliculas():
  peliculas = conexion.getPeliculas()
  if not peliculas:
    print("No hay películas en la base de datos.")
  else:
    conexion.listarPeliculas()


def agregar_cine():
  cine = Cine(input("Ingresar el nombre del cine: "),
              input("Ingresar la ubicación del cine: "))
  conexion.agregarCine(cine)


def modificar_cine():
  cines = conexion.getCines()
  if not cines:
    print("No hay cines en la base de datos.")
    return

  while True:
    id = input("Ingresar el ID del cine a modificar: ")
    cine_existente = False

    for cine in cines:
      if cine[0] == int(id):
        cine_existente = True

        cine = Cine(input("Ingresar el nuevo nombre del cine: "),
                    input("Ingresar la nueva dirección del cine: "))
        conexion.modificarCine(id, cine)
        break

    if cine_existente:
      break
    else:
      print("El cine con el ID especificado no existe. Intente nuevamente.")


def eliminar_cine():
  cines = conexion.getCines()
  if not cines:
    print("No hay cines en la base de datos.")
    return

  while True:
    id = input("Ingresar el ID del cine a eliminar: ")
    cine_existente = False

    for cine in cines:
      if cine[0] == int(id):
        cine_existente = True
        conexion.eliminarCine(id)
        print("Cine eliminado exitosamente.")
        break

    if cine_existente:
      break
    else:
      print("El cine con el ID especificado no existe. Intente nuevamente.")


def listar_cines():
  cines = conexion.getCines()
  if not cines:
    print("No hay cines en la base de datos.")
  else:
    conexion.listarCines()


def agregar_programacion():
  id_pelicula = int(input("Ingresar el ID de la película: "))
  id_cine = int(input("Ingresar el ID del cine: "))
  conexion.agregarProgramacion(id_pelicula, id_cine)


def mostrar_programacion():
  id_cine = int(input("Ingresar el id del cine: "))
  conexion.mostrarProgramacion(id_cine)


conexion = Conexion("baseDeDatos/bdd.db")
conexion.crearTabla()

while True:
  print("1. Agregar película")
  print("2. Modificar película")
  print("3. Eliminar película")
  print("4. Listar películas")
  print("5. Agregar cine")
  print("6. Modificar cine")
  print("7. Eliminar cine")
  print("8. Listar cine")
  print("9. Agregar película a programación")
  print("10. Mostrar programación")
  print("11. Salir")
  opcion = input("Elija una opción: ")

  if opcion == '1':
    agregar_pelicula()
  elif opcion == '2':
    modificar_pelicula()
  elif opcion == '3':
    eliminar_pelicula()
  elif opcion == '4':
    listar_peliculas()
  elif opcion == '5':
    agregar_cine()
  elif opcion == '6':
    modificar_cine()
  elif opcion == '7':
    eliminar_cine()
  elif opcion == '8':
    listar_cines()
  elif opcion == '9':
    agregar_programacion()
  elif opcion == '10':
    mostrar_programacion()
  elif opcion == '11':
    conexion.cerrarConexion()
    break
  else:
    print("Opción inválida. Por favor, intentar nuevamente.")

  input("Presiona Enter para continuar...")
  os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la consola

import sqlite3
from modulos.Pelicula import Pelicula
from modulos.PeliculaAnimada import PeliculaAnimada
from modulos.Cine import Cine


class Conexion:

  def __init__(self, nombre_base_datos):
    self.conexion = sqlite3.connect(nombre_base_datos)
    self.cursor = self.conexion.cursor()

  def crearTabla(self):
    self.cursor.execute('''CREATE TABLE IF NOT EXISTS peliculas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            duracion TEXT,
            genero TEXT,
            estudio_animacion TEXT
        )''')

    self.cursor.execute('''CREATE TABLE IF NOT EXISTS programacion(
        id_pelicula INTEGER,
        id_cine INTEGER
    )''')

    self.cursor.execute('''CREATE TABLE IF NOT EXISTS cines(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            direccion TEXT
        )''')

    self.conexion.commit()

  def agregarPelicula(self, pelicula):
    if isinstance(pelicula, PeliculaAnimada):
      self.cursor.execute(
          '''INSERT INTO peliculas(titulo, duracion, genero, estudio_animacion) VALUES (?, ?, ?, ?)''',
          (pelicula.get_titulo(), pelicula.get_duracion(),
           pelicula.get_genero(), pelicula.get_estudio_animacion()))
    elif isinstance(pelicula, Pelicula):
      self.cursor.execute(
          '''INSERT INTO peliculas(titulo, duracion, genero) VALUES (?, ?, ?)''',
          (pelicula.get_titulo(), pelicula.get_duracion(),
           pelicula.get_genero()))

    self.conexion.commit()

  def getPeliculas(self):
    self.cursor.execute('''SELECT * FROM peliculas''')
    peliculas = self.cursor.fetchall()
    return peliculas

  def getPelicula(self, id):
    self.cursor.execute("SELECT * FROM peliculas WHERE id=?", (id, ))
    pelicula_obj = self.cursor.fetchone()

    if pelicula_obj:
      if pelicula_obj[4]:
        pelicula = PeliculaAnimada(pelicula_obj[1], pelicula_obj[2],
                                   pelicula_obj[3], pelicula_obj[4])
      else:
        pelicula = Pelicula(pelicula_obj[1], pelicula_obj[2], pelicula_obj[3])

      return pelicula

  def listarPeliculas(self):
    self.cursor.execute("SELECT * FROM peliculas")
    peliculas = self.cursor.fetchall()

    for pelicula in peliculas:
      if pelicula[4]:
        pelicula_obj = PeliculaAnimada(pelicula[1], pelicula[2], pelicula[3],
                                       pelicula[4])
        print("-------------------")
        print(f'Id: {pelicula[0]}')
        pelicula_obj.mostrar_info()
        print("-------------------")
      else:
        pelicula_obj = Pelicula(pelicula[1], pelicula[2], pelicula[3])
        print("-------------------")
        print(f'Id: {pelicula[0]}')
        pelicula_obj.mostrar_info()
        print("-------------------")

  def modificarPelicula(self, id, pelicula):

    if isinstance(pelicula, PeliculaAnimada):
      self.cursor.execute(
          '''UPDATE peliculas SET titulo=?, duracion=?, genero=?, estudio_animacion=? WHERE id=?''',
          (pelicula.get_titulo(), pelicula.get_duracion(),
           pelicula.get_genero(), pelicula.get_estudio_animacion(), id))

    elif isinstance(pelicula, Pelicula):
      self.cursor.execute(
          '''UPDATE peliculas SET titulo=?, duracion=?, genero=? WHERE id=?''',
          (pelicula.get_titulo(), pelicula.get_duracion(),
           pelicula.get_genero(), id))

    self.conexion.commit()

  def eliminarPelicula(self, id):
    self.cursor.execute('''DELETE FROM peliculas WHERE id=?''', (id, ))
    self.conexion.commit()

  def agregarCine(self, cine):
    self.cursor.execute(
        '''INSERT INTO cines(nombre, direccion) VALUES (?, ?)''',
        (cine.get_nombre(), cine.get_direccion()))
    self.conexion.commit()

  def modificarCine(self, id, cine):
    self.cursor.execute(
        '''UPDATE cines SET nombre=?, direccion=? WHERE id=?''',
        (cine.get_nombre(), cine.get_direccion(), id))
    self.conexion.commit()

  def eliminarCine(self, id):
    self.cursor.execute('''DELETE FROM cines WHERE id=?''', (id, ))
    self.conexion.commit()

  def getCines(self):
    self.cursor.execute('''SELECT * FROM cines''')
    cines = self.cursor.fetchall()
    return cines

  def getCine(self, id):
    self.cursor.execute("SELECT * FROM cines WHERE id=?", (id, ))
    cine_obj = self.cursor.fetchone()
    cine = Cine(cine_obj[1], cine_obj[2])
    return cine
      

  def listarCines(self):
    self.cursor.execute("SELECT * FROM cines")
    cines = self.cursor.fetchall()

    for cine in cines:
      print("-------------------")
      print(f'Id: {cine[0]}')
      cine_obj = Cine(cine[1], cine[2])
      cine_obj.mostrar_info()
      print("-------------------")

  def mostrarProgramacion(self, id_cine):
    self.cursor.execute("SELECT * FROM programacion WHERE id_cine=?", (id_cine, ))
    progrmacion = self.cursor.fetchall()
    for p in progrmacion:
      id_pelicula = p[0]
      pelicula = self.getPelicula(id_pelicula)
      pelicula.mostrar_info()

  def agregarProgramacion(self, id_pelicula, id_cine):
    self.cursor.execute(
        "INSERT INTO programacion(id_pelicula, id_cine) VALUES (?, ?)",
        (id_pelicula, id_cine))
    self.conexion.commit()

  def cerrarConexion(self):
    self.cursor.close()
    self.conexion.close()

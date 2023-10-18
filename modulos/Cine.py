class Cine:

  def __init__(self, nombre, direccion):
    self._nombre = nombre
    self._direccion = direccion
    self._programacion = []

  def agregar_pelicula(self, pelicula):
    self._programacion.append(pelicula)

  def mostrar_info(self):
    print(f'Titulo: {self._nombre}')
    print(f'Dirección: {self._direccion}')

  def get_nombre(self):
    return self._nombre

  def set_nombre(self, nombre):
    self._nombre = nombre

  def get_direccion(self):
    return self._direccion

  def set_direccion(self, direccion):
    self._direccion = direccion

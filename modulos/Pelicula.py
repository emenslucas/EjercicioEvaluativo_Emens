class Pelicula:

  def __init__(self, titulo, duracion, genero):
    self._titulo = titulo
    self._duracion = duracion
    self._genero = genero

  def mostrar_info(self):
    print(f'Titulo: {self._titulo}')
    print(f'Duracion: {self._duracion}')
    print(f'Genero: {self._genero}')

  def get_titulo(self):
    return self._titulo

  def set_titulo(self, titulo):
    self._titulo = titulo

  def get_duracion(self):
    return self._duracion

  def set_duracion(self, duracion):
    self._duracion = duracion

  def get_genero(self):
    return self._genero

  def set_genero(self, genero):
    self._genero = genero

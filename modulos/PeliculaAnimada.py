from modulos.Pelicula import Pelicula


class PeliculaAnimada(Pelicula):

  def __init__(self, titulo, duracion, genero, estudio_animacion):
    super().__init__(titulo, duracion, genero)
    self._estudio_animacion = estudio_animacion

  def mostrar_info(self):
    super().mostrar_info()
    print(f'Estudio de Animación: {self._estudio_animacion}')

  def get_estudio_animacion(self):
    return self._estudio_animacion

  def set_estudio_animacion(self, estudio_animacion):
    self._estudio_animacion = estudio_animacion

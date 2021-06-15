import abc


class AbstractWindowImplementation(abc.ABC):
  @abc.abstractmethod()
  def draw_line(x0: int, y0: int, x1: int, y1: int):
    ...
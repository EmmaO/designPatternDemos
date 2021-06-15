from bridge.window_implementation.abstract_window_implementation import AbstractWindowImplementation

class Window:
  def __init__(self, window_implementation: AbstractWindowImplementation)
    self._window_implementation = window_implementation

  def draw_rect(self, x0: int, y0: int, x1: int, y1: int):
    self._window_implementation.draw_line(x0, y0, x0, y1)
    self._window_implementation.draw_line(x0, y1, x1, y1)
    self._window_implementation.draw_line(x1, y1, x1, y0)
    self._window_implementation.draw_line(x1, y0, x0, y0)

  def draw_line(self, x0: int, y0: int, x1: int, y1: int):
    self._window_implementation.draw_line(x0, y0, x1, y1)
from bridge.window_implementation.abstract_window_implementation import AbstractWindowImplementation
from bridge.3rdParty.windows_window_system import WindowsWindowSystem

class WindowsWindowImplementation(AbstractWindowImplementation):
  def __init__(self, windows_window_system: Optional[WindowsWindowSystem] = None):
    self._windows_window_system = (
      WindowsWindowSystem() if windows_window_system is None else windows_window_system
    )
  
  def draw_line(self, x0: int, y0: int, x1: int, y1: int):
    self._windows_window_system.draw_rect(x0 - 1, y0 -1, x1 + 1, y1 + 1, "black")
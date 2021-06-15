from bridge.window_implementation.abstract_window_implementation import AbstractWindowImplementation
from bridge.3rdParty.windows_window_system import WindowsWindowSystem

class WindowsWindowImplementation(AbstractWindowImplementation):
  def __init__(windows_window_system: Optional[WindowsWindowSystem] = None):
    self._windows_window_system = (
      WindowsWindowSystem() if windows_window_system is None else windows_window_system
    )
  
  def draw_line(x0: int, y0: int, x1: int, y1: int):
    ...
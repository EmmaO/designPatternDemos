from bridge.3rdParty.mac_window_system import MacWindowSystem
from typing import Optional

class MacWindowImplementation(AbstractWindowImplementation):
  def __init__(self, mac_window_system: Optional[MacWindowSystem] = None):
    self._mac_window_system = (
      MacWindowSystem() if mac_window_system is None else mac_window_system
    )
  
  def draw_line(self, x0: int, y0: int, x1: int, y1: int):
    self.mac_window_system.draw_line(x0, y0, x1, y1)
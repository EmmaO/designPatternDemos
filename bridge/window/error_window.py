from bridge.window.base_window import Window

STARTING_WIDTH = 100
STARTING_HEIGHT = 80

class ErrorWindow(Window):
  def __init__(self, window_implementation: AbstractWindowImplementation):
    super.__init__(window_implementation)
    # draw window with cross in top left
    self.draw_rect(0, 0, STARTING_WIDTH, STARTING_HEIGHT)
    self.draw_rect(3, 3, 23, 23)
    self.draw_line(4, 4, 22, 22)
    self.draw_line(22, 4, 4, 22)
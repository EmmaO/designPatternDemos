from abc import ABC
from typing import List, Optional, Set

class Logger():
  def print(msg: str):
    print(msg)

logger = Logger()

class Lamp:
  def __init__(self, starting_oil_mins = 17) -> None:
    self._oil_mins_remaining = starting_oil_mins
  
  def tick(self, time_elapsed_mins: int):
    self._oil_mins_remaining -= time_elapsed_mins
  
  def get_oil_remaining(self):
    return self._oil_mins_remaining

@ABC
class AbstractMover:
  def __init__(self, speed: int, location: str):
    self._speed = speed
    self._location = location

  def get_speed(self):
    return self._speed

  def get_location(self):
    return self._location

class SingleMover(AbstractMover):
  ...

class MoverGroup(AbstractMover):
  def __init__(self, children: List[AbstractMover] = []):
    self._children: List[AbstractMover] = children

  def get_speed(self):
    return max([child.get_speed() for child in self._children])

  def get_location(self):
    return self._children[0].get_location()

  def add_child(self, child: AbstractMover):
    if len(self._children > 0) and self._children[0].get_location() != child.get_location():
      logger.print("Can't group people who aren't in the same location")
    self._children.append(child)
  
  def pop_children(self):
    children = self._children
    self._children = []
    return children



class Game:
  def __init__(self):
    self._start_location = {
      "Anna": SingleMover(1, "start"),
      "Ben": SingleMover(2, "start"),
      "Caroline": SingleMover(5, "start"),
      "Deandra": SingleMover(10, "start")
    }
    self._end_location = {}
    self._lamp = Lamp(17)

    self._logger = Logger()

  
  def move(self, names_to_move: Set[str]):
    
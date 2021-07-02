import abc
from typing import Generic, List, Optional, TypeVar
from random import randrange

T = TypeVar('T')

class ListIterator(abc.ABC, Generic[T]):

  def __init__(self, list: List[T]):
    self._list = list

  @abc.abstractmethod
  def has_more(self):
    ...
  
  @abc.abstractmethod
  def next(self) -> Optional[T]:
    ...
  
class ForwardIterator(ListIterator):
  def __init__(self, list: List[T]):
      super().__init__(list)
      self._current_position = 0

  def has_more(self):
    return self._current_position < len(self._list)
  
  def next(self):
    if not self.has_more:
      return None

    val = self._list[self._current_position]
    self._current_position += 1
    return val

class RandomIterator(ListIterator):
  def __init__(self, list: List[T]):
      super().__init__(list)
      self._visited_indices = set()

  def has_more(self):
    return len(self._visited_indices) < len(self._list)
  
  def next(self):
    if not self.has_more:
      return None

    next_index = randrange(len(self._list))
    while(next_index in self._visited_indices):
      next_index = randrange(len(self._list))

    val = self._list[next_index]
    self._visited_indices.add(next_index)
    return val
      
  
my_list = [1, 2, 3, 4]
forward_iterator = ForwardIterator(my_list)
random_iterator = RandomIterator(my_list)

while forward_iterator.has_more():
  print(f"forward: {forward_iterator.next()}")
  print(f"random: {random_iterator.next()}")

print("done")
from abc import ABC, ABCMeta, abstractmethod

class Doubler(ABC):
  @abstractmethod
  def double_n_times(self, num: int, n: int):
    ...

class IterativeDoubler(Doubler):
  def double_n_times(self, num: int, n: int):
    for i in range(n):
      print(f"Iterative double iteration {i + 1}")
      num = num * 2
    
    return num

class RecursiveDoubler(Doubler):
  def double_n_times(self, num: int, n: int):
    if n <= 0:
      return num
    
    print(f"Recurive double. Recursions remaining = {n-1}")
    return self.double_n_times(num * 2, n -1)

class DoublableInt:
  def __init__(self, val, strategy: Doubler = IterativeDoubler()):
    self._val = val
    self._doubling_strategy = strategy

  def double_once(self):
    self._val = self._doubling_strategy.double_n_times(self._val, 1)
  
  def double_three_times(self):
    self._val = self._doubling_strategy.double_n_times(self._val, 3)
  
  def get(self):
    return self._val


a = DoublableInt(3)
b = DoublableInt(10, RecursiveDoubler())
c = DoublableInt(5, IterativeDoubler())

print(f"a = {a.get()}. Doubling once")
a.double_once()
print(f"a = {a.get()}")

print(f"b = {b.get()}. Doubling three times")
b.double_three_times()
print(f"b = {b.get()}")

print(f"c = {c.get()}. Doubling nine times")
c.double_three_times()
c.double_three_times()
c.double_three_times()
print(f"c = {c.get()}")
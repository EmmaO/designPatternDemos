import abc
from typing import List

class CostCalculable(abc.ABC):
  @abc.abstractmethod
  def get_annual_cost(self):
    ...


class Team(CostCalculable):
  def __init__(self, name: str, resources: List[CostCalculable]):
    self._resources = resources

  def get_annual_cost(self):
    total = 0
    for resource in self._resources:
      total += resource.get_annual_cost()
    
    return total

class ItemGroup(CostCalculable):
  def __init__(self, type: str, price_per_unit: int, units: int):
    self._type = type
    self._price_per_unit = price_per_unit
    self._units = units
  
  def get_annual_cost(self):
    return self._price_per_unit * self._units

class Worker(CostCalculable):
  def __init__(self, name:str, position: str, monthly_salary: int):
    self._name = name
    self._position = position
    self._monthly_salary = monthly_salary
  
  def get_annual_cost(self):
    return self._monthly_salary * 12


steve = Worker("Steve", "Code Monkey", 100)
art_department = Team("Art Department", resources=[
  Worker("Lauren", "Pencil Expert", 150),
  Worker("James", "Drawing Genius", 150),
  ItemGroup("Pencils", 1, 100)
])

company = Team("Acme", resources=[
  art_department,
  Team("Dev team", resources=[
    steve,
    Worker("Ellen", "Senior Code Monkey", 300),
    ItemGroup("Laptops", 400, 2)
  ]),
  Worker("Philbert", "CEO", 1000)
])

print(f"Cost of Steve: {steve.get_annual_cost()}")
print(f"Cost of Art: {art_department.get_annual_cost()}")
print(f"Cost of Company: {company.get_annual_cost()}")

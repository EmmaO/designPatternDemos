import abc
import dataclasses


@dataclasses.dataclass
class UiElement:
  fill: str
  border: str

class MenuBar(UiElement):
  ...

class Button(UiElement):
  ...

class AbstractUiElementFactory(abc.ABC):
  @abc.abstractmethod
  def get_button(self) -> Button:
    ...
  
  def get_menu_bar(self) -> MenuBar:
    ...


class DarkUiElementFactory(AbstractUiElementFactory):
  def get_button(self):
    return Button(fill="black", border="light-grey")
  
  def get_menu_bar(self):
    return MenuBar(fill="dark-grey", border="light-grey")

class LightUiElementFactory(AbstractUiElementFactory):
  def get_button(self):
    return Button(fill="light-grey", border="dark-grey")
  
  def get_menu_bar(self):
    return MenuBar(fill="light-grey", border="dark-grey")


class UiBuilder:
  def __init__(self, element_factory: AbstractUiElementFactory):
    self._element_factory = element_factory

  def build_ui(self):
    self._add(self._element_factory.get_menu_bar())
    self._add(self._element_factory.get_button())
    self._add(self._element_factory.get_button())
  
  def _add(self, element: UiElement):
    print(f"Adding {type(element)} (fill: {element.fill}, border: {element.border})")

UiBuilder(LightUiElementFactory()).build_ui()
print("-----")
UiBuilder(DarkUiElementFactory()).build_ui()
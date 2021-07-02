
from abc import abstractmethod, ABC
from typing import Any, Dict, Generic, TypeVar


T = TypeVar("T")
R = TypeVar("R")

class BaseRequestHandler(ABC, Generic[T, R]):
  def handle(self, request: T, context: Dict[str, Any]) -> R:
    if not context["user_authed"]:
      raise PermissionError("User is not authenticated")
    try:
      self.pre_execution_hook(request)
      response = self.execute(request)
      return self.post_execution_hook(request, response)
    except Exception as e:
      self.handle_exception(e, request)


  @abstractmethod
  def pre_execution_hook(self, request:T):
    return
  
  @abstractmethod
  def post_execution_hook(self, request:T, response:R):
    return response
  
  @abstractmethod
  def execute(self, request:T) -> R:
    raise NotImplementedError()
  
  def handle_exception(self, e: Exception, request: T):
    raise e

  
  
  
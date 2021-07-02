from typing import Generic, TypeVar
from base_request_handler import BaseRequestHandler

T = TypeVar("T")
R = TypeVar("R")

class NoisyRequestHandler(BaseRequestHandler, Generic[T, R]):
  def log(self, message):
    print(message)
  
  def pre_execution_hook(self, request: T):
    self.log(f"About to handle request {request}")
    return super().pre_execution_hook(request)
  
  def post_execution_hook(self, request: T, response: R):
    self.log(f"Request {request} has response {response}")
    return super().post_execution_hook(request, response)
  
  def handle_exception(self, e: Exception, request: T):
    self.log(f"Exception {e} raised when handling request: {request}")
    return super().handle_exception(request)
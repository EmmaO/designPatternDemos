import dataclasses
from typing import Mapping
from noisy_request_handler import NoisyRequestHandler

@dataclasses.dataclass
class AdditionRequest:
  x: int
  y: int

class AdditionRequestHandler(NoisyRequestHandler):
  def execute(self, request: AdditionRequest) -> int:
    return request.x + request.y


handler = AdditionRequestHandler()
result = handler.handle(AdditionRequest(2, 3), {"user_authed": True})

print(f"result: {result}")
from abc import ABC, abstractmethod
from datetime import datetime
from uuid import uuid4

class ILogger(ABC):
  @abstractmethod
  def print(self, msg: str):
    ...

class Logger(ILogger):
  def print(self, msg: str):
    print(msg)

class TimestampedLoggerDecorator(ILogger):
  def __init__(self, next:ILogger):
    self._next = next
  
  def print(self, msg: str):
    msg = f"[{datetime.utcnow()}]{msg}"
    self._next.print(msg)

class ImportantLoggerDecorator(ILogger):
  def __init__(self, next:ILogger):
    self._next = next
  
  def print(self, msg: str):
    msg = f"***{msg}***"
    self._next.print(msg)

class IdLoggerDecorator(ILogger):
  def __init__(self, next:ILogger):
    self._next = next
  
  def print(self, msg: str):
    msg = f"({str(uuid4())}){msg}"
    self._next.print(msg)

normal_logger = Logger()
fancy_logger = ImportantLoggerDecorator(Logger())
helpful_logger = TimestampedLoggerDecorator(IdLoggerDecorator(Logger()))

normal_logger.print("Hello, World")
fancy_logger.print("and all who inhabit it")
helpful_logger.print("Except for Bill.")
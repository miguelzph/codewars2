from src.exceptions.base_holerite_error import BaseHoleriteError

class IntegrityHoleriteError(BaseHoleriteError):
  
  def __init__(self, *args: object) -> None:
    super().__init__(*args)
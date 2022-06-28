from src.exceptions.integrity_holerite_error import IntegrityHoleriteError

class DuplicateEntryError(IntegrityHoleriteError):
  
  def __init__(self, *args: object) -> None:
    super().__init__(*args)
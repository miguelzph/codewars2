from src.exceptions.not_found_error import NotFoundError

class FuncionarioNotFoundError(NotFoundError):
  def __init__(self, *args: object) -> None:
    super().__init__(*args)
    
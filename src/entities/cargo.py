class Cargo():
  def __init__(self, codigo, descricao, salario_base, comissao):
    self.__codigo = codigo
    self.__descricao = descricao
    self.__salario_base = salario_base
    self.__comissao = comissao


  @property
  def codigo(self) -> str:
    return self.__codigo
    

  @property
  def descricao(self) -> str:
    return self.__descricao

  
  @property
  def salario_base(self) -> str:
    return self.__salario_base

  
  @property
  def comissao(self) -> str:
    return self.__comissao
    
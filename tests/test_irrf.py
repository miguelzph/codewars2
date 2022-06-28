import pytest
from src.business.irrf import calcula_irrf
from src.exceptions.invalid_salary_error import InvalidSalaryError

def test_ir_faixa_1():
  
  # Given
  salario_base = 500
  valor_inss = 50
  valor_comissao = 80
  
  # When
  irrf = calcula_irrf(salario_base, valor_inss, valor_comissao)
  
  # Then
  assert irrf == 0


def test_ir_faixa_2():
  
  # Given
  salario_base = 2500
  valor_inss = 229.40
  valor_comissao = 100
  
  # When
  irrf = calcula_irrf(salario_base, valor_inss, valor_comissao)
  
  # Then
  assert irrf == 34.99


def test_ir_faixa_3():
  
  # Given
  salario_base = 3500
  valor_inss = 355.29
  valor_comissao = 100
  
  # When
  irrf = calcula_irrf(salario_base, valor_inss, valor_comissao)
  
  # Then
  assert irrf == 131.91


def test_ir_faixa_4():
  
  # Given
  salario_base = 4500
  valor_inss = 495.29
  valor_comissao = 100
  
  # When
  irrf = calcula_irrf(salario_base, valor_inss, valor_comissao)
  
  # Then
  assert irrf == 287.43


def test_ir_faixa_5():
  
  # Given
  salario_base = 8500
  valor_inss = 751.99
  valor_comissao = 100 
  
  # When
  irrf = calcula_irrf(salario_base, valor_inss, valor_comissao)
  
  # Then
  assert irrf == 1288.84

def test_irff_salario_negativo():

  # Given
  salario_base = -1000
  valor_inss = 51
  valor_comissao = 100
  
  # When
  # Then
  with pytest.raises(InvalidSalaryError):
    calcula_irrf(salario_base, valor_inss, valor_comissao)
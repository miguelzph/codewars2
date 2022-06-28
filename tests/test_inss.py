import pytest
from src.business.inss import calcula_inss
from src.exceptions.invalid_salary_error import InvalidSalaryError

def test_inss_faixa_1():
  
  # Given
  salario_base = 1000
  valor_comissao = 100
  
  # When
  inss = calcula_inss(salario_base, valor_comissao)
  
  # Then
  assert inss == 8.40


def test_inss_faixa_2():

  # Given
  salario_base = 1200
  valor_comissao = 300
  
  # When
  inss = calcula_inss(salario_base, valor_comissao)
  
  # Then
  assert inss == 116.82


def test_inss_faixa_3():

  # Given
  salario_base = 3000
  valor_comissao = 90
  
  # When
  inss = calcula_inss(salario_base, valor_comissao)
  
  # Then
  assert inss == 279.80

  
def test_inss_faixa_4():

  # Given
  salario_base = 4499.95
  valor_comissao = 500.05
  
  # When
  inss = calcula_inss(salario_base, valor_comissao)
  
  # Then
  assert inss == 536.18


def test_inss_faixa_5():

  # Given
  salario_base = 8500
  valor_comissao = 100.92
  
  # When
  inss = calcula_inss(salario_base, valor_comissao)
  
  # Then
  assert inss == 828.38

def test_inss_salario_negativo():

  # Given
  salario_base = -1000
  valor_comissao = 100
  
  # When
  # Then
  with pytest.raises(InvalidSalaryError):
      calcula_inss(salario_base, valor_comissao)
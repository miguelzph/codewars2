from src.exceptions.invalid_salary_error import InvalidSalaryError

def calcula_irrf(salario_base: float, valor_inss: float, valor_comissao: float = 0) -> float:

  base_calculo = salario_base + valor_comissao - valor_inss

  if base_calculo > 0 and base_calculo <= 1903.88:
    valor_irrf = 0
  elif base_calculo > 1903.88 and base_calculo <= 2826.65:
    valor_irrf = base_calculo * 0.075 - 142.80
  elif base_calculo > 2826.65 and base_calculo <= 3751.05:
    valor_irrf = base_calculo * 0.15 - 354.80
  elif base_calculo > 3751.05 and base_calculo <= 4664.68:
    valor_irrf = base_calculo * 0.225 - 636.13
  elif base_calculo > 4664.68:
    valor_irrf = base_calculo * 0.275 - 869.36
  elif base_calculo < 0:
    raise InvalidSalaryError('Salário negativo -> inválido')
  
  return round(valor_irrf, 2)

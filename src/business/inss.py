from src.exceptions.invalid_salary_error import InvalidSalaryError

def calcula_inss(salario_base: float, valor_comissao: float = 0) -> float:

  base_calculo = salario_base + valor_comissao

  if base_calculo > 0 and base_calculo <= 1212.00:
    valor_inss = (1212 - base_calculo) * 0.075
    
  elif base_calculo > 1212.00 and base_calculo <= 2427.35:
    valor_inss = 1212 * 0.075 + (base_calculo - 1212) * 0.09
    
  elif base_calculo > 2427.35 and base_calculo <= 3641.03:
    valor_inss = 1212 * 0.075 + 1215.34 * 0.09 + (base_calculo - 2427.35) * 0.12
    
  elif base_calculo > 3641.03 and base_calculo <= 7087.22:
    valor_inss = 1212 * 0.075 + 1215.34 * 0.09 + 1213.67 * 0.12 + (base_calculo - 3641.03) * 0.14
    
  elif base_calculo > 7087.22:
    valor_inss =  828.38

  elif base_calculo < 0:  
    raise InvalidSalaryError('Salário negativo -> inválido')
  
  return round(valor_inss, 2)



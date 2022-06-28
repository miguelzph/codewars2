from src.business.inss import calcula_inss
from src.business.irrf import calcula_irrf
from src.exceptions.funcionario_not_found_error import FuncionarioNotFoundError


class Holerite():
    
    def __init__(self, matricula, database):
        
        self.matricula = matricula
        self.database = database
        self.faltas = None
        self.salario_base = None
        self.valor_comissao = None
        self.inss_folha = None
        self.irrf_folha = None
          
          
    def consultar_banco_dados(self):
  
        # teria meio que repetir o codigo do cadastro para verificar se a matricula existe  
        query = f"SELECT EXISTS(SELECT * from funcionarios f WHERE matricula={self.matricula})"
  
        resultado_query = self.database.query(query)
        
        linha_existe = resultado_query['fetchall'][0][0]
        
        if not linha_existe:
          raise FuncionarioNotFoundError('Funcionário não encontrado!')
        else:
            query = f"""
                SELECT matricula, nome, cpf, data_admissao, cargo, funcionarios.comissao, descricao,                              salario_base, cargos.comissao as 'comissao_percentual'
                FROM 
                	funcionarios
                LEFT JOIN 
                	cargos
                ON 
                	funcionarios.cargo = cargos.codigo
                WHERE matricula={self.matricula}"""
            resultado_query = self.database.query(query)
  
            funcionario = resultado_query['fetchall']
  
            nome_colunas =  [linha[0] for linha in resultado_query['description']]
        
            self.dados_funcionario = dict(zip(nome_colunas, funcionario))



        self.salario_base = self.dados_funcionario['salario_base']
        self.comissao_percentual = self.dados_funcionario['comissao_percentual']
        self.tem_comissao = self.dados_funcionario['comissao']
    
        return None
        

    def calcular_comissao(self):
        if self.tem_comissao == 'sim':
            self.valor_comissao = self.salario_base * self.comissao_percentual
        else: 
            self.valor_comissao = 0

        return None
        
    
    def preencher_inss(self):
        
        salario_base = self.salario_base
        valor_comissao = self.valor_comissao
        
        self.inss_folha = calcula_inss(salario_base, valor_comissao)
  
        return None

    
    def preencher_irrf(self):
  
        salario_base = self.salario_base
        valor_comissao = self.valor_comissao
        valor_inss = self.inss_folha
      
        self.irrf_folha = calcula_irrf(salario_base, valor_inss, valor_comissao)
  
        return None

    def calcular_desconto_falta(faltas):
        self.desconto_falta = 
  
    
    def gerar_holerite(self, faltas=0):
        self.faltas = faltas
        
        self.consultar_banco_dados()
        self.calcular_comissao()
        self.preencher_inss()
        self.preencher_irrf()

        return None
        
    
        


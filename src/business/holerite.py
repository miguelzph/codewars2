from src.business.inss import calcula_inss
from src.business.irrf import calcula_irrf
from src.exceptions.funcionario_not_found_error import FuncionarioNotFoundError
from src.exceptions.duplicate_entry_error import DuplicateEntryError


class Holerite():
    
    def __init__(self, matricula: int, mes_referencia: str, database):
        
        self.matricula = matricula
        self.database = database
        self.mes_referencia = mes_referencia

          
          
    def consultar_banco_dados(self):
  
        # teria meio que repetir o codigo do cadastro para verificar se a matricula existe  
        query = f"SELECT EXISTS(SELECT * from funcionarios f WHERE matricula={self.matricula})"
  
        resultado_query = self.database.query(query)
        
        linha_existe = resultado_query['fetchall'][0][0]
        
        if not linha_existe:
          raise FuncionarioNotFoundError('Funcionário não encontrado!')
        else:
            query = f"""
                SELECT matricula, nome, cpf, data_admissao, cargos_codigo, funcionarios.comissao, descricao, salario_base, cargos.comissao as 'comissao_percentual'
FROM 
	funcionarios
LEFT JOIN 
	cargos
ON 
	funcionarios.cargos_codigo = cargos.codigo
WHERE matricula={self.matricula}"""
            resultado_query = self.database.query(query)
  
            funcionario = resultado_query['fetchall'][0]
  
            nome_colunas =  [linha[0] for linha in resultado_query['description']]
        
            self.dados_funcionario = dict(zip(nome_colunas, funcionario))


        return None

    def transformar_dados_em_atributos(self):
        self.salario_base = self.dados_funcionario['salario_base']
        self.comissao_percentual = self.dados_funcionario['comissao_percentual']
        self.tem_comissao = self.dados_funcionario['comissao']
        self.nome = self.dados_funcionario['nome']
        self.funcao = self.dados_funcionario['descricao']
        self.data_admissao = self.dados_funcionario['data_admissao']
        
        

    def preencher_valor_comissao(self):
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

    
    def preencher_desconto_por_falta(self):
        self.desconto_faltas = (self.salario_base / 30) * self.faltas

        return None

    
    def preencher_fgts(self):
        self.fgts_folha = (self.salario_base + self.valor_comissao) * 0.08

        
    def salvar_holerite(self):

        query = """INSERT INTO holerites
      (salario_base, comissao, faltas, INSS, IRRF, desconto_faltas, FGTS, mes_referencia, funcionarios_matricula)
      VALUES (%(salario_base)s, %(comissao)s, %(faltas)s, %(INSS)s, %(IRRF)s, %(desconto_faltas)s, %(FGTS)s, %(mes_referencia)s, %(funcionarios_matricula)s)"""
    
        self.params = {
                "salario_base": self.salario_base,
                "comissao": self.valor_comissao,
                "faltas": self.faltas,
                "desconto_faltas": self.desconto_faltas,
                "INSS": self.inss_folha,
                "IRRF":self.irrf_folha,
                "FGTS": self.fgts_folha,
                "mes_referencia": self.mes_referencia,
                "funcionarios_matricula":self.matricula
            }
        self.database.query(query, params=self.params, commit=True)

        print('Holerite foi Salvo')
        return None
    
    def gerar_holerite(self,faltas=0):

        if self.matricula not in self.verificar_holerites_nao_gerados():
            raise DuplicateEntryError('Holerite do funcionário já existe')
        else:
            self.faltas = faltas
            
            self.consultar_banco_dados()
            self.transformar_dados_em_atributos()
            
            self.preencher_valor_comissao()
            self.preencher_inss()
            self.preencher_irrf()
            self.preencher_fgts()
            self.preencher_desconto_por_falta()
    
            
            self.salvar_holerite()
    
            print(self.params)
    
            return None


    def verificar_holerites_nao_gerados(self):
        query = f"""SELECT 
	funcionarios.matricula
FROM 
	funcionarios
LEFT JOIN (
			SELECT  funcionarios_matricula, mes_referencia 
			FROM holerites 
			WHERE mes_referencia= %(mes_referencia)s
		  ) AS temp_holorite
ON 
	funcionarios.matricula = temp_holorite.funcionarios_matricula
WHERE 
	mes_referencia IS NULL"""

        params = {'mes_referencia': self.mes_referencia}

        resultado_query = self.database.query(query, params=params)
        # talvez alguma exception
        lista_resultados = resultado_query['fetchall']

        matriculas_nao_geradas = [valor[0] for valor in lista_resultados]

        return matriculas_nao_geradas


    def gerar_holerites_pendentes(self):
        matriculas = self.verificar_holerites_nao_gerados()
        for matricula in matriculas:
            self.matricula = matricula
            self.gerar_holerite()

        return None
            

        


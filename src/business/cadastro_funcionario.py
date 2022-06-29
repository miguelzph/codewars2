from src.database.db import DB
from src.entities.funcionario import Funcionario
from src.exceptions.empty_table_error import EmptyTableError
from src.exceptions.funcionario_not_found_error import FuncionarioNotFoundError
from src.exceptions.null_data_error import NullDataError
from src.exceptions.duplicate_entry_error import DuplicateEntryError

class CadastroFuncionario():

    def __init__(self):
        self.database = DB()

    def verificar_existencia(self,valor, campo='matricula'):
        # verificando existencia
        query = f"SELECT EXISTS(SELECT * from funcionarios WHERE {campo}={valor})"

        resultado_query = self.database.query(query)
        
        return resultado_query['fetchall'][0][0]


    def verifica_nulos(self, funcionario):
        return all(funcionario.__dict__.values())
        
    
    def incluir(self, funcionario: Funcionario, commit=False) -> None:
      if not self.verifica_nulos(funcionario):  
        raise NullDataError("Não é permitida a entrada de dados nulos ou vazios!")
      else:
        if not self.verificar_existencia(campo='cpf', valor=funcionario.cpf):
          query = ("INSERT INTO funcionarios" 
                "(nome, cpf, data_admissao, cargos_codigo, comissao)"
                "VALUES (%(nome)s, %(cpf)s, %(data_admissao)s, %(cargos_codigo)s, %(comissao)s)")
              
          params = {
                  "nome": funcionario.nome,
                  "cpf": funcionario.cpf,
                  "data_admissao": funcionario.data_admissao,
                  "cargos_codigo": funcionario.cargo,
                  "comissao": funcionario.comissao
                  }
  
                  
          self.database.query(query, params=params, commit=True)
          
  
        else:
          raise DuplicateEntryError('CPF DUPLICADO!')
              
          
      return print("Funcionário incluido")
        

    def consultar_por_matricula(self, matricula: int):
        
        if not self.verificar_existencia(valor=matricula):
          raise FuncionarioNotFoundError('Funcionário não encontrado!')
        else:
            query = f"SELECT * FROM funcionarios WHERE matricula={matricula}"
            
            resultado_query = self.database.query(query)
            
            tupla_resultado = resultado_query['fetchall'][0]
                
            resultado = {'matricula': tupla_resultado[0],
                        'nome':tupla_resultado[1] ,
                        'cpf':tupla_resultado[2], 
                        'data_admissao':tupla_resultado[3],
                        'cargos':tupla_resultado[4],
                        'comissao':tupla_resultado[5]}
        
        print(resultado)

        return resultado
        

    def excluir_por_matricula(self, matricula):

        
        if not self.verificar_existencia(valor=matricula):
          raise FuncionarioNotFoundError('Funcionário não encontrado!')
        else:
            query = f"DELETE FROM funcionarios WHERE matricula={matricula}"

            self.database.query(query)
            
            print('Cadastro deletado!')

            return True

    
    def listar_todos(self):

        query = f"SELECT * FROM funcionarios"
        
        resultado_query = self.database.query(query)
        
        funcionarios = resultado_query['fetchall']
        
        if not funcionarios:
            raise EmptyTableError('Tabela vazia!')
        else:
            nome_colunas =  [linha[0] for linha in resultado_query['description']]
        
            lista_funcionarios = [dict(zip(nome_colunas, funcionario)) for funcionario in funcionarios]
        
            print(lista_funcionarios)

            return lista_funcionarios

  
    def alterar_por_matricula(self, matricula, campo_de, valor_para):
         
        if not self.verificar_existencia(valor=matricula):
          raise FuncionarioNotFoundError('Funcionário não encontrado!') 
        if valor_para == None or valor_para == '':
            raise NullDataError("Não é permitida a entrada de dados nulos ou vazios!")
        if campo_de not in ['nome', 'cpf', 'data_admissao', 'cargos_codigo', 'comissao']:
            pass# field not exist
            print('A coluna não existe na tabela')
        
        query = f"""
            UPDATE funcionarios SET {campo_de} = (%(valor_para)s)
            WHERE matricula={matricula}"""
              
        params = {
                  #"campo_de": campo_de,
                  "valor_para": valor_para #,
                 # "matricula": matricula
                  }
        #query = f"""UPDATE funcionarios SET {campo_de}='{valor_para}' WHERE matricula={matricula}"""
            
        self.database.query(query,params=params, commit=True)

        return True
        
import pytest
import datetime

from src.entities.funcionario import Funcionario
from src.business.cadastro_funcionario import CadastroFuncionario

from src.exceptions.funcionario_not_found_error import FuncionarioNotFoundError
from src.exceptions.null_data_error import NullDataError
from src.exceptions.duplicate_entry_error import DuplicateEntryError

# Algumas vezes os testes dão um erro de conexão, tentei passar o cadastro no fixture e como global e nenhum dos dois adiantou
pytest.cadastro_funcionario = CadastroFuncionario()

# @pytest.fixture()
# def cadastro_funcionario():
#    cadastro = CadastroFuncionario()
#    return cadastro


def test_incluir_funcionario():
  # Given  
  funcionario_teste = Funcionario('testezz', '9345631111', '2021-10-20', 20, 1)
  # When
  # Then
  assert pytest.cadastro_funcionario.incluir(funcionario_teste) == None

def test_excluir_funcionario(): 
  # Given
  matricula_teste = pytest.cadastro_funcionario.listar_todos()[-1]['matricula']
  # When
  # Then
  assert pytest.cadastro_funcionario.excluir_por_matricula(matricula_teste) == True

# CONSULTAR
def test_consultar():
  # Given
  funcionario_teste = Funcionario('teste', '1223334445', '2021-10-20', 20, 'sim')
  pytest.cadastro_funcionario.incluir(funcionario_teste)
  matricula_teste = pytest.cadastro_funcionario.listar_todos()[-1]['matricula']  
  # When
  resultado = pytest.cadastro_funcionario.consultar_por_matricula(matricula_teste)
  # Then
  assert resultado == {'matricula': matricula_teste, 'nome': 'teste', 'CPF': '1223334445', 'data_admissao': datetime.date(2021, 10, 20), 'cargos_codigo': 20, 'comissao': 'sim'}

def test_consultar_nao_existente():
    
  with pytest.raises(FuncionarioNotFoundError):
    pytest.cadastro_funcionario.consultar_por_matricula(0)

# LISTAR TODOS
def test_listar_todos():
    resultado = pytest.cadastro_funcionario.listar_todos()

    assert len(resultado) > 0

# INCLUIR
def test_incluir_cpf_duplicado():
  # Given  
  funcionario_1 = Funcionario('Teste_cpf_duplicado', '11111111100', '2021-10-20', 20, 'sim')
  funcionario_2 = Funcionario('Teste_cpf_duplicado_1', '11111111100', '2021-10-02', 31, 'nao')
  pytest.cadastro_funcionario.incluir(funcionario_1)
  # When
  # Then
  with pytest.raises(DuplicateEntryError):
    pytest.cadastro_funcionario.incluir(funcionario_2)

def test_incluir_dado_nulo():
  # Given  
  funcionario = Funcionario(None, '11111111111', '2021-10-20', 20, 1)
  # When
  # Then
  with pytest.raises(NullDataError):
    pytest.cadastro_funcionario.incluir(funcionario)

def test_incluir_dado_vazio():
  # Given  
  funcionario = Funcionario('Teste', '', '2021-10-20', 20, 1)
  # When
  # Then 
  with pytest.raises(NullDataError):
    pytest.cadastro_funcionario.incluir(funcionario)
    
def test_excluir_nao_existente():
  with pytest.raises(FuncionarioNotFoundError):
    pytest.cadastro_funcionario.excluir_por_matricula(0)
    
    
    
    
    


    




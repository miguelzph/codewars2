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

# CONSULTAR
def test_consultar():
    resultado = pytest.cadastro_funcionario.consultar_por_matricula(2104)

    assert resultado == {'matricula': 2104, 'nome': 'Ana Maria Silva', 'cpf': '11111111100', 'data_admissao': datetime.date(2019, 7, 2), 'cargo': 32, 'comissao': 'sim'}

def test_consultar_nao_existente():
    
    with pytest.raises(FuncionarioNotFoundError):
        pytest.cadastro_funcionario.consultar_por_matricula(0)

# LISTAR TODOS
def test_listar_todos():
    resultado = pytest.cadastro_funcionario.listar_todos()

    assert len(resultado) > 0

# INCLUIR
def test_incluir_cpf_duplicado():
    funcionario = Funcionario('Teste_cpf_duplicado', '11111111100', '2021-10-20', 20, 1)
    
    with pytest.raises(DuplicateEntryError):
        pytest.cadastro_funcionario.incluir(funcionario)

def test_incluir_dado_nulo():
    funcionario = Funcionario(None, '11111111111', '2021-10-20', 20, 1)
    
    with pytest.raises(NullDataError):
        pytest.cadastro_funcionario.incluir(funcionario)

def test_incluir_dado_vazio():
    funcionario = Funcionario('Teste', '', '2021-10-20', 20, 1)
    
    with pytest.raises(NullDataError):
        pytest.cadastro_funcionario.incluir(funcionario)

# Só consegui pensar nos 2 proximos testes sendo dependentes (para não deixar sujeira no banco)
def test_incluir_funcionario():
    funcionario_teste = Funcionario('testezz', '9345631111', '2021-10-20', 20, 1)
    
    assert pytest.cadastro_funcionario.incluir(funcionario_teste) == None


def test_excluir_funcionario(): 
  matricula_teste = pytest.cadastro_funcionario.listar_todos()[-1]['matricula']
  assert pytest.cadastro_funcionario.excluir_por_matricula(matricula_teste) == True

    

def test_excluir_nao_existente():
    
    with pytest.raises(FuncionarioNotFoundError):
        pytest.cadastro_funcionario.excluir_por_matricula(0)
    
    
    
    
    


    




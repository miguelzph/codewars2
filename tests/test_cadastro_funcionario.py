import pytest
import datetime

from src.entities.funcionario import Funcionario
from src.business.cadastro_funcionario import CadastroFuncionario

from src.exceptions.funcionario_not_found_error import FuncionarioNotFoundError
from mysql.connector import IntegrityError

# Algumas vezes os testes dão um erro de conexão, tentei passar o cadastro no fixture e como global e nenhum dos dois adiantou
pytest.cadastro_funcionario = CadastroFuncionario()

#@pytest.fixture()
#def cadastro_funcionario():
#    cadastro = CadastroFuncionario()
#    return cadastro

# CONSULTAR
def test_consultar():
    resultado = pytest.cadastro_funcionario.consultar_por_matricula(1)

    assert resultado == {'matricula': 1, 'nome': 'Vitor', 'cpf': '01234567891', 'data_admissao': datetime.date(2022, 6, 23), 'cargo': 6, 'comissao': 'sim'}

def test_consultar_nao_existente():
    
    with pytest.raises(FuncionarioNotFoundError):
        pytest.cadastro_funcionario.consultar_por_matricula(0)

# LISTAR TODOS
def test_listar_todos():
    resultado = pytest.cadastro_funcionario.listar_todos()

    assert len(resultado) > 0

# INCLUIR
def test_incluir_cpf_duplicado():
    funcionario = Funcionario('Teste_cpf_duplicado', '01234567891', '2021-10-20', 20, 1)
    
    with pytest.raises(IntegrityError):
        pytest.cadastro_funcionario.incluir(funcionario)

# Só consegui pensar nos 2 proximos testes sendo dependentes (para não deixar sujeira no banco)
def test_incluir_funcionario():
    funcionario_teste = Funcionario('testezz', '12345631111', '2021-10-20', 20, 1)
    
    assert pytest.cadastro_funcionario.incluir(funcionario_teste) == None


def test_excluir_funcionario(): #nao sei como pegar a matricula do anterior
    # o ideal seria excluir o que foi adicionado no anterior
    assert pytest.cadastro_funcionario.excluir_por_matricula(2084) == True
    

def test_excluir_nao_existente():
    
    with pytest.raises(FuncionarioNotFoundError):
        pytest.cadastro_funcionario.excluir_por_matricula(0)
    
    
    
    
    


    




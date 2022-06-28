
import mysql.connector
from datetime import date
from src.entities.funcionario import Funcionario
from src.business.cadastro_funcionario import CadastroFuncionario


# achei essa classe que podemos usar para não ficar repetindo a conexão toda vez --> https://stackoverflow.com/questions/55833375/database-connection-function-for-python

# é bem de boa consultar/excluir por outro campo é só colocar o tipo como parametro --> teria que validar se o tipo escolhido é cpf ou matricula


#funcionario_teste = Funcionario(None, '92234567891', '2021-10-20', 20, 1)
#cadastro_teste = CadastroFuncionario()

#cadastro_teste.incluir(funcionario_teste)

#cadastro_teste.excluir_por_matricula(1222)
#cadastro_teste.listar_todos()
#cadastro_teste.consultar_por_matricula(0)


from src.business.holerite import Holerite
from src.database.db import DB

database = DB()

holerite = Holerite(2030, database)

holerite.gerar_holerite()

print(holerite.__dict__)
print(holerite.__dir__)


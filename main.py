from datetime import date
from src.entities.funcionario import Funcionario
from src.business.cadastro_funcionario import CadastroFuncionario


# é bem de boa consultar/excluir por outro campo é só colocar o tipo como parametro --> teria que validar se o tipo escolhido é cpf ou matricula

#funcionario_teste = Funcionario('Nome', '5656856939', '2021-10-20', 10, 1)
cadastro_teste = CadastroFuncionario()
cadastro_teste.consultar_por_matricula(0)
#cadastro_teste.excluir_por_matricula(2131)
#cadastro_teste.alterar_por_matricula(2105, 'cargo', 30) # 20
#cadastro_teste.excluir_por_matricula(1222)
#cadastro_teste.listar_todos()
#cadastro_teste.consultar_por_matricula(0)


#from src.business.holerite import Holerite
#from src.database.db import DB

#database = DB()

#holerite = Holerite(2104, mes_referencia='2022-07', database=database)

#holerite.gerar_holerite(faltas=1)

#print(holerite.__dict__)

#from sistema import main

#main()



from datetime import date
from src.entities.funcionario import Funcionario
from src.business.cadastro_funcionario import CadastroFuncionario
from sistema import main

#funcionario_teste = Funcionario('Pablo Henrique', '33333333333', '2021-09-10', 10, 'sim')
#cadastro_teste = CadastroFuncionario()
#cadastro_teste.incluir(funcionario_teste, commit=True)
#cadastro_teste.consultar_por_matricula()
#cadastro_teste.excluir_por_matricula(2131)
#cadastro_teste.alterar_por_matricula(2105, 'cargo', 30) # 20
#cadastro_teste.excluir_por_matricula(1222)
#cadastro_teste.listar_todos()
#cadastro_teste.consultar_por_matricula(0)

#from src.business.holerite import Holerite
#from src.database.db import DB

#database = DB()

#holerite = Holerite(2145, mes_referencia='2022-05', database=database)

#holerite.gerar_holerites_pendentes()

#holerite.gerar_holerite(faltas=1)

#print(holerite.__dict__)

if __name__ == '__main__':
    main()



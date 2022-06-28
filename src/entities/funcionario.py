
'''No python tem a biblioteca "uuid" que gera os ids que o Emerson comentou. Poderiamos criar uma classe Entity que gera esse id e serviria para adicionar tanto em funcionarios como em cargos(em cargos pode ser adicionado manualmente já que não sei se vamos criar essa classe agora).'''

class Funcionario():
    def __init__(self, nome: str, cpf: str, data_admissao: str, cargo: int, comissao: int):
        self.nome = nome
        self.__cpf = cpf
        self.data_admissao = data_admissao
        self.cargo = cargo
        self.comissao = comissao

    @property
    def cpf(self) -> str:
        return self.__cpf

    
        
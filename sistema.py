from src.database.db import DB
from src.business.cadastro_funcionario import CadastroFuncionario
from src.business.holerite import Holerite
from src.entities.funcionario import Funcionario
import os



def menu_funcionario(cadastro):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        option = input('''    -----MENU FUNCIONARIOS-----
    [1]: Adicionar funcionário
    [2]: Consultar funcionário
    [3]: Listar todos os funcionários
    [4]: Alterar os dados funcionário
    [5]: Excluir funcionário

    [9]: Voltar ao Menu Inicial
    [0]: Sair do sistema
                       
    Selecione uma opção:''')

        print('\n')
    
        if option == '1':
            try:
                nome = input('Digite o nome: ')
                cpf = input('Digite o cpf [apenas dígitos]: ')
                data_admissao = input('Digite a data [ano-mes-dia]: ')
                cargo = input('Digite o código do cargo: ')
                comissao = input('O Funcionaio possui comissão [sim; nao]? ')
                funcionario = Funcionario(nome, cpf, data_admissao, cargo, comissao)
                cadastro.incluir(funcionario, commit=True)
            except Exception as ex:
                print(f'Entrada invalida! {ex}')
                
        elif option == '2':
            try:
                matricula = int(input('Digite a matricula: '))
                cadastro.consultar_por_matricula(matricula)
            except Exception as ex:
                print(f'Entrada invalida! {ex}')
                
        elif option == '3':
            try:
                cadastro.listar_todos()
            except Exception as ex:
                print(f'A opção está indisponível: {ex}')
                
        elif option == '4':
            try:
                matricula = int(input('Digite a matricula: '))
                campo = input('Qual campo será alterado?[nome; cpf; data_admissao; comissao; cargos_codigo]')
                novo_valor = input(f'Qual o novo valor do campo {campo}?')
                cadastro.alterar_por_matricula(matricula, campo, novo_valor)
                print('A informação foi alterada!')
            except Exception as ex:
                print(f'Entrada invalida! {ex}')
                
        elif option == '5':
            try:
                matricula = int(input('Digite a matricula: '))
                cadastro.excluir_por_matricula(matricula, commit=True)
                print(f'Funcionário de matricula {matricula} excluido!')
            except Exception as ex:
                print(f'Entrada invalida: {ex}')
                
        elif option == '9':
            return None
        elif option == '0':
            print('Saindo!')
            exit()
        else:
            print('Opção invalida!')
        
        print('\n')
        input('Aperte ENTER para voltar ao menu.')
        print('\n')
        


def menu_holerite(database):

    while True:

        os.system('cls' if os.name == 'nt' else 'clear')
        
        option = input('''    -----MENU HOLERITES-----
    [1]: Gerar Holerite
    [2]: Gerar Holerites Pendentes

    [9]: Voltar ao Menu Inicial
    [0]: Sair do sistema
                   
    Selecione uma opção:''')
    
        if option == '1':
            try:
                matricula = int(input('Digite a matricula do funcionario: '))
                mes_referencia = input('Qual o mês de referência [ano-mes]? ')

                holerite = Holerite(matricula, mes_referencia=mes_referencia, database=database)

                qtd_faltas = int(input('Quantas faltas o funcionario possui? '))

                holerite.gerar_holerite(faltas=qtd_faltas)
                
            except Exception as ex:
                print(f'Entrada invalida: {ex}')
        elif option == '2':
            try:
                mes_referencia = input('Qual o mês de referência [ano-mes]? ')

                holerite = Holerite(0, mes_referencia=mes_referencia, database=database)

                holerite.gerar_holerites_pendentes()
                
            except Exception as ex:
                print(f'Entrada invalida: {ex}')
            
        elif option == '9':
            return None
        elif option == '0':
            print('Saindo!')
            exit()
        else:
            print('Opção invalida!')
        
        print('\n')
        input('Aperte ENTER para voltar ao menu.')
        print('\n')


def main():

    database = DB()
    
    cadastro = CadastroFuncionario()
    
    while True:

        os.system('cls' if os.name == 'nt' else 'clear')
    
        option = input('''Bem vindo ao Menu! Escolha uma das opções:
    [1]: Funcionarios
    [2]: Holerites
    [0]: Sair do sistema
        
    Selecione uma opção:''')

        print('\n')
        
        if option == '1':
            menu_funcionario(cadastro)
        elif option == '2':
            menu_holerite(database)
        elif option == '0':
            print('Saindo!')
            exit()
        else:
            print('Opção invalida!')
    
        print('\n')

if __name__ == '__main__':
    main()
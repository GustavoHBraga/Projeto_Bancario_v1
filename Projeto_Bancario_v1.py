"""
Criação de um menu com as opções para o usuário:
"""

menu = """
[1] SACAR
[2] DEPOSITAR
[3] EXTRATO
[4] SAIR
"""

"""
Variáveis iniciais para controle do EXTRATO bancário, SALDO, número de saques e limites:
"""
LIMITE = 500
LIMITE_SAQUES = 3
EXTRATO = ""
SALDO = 0

"""
Looping infinito para manter o menu em execução até que o usuário escolha a opção para sair:

"""
while True:
    
    # Exibição do menu e leitura da opção escolhida pelo usuário:
    opcao = int(input(menu).strip())

    # Condição para opção de saque:
    if (opcao == 1):
        valor = float(input('Informe o valor que deseja sacar:'))

        # Verificação se o valor do saque está dentro do limite permitido e se o SALDO é suficiente:
        if valor <= LIMITE and valor <= SALDO and LIMITE_SAQUES != 0:
            SALDO -= valor
            EXTRATO += f"Saque: R${valor}\n"
            EXTRATO += f"SALDO da conta: R${SALDO}\n"
            LIMITE_SAQUES -= 1
            print('Valor sacado  com sucesso !')

        # Verificação se o limite diário de saques já foi alcançado:
        elif(LIMITE_SAQUES == 0):
            print('Operação falhou. Excedeu o limite de saques, tente amanhã.')
        
        # Verificação se o valor do saque é maior que o limite permitido:
        elif(valor > LIMITE):
            print(f'Operação falhou. Excedeu o valor limite de R$:{LIMITE} para sacar.')

        # Verificação se o SALDO é insuficiente:
        elif(valor >= SALDO):
            print('Operação falhou. SALDO insuficiente')

        # Verificação para casos em que o valor do saque não é válido:
        else:
            print('Operação falhou. O valor informado não é valido.')

    # Condição para opção de depósito:
    elif (opcao == 2):

        valor = float(input('Informe o valor que deseja depositar:'))

        # Verificação se o valor do depósito é válido:
        if valor > 0:
            SALDO += valor
            EXTRATO += f"Deposito: R${valor}\n"
            print('Valor depositado com sucesso !')

        # Verificação para casos em que o valor do depósito não é válido:
        else:
            print('Operação falhou. O valor informado não é valido.')

    # Condição para opção de visualizar EXTRATO:
    elif (opcao == 3):
        print(EXTRATO)

    # Condição para opção de sair do programa:
    elif (opcao == 4):
        print('SAINDO...')
        break

    # Verificação para casos em que a opção escolhida não é válida:
    else:
        print('Numero invalido ! Digite outro numero.')

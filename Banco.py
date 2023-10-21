import os

def menu(id):
    if id == 1:
        print('\n..:: Banco Fundamentos SA ::..\n')
        print('1 - Abrir conta')
        print('7 - Sair')
        
        item = input('Escolha uma opção: ')
    
    else:
        print('\n..:: Banco Fundamentos SA ::..\n')
        print('2 - Realizar Depósito')
        print('3 - Realizar Saque')
        print('4 - Aplicar Juros')
        print('5 - Realizar empréstimo')
        print('6 - Extrato')
        print('7 - Sair')
        
        item = input('Escolha uma opção: ')
    
    return item

def abrirContaNome():
    a = str(input('Digite o seu nome completo: '))
    return a
def abrirContaSaldo():
    saldoInicial = float(input('Digite seu saldo inicial: R$'))
    return saldoInicial

def realizaDeposito(saldoInicial):
    cont = 1
    while cont == 1:
        deposito = input('Digite o valor a ser depositado: R$')
        if deposito.isnumeric():
            deposito = float(deposito)
            if deposito <= 0:
                print('Valor do depósito precisa ser maior do que R$0.00 !')
            else:
                cont = 5
                return deposito
        else:
            print('Valor de depósito não é numérico!')

def realizaSaque(saldoAtual):
    print('Notas dispoíveis: ')
    print('R$ 5')
    print('R$ 10')
    print('R$ 20')
    print('R$ 50')
    print('R$ 100')
    cont = 1

    while cont == 1:
        saque = input('Digite o valor a ser sacado: R$')
        if saque.isnumeric():
            saque = float(saque)
            if saque <= 0:
                print('Valor de saque precisa ser maior do que R$0.00 !')

            elif saque > saldoAtual:
                print('Valor de saque é maior do que saldo em conta')

            elif saque % 5 == 0:
                return saque
        else:
            print('Valor de saque não é numérico!')
            
def aplicaJuros(saldoatual):
    cont = 1
    while cont == 1:
        taxa = float(input('Digite a taxa de juros para rentabilidade (%): '))
        if taxa > 0:
            taxa /= 100
            juros = saldoatual * taxa
            return juros
        else:
            print('Taxa de juros precisa ser maior que zero!')

def simulaEmprestimo(saldoatual):
    cont = 1
    while cont == 1:
        emprestimo = input('Digite o valor do empréstimo: R$')
        taxa = input('Digite a taxa de juros do empréstimo (%): ')
        numMeses = input('Digite o número de parcelas para o pagamento: ')
        if emprestimo.isnumeric() and taxa.isnumeric() and numMeses.isnumeric() :
            emprestimo = float(emprestimo)
            taxa = float(taxa)
            numMeses = int(numMeses)
            if emprestimo > 0 and taxa > 0 and numMeses > 0:
                taxa /= 100
                emprestimo_final = emprestimo * ((1 + taxa) ** numMeses)
                parcela = emprestimo_final / numMeses
                juros = emprestimo_final - emprestimo
                print('\nParcela : R$' + '{:.2f}'.format(parcela))
                print('Total de parcelas: ', numMeses)
                print('\nTotal de juros : R$' + '{:.2f}'.format(juros))
                print('Total a pagar : R$' + '{:.2f}'.format(emprestimo_final))
                 
                return emprestimo
            else:
                print('Valores precisam ser maiores que zero!')

        else:
            print('Valores precisam ser numéricos!')
# def extrato():


if __name__ == '__main__':
    escolha = '0'
    id = 1
    nome_cliente = ''
    saldo_inicial = 0
    saldo_atual = 0
    qtd_dep = 0
    soma_dep = 0
    qtd_saque = 0
    soma_saque = 0
    saldo_min = 0
    saldo_max = 0
    soma_juros = 0
    
    while(escolha != '7'):
        escolha = menu(id)

        if escolha == '1':
            nome_cliente = abrirContaNome()
            saldo_inicial = abrirContaSaldo()
            saldo_atual = saldo_inicial
            saldo_min = saldo_atual
            id = 5
            print('\nSeu saldo atual é de : R$' + '{:.2f}'.format(saldo_inicial))

        elif escolha == '2':
            dep = realizaDeposito(saldo_atual)
            saldo_atual += dep
            soma_dep += dep
            print('\nSaldo é R$' + '{:.2f}'.format(saldo_atual))
            qtd_dep += 1

        elif escolha == '3':
            saq = realizaSaque(saldo_atual)
            saldo_atual -= saq
            soma_saque += saq
            qtd_saque += 1
            print('\nSaldo é R$' + '{:.2f}'.format(saldo_atual))
        
        elif escolha == '4':
            juros = aplicaJuros(saldo_atual)
            saldo_atual += juros
            soma_juros += juros
            print('\nSaldo após juros R$' + '{:.2f}'.format(saldo_atual))
            
        elif escolha == '5':
            saldo_atual += simulaEmprestimo(saldo_atual)
            print('\nSaldo após empréstimo R$' + '{:.2f}'.format(saldo_atual))
            
        elif escolha == '6':
            print('\n\nNome do cliente: ', nome_cliente)
            print('Saldo inicial: R$' + '{:.2f}'.format(saldo_inicial))
            print('Saldo atual: R$' + '{:.2f}'.format(saldo_atual))
            
            print('\nQuantidade de depósitos: ', qtd_dep)
            print('Valor total dos depósitos : R$' + '{:.2f}'.format(soma_dep))
            
            print('\nQuantidade de saques: ', qtd_saque)
            print('Valor total sacado: R$' + '{:.2f}'.format(soma_saque))
            
            print('\nValor total de juros recebidos: R$' + '{:.2f}'.format(soma_juros))
            print('Saldo Mínimo: R$' + '{:.2f}'.format(saldo_min))
            print('Saldo Máximo: R$' + '{:.2f}'.format(saldo_max))
            
        if saldo_min > saldo_atual:
            saldo_min = saldo_atual
        if saldo_max < saldo_atual:
            saldo_max = saldo_atual
            
    input('\nPressione ENTER para continuar')
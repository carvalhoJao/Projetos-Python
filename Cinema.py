import string
import csv


def menu(id):
    print('\n..:: Cinemark do Camelô ::..\n')
    print('1 - Carregar Dados')
    print('2 - Consultar Situação de um assento')
    print('3 - Reservar Assentos')
    print('4 - Liberar Reserva de assentos')
    print('5 - Visualizar mapa do cinema')
    print('6 - Relatórios')
    print('7 - Salvar dados')
    print('8 - Sair')
    
    item = input('Escolha uma opção: ')

    return item

def carregarDados(matriz):

    nomeArquivo = str(input('Informe o nome do arquivo a carregar: '))
    f = open(nomeArquivo)
    reader = csv.reader(f)
    matrizCrua = list(reader)
    dados = [[r[0], r[1], int(r[2])] for r in matrizCrua[1::]]
    if len(dados) > len(matriz):
        print('Assentos do arquivo são maiores que os do cinema! \nInsira um arquivo com menos assentos')
        return
    for i in range(len(dados)):
        pos = str(dados[i][0])
        linha = ord(pos[0]) - 65
        if len(pos) == 3:
            ajud = str(pos[1]) + str(pos[2])
            coluna = int(ajud) - 1
        else:
            coluna = int(pos[1]) - 1    
        matriz[linha][coluna] = str(dados[i][1]) + ',' + str(dados[i][2])  
    f.close()


def consultaAssento(matriz, fileira, assento):
    print('----Consulta de assentos---- ')
    consultaFil = (input('Digite a fileira: '))
    consultaFil = ord(consultaFil) - 97
    consultaAss = int(input('Digite o numero do assento: '))
    if matriz[consultaFil][consultaAss-1] == ' .':
        print('Liberado!')
    else :
        print('Ocupado!')
        print(matriz[consultaFil][i].split(','))
        

def reservarAssento(matriz):
    print('---- Reserva de Assentos ----')
    consultaFil = (input('Digite a fileira: '))
    consultaFil = ord(consultaFil) - 97
    consultaAss = int(input('Digite o numero do assento: '))
    consultaAss -= 1
    qtdAssentos = int(input('Informe a quantidade de assentos a serem reservados: '))
    
    for i in range(consultaAss, qtdAssentos):
        if matriz[consultaFil][i] != "":
            print('Assentos indisponíveis!')
            return 0
    for i in range(consultaAss, qtdAssentos + consultaAss):
        cont = 1
        while cont < 5:
            sexo = str(input('Digite o sexo do cliente (m / f): '))
            if sexo == 'm' or sexo == 'M' :
                break
            elif sexo == 'f' or sexo == 'F':
                break
            else:
                print('Formato inválido! Digite novamente')
        while cont < 5:
            idade = input('Digite a idade do cliente: ')
            if idade.isnumeric():
                idade = str(idade)
                break
            else:
                print('Valor de idade não é numérico')
        
        info = str(sexo + ',' + idade)
        matriz[consultaFil][i] = info
    print('Assentos reservados')

        
def liberarAssento(matriz):
    print('---- Cancelamento de reserva ----')
    consultaFil = (input('Digite a fileira: '))
    consultaFil = ord(consultaFil) - 97
    consultaAss = int(input('Digite o numero do assento: '))
    consultaAss -= 1
    qtdAssentos = int(input('Informe a quantidade de assentos a serem excluidos: '))
    for i in range(consultaAss, qtdAssentos):
        if matriz[consultaFil][i] == "":
            print('Assentos vazios!')
            return 0
    for i in range(consultaAss, qtdAssentos + consultaAss):
        matriz[consultaFil][i] = ""
    print('Reserva(s) excluida(s)!')

def mapaCine(matriz, fileiras, assentos):
    m = list(range(1, assentos + 1, 1))
    a = list(string.ascii_uppercase)
    print("   ", end= '')
    for i in range(assentos):
        print(f'{m[i]:02d}', end= ' ')
    print('')
    for i in range(fileiras + 1):
        print(a[i], end= ' ')
        for j in range(assentos):
            if matriz[i][j] == "":
                print(" .", end= ' ')
            elif matriz[i][j] != "":
                print(' X', end=" ")
        print('')

def imprimeRelatorio(matriz, fileira, assento, ingresso):
    meiaMenor = 0
    meiaIdoso = 0
    inteira = 0
    total = 0
    testaIdade = []
    ingMasc = 0
    ingFem = 0
    print('---- Relatórios ----')
    for i in range(fileira + 1):
        for j in range(assento):
            if matriz[i][j] != "":
                total += 1
                testaIdade = matriz[i][j].split(',')
                testaIdade[1] = int(testaIdade[1])  
                if testaIdade[1] <= 17:
                    meiaMenor += 1
                    print(chr(i + 65), end='')
                    print(j + 1, end=' ')
                    print(testaIdade, end=' ')
                    print('R$ ', (ingresso / 2))
                if testaIdade[1] >= 18 and testaIdade[1] < 60:
                    inteira += 1
                    print(chr(i + 65), end='')
                    print(j + 1, end=' ')
                    print(testaIdade, end=' ')
                    print('R$ ', ingresso)
                if testaIdade[1] >= 60:
                    meiaIdoso += 1
                    print(chr(i + 65), end='')
                    print(j + 1, end=' ')
                    print(testaIdade, end=' ')
                    print('R$ ', (ingresso / 2))
                if testaIdade[0] == 'm' or testaIdade[0] == 'M':
                    ingMasc += 1
                if testaIdade[0] == 'f' or testaIdade[0] == 'F':
                    ingFem += 1

    ingMeiaMenor = (ingresso / 2) * meiaMenor
    percMeiaMenor = (meiaMenor / total) * 100
    
    ingInteira = ingresso * inteira
    percInteira = (inteira / total) * 100

    ingMeiaIdoso = (ingresso / 2) * meiaIdoso
    percMeiaIdoso = (meiaIdoso / total) * 100
    
    
    print('Quantidade total de assentos: ', fileira * assento)
    print('Liberados  : ', (fileira * assento) - total)
    print('Reservados : ', total)
    print('Reservas Masculinas: ', ingMasc)
    print('Reservas femininas: ', ingFem)
    

# ---------- Impressão do Gráfico -------------------
    
    print('\nMeia Menor :  ' + f'{meiaMenor:2d}' + ' -  ' + '{:.1f}'.format(percMeiaMenor) + '% |', end= ' ')
    for i in range(1, total + 1, 1):
        if i <= meiaMenor:
            print('=', end= ' ')
        else:
            print('-', end= ' ')
    print('| R$   ' + '{:.2f}'.format(ingMeiaMenor))

# inteira ------------------------------------

    print('Inteira    :  ' + f'{inteira:2d}' + ' -  ' + '{:.1f}'.format(percInteira) + '% |', end= ' ')
    for i in range(1, total + 1, 1):
        if i <= inteira:
            print('=', end= ' ')
        else:
            print('-', end= ' ')
    print('| R$   ' + '{:.2f}'.format(ingInteira))

# Meia Idoso ------------------------------------------------------------------

    print('Meia Idoso :  ' + f'{meiaIdoso:2d}' + ' -  ' + '{:.1f}'.format(percMeiaIdoso) + '% |', end= ' ')
    for i in range(1, total + 1, 1):
        if i <= meiaIdoso:
            print('=', end= ' ')
        else:
            print('-', end= ' ')
    print('| R$   ' + '{:.2f}'.format(ingMeiaIdoso))

# Total ----------------------------------------

    print('Total      :  ' + f'{total:2d}' + ' - 100,0% |', end= ' ')
    for i in range(1, total + 1, 1):
        print('=', end= ' ')
    print('| R$   ' + '{:.2f}'.format(ingMeiaMenor + ingInteira + ingMeiaIdoso))

# Listgem ----------------------------------

def salvarDados(matriz, fileira, assento):
    nomeArquivo = str(input('Digite o nome do arquivo a ser salvo: ')) + '.txt'   
   
    arq = open(nomeArquivo, 'a')
    arq.write('\n\nAssento, Sexo, Idade\n')
    for i in range(fileira + 1):
        for j in range(assento):
            if matriz[i][j] != '':
                arq.write(chr(i + 65) + str(j + 1) + ',' + matriz[i][j] + '\n')
                
    arq.close()
                
                
if __name__ == '__main__':
    escolha = '0'
    cont = 2
    while cont < 5:
        valorIng = input('Digite o valor do ingresso: R$')
        if valorIng.replace('.','',1).isdigit():
            break
        else:
            print('Valor não é numérico!')
    valorIng = float(valorIng)
    while cont < 5:
        fileiras = input('Digita a quantidade de fileiras: ')
        if fileiras.isnumeric():
            break
        else:
            print('Valor não é numérico!')

    fileiras = int(fileiras)

    while cont < 5:
        assentos = input('Digite a quantidade de assentos por fileira: ')
        if assentos.isnumeric():
            break
        else:
            print('Valor não é numérico!')

    assentos = int(assentos)

    cinema = []
    for i in range(fileiras + 1):
        cinema.append([""] * assentos)
        
    while(escolha != '8'):
        escolha = menu(id)
        if escolha == '1':
            carregarDados(cinema)        
        elif escolha == '2':
            consultaAssento(cinema, fileiras, assentos)
        elif escolha == '3':
            reservarAssento(cinema)
        elif escolha == '4':
            liberarAssento(cinema)
        elif escolha == '5':
            mapaCine(cinema, fileiras, assentos)
        elif escolha == '6':
            imprimeRelatorio(cinema, fileiras, assentos, valorIng)
        elif escolha == '7':
            salvarDados(cinema, fileiras, assentos)

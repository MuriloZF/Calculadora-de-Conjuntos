def menu():
    menuOption = "1"
    while menuOption != "2":
        print("Seja bem-vindo a Calculadora de Conjuntos!")
        print("Para prosseguir, escolha um arquivo no formato txt que contenha os conjuntos e a operação que deseja realizar.")
        print("Para mais informações, leia o arquivo 'README'!")
        menuOption = str(input('Escolha o que deseja fazer:\n'
                               '1- Continuar\n'
                               '2- Sair\n'
                               'Escolha: '))
        if menuOption != "1" and menuOption != "2":
            print("Comando inválido! Tente novamente")
        if menuOption == "2":
            exit()
        if menuOption == "1":
            break

def leitura():
    while True:
        try:
            nomeArquivo = str(input("Digite o nome do arquivo: "))
            with open(f"TXT AQUI/{nomeArquivo}.txt", "r") as arquivo:
              linhas = [linha.strip() for linha in arquivo.readlines()]

              operacao = linhas[1].strip()

              conjuntos = [set(map(int, linha.split(','))) for linha in linhas if ',' in linha]

              break

        except FileNotFoundError:
            print("Arquivo não encontrado!")
    print(conjuntos)
    print(operacao)
    return operacao, conjuntos

def operacao(operacao, conjuntos):
    resultado = None
    if operacao == "U" or operacao == "u":
        resultado = set.union(*conjuntos)
        print(f'AuB =', resultado)

    elif operacao == "I" or operacao == "i":
        resultado = set.intersection(*conjuntos)
        print(f'A∩B =', resultado)

    elif operacao == "D" or operacao == "d":
        resultado = set.difference(*conjuntos)
        print(f'A-B = ', resultado)

    elif operacao == "C" or operacao == "c":
        resultado = {(a, b) for a in conjuntos[0] for b in conjuntos[1]}
        print(f'AxB = ', resultado)

    while True:
        menuOption = str(input("Deseja retornar ao menu?\n"
                               "1- Sim, voltar ao menu\n"
                               "2- Não, encerrar o programa\n"
                               "Escolha: "))
        if menuOption == "1":
            main()
        elif menuOption == "2":
            exit()
        else:
            print("Opção inválida!")
def main():
    menu()
    operacao_str, conjuntos = leitura()
    operacao(operacao_str, conjuntos)

main()

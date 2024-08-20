from datetime import date, datetime
from Pessoa import Endereco, PessoaFisica, PessoaJuridica


def main():

    listaPF = []
    listaJ = []
    while True:
        opcao = int(input("Escolha uma opcao: 1 - Pessoa Fisica / 2 - Pessoa Juridica / 0 - Sair: "))
        if opcao == 1:
            while True:
                opcaoPF = int(input("Escolha uma opcao: 1 - Cadastrar Pessoa Fisica / 2 - Listar Pessoa Fisica / 3 - Voltar menu anterior: "))
                if opcaoPF == 1:
                    novaPF = PessoaFisica()
                    novoEnderecoPF = Endereco()

                    novaPF.nome = input("Digite o nome da Pessoa Fisica: ")
                    novaPF.cpf = input("Digite o cpf da Pessoa Fisica: ")
                    novaPF.rendimento = float(input("Digite o rendimento mensal da Pessoa Fisica(SOMENTE NUMEROS): "))
                    
                    data_Nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
                    novaPF.dataNascimento = datetime.strptime(data_Nascimento, '%d/%m/%Y').date()
                    idade = (date.today() - novaPF.dataNascimento).days // 365

                    if idade >= 18:
                        print("Pessoa Fisica tem mais de 18 anos")
                    else:
                        print("Pessoa Fisica tem menos de 18 anos. Retorne ao menu...")
                        continue

                    novoEnderecoPF.logradouro = input("Digite o Logradouro: ")
                    novoEnderecoPF.numero = input("Digite o numero: ")

                    endereco_Comercial = input("Esse endereco e comercial? (S/N): ")
                    novoEnderecoPF.enderecoComercial = endereco_Comercial.strip().upper() == "S"

                    novaPF.endereco = novoEnderecoPF

                    listaPF.append(novaPF)

                    print("Cadastro realizado com sucesso!")

                elif opcaoPF == 2:
                    if listaPF:
                        for cadaPF in listaPF:
                            print(f"Nome: {cadaPF.nome}")
                            print(f"CPF: {cadaPF.cpf}")
                            print(f"Endereco: {cadaPF.endereco.logradouro}, N: 1{cadaPF.endereco.numero}")
                            print(f"Data Nascimento: {cadaPF.dataNascimento.strftime('%d/%m/%Y')}")
                            print(f"Imposto a ser pago: {cadaPF.calcularImposto(cadaPF.rendimento)}")
                            print("Digite 0 para sair")
                            input()
                    else:
                        print("Lista vazia!")

                elif opcaoPF == 0:
                    print("Voltando ao menu anterior")
                    break

                else:
                    print("Opcao invalida, por favor digite uma das opcoes indicadas: ")

        elif opcao == 2:
            print("Funcionalidade para pessoa juridica nao implementada")
            pass

        elif opcao == 0:
            print("Obrigado por utilizar o nosso sistema!")
            break
        else:
            print("Opcao invalida! Por favor digite uma das opcoes validas!")

        if opcao == 2:
            while True:
                opcaoJ = int(input("Escolha uma opcao: 1 - Cadastrar Pessoa Juridica / 2 - Listar Pessoa Juridica / 3 - Voltar menu anterior: "))
                if opcaoJ == 1:
                    novaJ = PessoaJuridica()
                    novoEnderecoJ = Endereco()

                    novaJ.nome = input("Digite o nome da Pessoa Juridica: ")
                    novaJ.cnpj = input("Digite o cnpj da Pessoa Juridica: ")
                    novaJ.rendimento = float(input("Digite o rendimento mensal da Pessoa Juridica(SOMENTE NUMEROS): "))
                    
                    data_Nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
                    novaJ.dataNascimento = datetime.strptime(data_Nascimento, '%d/%m/%Y').date()
                    idade = (date.today() - novaJ.dataNascimento).days // 365

                    if idade >= 18:
                        print("Pessoa Juridica tem mais de 18 anos")
                    else:
                        print("Pessoa Juridica tem menos de 18 anos. Retorne ao menu...")
                        continue

                    novoEnderecoJ.logradouro = input("Digite o Logradouro: ")
                    novoEnderecoJ.numero = input("Digite o numero: ")

                    endereco_Comercial = input("Esse endereco e comercial? (S/N): ")
                    novoEnderecoPF.enderecoComercial = endereco_Comercial.strip().upper() == "S"

                    novaJ.endereco = novoEnderecoJ

                    listaJ.append(novaJ)

                    print("Cadastro realizado com sucesso!")

                elif opcaoJ == 2:
                    if listaJ:
                        for cadaJ in listaJ:
                            print(f"Nome: {cadaJ.nome}")
                            print(f"CPF: {cadaJ.cnpj}")
                            print(f"Endereco: {cadaJ.endereco.logradouro}, N: 1{cadaJ.endereco.numero}")
                            print(f"Data Nascimento: {cadaJ.dataNascimento.strftime('%d/%m/%Y')}")
                            print(f"Imposto a ser pago: {cadaJ.calcularImposto(cadaJ.rendimento)}")
                            print("Digite 0 para sair")
                            input()
                    else:
                        print("Lista vazia!")

                elif opcaoJ == 0:
                    print("Voltando ao menu anterior")
                    break

                else:
                    print("Opcao invalida, por favor digite uma das opcoes indicadas: ")

if __name__ == "__main__":
    main()
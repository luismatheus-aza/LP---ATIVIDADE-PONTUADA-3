import os
import time

avioes_registrados = [-1] * 4
numero_assentos = [-1] * 4
reservas = []

def menu():
    os.system("cls")
    print("===== = = = = = = = = = = = = = =====")
    print("=== AGENDAMENTO DA TRANSPORTADORA ===")
    print("===== = = = = = = = = = = = = = =====")
    print("\n1 = Cadastrar aviões =")
    print("2 = Cadastrar assentos =")
    print("3 = Reservar passagem =")
    print("4 = Consultar por avião =")
    print("5 = Consultar por passageiro =")
    print("6 = Sair =")

def buscar_aviao(numero):
    for i in range(4):
        if avioes_registrados[i] == numero:
            return i
    return -1

while True:
    menu()

    opcao = int(input("\nDigite a opção: "))

    #Primeira Opção (Cadastrar os Aviões)
    if opcao == 1:
        for i in range(4):
            num = int(input(f"Número do avião {i+1}: "))

            if num in avioes_registrados:
                print("Esse avião já foi cadastrado!")
                continue

            avioes_registrados[i] = num

    #Segunda Opção (Casdastrar os Assentos)
    elif opcao == 2:
        for i in range(4):
            if avioes_registrados[i] == -1:
                print("Cadastre os aviões primeiro!")
                break

            numero_assentos[i] = int(
                input(f"Assentos do avião {avioes_registrados[i]}: ")
            )

    #Terceira opção (limitando número de reservas)
    elif opcao == 3:
        if len(reservas) >= 20:
            print("Limite de reservas atingido!")
            continue

        num = int(input("Número do avião: "))
        indice = buscar_aviao(num)

        if indice == -1:
            print("Este avião não existe!")

        elif numero_assentos[indice] <= 0:
            print("Não há assentos disponíveis!")

        else:
            nome = input("Nome do passageiro: ")
            reservas.append({
                "numero_aviao": num,
                "nome_passageiro": nome
            })

            numero_assentos[indice] -= 1
            print("Reserva realizada com sucesso!")

    #Quarta opção (Consultar aviões disponiveis)
    elif opcao == 4:
        num = int(input("Número do avião: "))
        indice = buscar_aviao(num)

        if indice == -1:
            print("Este avião não existe!")
    #Percorre a lista "Reserva" buscando oque vai ser colocado na nova lista para filtrar as reservas:
        else:
            encontrados = [
                r for r in reservas if r["numero_aviao"] == num
            ]

            if not encontrados:
                print("Nenhuma reserva encontrada para este avião!")
            else:
                print("Passageiros:")
                for r in encontrados:
                    print("-", r["nome_passageiro"])

    #Quinta Opção (Agora com passageiros (CONSULTA))
    elif opcao == 5:
        nome = input("Nome do passageiro: ").lower()
        encontrados = [
            r for r in reservas if r["nome_passageiro"].lower() == nome
        ]

        if not encontrados:
            print("Nenhuma reserva encontrada!")
        else:
            print("Reservas encontradas:")
            for r in encontrados:
                print(f"Avião {r['numero_aviao']}")

    #Sexta Opção (Saída)
    elif opcao == 6:
        print("Encerrando sistema")
        print("", end="")
        for i in range(3):
            time.sleep(0.5)
            print(".", end="", flush=True)
        print()
        break

    else:
        print("Opção inválida!")
    #Saída com o ENTER (😎) farmei aura
    input("\nPressione ENTER para continuar...")
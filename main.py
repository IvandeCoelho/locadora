# Listas de dados
clientes = []
dependentes = []
filmes = []
dvds = []

# Menu Principal
def menu_principal():
    while True:
        print("\n\033[0;30;47m--- MENU PRINCIPAL ---\033[m\n"
              "1 - Gerenciar Clientes\n"
              "2 - Gerenciar Dependentes\n"
              "3 - Gerenciar Filmes\n"
              "4 - Gerenciar Cópias de DVD\n"
              "5 - Locação\n"
              "6 - Devolução\n"
              "7 - Relatórios\n"
              "8 - Sair")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                gerenciar_clientes()
            case "2":
                gerenciar_dependentes()
            case "3":
                gerenciar_filmes()
            case "4":
                gerenciar_copias()
            case "5":
                realizar_locacao()
            case "6":
                realizar_devolucao()
            case "7":
                relatorios()
            case "8":
                print("Saindo do programa...")
                break
            case _:
                print("\033[1;30;42mOpção inválida. Tente novamente.\033[m")

# OK
def gerenciar_clientes():
    while True:
        print("\n\n\033[0;30;44m--- GERENCIAR CLIENTES ---\033[m\n"
              "1 - Cadastrar Cliente\n"
              "2 - Listar Clientes\n"
              "3 - Remover Cliente\n"
              "0 - Voltar")

        opc = input("Escolha uma opção: ")

        match opc:
            case "1":
                nome = input("Digite o nome do cliente: ")
                telefone = input("Digite o telefone: ")
                while True:
                    dep = input(
                        "Digite o nome de um dependente (ou pressione Enter para finalizar): ")
                    if dep == "":
                        break
                    dependentes.append(dep)

                cliente = {
                    "id": len(clientes)+1,
                    "nome": nome,
                    "telefone": telefone,
                    "dependentes":  dependentes,
                    "dvds_locados": 0
                }
                clientes.append(cliente)
                print(
                    f"\033[1;43mCliente '{nome}' cadastrado com sucesso!\033[m")

            case "2":
                print("\n--- Lista de Clientes ---")
                if not clientes:
                    print("\033[1;30;42mNenhum cliente cadastrado.\033[m")
                else:
                    for i, cliente in enumerate(clientes, start=1):
                        print(f"{i}. {cliente}")
            case "3":
                print("\n--- Remover Cliente ---")
                if not clientes:
                    print(
                        "\033[1;30;42m Não existem cleintes cadastrados!.\033[m")
                else:
                    for i, cliente in enumerate(clientes, start=1):
                        print(f"{i} - {cliente}")
                    id_remover = int(
                        input("Digite o ID do cleinte para remover: "))
                    for cliente in clientes:
                        if cliente["id"] == id_remover:
                            clientes.remove(cliente)
                            print(
                                f"\033[1;30;42mCliente com ID {id_remover} removido com sucesso!\033[m")
                            break
            case "0":
                break
            case _:
                print("\033[1;30;42mOpção inválida. Tente novamente.\033[m")

# OK
def gerenciar_dependentes():
    while True:
        print("\n\n\033[0;30;44m--- GERENCIAR DEPENDENTE ---\033[m\n "
              "1. Cadastrar dependente\n"
              "2. Listar dependentes\n"
              "3. Remover dependente\n"
              "0. Voltar")

        opc = input("Escolha uma opção: ")

        match opc:
            case "1":
                nome = input("Digite o nome do dependente: ")
                dependentes.append(nome)
                print(
                    f"\033[1;43mDependente {nome} Cadastrado com sucesso!\033[m")
                ...
            case "2":
                if not dependentes:
                    print("\033[1;30;42mNenhum dependente encontrado\033[m")
                else:
                    for i, dependente in enumerate(dependentes, start=1):
                        print(f"{i} - {dependente}")
                ...
            case "3":
                ...
            case "0":
                break
            case _:
                print("\033[1;30;42mOpção inválida. Tente novamente.\033[m")

# OK
def gerenciar_filmes():
    while True:
        print("\n\n\033[0;30;46m--- GERENCIAR FILMES ---\033[m\n"
              "1 - Cadastrar Filme\n"
              "2 - Listar Filme\n"
              "3 - Remover Filme\n"
              "0 - Voltar")
        opc = input("Escolha uma opção: ")
        match opc:
            case "1":
                titulo = input("Informe o Titulo: ")
                ano = int(input("Informe o Ano: "))
                genero = input("Informe o Genero: ")
                filme = {
                    "id": len(filmes)+1,
                    "titulo": titulo,
                    "genro": genero,
                    "ano": ano
                }
                filmes.append(filme)
                print(
                    f"\033[1;43mFilme {titulo} cadastrado com sucesso!\033[m")

            case "2":
                print("--------Listando filmes------------")
                if not filmes:
                    print("\033[1;30;42mNenhum filme cadastrado\033[m")
                else:
                    for i, filme in enumerate(filmes, start=1):
                        print(f"{i} - {filme}")

            case "3":
                if not filmes:
                    print(
                        "\033[1;30;42m Não existem filmes cadastrados!.\033[m")
                else:
                    for i, filme in enumerate(filmes, start=1):
                        print(f"{i} - {filme}")
                    id_remover = int(
                        input("Digite o ID do filme para remover: "))
                    for filme in filmes:
                        if filme["id"] == id_remover:
                            filmes.remove(filme)
                            print(
                                f"\033[1;30;42mFilme com ID {id_remover} removido com sucesso!\033[m")
                            break

            case "0":
                break
            case _:
                print("\033[1;30;42mOpção inválida. Tente novamente.\033[m")

# OK
def gerenciar_copias():
    while True:
        print("\n\n\033[0;30;44m--- GERENCIAR DEPENDENTE ---\033[m\n"
              "1. Cadastrar cópia\n"
              "2. Listar cópias\n"
              "3. Remover cópia\n"
              "0. Voltar")
        opc = input("Escolha uma opção: ")
        match opc:
            case "1":
                print("\n--- Cadastro de Cópias ---")
                if not filmes:
                    print("\033[1;30;42mNenhum filme cadastrado\033[m")
                    break
                else:
                    for i, filme in enumerate(filmes, start=1):
                        print(f"{i} - {filme}")

                    id_filme = int(
                        input("Informe o ID do filme para criar cópia: "))
                    qnt_copias = int(input("Quantidade de cópias: "))

                    for filme in filmes:
                        if filme["id"] == id_filme:
                            nome_filme = filme['titulo']
                            break

                dvd = {
                    "id": len(dvds)+1,
                    "nome_filme": nome_filme,
                    "quantidade": qnt_copias,
                    "quantidade_total": qnt_copias
                }

                dvds.append(dvd)
                print(f"\033[1;43m Cadastrado com sucesso!\033[m")

            case "2":
                print("--------Listando cópias------------")
                if not dvds:
                    print("\033[1;30;42mNenhuma cópia cadastrado\033[m")
                else:
                    for i, dvd in enumerate(dvds, start=1):
                        print(f"{i} - {dvd}")
            case "3":
                if not dvds:
                    print(
                        "\033[1;30;42m Não existem filmes cadastrados!.\033[m")
                else:
                    for i, dvd in enumerate(dvds, start=1):
                        print(f"{i} - {dvd}")
                    id_remover = int(
                        input("Digite o ID do filme para remover: "))
                    for dvd in dvds:
                        if dvd["id"] == id_remover:
                            dvds.remove(dvd)
                            print(
                                f"\033[1;30;42mFilme com ID {id_remover} removido com sucesso!\033[m")
                            break

            case "0":
                break
            case _:
                print("\033[1;30;42mOpção inválida. Tente novamente.\033[m")

# OK
def realizar_locacao():
    while True:
        print("\n\n\033[0;30;44m--- GERENCIAR LOCAÇÃO ---\033[m\n"
              "1. Realizar locação\n"
              "0. Voltar")
        opc = input("Escolha uma opção: ")

        match opc:
            case "1":
                print("\n--- Lista de Clientes ---")
                if not clientes:
                    print("\033[1;30;42mNenhum cliente cadastrado.\033[m")
                    return
                for cliente in clientes:
                    print(
                        f"{cliente['id']} - {cliente['nome']} (Locações: {cliente['dvds_locados']})")

                id_cliente = int(input("Digite o ID do cliente: "))
                cliente_encontrado = None
                for cliente in clientes:
                    if cliente["id"] == id_cliente:
                        cliente_encontrado = cliente
                        break
                if not cliente_encontrado:
                    print("\033[1;30;42mCliente não encontrado.\033[m")
                    break

                print("\n--- DVDs Disponíveis ---")
                dvds_disponiveis = [
                    dvd for dvd in dvds if dvd["quantidade"] > 0]
                if not dvds_disponiveis:
                    print(
                        "\033[1;30;42mNenhum DVD disponível para locação.\033[m")
                    break

                for dvd in dvds_disponiveis:
                    print(
                        f"{dvd['id']} - {dvd['nome_filme']} ({dvd['quantidade']} disponíveis)")

                id_dvd = int(input("Digite o ID do DVD para locar: "))
                dvd_encontrado = None
                for dvd in dvds:
                    if dvd["id"] == id_dvd and dvd["quantidade"] > 0:
                        dvd_encontrado = dvd
                        break
                if not dvd_encontrado:
                    print(
                        "\033[1;30;42mDVD não encontrado ou está indisponível.\033[m")
                    return

                dvd_encontrado["quantidade"] -= 1
                cliente_encontrado["dvds_locados"] += 1
                print(f"\033[1;43mLocação realizada com sucesso!\033[m")
                print(
                    f"Cliente: {cliente_encontrado['nome']} -> Filme: {dvd_encontrado['nome_filme']}")

            case "0":
                break
            case _:
                print("\033[1;30;42mOpção inválida. Tente novamente.\033[m")

# OK
def realizar_devolucao():
    print("\n\033[0;30;44m--- DEVOLUÇÃO DE DVD ---\033[m")

    # Verifica clientes com DVDs locados
    clientes_locando = [
        cliente for cliente in clientes if cliente["dvds_locados"] > 0]

    if not clientes_locando:
        print("\033[1;30;42mNenhum cliente com DVDs locados.\033[m")
        return

    # Exibe lista de clientes
    print("\n\033[0;30;44m---- Clientes com DVDs locados ---\033[m")
    for cliente in clientes_locando:
        print(
            f"ID: {cliente['id']} | Nome: {cliente['nome']} | Locados: {cliente['dvds_locados']}")

    # Recebe ID do cliente
    id_cliente = int(input("Digite o ID do cliente que está devolvendo: "))

    # Busca cliente
    for cliente in clientes_locando:
        if cliente["id"] == id_cliente:
            # Procura qualquer DVD que esteja com cópia locada
            for dvd in dvds:
                if dvd["quantidade"] < dvd["quantidade_total"]:
                    dvd["quantidade"] += 1
                    cliente["dvds_locados"] -= 1
                    print(f"\033[1;42mDevolução feita com sucesso!\033[m")
                    print(
                        f"{cliente['nome']} devolveu uma cópia de '{dvd['nome_filme']}'")
                    return

            print(
                "\033[1;30;42mErro: nenhum DVD encontrado para devolução.\033[m")
            return

    print("\033[1;30;42mCliente não encontrado.\033[m")

# OK
def relatorios():
    while True:
        print("\n\n\033[0;30;44m--- RELATÓRIOS ---\033[m\n"
              "1 - Listar DVDs disponíveis\n"
              "2 - Listar DVDs locados\n"
              "3 - Listar locação por cliente\n"
              "0 - Voltar")
        opc = input("Escolha uma opção: ")
        match opc:
            case "1":
                if not dvds:
                    print("\033[1;30;42mNenhum DVD cadastrado.\033[m")
                else:
                    print("\n\033[0;30;44m--- DVDs Disponíveis ---\033[m")
                    for dvd in dvds:
                        if dvd["quantidade"] > 0:
                            print(
                                f"{dvd['id']} - {dvd['nome_filme']} ({dvd['quantidade']} disponíveis)")
            case "2":

                algum_locado = False
                for dvd in dvds:
                    print("\n\033[0;30;44m--- DVDs Locados ---\033[m")
                    if "quantidade_total" in dvd and dvd["quantidade"] < dvd["quantidade_total"]:
                        locados = dvd["quantidade_total"] - dvd["quantidade"]
                        print(
                            f"{dvd['id']} - {dvd['nome_filme']} ({locados} locado(s))")
                        algum_locado = True
                if not algum_locado:
                    print("\033[1;30;42mNenhum DVD locado no momento.\033[m")
            case "3":
                if not clientes:
                    print("\033[1;30;42mNenhum cliente cadastrado.\033[m")
                else:
                    print("\n\033[0;30;44m--- Clientes ---\033[m")
                    for cliente in clientes:
                        print(
                            f"{cliente['id']} - {cliente['nome']} (Locações: {cliente['dvds_locados']})")
                    id_cliente = int(input("Digite o ID do cliente: "))
                    cliente_encontrado = None
                    for cliente in clientes:
                        if cliente["id"] == id_cliente:
                            cliente_encontrado = cliente
                            break
                    if not cliente_encontrado:
                        print("\033[1;30;42mCliente não encontrado.\033[m")
                    else:
                        print(
                            f"Cliente '{cliente_encontrado['nome']}' tem {cliente_encontrado['dvds_locados']} DVD(s) locado(s).")
            case "0":
                break
            case _:
                print("\033[1;30;42mOpção inválida. Tente novamente.\033[m")

if __name__ == "__main__":
    menu_principal()

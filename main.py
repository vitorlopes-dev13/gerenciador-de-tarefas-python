from tarefa import Tarefa

tarefas = []

def cadastrar_tarefa():
    titulo = input("Digite o título da tarefa: ")
    tarefa = Tarefa(titulo)
    tarefas.append(tarefa)
    print("Tarefa cadastrada com sucesso!")


def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    print("\nLista de Tarefas:")
    for i, tarefa in enumerate(tarefas):
        print(f"{i + 1} - {tarefa.titulo} ({tarefa.status()})")


def concluir_tarefa():
    listar_tarefas()
    if not tarefas:
        return

    numero = int(input("Digite o número da tarefa para concluir: "))
    if 1 <= numero <= len(tarefas):
        tarefas[numero - 1].concluida = True
        print("Tarefa marcada como concluída!")
    else:
        print("Número inválido!")


while True:
    print("\n--- MENU ---")
    print("1 - Cadastrar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_tarefa()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        concluir_tarefa()
    elif opcao == "0":
        print("Encerrando sistema...")
        break
    else:
        print("Opção inválida!")

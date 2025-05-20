from ficha import menu_fichas

def menu_cardapio():
    while True:
        print("\n--- CARDÁPIO ---")
        print("1. Listar")
        print("2. Adicionar")
        print("3. Atualizar")
        print("4. Remover")
        print("0. Voltar")
        op = input("Escolha uma opção: ")

def main():
    while True:
        print("\n==== SISTEMA DO RESTAURANTE ====")
        print("1. Gerenciar Cardápio")
        print("2. Gerenciar Pedidos")
        print("3. Gerenciar Fichas Técnicas")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_cardapio()

        elif opcao == "2":
            menu_pedidos()

        elif opcao == "3":
            menu_fichas()
            
        elif opcao == "0":
            print("Saindo do sistema.")
            break
        
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
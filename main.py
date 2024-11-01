# variaveis
usuarios = []
postagens = []
proximo_id_usuario = 1
proximo_id_postagem = 1

# funções

def criar_usuario(nome):
    global proximo_id_usuario
    usuario = {
        'id': proximo_id_usuario,
        'nome': nome,
        'seguidores': [],
        'seguindo': []
    }

    usuarios.append(usuario)
    proximo_id_usuario += 1

def criar_postagem(usuario, texto):
    global proximo_id_postagem
    postagem = {'id': proximo_id_postagem,
                'usuario': usuario,
                'texto': texto
               }
    postagens.append(postagem)
    proximo_id_postagem += 1

def seguir_usuario(usuario_seguidor, usuario_a_seguir):
    pass

def curtir_postagem(usuario, postagem):
    pass

def comentar_postagem(usuario, postagem, texto):
    pass

def encontrar_usuario_por_id(user_id):
    pass

def encontrar_postagem_por_id(post_id):
    pass

# menu
def exibir_menu():
    while True:
        print("\n--- Menu ---")
        print("1. Criar Usuário")
        print("2. Criar Postagem")
        print("3. Seguir Usuário")
        print("4. Curtir Postagem")
        print("5. Comentar em Postagem")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do usuário: ")
            criar_usuario(nome)
            print("Usuário criado com sucesso!")
        
        elif opcao == "2":
            user_id = int(input("Digite o ID do autor da postagem: "))
            # usuario = encontrar_usuario_por_id(user_id)
            texto = input("Digite o texto da postagem: ")
            # criar_postagem(usuario, texto)
            print("Postagem criada com sucesso!")
        
        elif opcao == "3":
            user_id = int(input("Digite o seu ID: "))
            target_id = int(input("Digite o ID do usuário que deseja seguir: "))
            # seguir_usuario(user_id, target_id)
            print("Usuário seguido com sucesso!")
        
        elif opcao == "4":
            user_id = int(input("Digite o seu ID: "))
            post_id = int(input("Digite o ID da postagem que deseja curtir: "))
            # curtir_postagem(user_id, post_id)
            print("Postagem curtida com sucesso!")
        
        elif opcao == "5":
            user_id = int(input("Digite o seu ID: "))
            post_id = int(input("Digite o ID da postagem que deseja comentar: "))
            texto = input("Digite o texto do comentário: ")
            # comentar_postagem(user_id, post_id, texto)
            print("Comentário adicionado com sucesso!")
        
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


#exibir_menu()

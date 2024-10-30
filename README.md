
Caso de Teste 1: Criar Usuário
Objetivo: Verificar se o sistema permite a criação de um novo usuário com um nome válido e rejeita entradas inválidas.

Teste 1.1 - Criar Usuário com Nome Válido

Entrada: Nome = "Alice"
Procedimento: Chamar criar_usuario("Alice").
Resultado Esperado: Usuário criado com ID único, nome "Alice" e listas vazias de seguidores e seguidos.
Teste 1.2 - Criar Usuário com Nome em Branco

Entrada: Nome = ""
Procedimento: Chamar criar_usuario("").
Resultado Esperado: Erro retornado indicando que o nome não pode estar em branco.
Caso de Teste 2: Criar Postagem
Objetivo: Verificar se o sistema permite a criação de postagens para um usuário válido e rejeita entradas inválidas.

Teste 2.1 - Criar Postagem com Texto Válido

Pré-condição: Usuário com ID 1 existente.
Entrada: Usuário ID = 1, Texto = "Olá, mundo!"
Procedimento: Chamar criar_postagem(usuario, "Olá, mundo!").
Resultado Esperado: Postagem criada com ID único, autor ID = 1 e texto "Olá, mundo!".
Teste 2.2 - Criar Postagem com Texto em Branco

Pré-condição: Usuário com ID 1 existente.
Entrada: Usuário ID = 1, Texto = ""
Procedimento: Chamar criar_postagem(usuario, "").
Resultado Esperado: Erro retornado indicando que o texto não pode estar em branco.
Caso de Teste 3: Seguir Usuário
Objetivo: Verificar se o sistema permite que um usuário siga outro e impede seguir o mesmo usuário mais de uma vez.

Teste 3.1 - Seguir Usuário com IDs Válidos

Pré-condição: Dois usuários existentes, ID 1 e ID 2.
Entrada: Usuário ID = 1, Usuário a seguir ID = 2.
Procedimento: Chamar seguir_usuario(usuario1, usuario2).
Resultado Esperado: Usuário 1 começa a seguir o usuário 2, confirmando a ação com mensagem.
Teste 3.2 - Tentar Seguir o Mesmo Usuário Novamente

Pré-condição: Usuário 1 já está seguindo o usuário 2.
Entrada: Usuário ID = 1, Usuário a seguir ID = 2.
Procedimento: Chamar seguir_usuario(usuario1, usuario2) novamente.
Resultado Esperado: Mensagem informando que o usuário 1 já está seguindo o usuário 2.
Teste 3.3 - Seguir Usuário Inexistente

Entrada: Usuário ID = 1, Usuário a seguir ID = 999 (inexistente).
Procedimento: Chamar seguir_usuario(usuario1, usuario_inexistente).
Resultado Esperado: Erro indicando que o usuário a ser seguido não foi encontrado.
Caso de Teste 4: Curtir Postagem
Objetivo: Verificar se o sistema permite que um usuário curta uma postagem e impede que a mesma postagem seja curtida duas vezes pelo mesmo usuário.

Teste 4.1 - Curtir Postagem com IDs Válidos

Pré-condição: Usuário 1 e postagem de ID 1 existente.
Entrada: Usuário ID = 1, Postagem ID = 1.
Procedimento: Chamar curtir_postagem(usuario, postagem).
Resultado Esperado: Usuário 1 curte a postagem, com confirmação da ação.
Teste 4.2 - Tentar Curtir a Mesma Postagem Novamente

Pré-condição: Usuário 1 já curtiu a postagem de ID 1.
Entrada: Usuário ID = 1, Postagem ID = 1.
Procedimento: Chamar curtir_postagem(usuario, postagem) novamente.
Resultado Esperado: Mensagem informando que o usuário já curtiu a postagem.
Teste 4.3 - Curtir Postagem Inexistente

Entrada: Usuário ID = 1, Postagem ID = 999 (inexistente).
Procedimento: Chamar curtir_postagem(usuario, postagem_inexistente).
Resultado Esperado: Erro indicando que a postagem não foi encontrada.
Caso de Teste 5: Comentar em Postagem
Objetivo: Verificar se o sistema permite que um usuário comente em uma postagem válida e impede comentários em branco.

Teste 5.1 - Comentar em Postagem com Texto Válido

Pré-condição: Usuário 1 e postagem de ID 1 existente.
Entrada: Usuário ID = 1, Postagem ID = 1, Texto = "Ótimo post!"
Procedimento: Chamar comentar_postagem(usuario, postagem, "Ótimo post!").
Resultado Esperado: Comentário é adicionado à postagem com a mensagem de sucesso.
Teste 5.2 - Comentar em Postagem com Texto em Branco

Pré-condição: Usuário 1 e postagem de ID 1 existente.
Entrada: Usuário ID = 1, Postagem ID = 1, Texto = ""
Procedimento: Chamar comentar_postagem(usuario, postagem, "").
Resultado Esperado: Erro informando que o comentário não pode estar em branco.
Teste 5.3 - Comentar em Postagem Inexistente

Entrada: Usuário ID = 1, Postagem ID = 999 (inexistente), Texto = "Comentário"
Procedimento: Chamar comentar_postagem(usuario, postagem_inexistente, "Comentário").
Resultado Esperado: Erro informando que a postagem não foi encontrada.

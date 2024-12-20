import pytest
from main import *


def testaCriarUsuarioValido():
    resetar()
    criar_usuario("Gleison")
    assert usuarios[0] == {
        'id':1, 'nome':'Gleison',
         'seguidores':[], 'seguindo':[]}

def testaCriarUsuarioSemNome():
    resetar()
    with pytest.raises(Exception) as error:
        criar_usuario("")

def testaCriarPostagemValida():
    resetar()
    criar_usuario("Maria")
    criar_postagem(1, "Olá Mundo")

    assert postagens[0] == {
        'id':1, 'usuario':1, 'mensagem': 'Olá Mundo',
        'curtidores':[]
    }

def testCriarPostagemTextoEmBranco():
    resetar()
    criar_usuario('arthur')
    with pytest.raises(Exception) as error:
        criar_postagem(1,"")

def testaRetornaUsuarioPorId():
    resetar()
    criar_usuario('juan')
    criar_usuario('gleison')
    usuario = encontrar_usuario_por_id(2)
    assert usuario == {
        'id':2,
        'nome':'gleison',
        'seguidores':[],
        'seguindo':[]
    }

def testaUsuariosInseridosNaLista():
    resetar()
    criar_usuario('jose')
    criar_usuario('maria')
    listaEsperada = [{
        'id':1, 'nome':'jose', 'seguidores':[], 'seguindo':[]
    },{
        'id':2, 'nome':'maria', 'seguidores':[], 'seguindo':[]
    }]

    assert usuarios == listaEsperada

def testaCriarPostagemUsuarioInexistente():
    resetar()
    with pytest.raises(IndexError) as error:
        criar_postagem(1,'relou')

def testaSeguirUsuarioExistente():
    resetar()
    criar_usuario('gleison')
    criar_usuario('karen')
    seguir_usuario(1,2)

    assert usuarios[0]['seguindo'] == [2]
    assert usuarios[1]['seguidores'] == [1]

def testaSeguirUsuarioInexistente():
    resetar()
    criar_usuario('gleison')
    with pytest.raises(Exception) as error:
        seguir_usuario(1,4)

def testaSeguirMesmoUsuario():
    resetar()
    criar_usuario('gleison')
    with pytest.raises(Exception) as error:
        seguir_usuario(1,1)

def testaCurtirPostagemValida():
    resetar()
    criar_usuario('gleison')
    criar_usuario('jose')
    criar_postagem(1, 'Acorda povo!')
    curtir_postagem(2, 1)

    assert postagens[0]['curtidores'] == [2]

def testaCurtirPostagemNovamente():
    resetar()
    criar_usuario('gleison')
    criar_usuario('jose')
    criar_postagem(1, 'Adoro testar!')
    curtir_postagem(2, 1)
    with pytest.raises(Exception) as error:
        curtir_postagem(2, 1)








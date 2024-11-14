import pytest
from main import *

def setup_function():
    usuarios.clear()
    postagens.clear()
    proximo_id_usuario = 1
    proximo_id_postagem = 1

def testaCriarUsuarioValido():
    setup_function()
    criar_usuario("Gleison")
    assert usuarios[0] == {
        'id':1, 'nome':'Gleison',
         'seguidores':[], 'seguindo':[]}

def testaCriarUsuarioSemNome():
    setup_function()
    with pytest.raises(Exception) as error:
        criar_usuario("")

def testaCriarPostagemValida():
    setup_function()
    criar_usuario("Maria")
    criar_postagem(1, "Olá Mundo")

    assert postagens[0] == {
        'id':1, 'usuario':1, 'mensagem': 'Olá Mundo'
    }

def testaRetornaUsuarioPorId():
    setup_function()
    criar_usuario('juan')
    usuario = encontrar_usuario_por_id(1)
    assert usuario == {
        'id':1,
        'nome':'juan',
        'seguidores':[],
        'seguindo':[]
    }

def testaCriarPostagemUsuarioInexistente():
    setup_function()
    with pytest.raises(IndexError) as error:
        criar_postagem(1,'relou')







import pytest
from main import *

def setup_function():
    usuarios.clear()
    postagens.clear()
    proximo_id_usuario = 1
    proximo_id_postagem = 1

def testaCriarUsuarioValido():
    criar_usuario("Gleison")
    assert usuarios[0] == {
        'id':1, 'nome':'Gleison',
         'seguidores':[], 'seguindo':[]}

def testaCriarUsuarioSemNome():
    with pytest.raises(Exception) as error:
        criar_usuario("")

def testaCriarPostagemValida():
    criar_usuario("Maria")
    criar_postagem(1, "Olá Mundo")

    assert postagens[0] == {
        'id':1, 'usuario':1, 'mensagem': 'Olá Mundo'
    }

def testaCriarPostagemUsuarioInexistente():
    with pytest.raises(IndexError) as error:
        criar_postagem(1,'relou')







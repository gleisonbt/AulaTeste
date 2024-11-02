from pytest import *
from main import *

def setup_function():
    usuarios.clear()
    postagens.clear
    proximo_id_usuario = 1
    proximo_id_postagem = 1

def testaCriarUsuarioValido():
    criar_usuario("Gleison")
    assert usuarios[0] == {
        'id':1, 'nome':'Gleison',
         'seguidores':[], 'seguindo':[]}


def testaCriarPostagemValida():
    criar_usuario('Gleison')
    criar_postagem(1, 'Ola pessoas')
    assert postagens[0] == {
        'id':1, 'usuario': 1, 
        'texto': 'Ola pessoas'
    }


def testaCriarPostagemComUsuarioInvalido():
    #criar_postagem(3) deve falhar
    criar_postagem(3, "oie")



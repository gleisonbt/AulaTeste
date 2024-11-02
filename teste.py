from pytest import *
from main import *

def setup_function():
    usuarios = []
    postagens = []
    proximo_id_usuario = 1
    proximo_id_postagem = 1

def testaCriarUsuario():
    criar_usuario("Gleison")
    print("lista usuarios: " + str(len(usuarios)))
    assert usuarios[proximo_id_usuario - 1] == {
        'id':1, 'nome':'Gleison',
         'seguidores':[], 'seguindo':[]}

def testaCriarPostagemComUsuarioInvalido():
    #criar_postagem(3) deve falhar
    criar_postagem(3, "oie")

def testaCriarPostagem():
    criar_postagem(1, 'Ola pessoas')
    assert postagens[proximo_id_postagem - 2] == {
        'id':1, 'usuario': 1, 
        'texto': 'Ola pessoas'
    }

def testaEncontrarUsuarioPorId():
    criar_usuario('Agatha')
    assert encontrar_usuario_por_id(2) == {
       'id':2,
       'nome':'Agatha',
       'seguidores':[],
       'seguindo':[] 
    }

def testaEncontrarPostagemPorId():
    criar_postagem(2,"Humildade sempre")
    assert encontrar_postagem_por_id(2) == {
        'id':2,
        'usuario':2,
        'texto':'Humildade sempre'
    }
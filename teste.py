from pytest import *
from main import *

def testaCriarUsuario():
    criar_usuario("Gleison")
    assert usuarios[proximo_id_usuario - 2] == {
        'id':1, 'nome':'Gleison',
         'seguidores':[], 'seguindo':[]}

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
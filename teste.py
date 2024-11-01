from pytest import *
from main import *

def testaCriarUsuario():
    criar_usuario("Gleison")
    assert usuarios[proximo_id_usuario - 2] == {'id':1, 'nome':'Gleison',
         'seguidores':[], 'seguindo':[]}

def testaCriarPostagem():
    criar_postagem(1, 'Ola pessoas')
    assert postagens[proximo_id_postagem - 2] == {
        'id':1, 'usuario': 1, 
        'texto': 'Ola pessoas'
    }
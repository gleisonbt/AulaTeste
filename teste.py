from pytest import *
from main import *

def testaCriarUsuario():
    criar_usuario("Lucas")
    assert usuarios[len(usuarios) - 1] == {'id':1, 
    'nome':'Lucas', 
    'seguidores': [],
    'seguindo': []}    